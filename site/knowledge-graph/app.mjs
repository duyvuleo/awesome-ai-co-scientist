import {readState,stateSearch,selectRows,neighborhood,neighborhoodLayout,selectionExport} from './model.mjs?v=1';

const $ = id => document.getElementById(id);
function el(tag,text,cls) {const node=document.createElement(tag);if(text!==undefined)node.textContent=text;if(cls)node.className=cls;return node;}
function link(label,url) {const a=el('a',label);a.href=url;a.target='_blank';a.rel='noopener noreferrer';return a;}
function badge(text) {return el('span',text,'badge');}
let payload,state,graph,lastGraphWidth=0;

function updateUrl() {history.replaceState(null,'',location.pathname+stateSearch(state));}
function choose(id,scroll=false) {state.selected=id;render();if(scroll)$('details').scrollIntoView({behavior:'smooth',block:'start'});}
function inspectButton(row) {const b=el('button','Inspect evidence','inspect');b.type='button';b.addEventListener('click',()=>choose(row.id,true));return b;}
function stateLabel(row) {return row.attention!=='clear'?'source review needed':`${row.review_state} · ${row.lifecycle}`;}

function renderRows(rows) {
  const root=$('rows');root.replaceChildren();
  if(!rows.length){root.append(el('p','No statements match these filters. Clear the search or choose another question.','muted'));return;}
  if(state.view==='cards') {
    const grid=el('div',undefined,'cards');
    for(const row of rows){const card=el('article',undefined,'card'+(state.selected===row.id?' selected':''));card.append(badge(row.predicate.replaceAll('_',' ')),badge(stateLabel(row)),el('p',row.text),el('p',row.scope,'row-scope'),inspectButton(row));grid.append(card);}root.append(grid);
  } else {
    const wrap=el('div',undefined,'table-wrap');const table=el('table');
    const head=el('thead');const hr=el('tr');for(const text of ['Assertion & scope','Relation','Evidence & state','Details'])hr.append(el('th',text));head.append(hr);table.append(head);
    const body=el('tbody');for(const row of rows){const tr=el('tr',undefined,state.selected===row.id?'selected':'');const text=el('td');text.append(el('p',row.text),el('p',row.scope,'row-scope'));const relation=el('td',row.predicate.replaceAll('_',' '),'relation');const evidence=el('td');evidence.append(el('p',[...new Set(row.evidence.map(e=>e.scope))].join(' · ')),badge(stateLabel(row)));const details=el('td');details.append(inspectButton(row));tr.append(text,relation,evidence,details);body.append(tr);}table.append(body);wrap.append(table);root.append(wrap);
  }
}

