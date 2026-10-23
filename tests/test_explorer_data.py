"""Explorer grouping, provenance, and semantic edge boundaries."""
from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from explorer_data import build_payload, preview_svg
from catalog import load, ROOT
from comparison import load_comparisons


def entry(ident, kind, url, **extra):
    return dict(id=ident,name=ident,kind=kind,date='2026-01-01',year=2026,
                added_on='2026-10-24',checked='2026-10-24',category='hypothesis',
                summary='A catalog record with primary evidence.',evidence='preprint',
                url=url,sources=[url],tags=['hypothesis-generation','code-available'],**extra)


class ExplorerDataTests(unittest.TestCase):
    def test_work_counts_do_not_double_count_paper_and_implementation(self):
        entries=[entry('paper','paper','https://arxiv.org/abs/2610.00001'),
                 entry('system','system','https://github.com/example/system',paper_url='https://arxiv.org/abs/2610.00001')]
        entries[0]['related']=['system'];entries[1]['related']=['paper']
        original=deepcopy(entries)
        payload=build_payload(entries,{'systems':[]},{'excluded_tags':['code-available'],'aliases':{},'labels':{}})
        self.assertEqual(len(payload['works']),1)
        self.assertEqual(payload['themes'][0]['count'],1)
        self.assertEqual(payload['relations'],[])
        self.assertEqual(len(payload['records']),2)
        self.assertEqual(entries,original)
        self.assertEqual(payload['records'][0]['sources'],original[0]['sources'])

    def test_related_is_not_promoted_to_citation_or_influence(self):
        a=entry('a','paper','https://example.org/a',related=['b'])
        b=entry('b','tool','https://example.org/b',related=['a'])
        payload=build_payload([a,b],{'systems':[]},{'excluded_tags':[],'aliases':{},'labels':{}})
        self.assertEqual(payload['relations'],[{'source':'a','target':'b','kind':'catalog-related','entry_pairs':[['a','b']]}])

    def test_aliases_count_once_per_work_and_preserve_original_tags(self):
        a=entry('a','paper','https://example.org/a');a['tags']=['biomedical','biomedicine']
        payload=build_payload([a],{'systems':[]},{'excluded_tags':[],'aliases':{'biomedical':'biomedicine'},'labels':{}})
        self.assertEqual(payload['themes'],[{'id':'biomedicine','label':'Biomedicine','count':1}])
        self.assertEqual(payload['records'][0]['tags'],['biomedical','biomedicine'])

    def test_actual_catalog_is_complete_and_preview_is_well_formed(self):
        entries=load();taxonomy=json.loads((ROOT/'data/explorer-taxonomy.json').read_text())
        payload=build_payload(entries,load_comparisons(),taxonomy)
        self.assertEqual({e['id'] for e in entries},{r['id'] for r in payload['records']})
        self.assertEqual(sum(len(w['entry_ids']) for w in payload['works']),len(entries))
        ids={w['id'] for w in payload['works']}
        self.assertTrue(all(e['source'] in ids and e['target'] in ids for e in payload['relations']))
        self.assertEqual({c['system_id'] for c in payload['comparisons']},{e['id'] for e in entries if e['kind']=='system'})
        self.assertEqual(payload,build_payload(list(reversed(entries)),load_comparisons(),taxonomy))
        import xml.etree.ElementTree as ET
        ET.fromstring(preview_svg(payload))

if __name__=='__main__':unittest.main()
