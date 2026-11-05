"""Versioned evidence queries. Standard library only; never executes research code."""
import argparse
from copy import deepcopy
from datetime import date, datetime, timezone
import hashlib
from html import escape
import json
import math
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data/knowledge-graph/pilot.json'
SCHEMA = ROOT / 'data/knowledge-graph/schema.json'
BASE = 'https://duyvuleo.github.io/awesome-ai-co-scientist/knowledge-graph/id/'
COLLECTIONS = ('objects', 'sources', 'evidence', 'configurations', 'evaluations',
               'statements', 'reviews', 'source_events', 'questions')
CONTEXT_FIELDS = ('benchmark_version', 'task_set', 'split', 'metric', 'aggregation',
                  'model', 'scaffold', 'budget', 'human_role', 'protocol', 'artifact_version')
RELATIONS = {
    'describes': ({'paper-version'}, {'method'}),
    'implements': ({'software-version'}, {'method'}),
    'planned_component': ({'software-version'}, {'method', 'benchmark'}),
    'revises': ({'benchmark-version'}, {'benchmark-version'}),
    'includes': ({'benchmark-version'}, {'benchmark-version'}),
    'has_observation': ({'benchmark-version'}, {'outcome'}),
    'evaluated_on': ({'evaluation'}, {'benchmark-version'}),
    'uses': ({'evaluation'}, {'configuration'}),
    'reports': ({'evaluation'}, {'outcome'}),
    'has_human_role': ({'evaluation'}, {'human-role'}),
    'has_scope': ({'evaluation'}, {'scope'}),
    'untested_scope': ({'evaluation'}, {'scope'}),
}


def strict_json(text):
    def pairs(values):
        result = {}
        for key, value in values:
            if key in result:
                raise ValueError(f'duplicate JSON key: {key}')
            result[key] = value
        return result
    def constant(value):
        raise ValueError(f'nonfinite JSON value: {value}')
    return json.loads(text, object_pairs_hook=pairs, parse_constant=constant)


def load(path=DATA):
    return strict_json(Path(path).read_text(encoding='utf-8'))