function renderDetails(row) {
  $('details').hidden=!row;if(!row)return;
  const root=$('detail-body');root.replaceChildren();
  root.append(el('p',row.text,'details-text'),el('p',row.scope),badge(stateLabel(row)),el('p',`${row.subject_label} → ${row.predicate.replaceAll('_',' ')} → ${row.object_label}`,'muted'),el('code',row.id));
  if(row.object_record.measurement){const m=row.object_record.measurement;root.append(el('h3','Recorded outcome'),el('p',`${m.metric}: ${m.value}${m.denominator!==null?' / '+m.denominator:''} ${m.unit} · ${m.stage}`));}
  const review=row.review;root.append(el('h3','Review and history'));
  root.append(el('p',review?`${review.decision} · ${review.reviewer.label} (${review.reviewer.role}) · ${review.recorded_at}`:'Candidate: no recorded review.'));
  if(review)root.append(el('p',review.reason,'muted'));
  for(const event of row.source_events){const pending=row.pending_source_events.some(e=>e.id===event.id);root.append(el('p',`${event.kind}: ${event.reason} (${event.recorded_at}) · ${pending?'review needed':'reviewed after event'}`,pending?'warning':'muted'));}
  const revisions=payload.statements.filter(s=>s.claim_id===row.claim_id).sort((a,b)=>a.revision-b.revision);
  const history=el('p');for(const revision of revisions){const b=el('button',`r${revision.revision} · ${revision.lifecycle}`);b.type='button';b.addEventListener('click',()=>{state.history=true;choose(revision.id);});history.append(b,document.createTextNode(' '));}root.append(history);
  root.append(el('h3','Source passages'));const sources=el('ul',undefined,'source-list');
  for(const evidence of row.evidence){const item=el('li');item.append(link(evidence.source.label,evidence.source.url),el('p',evidence.locator),el('p',`${evidence.stance} · ${evidence.basis} · ${evidence.scope}`,'source-meta'),el('p',`Source pin: ${evidence.source.pin}`,'source-meta'),el('p',`Published: ${evidence.source.published_on??'not established'} · Inspected: ${evidence.source.observed_on}`,'source-meta'));if(evidence.executed_at)item.append(el('p',`Original execution: ${evidence.executed_at}`,'source-meta'));sources.append(item);}root.append(sources);
  for(const evaluation of row.evaluations){root.append(el('h3',evaluation.label),el('p',evaluation.configuration.details));const wrap=el('div',undefined,'table-wrap');const table=el('table',undefined,'context');const body=el('tbody');for(const [field,value]of Object.entries(evaluation.context)){const tr=el('tr');tr.append(el('td',field.replaceAll('_',' ')),el('td',value??`Not established. ${evaluation.missing_reasons[field]??''}`));body.append(tr);}table.append(body);wrap.append(table);root.append(wrap);const disclosure=el('details');disclosure.append(el('summary','Evaluation and configuration sources'));const contextSources=new Map([...evaluation.evidence,...evaluation.configuration.evidence].map(e=>[e.id,e]));for(const e of contextSources.values())disclosure.append(link(e.source.label,e.source.url),el('p',e.locator,'source-meta'));root.append(disclosure);if(evaluation.executed_at)root.append(el('p',`Original execution: ${evaluation.executed_at}`,'muted'));}
}

function renderGraph(row) {
  if(graph){graph.destroy();graph=null;}
  if(!row){$('graph-note').textContent='No matching assertion. Evidence remains available in the table.';return;}
  if(!globalThis.cytoscape){$('graph-note').textContent='Graph renderer unavailable. All evidence and context remain available in the table and details.';return;}
  const style=getComputedStyle(document.documentElement);const ink=style.getPropertyValue('--ink').trim();const bg=style.getPropertyValue('--panel').trim();
  const elements=neighborhood(payload,row);const layout=neighborhoodLayout(elements,row.id,row.subject,$('graph').clientWidth);
  lastGraphWidth=$('graph').clientWidth;
  $('graph').style.height=layout.height+'px';for(const element of elements)if(!element.data.source)element.position=layout.positions[element.data.id];
  graph=globalThis.cytoscape({container:$('graph'),elements,minZoom:.15,maxZoom:3,zoom:1,
    style:[{selector:'node',style:{'label':'data(label)','text-wrap':'wrap','text-max-width':layout.nodeWidth-10,'font-size':layout.fontSize,'color':'#17332b','text-valign':'center','text-halign':'center','background-color':'#bdcfc5','border-width':1,'border-color':'#6d8c7c','width':layout.nodeWidth,'height':65,'shape':'roundrectangle'}},
      {selector:'node[kind="assertion"]',style:{'background-color':'#e3c38d','shape':'roundrectangle','height':70}},
      {selector:'node[kind="source"]',style:{'background-color':'#a9c7d7'}},
      {selector:'node[kind="evaluation"]',style:{'background-color':'#aec8a1'}},
      {selector:'edge',style:{'label':'data(label)','font-size':10,'color':ink,'text-wrap':'wrap','text-max-width':130,'text-background-color':bg,'text-background-opacity':.9,'text-background-padding':3,'curve-style':'bezier','target-arrow-shape':'triangle','line-color':'#789387','target-arrow-color':'#789387','width':1.4}}],
    layout:{name:'preset',fit:false}});
  $('graph-note').textContent=`${row.subject_label} → ${row.predicate.replaceAll('_',' ')} → ${row.object_label}. Labels remain visible; inspect the sources and context below.`;
}

