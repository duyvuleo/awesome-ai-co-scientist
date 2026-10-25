import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {normalizeState,fromURL,toURL,selectWorks,themeCounts,graphElements,exportRecords} from '../site/model.mjs';
const data=JSON.parse(readFileSync(new URL('../site/data.json',import.meta.url),'utf8'));
const blank=()=>normalizeState({},data);
test('default selection preserves all works',()=>assert.equal(selectWorks(data,blank()).length,data.works.length));
test('filters combine and topic counts deduplicate grouped records',()=>{
 const s=normalizeState({kind:'system',theme:'hypothesis-generation'},data);
 const works=selectWorks(data,s);assert.ok(works.length);
 assert.ok(works.every(w=>w.kinds.includes('system')&&w.themes.includes('hypothesis-generation')));
 const c=themeCounts(data,works).find(t=>t.id==='hypothesis-generation');assert.equal(c.count,works.length);
});
test('year and type must match the same member record',()=>{
 const fake={works:[{id:'w',entry_ids:['p','s'],themes:[]}],records:[{id:'p',kind:'paper',year:2024,name:'p',summary:'x',tags:[],code_links:[]},{id:'s',kind:'system',year:2025,name:'s',summary:'x',tags:[],code_links:[]}],relations:[]};
 assert.equal(selectWorks(fake,{...blank(),year:'2024',kind:'system'}).length,0);
});
test('empty search produces empty results and graph without dangling edges',()=>{
 const s={...blank(),q:'zzzz-no-such-resource'};const works=selectWorks(data,s);assert.equal(works.length,0);
 assert.deepEqual(graphElements(data,works,s),{nodes:[],edges:[]});
});
test('graph edges connect works only to their recorded themes',()=>{
 const s=blank();const g=graphElements(data,selectWorks(data,s),s);const nodes=new Map(g.nodes.map(n=>[n.data.id,n.data]));
 assert.ok(g.edges.length);
 for(const {data:e} of g.edges){
  assert.equal(e.type,'theme');
  assert.equal(nodes.get(e.source).type,'theme');assert.equal(nodes.get(e.target).type,'work');
  const work=data.works.find(w=>w.id===nodes.get(e.target).work);
  assert.ok(work.themes.includes(nodes.get(e.source).theme));
 }
});
test('shared URLs round-trip filters and resolve member record IDs',()=>{
 const s=normalizeState({q:'memory & evidence',kind:'system',year:'2026',code:true,theme:'research-memory',selected:'discoveryrsi-system',mode:'catalog'},data);
 assert.equal(s.selected,'discoveryrsi');assert.deepEqual(fromURL('?'+toURL(s),data),s);
 assert.deepEqual(fromURL('?theme=unknown&selected=missing&sort=bad',data).theme,[]);
});
test('selection export retains every member and all sources without mutation',()=>{
 const before=JSON.stringify(data);const works=data.works.filter(w=>w.id==='discoveryrsi');const out=exportRecords(data,works);
 assert.equal(out.work_count,1);assert.equal(out.entries.length,3);
 assert.ok(out.entries.every(e=>e.sources.length&&e.catalog_url.startsWith('https://github.com/')));
 assert.equal(JSON.stringify(data),before);
});
test('old catalog URLs preserve filters and use the theme graph',()=>{
 const old=fromURL('?theme=ideation&theme=verification&mode=catalog',data);
 const current=fromURL('?theme=ideation&theme=verification',data);
 assert.deepEqual(old,current);assert.ok(!toURL(old).includes('mode='));
 assert.ok(graphElements(data,selectWorks(data,old),old).nodes.some(n=>n.data.type==='theme'));
});
test('selecting a theme gives one labeled hub for the matching works',()=>{
 const s=normalizeState({theme:'verification'},data);const works=selectWorks(data,s);const g=graphElements(data,works,s);
 assert.equal(g.nodes.filter(n=>n.data.type==='theme').length,1);
 assert.equal(g.edges.filter(e=>e.data.type==='theme').length,works.length);
});

