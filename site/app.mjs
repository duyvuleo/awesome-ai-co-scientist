import {layoutGraph} from './graph-layout.mjs?v=reading-views-5';
import {fromURL,toURL,normalizeState,selectWorks,themeCounts,graphElements,exportRecords,domainThemes} from './model.mjs?v=reading-views-5';
const $ = id => document.getElementById(id);
const repo = 'https://github.com/duyvuleo/awesome-ai-co-scientist';
const names = {paper:'Paper',system:'System',tool:'Tool',benchmark:'Benchmark'};
const dimensionNames = {human_involvement:'Human involvement',hypothesis_generation:'Hypothesis generation',experiment_execution:'Experiment execution',memory:'Research memory',verification:'Verification',available_code:'Available code',evaluation_setting:'Evaluation setting'};
let data,state,cy,visible=[],graphBaseZoom=1;
const records = new Map(), works = new Map(), themes = new Map();
function el(tag,text,cls) {const n=document.createElement(tag); if(text!==undefined)n.textContent=text;if(cls)n.className=cls;return n;}
function link(text,url,cls) {const n=el('a',text,cls);try {const u=new URL(url);if(u.protocol!=='https:')return el('span',text);n.href=u.href;}catch{return el('span',text);}n.target='_blank';n.rel='noopener noreferrer';return n;}
function button(text,fn,cls){const n=el('button',text,cls);n.type='button';n.addEventListener('click',fn);return n;}
function pretty(value){return value.replaceAll('-',' ');}
function syncControls(){for(const k of ['kind','year','domain','sort','match'])$(k).value=state[k];$('search').value=state.q;$('code').checked=state.code;$('labels').checked=state.labels;}
function setState(patch,{graph=true}={}){state=normalizeState({...state,...patch},data);render({graph});}
function chooseTheme(id){setState({theme:state.theme.includes(id)?state.theme.filter(t=>t!==id):[...state.theme,id],focus:'',selected:''});}
function chooseWork(id){setState({selected:id},{graph:false});if(window.innerWidth<781)$('inspector').scrollIntoView({behavior:'auto',block:'start'});}
function updateURL(){const query=toURL(state);history.replaceState(null,'',location.pathname+(query?'?'+query:''));}
function render({graph=true}={}){
  const focusedTheme=document.activeElement?.dataset.theme;
  visible=selectWorks(data,state);
  if(state.selected&&!visible.some(w=>w.id===state.selected))state.selected='';
  syncControls();updateURL();
  const recordCount=visible.reduce((n,w)=>n+w.entry_ids.length,0);
  $('match-count').textContent=`${visible.length} of ${data.works.length} works · ${recordCount} catalog records`;
  $('active-filters').replaceChildren();
  for(const id of state.theme)$('active-filters').append(button(`${themes.get(id).label} ×`,()=>chooseTheme(id)));
  $('clear-themes').hidden=!state.theme.length;
  if(state.focus)$('active-filters').append(button('Neighborhood ×',()=>setState({focus:''})));
  renderCloud();renderRows();
  const layoutChanged=renderDetails();
  if(graph||layoutChanged)renderGraph();else {highlightGraph();$('graph-work').value=state.selected;$('graph-open').disabled=!state.selected;}
  $('export').disabled=!visible.length;
  if(focusedTheme)document.querySelector('#cloud button[data-theme="'+CSS.escape(focusedTheme)+'"]')?.focus({preventScroll:true});
}
function themeButton(t,size){const b=button(t.label,()=>chooseTheme(t.id));b.dataset.theme=t.id;b.setAttribute('aria-label',`${t.label}: ${t.count} ${t.count===1?'work':'works'}`);b.setAttribute('aria-pressed',String(state.theme.includes(t.id)));b.style.fontSize=size+'px';b.style.setProperty('--word-size',size+'px');b.append(el('sup',t.count));return b;}
function renderCloud(){
  const base=selectWorks(data,state,{ignoreTheme:true});
  const counts=themeCounts(data,base);
  let top=counts.slice(0,window.innerWidth<781?16:26);
  // Retain selected themes even when other filters leave them with no matches.
  for(const id of state.theme)if(!counts.some(t=>t.id===id))counts.push({...themes.get(id),count:0});
  for(const id of state.theme)if(!top.some(t=>t.id===id))top.push(counts.find(t=>t.id===id));
  // Deterministic alternating order keeps the cloud balanced without rotation.
  top=top.filter((_,i)=>i%2===0).concat(top.filter((_,i)=>i%2===1).reverse());
  $('cloud').replaceChildren();
  const max=Math.max(1,...counts.map(t=>t.count));
  for(const t of top)$('cloud').append(themeButton(t,14+22*Math.sqrt(t.count/max)));
  if(!top.length)$('cloud').append(el('p','No themes match the current filters.','empty'));
  $('topic-counts').replaceChildren();
  for(const t of counts){const b=button('',()=>chooseTheme(t.id));b.append(el('span',t.label),el('strong',t.count));b.setAttribute('aria-pressed',String(state.theme.includes(t.id)));$('topic-counts').append(b);}
}
function workChips(w){
  const chips=el('div',undefined,'chips');for(const kind of w.kinds)chips.append(el('span',names[kind],'chip'));
  chips.append(el('span',pretty(records.get(w.id).evidence),'chip'));return chips;
}
function renderRows(){
  const cards=state.view==='cards';
  $('reading-table').hidden=cards;$('reading-cards').hidden=!cards;
  for(const view of ['table','cards'])$('view-'+view).setAttribute('aria-pressed',String(state.view===view));
  $('view-help').textContent=cards?'Full summaries with publication status and source links.':'Compare works by date, resource, and evidence.';
  $('rows').replaceChildren();$('reading-cards').replaceChildren();
  const fragment=document.createDocumentFragment();
  for(const w of visible){
    if(cards){
      const card=el('article',undefined,'reading-work');card.classList.toggle('is-selected',w.id===state.selected);
      const meta=el('div',undefined,'work-meta');meta.append(el('span',w.date),el('span',`${w.entry_ids.length} catalog record${w.entry_ids.length===1?'':'s'}`));
      const title=el('h3');title.append(link(w.name,records.get(w.id).url));
      const actions=el('div',undefined,'work-actions');actions.append(link('Primary source ↗',records.get(w.id).url));
      const inspect=button('Inspect evidence',()=>{chooseWork(w.id);$('inspector').scrollIntoView({behavior:'auto',block:'start'});});inspect.setAttribute('aria-label','Inspect '+w.name);actions.append(inspect);
      card.append(meta,title,workChips(w),el('p',w.summary,'work-summary'),actions);fragment.append(card);
    }else{
      const tr=el('tr');if(w.id===state.selected)tr.className='is-selected';
      const date=el('td',w.date),name=el('td'),summary=el('td'),action=el('td');
      name.append(button(w.name,()=>chooseWork(w.id),'work-name'),workChips(w));
      summary.append(el('div',w.summary,'summary-clamp'));const b=button('Inspect ↗',()=>chooseWork(w.id),'inspect');b.setAttribute('aria-label','Inspect '+w.name);action.append(b);tr.append(date,name,summary,action);fragment.append(tr);
    }
  }
  $(cards?'reading-cards':'rows').append(fragment);$('empty').hidden=!!visible.length;
}
function appendSources(parent,urls){const ul=el('ul');urls.forEach((u,i)=>{const li=el('li');li.append(link(`Source ${i+1} · ${new URL(u).hostname}`,u));ul.append(li);});parent.append(ul);}
function renderDetails(){
  const panel=$('detail'),inspector=$('inspector'),w=works.get(state.selected);
  const layoutChanged=inspector.hidden===!!w;
  inspector.hidden=!w;
  inspector.parentElement.classList.toggle('has-selection',!!w);
  panel.replaceChildren();
  if(!w)return layoutChanged;
  const top=el('div',undefined,'detail-top');top.append(el('p','SELECTED WORK','eyebrow'),button('×',()=>setState({selected:''},{graph:false})));top.lastChild.setAttribute('aria-label','Close work details');panel.append(top,el('h2',w.name));
  const chips=el('div',undefined,'chips');w.kinds.forEach(k=>chips.append(el('span',names[k],'chip')));chips.append(el('span',w.date,'chip'));panel.append(chips,el('p',w.summary,'detail-summary'));
  const actions=el('div',undefined,'detail-actions');actions.append(link('Primary source ↗',records.get(w.id).url,'primary'),button(state.focus===w.id?'Show all works':'Focus neighborhood',()=>setState({focus:state.focus===w.id?'':w.id,theme:[]})));panel.append(actions);
  panel.append(el('h3','Research themes'));const tagWrap=el('div',undefined,'detail-tags');for(const t of w.themes)tagWrap.append(button(themes.get(t)?.label||pretty(t),()=>chooseTheme(t)));panel.append(tagWrap,el('h3',`${w.entry_ids.length} catalog record${w.entry_ids.length===1?'':'s'}`));
  for(const id of w.entry_ids){const r=records.get(id),detail=el('details',undefined,'record');detail.append(el('summary',`${names[r.kind]} · ${pretty(r.evidence)}`));if(id===w.id)detail.open=true;
    if(id!==w.id)detail.append(el('p',r.summary));if(r.status)detail.append(el('p',r.status));
    const links=el('div',undefined,'detail-actions');links.append(link('Catalog entry ↗',r.catalog_url));for(const u of r.code_links)links.append(link('Code / artifact ↗',u));detail.append(links);
    detail.append(el('p',`Published / released: ${r.date}${r.date.length===4?' (year only)':''} · Added: ${r.added_on} · Source checked: ${r.checked}`,'source-meta'));appendSources(detail,r.sources);panel.append(detail);
  }
  for(const comparison of data.comparisons.filter(c=>w.entry_ids.includes(c.system_id))){
    const detail=el('details',undefined,'record');detail.append(el('summary','Capability & evidence · '+comparison.short_name));detail.append(el('p',comparison.limitations));
    for(const [key,cell] of Object.entries(comparison.dimensions)){const block=el('div',undefined,'capability');block.append(el('strong',dimensionNames[key]),el('p',cell.text),el('small',`Basis: ${pretty(cell.basis)}`));appendSources(block,cell.sources);detail.append(block);}panel.append(detail);
  }
  const associated=data.relations.filter(e=>e.source===w.id||e.target===w.id);
  if(associated.length){panel.append(el('h3','Related catalog entries'));for(const edge of associated){const other=works.get(edge.source===w.id?edge.target:edge.source);panel.append(button(other.name,()=>setState({focus:'',q:'',theme:[],kind:'',year:'',domain:'',code:false,selected:other.id}),'quiet'));}panel.append(el('p','Navigation links from the catalog. These do not specify how one work builds on or evaluates another.'));}
  return layoutChanged;
}
function updateGraphZoom(){
  if(!cy)return;
  $('graph-zoom').textContent=Math.round(cy.zoom()/graphBaseZoom*100)+'%';
  $('zoom-in').disabled=cy.zoom()>=cy.maxZoom();$('zoom-out').disabled=cy.zoom()<=cy.minZoom();
}
function resetGraphView(){if(!cy)return;cy.fit(undefined,30);graphBaseZoom=cy.zoom();updateGraphZoom();}
function renderGraph(){
  const model=layoutGraph(graphElements(data,visible,state),{narrow:$('graph').clientWidth<600});
  const topicNodes=model.nodes.filter(n=>n.data.type==='theme');
  $('graph-count').textContent=`${visible.length} works · ${topicNodes.length} themes · ${model.edges.length} theme links`;
  $('graph-empty').hidden=visible.length>0;$('graph-tooltip').hidden=true;
  $('graph-note').textContent='Lines connect works to their recorded themes. Circle sizes and numbers count matching works; positions do not measure similarity.';
  const select=$('graph-work');select.replaceChildren(el('option','Choose a work'));select.firstChild.value='';
  for(const w of [...visible].sort((a,b)=>a.name.localeCompare(b.name))){const o=el('option',w.name);o.value=w.id;select.append(o);}
  select.value=state.selected;$('graph-open').disabled=!select.value;
  if(!window.cytoscape){$('graph-note').textContent='Graph renderer unavailable. All results and evidence remain accessible in the table.';return;}
  if(cy)cy.destroy();
  const css=getComputedStyle($('graph'));const color=name=>css.getPropertyValue(name).trim();
  cy=window.cytoscape({container:$('graph'),elements:[...model.nodes,...model.edges],minZoom:.15,maxZoom:4,
    style:[{selector:'node',style:{'font-family':'system-ui','font-size':11,'color':color('--graph-ink'),'text-wrap':'wrap','text-max-width':105,'text-valign':'bottom','text-margin-y':6,'overlay-opacity':0}},
      {selector:'node[type="work"]',style:{'width':12,'height':12,'label':'data(label)','text-opacity':state.labels?1:0,'background-color':color('--graph-paper'),'border-width':1.5,'border-color':color('--graph-bg'),'text-outline-width':2,'text-outline-color':color('--graph-bg')}},
      ...['system','tool','benchmark'].map(k=>({selector:`node[kind="${k}"]`,style:{'background-color':color('--graph-'+k),'shape':k==='system'?'round-rectangle':k==='tool'?'diamond':'ellipse'}})),
      {selector:'node[type="theme"]',style:{'shape':'ellipse','width':'data(diameter)','height':'data(diameter)','label':'data(displayLabel)','font-size':15,'font-weight':600,'text-max-width':135,'text-halign':'data(halign)','text-valign':'data(valign)','text-margin-x':'data(marginX)','text-margin-y':'data(marginY)','background-color':color('--graph-theme'),'color':color('--graph-ink'),'border-width':1.5,'border-color':color('--graph-bg'),'text-outline-width':3,'text-outline-color':color('--graph-bg')}},
      {selector:'edge',style:{'width':1,'line-color':color('--graph-edge'),'curve-style':'straight','opacity':.16}},
      {selector:'node.faded',style:{'opacity':.3}},
      {selector:'edge.faded',style:{'opacity':.035}},
      {selector:'.chosen',style:{'border-width':3,'border-color':color('--graph-ink'),'font-weight':700}},
      {selector:'edge.connected',style:{'opacity':.8,'line-color':color('--graph-theme'),'width':1.8}},
      {selector:'.hovered',style:{'border-width':3,'border-color':color('--graph-ink'),'text-opacity':1,'z-index':10}}],
    layout:{name:'preset',fit:true,padding:30}});
  graphBaseZoom=cy.zoom();cy.on('zoom',updateGraphZoom);updateGraphZoom();
  cy.on('tap','node',event=>{const n=event.target;if(n.data('type')==='theme')chooseTheme(n.data('theme'));else chooseWork(n.data('work'));});
  cy.on('mouseover','node',event=>{
    const n=event.target;highlightGraph(n.id());n.addClass('hovered');
    $('graph-tooltip').textContent=n.data('name')+(n.data('type')==='theme'?` · ${n.data('count')} matching works`:'');$('graph-tooltip').hidden=false;
  });
  cy.on('mouseout','node',()=>{$('graph-tooltip').hidden=true;highlightGraph();});
  cy.on('tap',event=>{if(event.target===cy){$('graph-tooltip').hidden=true;highlightGraph();}});
  highlightGraph();
}
function highlightGraph(focusId){
  if(!cy)return;cy.elements().removeClass('faded chosen connected hovered');
  const id=focusId||(state.selected?'w:'+state.selected:'');
  if(id){const n=cy.getElementById(id);if(n.length){cy.elements().addClass('faded');n.closedNeighborhood().removeClass('faded');n.addClass('chosen');n.connectedEdges().addClass('connected');}}
}
async function init(){
  try{
    const response=await fetch('./data.json');if(!response.ok)throw new Error('Catalog could not be loaded.');data=await response.json();
    if(data.schema_version!==1)throw new Error('Unsupported catalog format.');
    data.records.forEach(r=>records.set(r.id,r));data.works.forEach(w=>works.set(w.id,w));data.themes.forEach(t=>themes.set(t.id,t));
    state=fromURL(location.search,data);
    $('collection-stats').replaceChildren();for(const [count,label] of [[data.works.length,'grouped works'],[data.records.length,'catalog records'],[data.themes.length,'research themes'],[data.comparisons.length,'system comparisons']]){const d=el('div');d.append(el('strong',count),el('span',label));$('collection-stats').append(d);}
    const years=[...new Set(data.records.map(r=>r.year))].sort((a,b)=>b-a);for(const y of years){const o=el('option',y);o.value=y;$('year').append(o);}
    for(const id of domainThemes){const t=themes.get(id);if(t){const o=el('option',t.label);o.value=id;$('domain').append(o);}}
    let timer;$('search').addEventListener('input',()=>{clearTimeout(timer);timer=setTimeout(()=>setState({q:$('search').value,focus:''}),150);});
    for(const key of ['kind','year','domain','sort','match'])$(key).addEventListener('change',()=>setState({[key]:$(key).value}));
    $('clear-themes').addEventListener('click',()=>setState({theme:[],focus:'',selected:''}));
    // A display preference must not reset the graph's current zoom or pan.
    $('labels').addEventListener('change',()=>{state=normalizeState({...state,labels:$('labels').checked},data);updateURL();cy?.style().selector('node[type="work"]').style('text-opacity',state.labels?1:0).update();});
    for(const view of ['table','cards'])$('view-'+view).addEventListener('click',()=>{state=normalizeState({...state,view},data);updateURL();renderRows();});
    $('code').addEventListener('change',()=>setState({code:$('code').checked}));
    $('reset').addEventListener('click',()=>{clearTimeout(timer);state=normalizeState({},data);render();});
    $('zoom-in').addEventListener('click',()=>cy?.zoom({level:Math.min(4,cy.zoom()*1.3),renderedPosition:{x:cy.width()/2,y:cy.height()/2}}));
    $('zoom-out').addEventListener('click',()=>cy?.zoom({level:Math.max(.15,cy.zoom()/1.3),renderedPosition:{x:cy.width()/2,y:cy.height()/2}}));
    $('fit').addEventListener('click',resetGraphView);
    $('graph-work').addEventListener('change',()=>{$('graph-open').disabled=!$('graph-work').value;highlightGraph($('graph-work').value?'w:'+$('graph-work').value:undefined);});
    $('graph-open').addEventListener('click',()=>{if($('graph-work').value)chooseWork($('graph-work').value);});
    $('export').addEventListener('click',()=>{const payload=exportRecords(data,visible);const url=URL.createObjectURL(new Blob([JSON.stringify(payload,null,2)+'\n'],{type:'application/json'}));const a=el('a');a.href=url;a.download='ai-co-scientist-selection.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);});
    let resizeTimer;window.addEventListener('resize',()=>{clearTimeout(resizeTimer);resizeTimer=setTimeout(()=>{renderCloud();renderGraph();},150);});
    window.addEventListener('popstate',()=>{state=fromURL(location.search,data);render();});
    document.addEventListener('keydown',e=>{if(e.key==='Escape'&&state.selected)setState({selected:''},{graph:false});});
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>renderGraph());
    $('source-date').textContent='Latest source check: '+data.checked;
    render();
  }catch(error){$('error').hidden=false;$('error').replaceChildren(el('strong','The explorer could not load. '),el('span',error.message+' '),link('Read the catalogs instead.',repo));$('match-count').textContent='Catalog unavailable';}
}
init();