function render() {
  const rows=selectRows(payload,state);
  if(!rows.some(s=>s.id===state.selected))state.selected=rows[0]?.id||'';
  const row=rows.find(s=>s.id===state.selected);
  $('question').value=state.question;$('search').value=state.q;$('family').value=state.family;$('history').checked=state.history;
  $('table-view').setAttribute('aria-pressed',String(state.view==='table'));$('cards-view').setAttribute('aria-pressed',String(state.view==='cards'));
  const answer=payload.answers.find(a=>a.question.id===state.question);const root=$('answer');root.replaceChildren();
  if(answer){root.append(el('p',answer.summary),el('p',answer.question.scope,'muted'),el('p',`${answer.statements.length} eligible assertions · ${answer.status.replaceAll('-',' ')}`,'muted'));if(answer.withheld.length)root.append(el('p',`${answer.withheld.length} assertions withheld pending source review.`,'warning'));}
  else root.append(el('p','Browse the pilot’s qualified assertions. Select a row to inspect its evidence and evaluation conditions.'));
  $('result-count').textContent=`${rows.length} matching assertion revisions · ${state.history?'history and pending records included':'current accepted statements'}`;
  renderRows(rows);renderDetails(row);renderGraph(row);updateUrl();
}

async function start() {
  try{const response=await fetch('./data.json');if(!response.ok)throw new Error(`Data request returned HTTP ${response.status}`);payload=await response.json();state=readState(location.search,payload);
    const counts=payload.counts;$('counts').textContent=`${counts.statements} reviewed statements · ${counts.evaluations} evaluation records · ${counts.sources} pinned sources · ${counts.studies} study records`;
    for(const answer of payload.answers){const option=el('option',answer.question.prompt);option.value=answer.question.id;$('question').append(option);}const browse=el('option','Browse all assertions');browse.value='browse';$('question').append(browse);
    for(const family of [...new Set(payload.statements.map(s=>s.family))].sort()){const option=el('option',family.replaceAll('-',' '));option.value=family;$('family').append(option);}
    $('question').addEventListener('change',()=>{state.question=$('question').value;state.family='';state.q='';state.selected='';render();});
    $('search').addEventListener('input',()=>{state.q=$('search').value;render();});$('family').addEventListener('change',()=>{state.family=$('family').value;render();});$('history').addEventListener('change',()=>{state.history=$('history').checked;render();});
    for(const view of ['table','cards'])$(view+'-view').addEventListener('click',()=>{state.view=view;render();});
    $('fit').addEventListener('click',()=>graph?.fit(undefined,35));$('close').addEventListener('click',()=>{$('details').hidden=true;});
    $('export').addEventListener('click',()=>{const blob=new Blob([JSON.stringify(selectionExport(payload,selectRows(payload,state)),null,2)],{type:'application/json'});const url=URL.createObjectURL(blob);const a=el('a');a.href=url;a.download='ai-co-scientist-evidence-selection.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);});
    window.addEventListener('popstate',()=>{state=readState(location.search,payload);render();});window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>renderGraph(selectRows(payload,state).find(s=>s.id===state.selected)));
    let resizeTimer;window.addEventListener('resize',()=>{clearTimeout(resizeTimer);resizeTimer=setTimeout(()=>renderGraph(selectRows(payload,state).find(s=>s.id===state.selected)),120);});
    new ResizeObserver(()=>{if($('graph').clientWidth!==lastGraphWidth)renderGraph(selectRows(payload,state).find(s=>s.id===state.selected));}).observe($('graph'));
    render();
  }catch(error){$('error').hidden=false;$('error').textContent=`The pilot could not load. ${error.message}. Open the generated evidence page on GitHub or serve the site through HTTP.`;$('counts').textContent='Pilot data unavailable.';}
}
start();