const themeFixture={
 themes:[{id:'a',label:'A'},{id:'b',label:'B'},{id:'c',label:'C'}],
 works:[{id:'a-only',entry_ids:['a-only'],themes:['a']},{id:'b-only',entry_ids:['b-only'],themes:['b']},{id:'both',entry_ids:['both'],themes:['a','b']},{id:'neither',entry_ids:['neither'],themes:['c']}].map(w=>({...w,name:w.id,kind:'paper'})),
 records:['a-only','b-only','both','neither'].map(id=>({id,kind:'paper',year:2026,name:id,summary:'',tags:[],code_links:[]})),relations:[]
};
test('multiple themes support union and intersection without duplicating works',()=>{
 const any=normalizeState({theme:['a','b']},themeFixture);
 assert.deepEqual(selectWorks(themeFixture,any).map(w=>w.id),['a-only','b-only','both']);
 assert.deepEqual(selectWorks(themeFixture,{...any,match:'all'}).map(w=>w.id),['both']);
 assert.equal(selectWorks(themeFixture,{...any,theme:[]}).length,4);
 assert.deepEqual(selectWorks(themeFixture,{...any,theme:['a','c'],match:'all'}),[]);
 assert.equal(selectWorks(themeFixture,{...any,match:'all'},{ignoreTheme:true}).length,4);
});
test('repeated theme URLs preserve selections and match mode, and accept old links',()=>{
 const state=fromURL('?theme=a&theme=b&theme=a&theme=unknown&match=all',themeFixture);
 assert.deepEqual(state.theme,['a','b']);assert.equal(state.match,'all');
 assert.deepEqual(fromURL('?'+toURL(state),themeFixture),state);
 assert.deepEqual(fromURL('?theme=a',themeFixture).theme,['a']);
 assert.equal(fromURL('?match=unsupported',themeFixture).match,'any');
 assert.deepEqual(normalizeState({theme:['a',null,{},'a']},themeFixture).theme,['a']);
});
test('selected themes appear as distinct hubs with only valid shared-tag edges',()=>{
 const state=normalizeState({theme:['a','b']},themeFixture);
 const graph=graphElements(themeFixture,selectWorks(themeFixture,state),state);
 assert.deepEqual(graph.nodes.filter(n=>n.data.type==='theme').map(n=>n.data.theme),['a','b']);
 assert.equal(graph.edges.length,4);
 const ids=new Set(graph.nodes.map(n=>n.data.id));
 assert.ok(graph.edges.every(e=>ids.has(e.data.source)&&ids.has(e.data.target)));
 const both=graphElements(themeFixture,selectWorks(themeFixture,{...state,match:'all'}),state);
 assert.equal(both.edges.length,2);
});

test('catalog links do not create graph edges or topical neighbors',()=>{
 const linked={...themeFixture,relations:[{source:'a-only',target:'neither',kind:'catalog-related'}]};
 const s=normalizeState({focus:'a-only'},linked);
 assert.deepEqual(selectWorks(linked,s).map(w=>w.id),['a-only','both']);
 assert.deepEqual(graphElements(linked,linked.works,blank()),graphElements(themeFixture,themeFixture.works,blank()));
});

test('label preference defaults on, round-trips, and does not filter records',()=>{
 const shown=fromURL('?theme=verification',data);
 const hidden=fromURL('?theme=verification&labels=0',data);
 assert.equal(shown.labels,true);assert.equal(hidden.labels,false);
 assert.deepEqual(fromURL('?'+toURL(hidden),data),hidden);
 assert.deepEqual(selectWorks(data,hidden),selectWorks(data,shown));
 assert.equal(normalizeState({...hidden,theme:['ideation']},data).labels,false);
 assert.equal(normalizeState({},data).labels,true);
 assert.equal(fromURL('?labels=unexpected',data).labels,true);
 assert.ok(!toURL(shown).includes('labels='));
});
