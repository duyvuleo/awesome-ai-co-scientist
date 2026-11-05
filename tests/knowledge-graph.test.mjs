import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {readState,stateSearch,selectRows,neighborhood,neighborhoodLayout,selectionExport} from '../site/knowledge-graph/model.mjs';

const payload=JSON.parse(fs.readFileSync(new URL('../site/knowledge-graph/data.json',import.meta.url),'utf8'));

test('pilot defaults to the reviewed release-scope answer',()=>{
  const state=readState('',payload);const rows=selectRows(payload,state);
  assert.equal(rows.length,4);assert.ok(rows.every(s=>s.review_state==='accepted'&&s.lifecycle==='current'));
});
test('URL state round trips without losing question, filters or view',()=>{
  for(const question of ['browse',...payload.answers.map(a=>a.question.id)])for(const view of ['table','cards']){
    const state={question,family:'sciencecua',q:'code & release',history:true,view,selected:payload.statements[0].id};
    assert.deepEqual(readState(stateSearch(state),payload),state);
  }
});
test('invalid selections normalize without inventing graph objects',()=>{
  const state=readState('?question=no&family=no&selected=no&view=no',payload);
  assert.equal(state.question,'release-scope');assert.equal(state.family,'');assert.equal(state.selected,'');assert.equal(state.view,'table');
});
test('filters return no matches rather than unrelated evidence',()=>{
  const state={...readState('',payload),q:'nonexistent-claim'};assert.deepEqual(selectRows(payload,state),[]);
  assert.deepEqual(neighborhood(payload,null),[]);
});
test('every neighborhood retains typed assertion and explicit source links',()=>{
  for(const row of payload.statements){
    const elements=neighborhood(payload,row);const nodes=new Set(elements.filter(x=>!x.data.source).map(x=>x.data.id));
    assert.ok(nodes.has(row.id));assert.ok(nodes.has(row.subject));assert.ok(nodes.has(row.object));
    for(const edge of elements.filter(x=>x.data.source)){assert.ok(nodes.has(edge.data.source));assert.ok(nodes.has(edge.data.target));assert.ok(!/outperforms|cites|shares theme/.test(edge.data.label));}
    for(const evidence of row.evidence)assert.ok(nodes.has(evidence.source.id));
    const sourceEdges=elements.filter(e=>e.data.target===row.id&&e.data.evidence_ids?.length);
    assert.deepEqual(new Set(sourceEdges.flatMap(e=>e.data.evidence_ids)),new Set(row.evidence_ids));
    assert.equal(new Set(sourceEdges.map(e=>e.data.source+' '+e.data.label)).size,sourceEdges.length);
  }
});
test('graph presentation is independent of unrelated record ordering',()=>{
  for(const row of payload.statements){const reversed={...payload,objects:[...payload.objects].reverse(),statements:[...payload.statements].reverse()};assert.deepEqual(neighborhood(reversed,row),neighborhood(payload,row));}
});
test('desktop and narrow layouts retain all nodes within readable, nonoverlapping boxes',()=>{
  for(const row of payload.statements)for(const width of [290,360,560,760,1180]){
    const elements=neighborhood(payload,row);const layout=neighborhoodLayout(elements,row.id,row.subject,width);
    const positions=Object.values(layout.positions);assert.equal(positions.length,elements.filter(e=>!e.data.source).length);
    for(const p of positions){assert.ok(p.x>=layout.nodeWidth/2&&p.x<=width-layout.nodeWidth/2);assert.ok(p.y>=35&&p.y<=layout.height-35);}
    for(let i=0;i<positions.length;i++)for(let j=i+1;j<positions.length;j++)assert.ok(Math.abs(positions[i].x-positions[j].x)>=layout.nodeWidth||Math.abs(positions[i].y-positions[j].y)>=70);
    assert.ok(layout.fontSize>=11);
  }
});
test('selection export preserves pins, scopes, typed outcomes and evaluation contexts',()=>{
  const original=JSON.stringify(payload);const rows=selectRows(payload,{...readState('',payload),question:'local-reproduction'});
  const exported=selectionExport(payload,rows);assert.equal(exported.statements.length,8);
  for(const row of exported.statements){assert.ok(row.evidence.length);assert.ok(row.scope);assert.ok(row.object_record);assert.ok(row.evaluations.length);}
  exported.statements[0].scope='changed';assert.equal(JSON.stringify(payload),original);
});
test('pending and superseded records require explicit history selection',()=>{
  const row={...structuredClone(payload.statements[0]),id:'synthetic-candidate',review_state:'candidate',lifecycle:'unpublished'};
  const fixture={...payload,statements:[...payload.statements,row]};const state={...readState('',payload),question:'browse'};
  assert.ok(!selectRows(fixture,state).some(s=>s.id===row.id));assert.ok(selectRows(fixture,{...state,history:true}).some(s=>s.id===row.id));
});
