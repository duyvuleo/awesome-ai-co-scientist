"""Build public explorer data and a static preview from the canonical catalogs."""
from collections import Counter
from html import escape
import json
import math
from catalog import ROOT, ordered, recent_groups
from explore import code_links

REPO = 'https://github.com/duyvuleo/awesome-ai-co-scientist'
PAGES = {'paper': 'papers', 'system': 'systems', 'tool': 'tools', 'benchmark': 'benchmarks'}


def build_payload(entries, comparisons, taxonomy):
    excluded = set(taxonomy['excluded_tags'])
    aliases = taxonomy['aliases']
    labels = taxonomy['labels']
    works, entry_to_work, records = [], {}, []
    for group in recent_groups(entries):
        primary = group[0]
        tags = sorted({aliases.get(tag, tag) for entry in group for tag in entry['tags'] if tag not in excluded})
        work = {
            'id': primary['id'], 'name': primary['name'], 'date': primary['date'],
            'year': primary['year'], 'kind': primary['kind'], 'summary': primary['summary'],
            'entry_ids': [e['id'] for e in group], 'themes': tags,
            'kinds': sorted({e['kind'] for e in group}),
            'years': sorted({e['year'] for e in group}),
            'categories': sorted({e['category'] for e in group}),
            'has_code': any(code_links(e) for e in group),
            'added_on': max(e['added_on'] for e in group),
        }
        works.append(work)
        for entry in group:
            entry_to_work[entry['id']] = primary['id']
    for entry in ordered(entries):
        records.append({**entry, 'work_id': entry_to_work[entry['id']],
                        'catalog_url': f'{REPO}/blob/main/docs/{PAGES[entry["kind"]]}.md#{entry["id"]}',
                        'code_links': code_links(entry)})
    # Undirected catalog relationships, without inventing stronger edge semantics.
    pairs = {}
    for entry in entries:
        for target in entry.get('related', []):
            source_work, target_work = entry_to_work[entry['id']], entry_to_work[target]
            if source_work == target_work:
                continue
            key = tuple(sorted((source_work, target_work)))
            pair = tuple(sorted((entry['id'], target)))
            pairs.setdefault(key, set()).add(pair)
    relations = [{'source': a, 'target': b, 'kind': 'catalog-related',
                  'entry_pairs': [list(pair) for pair in sorted(pairs[(a, b)])]}
                 for a, b in sorted(pairs)]
    counts = Counter(tag for work in works for tag in work['themes'])
    themes = [{'id': tag, 'label': labels.get(tag, tag.replace('-', ' ').capitalize()), 'count': count}
              for tag, count in sorted(counts.items(), key=lambda item: (-item[1], item[0]))]
    return {'schema_version': 1, 'checked': max(e['checked'] for e in entries),
            'repository': REPO, 'counts': dict(Counter(e['kind'] for e in entries)),
            'works': ordered(works), 'records': records, 'themes': themes, 'relations': relations,
            'comparisons': comparisons['systems']}


def preview_svg(payload):
    """Stable, data-derived overview; the interactive site carries all details."""
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="390" viewBox="0 0 1200 390" role="img" aria-labelledby="title desc">',
             '<title id="title">Explore AI co-scientist research</title>',
             '<desc id="desc">A theme cloud and a sample of shared-theme connections. Click to explore the full collection.</desc>',
             '<rect width="1200" height="390" rx="18" fill="#f5f7f5"/>',
             '<text x="36" y="45" font-family="system-ui,sans-serif" font-size="13" letter-spacing="2" fill="#537568">EXPLORE THE COLLECTION</text>',
             '<text x="36" y="88" font-family="Georgia,serif" font-size="32" fill="#182d2a">Follow the ideas. Inspect the evidence.</text>',
             f'<text x="36" y="121" font-family="system-ui,sans-serif" font-size="15" fill="#526561">{len(payload["works"])} grouped works · {len(payload["records"])} catalog records · Click to explore</text>',
             '<line x1="688" y1="151" x2="688" y2="350" stroke="#d4dfd9"/>']
    positions = [(36,190),(340,190),(50,238),(380,235),(36,282),(340,282),(48,328),(400,327)]
    top = payload['themes'][:8]
    for (x, y), theme in zip(positions, top):
        size = min(28, 15 + math.sqrt(theme['count']) * 2)
        parts.append(f'<text x="{x}" y="{y}" font-family="system-ui,sans-serif" font-size="{size:.1f}" fill="#176d62">{escape(theme["label"])}</text>')
    theme = top[0]
    examples = [w for w in payload['works'] if theme['id'] in w['themes']][:6]
    for index, work in enumerate(examples):
        angle = index * 2 * math.pi / len(examples)
        x, y = 937 + 155 * math.cos(angle), 245 + 76 * math.sin(angle)
        parts.append(f'<line x1="937" y1="245" x2="{x}" y2="{y}" stroke="#bbd1c6" stroke-dasharray="4 4"/>')
        parts.append(f'<circle cx="{x}" cy="{y}" r="8" fill="#397f9c"><title>{escape(work["name"])}</title></circle>')
    parts += ['<circle cx="937" cy="245" r="29" fill="#176d62"/>',
              '<text x="937" y="250" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="white">Theme</text>',
              f'<text x="937" y="356" text-anchor="middle" font-family="system-ui,sans-serif" font-size="13" fill="#526561">{escape(theme["label"])} · shared tags, not citations</text>', '</svg>']
    return '\n'.join(parts) + '\n'


def outputs(entries, comparisons):
    taxonomy = json.loads((ROOT / 'data/explorer-taxonomy.json').read_text())
    payload = build_payload(entries, comparisons, taxonomy)
    return {ROOT / 'site/data.json': json.dumps(payload, ensure_ascii=False, indent=2) + '\n',
            ROOT / 'assets/explorer-preview.svg': preview_svg(payload)}