def stamp(value):
    if not isinstance(value, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', value):
        raise ValueError('expected UTC timestamp YYYY-MM-DDTHH:MM:SSZ')
    return datetime.fromisoformat(value.replace('Z', '+00:00'))


def cutoff(value=None):
    if value is None:
        return datetime.max.replace(tzinfo=timezone.utc)
    if re.fullmatch(r'\d{4}-\d{2}-\d{2}', value):
        value += 'T23:59:59Z'
    return stamp(value)


def shape_errors(value, shape, document=None, path='$'):
    """Validate the schema keywords used by our published JSON Schema profile.

    This small runtime is not a general JSON Schema implementation. The schema is
    also usable with a full draft-2020-12 validator; domain checks follow below.
    """
    document = document or shape
    if '$ref' in shape:
        target = document
        for part in shape['$ref'].removeprefix('#/').split('/'):
            target = target[part]
        return shape_errors(value, target, document, path)
    errors = []
    if 'anyOf' in shape:
        if not any(not shape_errors(value, option, document, path) for option in shape['anyOf']):
            return [f'{path}: does not match an allowed shape']
        return []
    expected = shape.get('type')
    valid = {'object': isinstance(value, dict), 'array': isinstance(value, list),
             'string': isinstance(value, str), 'integer': type(value) is int,
             'number': type(value) in (int, float), 'boolean': type(value) is bool,
             'null': value is None}
    if expected and not valid[expected]:
        return [f'{path}: expected {expected}']
    if 'const' in shape and value != shape['const']:
        errors.append(f'{path}: expected {shape["const"]!r}')
    if 'enum' in shape and value not in shape['enum']:
        errors.append(f'{path}: unknown value {value!r}')
    if isinstance(value, str):
        if len(value.strip()) < shape.get('minLength', 0):
            errors.append(f'{path}: empty text')
        if 'pattern' in shape and re.search(shape['pattern'], value) is None:
            errors.append(f'{path}: invalid format')
    if isinstance(value, dict):
        for key in shape.get('required', []):
            if key not in value:
                errors.append(f'{path}: missing {key}')
        properties = shape.get('properties', {})
        for key, item in value.items():
            if key in properties:
                errors += shape_errors(item, properties[key], document, f'{path}.{key}')
            elif shape.get('additionalProperties') is False:
                errors.append(f'{path}: unexpected field {key}')
            elif isinstance(shape.get('additionalProperties'), dict):
                errors += shape_errors(item, shape['additionalProperties'], document, f'{path}.{key}')
    if isinstance(value, list):
        if len(value) < shape.get('minItems', 0):
            errors.append(f'{path}: too few items')
        if shape.get('uniqueItems') and len({json.dumps(v, sort_keys=True) for v in value}) != len(value):
            errors.append(f'{path}: duplicate items')
        for index, item in enumerate(value):
            errors += shape_errors(item, shape.get('items', {}), document, f'{path}[{index}]')
    if type(value) in (int, float) and value < shape.get('minimum', float('-inf')):
        errors.append(f'{path}: below minimum')
    if type(value) is float and not math.isfinite(value):
        errors.append(f'{path}: nonfinite number')
    return errors


def schema_profile_errors(shape, document=None, path='$'):
    """Reject unsupported constraints rather than silently weakening validation."""
    document=document or shape
    supported={'$schema','$id','$defs','$ref','$comment','title','description','type','const','enum',
               'anyOf','properties','required','additionalProperties','items','minLength','pattern',
               'minItems','uniqueItems','minimum'}
    errors=[f'{path}: unsupported schema keyword {key}' for key in shape if key not in supported]
    if '$ref' in shape and (not re.fullmatch(r'#\/\$defs\/[a-z_]+',shape['$ref']) or shape['$ref'].split('/')[-1] not in document.get('$defs',{})):
        errors.append(f'{path}: unsupported or unresolved local schema reference')
    for key in ('properties','$defs'):
        for name,child in shape.get(key,{}).items():
            errors += schema_profile_errors(child,document,path+'.'+name)
    for key in ('items','additionalProperties'):
        if isinstance(shape.get(key),dict):errors += schema_profile_errors(shape[key],document,path+'.'+key)
    for child in shape.get('anyOf',[]):errors += schema_profile_errors(child,document,path+'.anyOf')
    return errors


def indexes(data):
    return {key: {item['id']: item for item in data[key]} for key in COLLECTIONS}


def validate(data, previous=None, check_local=True):
    schema=load(SCHEMA)
    errors=schema_profile_errors(schema)
    if errors:return errors
    errors = shape_errors(data, schema)
    if errors:
        return errors
    ix = indexes(data)
    all_ids = [item['id'] for key in COLLECTIONS for item in data[key]]
    if len(set(all_ids)) != len(all_ids):
        errors.append('IDs must be globally unique across graph collections')
    nodes = {**ix['objects'], **ix['configurations'], **ix['evaluations']}
    types = {ident: item.get('kind', 'configuration' if ident in ix['configurations'] else 'evaluation')
             for ident, item in nodes.items()}
    try:
        now = stamp(data['release']['recorded_at'])
    except ValueError as exc:
        return [str(exc)]
    def fail(ident, message):
        errors.append(f'{ident}: {message}')
    for key in COLLECTIONS:
        for item in data[key]:
            if 'recorded_at' in item:
                try:
                    if stamp(item['recorded_at']) > now:
                        fail(item['id'], 'recorded after graph release')
                except ValueError as exc:
                    fail(item['id'], str(exc))
    if errors:
        return errors
    from catalog import load as load_catalog, canonical_identity
    catalog_ids = {x['id'] for x in load_catalog()}
    for obj in data['objects']:
        if (obj['kind'] == 'outcome') != (obj['measurement'] is not None):
            fail(obj['id'], 'outcome objects require a typed measurement; other objects must not carry one')
        if not set(obj['catalog_ids']) <= catalog_ids:
            fail(obj['id'], 'unknown catalog identity')
        if obj['version_of'] and obj['version_of'] not in ix['objects']:
            fail(obj['id'], 'unknown parent object')
        parent_kind={'paper-version':'paper','software-version':'software','benchmark-version':'benchmark'}.get(obj['kind'])
        if parent_kind and (not obj['version'] or types.get(obj['version_of'])!=parent_kind or not obj['source_ids']):
            fail(obj['id'], 'version object needs a typed parent, version and source')
        for source in obj['source_ids']:
            if source not in ix['sources']:
                fail(obj['id'], 'unknown source')
    source_keys = set()
    for source in data['sources']:
        try:
            parsed = urlsplit(source['url'])
            parsed.port
        except ValueError:
            fail(source['id'], 'malformed public source URL')
            continue
        if (parsed.scheme != 'https' or not parsed.hostname or '.' not in parsed.hostname
                or parsed.username or parsed.password or re.search(r'\s', source['url'])
                or parsed.hostname in ('127.0.0.1', '0.0.0.0', 'localhost')
                or parsed.hostname.endswith(('.local', '.internal'))):
            fail(source['id'], 'source must be a public HTTPS URL without credentials')
        if source['object_id'] not in ix['objects']:
            fail(source['id'], 'unknown source object')
        if source['pin'] not in source['url']:
            fail(source['id'], 'source pin is missing from its URL')
        key = (canonical_identity(source['url']), source['pin'])
        if key in source_keys:
            fail(source['id'], 'duplicate canonical source version; retain the existing source identity')
        source_keys.add(key)
        if source['kind'] in ('code', 'execution-record') and not re.fullmatch(r'[a-f0-9]{40}', source['pin']):
            fail(source['id'], 'code/report source requires full commit pin')
        for field in ('observed_on', 'published_on'):
            try:
                if source[field] is not None:
                    date.fromisoformat(source[field])
            except ValueError:
                fail(source['id'], f'invalid {field}')
        if source['local_path']:
            path = ROOT / source['local_path']
            if (not path.resolve().is_relative_to((ROOT / 'reports/reproducibility').resolve())
                    or path.is_symlink()):
                fail(source['id'], 'local evidence must be a completed reproducibility record')
            elif check_local and (not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != source['sha256']):
                fail(source['id'], 'dated execution record hash does not match')
    for evidence in data['evidence']:
        if evidence['source_id'] not in ix['sources']:
            fail(evidence['id'], 'unknown evidence source')
        elif stamp(ix['sources'][evidence['source_id']]['recorded_at']) > stamp(evidence['recorded_at']):
            fail(evidence['id'], 'evidence predates its source record')
        if evidence['scope'] == 'local-component':
            source = ix['sources'].get(evidence['source_id'], {})
            if source.get('kind') != 'execution-record' or not evidence['executed_at']:
                fail(evidence['id'], 'component observation requires an execution record and original execution date')
        elif evidence['executed_at'] is not None:
            fail(evidence['id'], 'source review must not invent an execution time')
        if evidence['executed_at']:
            try:
                executed = datetime.fromisoformat(evidence['executed_at'])
                if executed.tzinfo is None or executed > stamp(evidence['recorded_at']):
                    fail(evidence['id'], 'invalid original execution timestamp')
            except ValueError:
                fail(evidence['id'], 'invalid execution timestamp')
    for cfg in data['configurations']:
        if not set(cfg['evidence_ids']) <= ix['evidence'].keys():
            fail(cfg['id'], 'unknown configuration evidence')
        elif any(stamp(ix['evidence'][e]['recorded_at'])>stamp(cfg['recorded_at']) for e in cfg['evidence_ids']):
            fail(cfg['id'], 'configuration predates its evidence')
    for ev in data['evaluations']:
        if ev['configuration_id'] not in ix['configurations'] or ev['study_id'] not in ix['objects']:
            fail(ev['id'], 'unknown evaluation configuration or study')
        if types.get(ev['study_id'])!='study':
            fail(ev['id'], 'evaluation must retain a study identity')
        if ev['subject_id'] not in ix['objects']:
            fail(ev['id'], 'unknown evaluated subject')
        if not set(ev['evidence_ids']) <= ix['evidence'].keys():
            fail(ev['id'], 'unknown evaluation evidence')
        elif any(stamp(ix['evidence'][e]['recorded_at'])>stamp(ev['recorded_at']) for e in ev['evidence_ids']):
            fail(ev['id'], 'evaluation predates its evidence')
        if ev['configuration_id'] in ix['configurations'] and stamp(ix['configurations'][ev['configuration_id']]['recorded_at'])>stamp(ev['recorded_at']):
            fail(ev['id'], 'evaluation predates its configuration')
        if set(ev['context']) != set(CONTEXT_FIELDS):
            fail(ev['id'], 'comparison context fields must be explicit')
        for field, value in ev['context'].items():
            if value is None and field not in ev['missing_reasons']:
                fail(ev['id'], f'unknown {field} needs a reason')
        if ev['scope'] == 'local-component' and not ev['executed_at']:
            fail(ev['id'], 'component evaluation needs its original execution time')
    chains = {}
    for statement in data['statements']:
        ident = statement['id']
        subject, obj = statement['subject'], statement['object']
        allowed_subjects, allowed_objects = RELATIONS[statement['predicate']]
        if types.get(subject) not in allowed_subjects or types.get(obj) not in allowed_objects:
            fail(ident, 'invalid typed relation endpoints')
        if not set(statement['evidence_ids']) <= ix['evidence'].keys():
            fail(ident, 'unknown evidence locator')
        if not set(statement['evaluation_ids']) <= ix['evaluations'].keys():
            fail(ident, 'unknown evaluation record')
        if statement['predicate'] == 'reports' and subject not in statement['evaluation_ids']:
            fail(ident, 'reported outcome must retain its evaluation context')
        for key, refs in (('evidence', statement['evidence_ids']), ('evaluations', statement['evaluation_ids'])):
            if any(ref in ix[key] and stamp(ix[key][ref]['recorded_at']) > stamp(statement['recorded_at']) for ref in refs):
                fail(ident, 'statement predates its evidence or evaluation record')
        chains.setdefault(statement['claim_id'], []).append(statement)
    for claim_id, revisions in chains.items():
        ordered = sorted(revisions, key=lambda x: x['revision'])
        for i, item in enumerate(ordered):
            if item['revision'] != i + 1:
                fail(claim_id, 'revisions must be contiguous from 1')
            if item['supersedes'] != (ordered[i - 1]['id'] if i else None):
                fail(item['id'], 'revision must link to its immediate predecessor')
            if i and stamp(item['recorded_at']) <= stamp(ordered[i-1]['recorded_at']):
                fail(item['id'], 'revision timestamp must advance')
    for review in data['reviews']:
        for ident in review['statement_ids']:
            if ident not in ix['statements']:
                fail(review['id'], 'review refers to an unknown statement')
            elif stamp(review['recorded_at']) < stamp(ix['statements'][ident]['recorded_at']):
                fail(review['id'], 'review predates its statement')
        for other in data['reviews']:
            if (other['id'] != review['id'] and other['recorded_at'] == review['recorded_at']
                    and set(other['statement_ids']) & set(review['statement_ids'])):
                fail(review['id'], 'two review decisions for a statement have the same timestamp')
    for event in data['source_events']:
        if event['source_id'] not in ix['sources']:
            fail(event['id'], 'unknown changed source')
    for question in data['questions']:
        if not set(question['subjects']) <= nodes.keys():
            fail(question['id'], 'question refers to unknown subjects')
    if previous is not None:
        for key in COLLECTIONS:
            after = ix[key]
            for old in previous[key]:
                if after.get(old['id']) != old:
                    fail(old['id'], f'append-only history changed in {key}')
        if stamp(data['release']['recorded_at']) < stamp(previous['release']['recorded_at']):
            errors.append('release timestamp moved backwards')
    return errors


def require_valid(data):
    errors = validate(data)
    if errors:
        raise ValueError('\n'.join(errors))


def snapshot(data, as_of=None, include_history=False):
    """Return copied statements with independent review/lifecycle/attention states."""
    end = cutoff(as_of)
    ix = indexes(data)
    statements = [s for s in data['statements'] if stamp(s['recorded_at']) <= end]
    states = []
    for statement in statements:
        reviews = sorted((r for r in data['reviews'] if statement['id'] in r['statement_ids']
                          and stamp(r['recorded_at']) <= end), key=lambda r: (r['recorded_at'], r['id']))
        review = reviews[-1] if reviews else None
        state = deepcopy(statement)
        state['review_state'] = review['decision'] if review else 'candidate'
        state['review'] = deepcopy(review)
        source_ids = {ix['evidence'][ident]['source_id'] for ident in statement['evidence_ids']}
        source_ids.update(ix['evidence'][e]['source_id']
                          for ident in statement['evaluation_ids']
                          for e in ix['evaluations'][ident]['evidence_ids'])
        source_ids.update(ix['evidence'][e]['source_id']
                          for ident in statement['evaluation_ids']
                          for e in ix['configurations'][ix['evaluations'][ident]['configuration_id']]['evidence_ids'])
        events = sorted((e for e in data['source_events'] if e['source_id'] in source_ids
                         and stamp(e['recorded_at']) <= end),
                        key=lambda e: (e['recorded_at'], e['id']))
        pending = [e for e in events if not review or stamp(e['recorded_at']) >= stamp(review['recorded_at'])]
        state['attention'] = 'source-review-needed' if pending else 'clear'
        state['source_events'] = deepcopy(events)
        state['pending_source_events'] = deepcopy(pending)
        state['source_ids'] = sorted(source_ids)
        state['lifecycle'] = 'current'
        states.append(state)
    accepted = {}
    for state in states:
        if state['review_state'] in ('accepted', 'retracted'):
            current = accepted.get(state['claim_id'])
            if current is None or state['revision'] > current['revision']:
                accepted[state['claim_id']] = state
    for state in states:
        if state['review_state'] == 'retracted':
            state['lifecycle'] = 'retracted'
        elif state['review_state'] == 'accepted' and accepted[state['claim_id']]['id'] != state['id']:
            state['lifecycle'] = 'superseded'
        elif state['review_state'] != 'accepted':
            state['lifecycle'] = 'unpublished'
    if not include_history:
        states = [s for s in states if s['lifecycle'] == 'current' and s['review_state'] == 'accepted']
    return sorted(states, key=lambda s: (s['family'], s['claim_id'], s['revision']))


def select(data, *, subject=None, predicate=None, family=None, query='', as_of=None, history=False):
    rows = snapshot(data, as_of, history)
    terms = query.casefold().split()
    return [s for s in rows if (not subject or s['subject'] == subject)
            and (not predicate or s['predicate'] == predicate) and (not family or s['family'] == family)
            and all(term in ' '.join([s['claim_id'], s['text'], s['scope']]).casefold() for term in terms)]


def enrich(data, rows):
    ix = indexes(data)
    nodes = {**ix['objects'], **ix['configurations'], **ix['evaluations']}
    result = []
    def citation(ident):
        evidence=ix['evidence'][ident]
        return {**deepcopy(evidence), 'source':deepcopy(ix['sources'][evidence['source_id']])}
    for row in rows:
        item = deepcopy(row)
        item['subject_label'] = nodes[row['subject']]['label']
        item['object_label'] = nodes[row['object']]['label']
        item['object_record'] = deepcopy(nodes[row['object']])
        item['evidence'] = [citation(e) for e in row['evidence_ids']]
        item['evaluations'] = [{**deepcopy(ix['evaluations'][e]),
                                'evidence':[citation(ident) for ident in ix['evaluations'][e]['evidence_ids']],
                                'configuration': {**deepcopy(ix['configurations'][ix['evaluations'][e]['configuration_id']]),
                                                  'evidence':[citation(ident) for ident in ix['configurations'][ix['evaluations'][e]['configuration_id']]['evidence_ids']]}}
                               for e in row['evaluation_ids']]
        result.append(item)
    return result


def answer(data, question_id, as_of=None):
    question = next((q for q in data['questions'] if q['id'] == question_id), None)
    if question is None:
        raise ValueError(f'unknown question: {question_id}')
    relevant = [s for s in snapshot(data, as_of) if s['subject'] in question['subjects']
                and s['predicate'] in question['predicates']]
    usable = [s for s in relevant if s['attention'] == 'clear']
    withheld = [s for s in relevant if s['attention'] != 'clear']
    nodes = indexes(data)['objects']
    labels = lambda predicate: list(dict.fromkeys(nodes[s['object']]['label'] for s in usable if s['predicate']==predicate))
    if labels('implements') or labels('planned_component'):
        parts=[]
        if labels('implements'): parts.append('Implemented at the inspected pin: ' + '; '.join(labels('implements')) + '.')
        if labels('planned_component'): parts.append('Listed as planned: ' + '; '.join(labels('planned_component')) + '.')
        summary=' '.join(parts)
    elif labels('revises'):
        summary='The recorded benchmark versions have a source-supported revision relationship. Task inventories, split roles and evaluator repairs must be reconciled before comparing scores.'
    elif labels('has_human_role'):
        summary='Recorded human role: ' + '; '.join(labels('has_human_role')) + '. Offline scoring and runtime delivery remain separate.'
    elif labels('has_scope'):
        summary='Recorded executed scope: ' + '; '.join(labels('has_scope')) + '. Untested: ' + '; '.join(labels('untested_scope')) + '.'
    elif labels('reports'):
        summary='Reported outcomes: ' + '; '.join(labels('reports')) + '.'
    else:
        summary='Not established in the inspected sources.' if not usable else 'The matching qualified assertions are listed below.'
    return {'question': deepcopy(question), 'as_of': as_of,
            'summary': summary,
            'status': 'source-review-needed' if withheld else ('source-scoped' if usable else 'not-established'),
            'scope_note': 'Answers report reviewed evidence within this pilot. Missing evidence is not absence of a capability.',
            'statements': enrich(data, usable), 'withheld': enrich(data, withheld),
            'unresolved_subjects': sorted(set(question['subjects']) - {s['subject'] for s in usable})}


def compare(data, left, right):
    ix = indexes(data)
    if left not in ix['evaluations'] or right not in ix['evaluations']:
        raise ValueError('compare requires two evaluation IDs')
    a, b = ix['evaluations'][left], ix['evaluations'][right]
    differences, unknown = [], []
    for field in CONTEXT_FIELDS:
        va, vb = a['context'][field], b['context'][field]
        if va is None or vb is None:
            unknown.append({'field': field, 'left': va, 'right': vb,
                            'left_reason': a['missing_reasons'].get(field), 'right_reason': b['missing_reasons'].get(field)})
        elif va != vb:
            differences.append({'field': field, 'left': va, 'right': vb})
    return {'left': deepcopy(a), 'right': deepcopy(b), 'differences': differences, 'unknown': unknown,
            'status': 'not-comparable' if differences else ('needs-review' if unknown else 'context-matched'),
            'note': 'Matching recorded context is not a ranking or proof of causal equivalence. Reported author comparisons retain their own scope.'}


def impact(data, source_id, as_of=None):
    if source_id not in indexes(data)['sources']:
        raise ValueError(f'unknown source: {source_id}')
    return [s['id'] for s in snapshot(data, as_of) if source_id in s['source_ids']]


def review_queue(data, as_of=None):
    return [s for s in snapshot(data, as_of, True)
            if s['lifecycle'] == 'unpublished' and s['review_state'] in ('candidate', 'deferred')
            or s['lifecycle'] == 'current' and s['attention'] != 'clear']


def git_previous(revision):
    """Read a CI-provided immutable base, allowing only an absent initial graph."""
    if not revision or revision == '0' * 40:
        return None
    if not re.fullmatch(r'[a-f0-9]{40}', revision):
        raise ValueError('Git base must be a full commit SHA')
    subprocess.run(['git', 'cat-file', '-e', revision + '^{commit}'], cwd=ROOT, check=True, capture_output=True)
    path = DATA.relative_to(ROOT).as_posix()
    tree = subprocess.run(['git', 'ls-tree', '--name-only', revision, '--', path], cwd=ROOT, check=True, capture_output=True, text=True)
    if not tree.stdout.strip():
        return None
    return strict_json(subprocess.run(['git', 'show', revision + ':' + path], cwd=ROOT, check=True, capture_output=True, text=True).stdout)


def release_diff(before, after):
    result = {}
    for key in COLLECTIONS:
        a = {r['id']: r for r in before[key]}
        b = {r['id']: r for r in after[key]}
        result[key] = {'added': sorted(b.keys() - a.keys()), 'removed': sorted(a.keys() - b.keys()),
                       'modified': sorted(k for k in a.keys() & b.keys() if a[k] != b[k])}
    return result


def apply_update(data, patch):
    """Apply an explicit append-only JSON update in memory; no file side effects."""
    unknown = set(patch) - set(COLLECTIONS) - {'release'}
    if unknown:
        raise ValueError('unknown update collections: ' + ', '.join(sorted(unknown)))
    result = deepcopy(data)
    for key in COLLECTIONS:
        result[key].extend(deepcopy(patch.get(key, [])))
    if 'release' not in patch:
        raise ValueError('update needs a new release record')
    result['release'] = deepcopy(patch['release'])
    errors = validate(result, previous=data)
    if errors:
        raise ValueError('\n'.join(errors))
    return result


def jsonld(data):
    """Qualified assertions in JSON-LD; no transitive scientific inference."""
    nodes = []
    for collection in ('objects', 'sources', 'evidence', 'configurations', 'evaluations', 'reviews', 'source_events'):
        for item in sorted(data[collection], key=lambda x: x['id']):
            node = {'@id': BASE + item['id'], '@type': 'kg:' + collection.removesuffix('s'),
                    'rdfs:label': item.get('label', item['id']), 'kg:record': {'@value': item, '@type': '@json'}}
            if collection == 'evidence':
                node['prov:wasDerivedFrom'] = {'@id': BASE + item['source_id']}
            if collection == 'objects':
                node['kg:kind'] = item['kind']
                if item['measurement']:
                    for field, value in item['measurement'].items():
                        if value is not None:
                            node['kg:' + field] = value
            if collection == 'sources':
                node['dcterms:source'] = {'@id': item['url']}
                node['kg:pin'] = item['pin']
            if collection == 'evaluations':
                for field in ('configuration_id', 'study_id', 'subject_id'):
                    node['kg:' + field] = {'@id': BASE + item[field]}
                node['kg:scope'] = item['scope']
            nodes.append(node)
    for state in snapshot(data, include_history=True):
        nodes.append({'@id': BASE + state['id'], '@type': 'rdf:Statement',
                      'rdf:subject': {'@id': BASE + state['subject']},
                      'rdf:predicate': {'@id': BASE + 'predicate/' + state['predicate']},
                      'rdf:object': {'@id': BASE + state['object']},
                      'dcterms:description': state['text'], 'kg:scope': state['scope'],
                      'kg:reviewState': state['review_state'], 'kg:lifecycle': state['lifecycle'],
                      'kg:attention': state['attention'],
                      'prov:wasDerivedFrom': [{'@id': BASE + e} for e in state['evidence_ids']],
                      'kg:hasReview': [{'@id': BASE + r['id']} for r in data['reviews'] if state['id'] in r['statement_ids']],
                      'kg:record': {'@value': state, '@type': '@json'}})
    return {'@context': {'kg': BASE, 'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
                         'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
                         'prov': 'http://www.w3.org/ns/prov#', 'dcterms': 'http://purl.org/dc/terms/'}, '@graph': nodes}


def build_payload(data):
    return {'schema_version': 1, 'release': deepcopy(data['release']),
            'objects': deepcopy(data['objects']), 'sources': deepcopy(data['sources']),
            'statements': enrich(data, snapshot(data, include_history=True)),
            'answers': [answer(data, q['id']) for q in sorted(data['questions'], key=lambda x: x['id'])],
            'review_queue': enrich(data, review_queue(data)),
            'counts': {'statements': len(snapshot(data)), 'revisions': len(data['statements']),
                       'evaluations': len(data['evaluations']), 'sources': len(data['sources']),
                       'studies': len({e['study_id'] for e in data['evaluations']})}}


def render_evidence(data):
    def cell(value):
        return escape(str(value), quote=False).replace('|', '&#124;').replace('\n', '<br>')
    lines = ['# Knowledge graph pilot: evidence', '',
             '[Guide](knowledge-graph.md) · [Standalone pilot](https://duyvuleo.github.io/awesome-ai-co-scientist/knowledge-graph/) · [Canonical records](../data/knowledge-graph/pilot.json)', '',
             'Generated source-scoped answers. Review records identify the actual reviewer role. Source review does not establish scientific truth or independent reproduction.', '']
    for q in sorted(data['questions'], key=lambda x: x['id']):
        response = answer(data, q['id'])
        lines += [f'<a id="{q["id"]}"></a>', '', '## ' + q['prompt'], '', q['scope'], '',
                  '| Assertion | Scope | Evidence |', '| --- | --- | --- |']
        for s in response['statements']:
            citations = '<br>'.join(f'[{cell(e["locator"])}]({e["source"]["url"]}) ({cell(e["scope"])})' for e in s['evidence'])
            lines.append(f'| <a id="{s["id"]}"></a>{cell(s["text"])} | {cell(s["scope"])} | {citations} |')
        if not response['statements']:
            lines.append('| Not established in the inspected sources. | No eligible reviewed statements. | — |')
        for s in response['withheld']:
            lines.append(f'| {cell(s["claim_id"])}: source review needed | Withheld from current answers. | {cell(s["source_ids"])} |')
        lines += ['']
    return '\n'.join(lines).rstrip() + '\n'


def outputs(data=None):
    data = load() if data is None else data
    require_valid(data)
    dump = lambda value: json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + '\n'
    return {ROOT / 'site/knowledge-graph/data.json': dump(build_payload(data)),
            ROOT / 'site/knowledge-graph/graph.jsonld': dump(jsonld(data)),
            ROOT / 'site/knowledge-graph/pilot.json': dump(data),
            ROOT / 'site/knowledge-graph/schema.json': dump(load(SCHEMA)),
            ROOT / 'docs/knowledge-graph-evidence.md': render_evidence(data)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, default=DATA)
    parser.add_argument('--format', choices=('text', 'json'), default='text')
    sub = parser.add_subparsers(dest='command', required=True)
    validate_parser = sub.add_parser('validate'); validate_parser.add_argument('--previous', type=Path)
    history_validate = sub.add_parser('validate-history'); history_validate.add_argument('--git-base', required=True)
    statements = sub.add_parser('statements')
    statements.add_argument('--subject'); statements.add_argument('--predicate', choices=tuple(RELATIONS))
    statements.add_argument('--family'); statements.add_argument('--query', default='')
    statements.add_argument('--as-of'); statements.add_argument('--history', action='store_true')
    answers = sub.add_parser('answer'); answers.add_argument('id'); answers.add_argument('--as-of')
    compare_parser = sub.add_parser('compare'); compare_parser.add_argument('left'); compare_parser.add_argument('right')
    impact_parser = sub.add_parser('impact'); impact_parser.add_argument('source'); impact_parser.add_argument('--as-of')
    queue = sub.add_parser('review-queue'); queue.add_argument('--as-of')
    history = sub.add_parser('history'); history.add_argument('claim'); history.add_argument('--as-of')
    diff = sub.add_parser('diff'); diff.add_argument('previous', type=Path)
    apply = sub.add_parser('apply'); apply.add_argument('patch', type=Path); apply.add_argument('--output', type=Path, required=True)
    sub.add_parser('export-jsonld')
    sub.add_parser('questions')
    args = parser.parse_args()
    try:
        data = load(args.data); require_valid(data)
        if args.command == 'validate':
            errors = validate(data, load(args.previous) if args.previous else None)
            if errors: raise ValueError('\n'.join(errors))
            value = {'valid': True, 'statements': len(snapshot(data)), 'scope': data['release']['scope']}
        elif args.command == 'validate-history':
            previous = git_previous(args.git_base)
            errors = validate(data, previous)
            if errors: raise ValueError('\n'.join(errors))
            value = {'valid': True, 'baseline_present': previous is not None, 'base': args.git_base}
        elif args.command == 'statements':
            value = enrich(data, select(data, subject=args.subject, predicate=args.predicate, family=args.family,
                                        query=args.query, as_of=args.as_of, history=args.history))
        elif args.command == 'answer': value = answer(data, args.id, args.as_of)
        elif args.command == 'compare': value = compare(data, args.left, args.right)
        elif args.command == 'impact': value = impact(data, args.source, args.as_of)
        elif args.command == 'review-queue': value = enrich(data, review_queue(data, args.as_of))
        elif args.command == 'history':
            value = enrich(data, [s for s in snapshot(data, args.as_of, True) if s['claim_id'] == args.claim])
            if not value: raise ValueError('unknown claim: ' + args.claim)
        elif args.command == 'diff': value = release_diff(load(args.previous), data)
        elif args.command == 'export-jsonld': value = jsonld(data)
        elif args.command == 'questions': value = deepcopy(data['questions'])
        elif args.command == 'apply':
            value = apply_update(data, load(args.patch))
            with args.output.open('x', encoding='utf-8') as output:
                json.dump(value, output, ensure_ascii=False, indent=2, allow_nan=False); output.write('\n')
            value = {'written': str(args.output), 'note': 'Review this candidate file before replacing canonical data.'}
        if args.format == 'json' or args.command == 'export-jsonld':
            print(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False))
        elif args.command == 'answer':
            print(value['question']['prompt'] + '\n' + value['status'] + '\n' + value['question']['scope'])
            for row in value['statements']:
                print('\n' + row['text'] + '\nScope: ' + row['scope'])
                for ev in row['evidence']:
                    print(f'  {ev["source"]["url"]} — {ev["locator"]} [{ev["scope"]}]')
            if not value['statements']: print('Not established in the inspected sources.')
            if value['withheld']: print('Some statements are withheld pending source review.')
        else: print(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False))
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as exc:
        parser.exit(2, str(exc) + '\n')


if __name__ == '__main__':
    main()
