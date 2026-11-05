"""Pilot answers and synthetic lifecycle/validation properties; no research runs."""
from copy import deepcopy
import json
from pathlib import Path
import random
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import knowledge_graph as kg


class GraphTests(unittest.TestCase):
    def setUp(self):
        self.data = kg.load()

    def later(self):
        data = deepcopy(self.data)
        data['release'] = {**data['release'], 'id': 'synthetic-later-release', 'recorded_at': '2026-11-07T00:00:00Z'}
        return data

    def revision(self, data, decision='accepted'):
        first = next(s for s in data['statements'] if s['claim_id'] == 'sc-code-construction')
        second = {**deepcopy(first), 'id': first['claim_id']+'-r2', 'revision': 2,
                  'supersedes': first['id'], 'recorded_at': '2026-11-06T01:00:00Z',
                  'text': 'Synthetic revised wording used only by lifecycle tests.'}
        data['statements'].append(second)
        data['reviews'].append({'id':'synthetic-review', 'statement_ids':[second['id']], 'decision':decision,
                                'reviewer':{'label':'Synthetic test reviewer','role':'contributor'},
                                'recorded_at':'2026-11-06T02:00:00Z','reason':'Synthetic fixture, not a real source claim.'})
        return first, second

    def test_real_pilot_has_valid_pins_and_preserves_component_scope(self):
        self.assertEqual(kg.validate(self.data), [])
        self.assertEqual(len(kg.snapshot(self.data)), 28)
        self.assertEqual(len(self.data['evaluations']), 9)
        self.assertEqual({e['scope'] for e in self.data['evidence']}, {'author-report','project-documentation','local-component'})
        self.assertTrue(all(r['reviewer']['role']=='assistant' for r in self.data['reviews']))
        self.assertFalse(any(e['scope']=='independent-scientific-result' for e in self.data['evidence']))

    def test_five_manual_source_located_answer_sets(self):
        expected = {
            'release-scope': {'sc-full-method','sc-code-construction','sc-code-evolution-planned','sc-code-benchmark-planned'},
            'benchmark-lineage': {'sb-verified-revises-original','sb-original-count','sb-verified-count','sb-revised-count','sb-evolution-count','sb-total-count','sb-ve-includes-verified','sb-ve-includes-evolution','sc-model-evaluated-on','sc-native-evaluated-on'},
            'memory-outcomes': {'car-initialization','car-final-outcomes','car-controls'},
            'human-involvement': {'cl-guided-human-role','cl-standard-human-role','cl-support-vs-target'},
            'local-reproduction': {'circle-scope','circle-untested','circle-baseline','circle-nan','scorer-scope','scorer-untested','scorer-arithmetic','scorer-malformed'},
        }
        # These sets encode the five reviewed source questions, not a count-only test.
        for ident, claims in expected.items():
            with self.subTest(question=ident):
                result = kg.answer(self.data, ident)
                self.assertEqual({s['claim_id'] for s in result['statements']}, claims)
                self.assertEqual(result['status'], 'source-scoped')
                self.assertTrue(all(e['locator'] and e['source']['pin'] for s in result['statements'] for e in s['evidence']))
        rows = kg.answer(self.data,'human-involvement')['statements']
        aggregate = next(s for s in rows if s['claim_id']=='cl-support-vs-target')
        self.assertEqual(aggregate['subject'],'eval-cl-panel')
        self.assertEqual(aggregate['object_record']['measurement']['denominator'],40)

    def test_missing_evidence_is_not_a_negative_capability_claim(self):
        data = self.later()
        data['reviews'][0]['decision'] = 'deferred'
        result = kg.answer(data,'release-scope')
        self.assertEqual(result['status'],'not-established')
        self.assertEqual(result['statements'],[])
        self.assertEqual(result['unresolved_subjects'],['sc-code','sc-paper-v1'])
        self.assertIn('not absence',result['scope_note'])

    def test_context_check_flags_modes_versions_metrics_and_missing_budgets(self):
        result = kg.compare(self.data,'eval-sc-model','eval-sc-native')
        self.assertEqual(result['status'],'not-comparable')
        self.assertIn('protocol',{x['field'] for x in result['differences']})
        self.assertIn('budget',{x['field'] for x in result['unknown']})
        data=deepcopy(self.data)
        a,b=data['evaluations'][:2]
        for field in kg.CONTEXT_FIELDS:
            a['context'][field]=b['context'][field]='same '+field
        self.assertEqual(kg.compare(data,a['id'],b['id'])['status'],'context-matched')
        for field in kg.CONTEXT_FIELDS:
            changed=deepcopy(data)
            changed['evaluations'][1]['context'][field]='different '+field
            result=kg.compare(changed,a['id'],b['id'])
            self.assertEqual(result['status'],'not-comparable',field)
            self.assertEqual(result['differences'][0]['field'],field)
        data['evaluations'][0]['context']['budget']=None
        self.assertEqual(kg.compare(data,a['id'],b['id'])['status'],'needs-review')

    def test_unreviewed_revision_does_not_replace_current(self):
        for decision in ('deferred','rejected'):
            data=self.later();first,second=self.revision(data,decision)
            current={s['id'] for s in kg.snapshot(data)}
            self.assertIn(first['id'],current)
            self.assertNotIn(second['id'],current)

    def test_acceptance_changes_current_but_preserves_as_of_and_input(self):
        data=self.later();first,second=self.revision(data)
        original=deepcopy(data)
        self.assertEqual(kg.validate(data,previous=self.data),[])
        self.assertIn(first['id'],{s['id'] for s in kg.snapshot(data,'2026-11-05')})
        self.assertIn(second['id'],{s['id'] for s in kg.snapshot(data,'2026-11-06')})
        self.assertEqual(next(s['lifecycle'] for s in kg.snapshot(data,include_history=True) if s['id']==first['id']),'superseded')
        self.assertEqual(data,original)

    def test_retraction_does_not_resurrect_superseded_revision(self):
        data=self.later();first,second=self.revision(data)
        data['reviews'].append({'id':'synthetic-retraction','statement_ids':[second['id']], 'decision':'retracted',
                                'reviewer':{'label':'Synthetic reviewer','role':'contributor'},
                                'recorded_at':'2026-11-06T03:00:00Z','reason':'Synthetic test retraction.'})
        self.assertFalse(any(s['claim_id']==first['claim_id'] for s in kg.snapshot(data)))
        self.assertEqual({s['lifecycle'] for s in kg.snapshot(data,include_history=True) if s['claim_id']==first['claim_id']},{'superseded','retracted'})

    def test_source_event_flags_dependencies_without_erasing_history(self):
        data=self.later()
        expected=set(kg.impact(data,'src-sc-paper'))
        data['source_events'].append({'id':'synthetic-correction','source_id':'src-sc-paper','kind':'correction',
                                     'recorded_at':'2026-11-06T01:00:00Z','reason':'Synthetic correction fixture.'})
        queue=kg.review_queue(data)
        self.assertEqual({s['id'] for s in queue},expected)
        self.assertEqual(len(kg.snapshot(data)),28)
        self.assertEqual(kg.answer(data,'benchmark-lineage')['statements'],[])
        self.assertEqual(kg.answer(data,'benchmark-lineage')['status'],'source-review-needed')
        self.assertEqual(kg.answer(data,'memory-outcomes'),kg.answer(self.data,'memory-outcomes'))
        self.assertEqual(len(kg.answer(data,'release-scope')['statements']),3)
        # A new review resolves only its explicit target, and only after the event.
        target=next(iter(expected))
        data['reviews'].append({'id':'synthetic-recheck','statement_ids':[target],'decision':'accepted',
                                'reviewer':{'label':'Synthetic reviewer','role':'contributor'},
                                'recorded_at':'2026-11-06T02:00:00Z','reason':'Synthetic source recheck.'})
        self.assertEqual({s['id'] for s in kg.review_queue(data)},expected-{target})
        resolved=next(s for s in kg.snapshot(data) if s['id']==target)
        self.assertEqual(len(resolved['source_events']),1)
        self.assertEqual(resolved['pending_source_events'],[])
        self.assertEqual(kg.review_queue(data,'2026-11-05'),[])

    def test_source_dependencies_include_configuration_evidence(self):
        data=deepcopy(self.data)
        cfg=next(c for c in data['configurations'] if c['id']=='cfg-cl-guided')
        cfg['evidence_ids']=['ev-sc-release']  # Synthetic dependency fixture only.
        impacted=kg.impact(data,'src-sc-code')
        self.assertIn('cl-guided-human-role-r1',impacted)
        self.assertNotIn('cl-standard-human-role-r1',impacted)

    def test_generated_order_invariance_and_serialization_roundtrip(self):
        oracle={q['id']:kg.answer(self.data,q['id']) for q in self.data['questions']}
        original=deepcopy(self.data)
        for seed in range(25):
            rng=random.Random(seed);data=deepcopy(self.data)
            for collection in kg.COLLECTIONS:rng.shuffle(data[collection])
            for ident,result in oracle.items():self.assertEqual(kg.answer(data,ident),result)
            encoded=json.dumps(data,ensure_ascii=False,allow_nan=False)
            self.assertEqual(kg.strict_json(encoded),data)
        self.assertEqual(self.data,original)

    def test_generated_revision_prefixes_preserve_history(self):
        for count in range(1,9):
            data=self.later();first=next(s for s in data['statements'] if s['claim_id']=='sc-code-construction')
            prior=first
            for revision in range(2,count+2):
                stamp=f'2026-11-06T{revision:02d}:00:00Z'
                row={**deepcopy(first),'id':f'{first["claim_id"]}-r{revision}','revision':revision,
                     'supersedes':prior['id'],'recorded_at':stamp,'text':f'Synthetic revision {revision}.'}
                data['statements'].append(row)
                data['reviews'].append({'id':f'synthetic-review-{revision}','statement_ids':[row['id']],'decision':'accepted',
                                        'recorded_at':stamp,'reason':'Synthetic generated fixture.',
                                        'reviewer':{'label':'Synthetic reviewer','role':'contributor'}})
                prior=row
            self.assertEqual(kg.validate(data,previous=self.data),[])
            self.assertEqual([s['id'] for s in kg.snapshot(data) if s['claim_id']==first['claim_id']],[prior['id']])
            self.assertEqual([s['id'] for s in kg.snapshot(data,'2026-11-05') if s['claim_id']==first['claim_id']],[first['id']])

    def test_append_only_update_rejects_mutation_and_deletion_in_every_collection(self):
        for collection in kg.COLLECTIONS:
            if not self.data[collection]:continue
            data=self.later();data[collection].pop(0)
            self.assertTrue(kg.validate(data,previous=self.data),collection)
            data=self.later();data[collection][0]['id']='synthetic-overwrite'
            self.assertTrue(kg.validate(data,previous=self.data),collection)
        update={'release':self.later()['release'],'source_events':[{'id':'synthetic-event','source_id':'src-sc-code','kind':'availability-change',
                   'recorded_at':'2026-11-06T01:00:00Z','reason':'Synthetic update fixture.'}]}
        after=kg.apply_update(self.data,update)
        self.assertEqual(kg.release_diff(self.data,after)['source_events']['added'],['synthetic-event'])
        self.assertEqual(kg.release_diff(self.data,after)['sources']['modified'],[])
        self.assertEqual(self.data,kg.load())

    def test_structural_validator_rejects_semantically_invalid_shapes(self):
        changes=[('statements','object','sc-paper'),('statements','evidence_ids',['missing-evidence']),
                 ('sources','pin','unpinned'),('sources','url','https://127.0.0.1/private'),
                 ('sources','url','https://[invalid'),
                 ('sources','recorded_at','2026-11-31T00:00:00Z'),
                 ('evidence','executed_at','2026-10-22T10:00:00+11:00')]
        for collection,key,value in changes:
            data=deepcopy(self.data);data[collection][0][key]=value
            self.assertTrue(kg.validate(data),(collection,key))
        data=deepcopy(self.data);data['statements'][0]['unexpected']='discard me'
        self.assertTrue(kg.validate(data))
        data=deepcopy(self.data);data['sources'][-1]['sha256']='0'*64
        self.assertTrue(kg.validate(data))
        data=deepcopy(self.data);data['sources'][-1]['local_path']='../private.txt'
        self.assertTrue(kg.validate(data))

    def test_schema_and_runtime_relation_vocabulary_agree(self):
        schema=kg.load(kg.SCHEMA)
        self.assertEqual(set(schema['$defs']['statement']['properties']['predicate']['enum']),set(kg.RELATIONS))

    def test_unknown_schema_constraints_fail_closed(self):
        schema=kg.load(kg.SCHEMA)
        self.assertEqual(kg.schema_profile_errors(schema),[])
        schema['$defs']['statement']['properties']['scope']['maxLength']=20
        self.assertTrue(any('unsupported schema keyword' in e for e in kg.schema_profile_errors(schema)))

    def test_historical_answers_cannot_reference_future_context_records(self):
        for collection in ('sources','evidence','configurations','evaluations'):
            data=self.later();data[collection][0]['recorded_at']='2026-11-06T00:00:00Z'
            self.assertTrue(kg.validate(data),collection)

    def test_source_identity_deduplicates_aliases_but_keeps_revisions_distinct(self):
        data=self.later();source=deepcopy(data['sources'][0]);source['id']='synthetic-duplicate-source'
        source['url']='https://arxiv.org/abs/2611.03238v1';data['sources'].append(source)
        self.assertTrue(any('duplicate canonical source version' in e for e in kg.validate(data)))
        source['url']='https://arxiv.org/html/2611.03238v2';source['pin']='v2'
        self.assertEqual(kg.validate(data),[])

    def test_duplicate_and_nonfinite_json_are_rejected(self):
        for text in ('{"id":1,"id":2}','{"value":NaN}','{"value":Infinity}'):
            with self.assertRaises(ValueError):kg.strict_json(text)

    def test_qualified_export_does_not_assert_unqualified_scientific_edges(self):
        original=deepcopy(self.data);export=kg.jsonld(self.data)
        statements=[n for n in export['@graph'] if n['@type']=='rdf:Statement']
        self.assertEqual(len(statements),28)
        self.assertTrue(all('kg:scope' in s and 'prov:wasDerivedFrom' in s for s in statements))
        baseline=next(n for n in export['@graph'] if n['@id'].endswith('/out-circle-baseline'))
        self.assertEqual(baseline['kg:value'],0.9597642169962064)
        self.assertFalse(any('outperforms' in key or 'builds_on' in key for node in export['@graph'] for key in node))
        self.assertEqual(self.data,original)

    def test_cli_unknown_question_and_exclusive_candidate_output(self):
        cmd=[sys.executable,str(kg.ROOT/'scripts/knowledge_graph.py')]
        result=subprocess.run(cmd+['answer','unknown'],capture_output=True,text=True)
        self.assertEqual(result.returncode,2)
        self.assertIn('unknown question',result.stderr)
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);patch=root/'patch.json';output=root/'candidate.json'
            patch.write_text(json.dumps({'release':self.later()['release']}))
            result=subprocess.run(cmd+['apply',str(patch),'--output',str(output)],capture_output=True,text=True)
            self.assertEqual(result.returncode,0,result.stderr)
            before=output.read_bytes()
            result=subprocess.run(cmd+['apply',str(patch),'--output',str(output)],capture_output=True,text=True)
            self.assertEqual(result.returncode,2)
            self.assertEqual(output.read_bytes(),before)

    def test_historical_reports_and_original_cost_dates_survive_build(self):
        paths=[kg.ROOT/s['local_path'] for s in self.data['sources'] if s['local_path']]
        before={str(p):p.read_bytes() for p in paths}
        output=kg.outputs(self.data)
        self.assertEqual(len(output),5)
        self.assertEqual(kg.strict_json(output[kg.ROOT/'site/knowledge-graph/pilot.json']),self.data)
        self.assertEqual(before,{str(p):p.read_bytes() for p in paths})
        for row in kg.answer(self.data,'local-reproduction')['statements']:
            self.assertTrue(all(e['executed_at'].startswith('2026-10-22') for e in row['evidence']))
            self.assertTrue(all(e['scope']=='local-component' for e in row['evidence']))
            self.assertTrue(all(e['source']['pin'] for v in row['evaluations'] for e in v['configuration']['evidence']))


if __name__=='__main__':unittest.main()
