// Topic hubs outside resource rings, adapted from awesome-agents-that-learn.
// Coordinates aid navigation only; they do not measure semantic similarity.
export function layoutGraph(model, {narrow=false}={}) {
  const width=narrow?720:1100, height=narrow?980:720;
  const cx=width/2,cy=height/2;
  const nodes=model.nodes.map(n=>({...n,data:{...n.data}}));
  const topics=nodes.filter(n=>n.data.type==='theme').sort((a,b)=>a.data.label.localeCompare(b.data.label));
  const rank=new Map(topics.map((n,i)=>[n.data.id,i]));
  const memberships=new Map();
  for(const e of model.edges){const list=memberships.get(e.data.target)||[];list.push(rank.get(e.data.source));memberships.set(e.data.target,list);}
  const works=nodes.filter(n=>n.data.type==='work').sort((a,b)=>{
    const first=n=>Math.min(...(memberships.get(n.data.id)||[topics.length]));
    return first(a)-first(b)||a.data.name.localeCompare(b.data.name)||a.data.id.localeCompare(b.data.id);
  });
  topics.forEach((n,i)=>{
    const angle=-Math.PI/2+i/topics.length*2*Math.PI;
    const sx=Math.sin(angle),sy=Math.cos(angle);
    n.position={x:cx+sx*(narrow?205:365),y:cy+sy*(narrow?345:235)};
    n.data.displayLabel=`${n.data.label}\n${n.data.count}`;
    n.data.diameter=18+Math.min(16,2*Math.sqrt(n.data.count));
    n.data.halign=narrow||Math.abs(sx)<.25?'center':sx>0?'right':'left';
    n.data.valign=narrow?(sy<-.2?'top':'bottom'):Math.abs(sx)<.25?(sy<0?'top':'bottom'):'center';
    n.data.marginX=narrow?0:sx*12;
    n.data.marginY=narrow?(sy<-.2?-12:12):sy*15;
  });
  works.forEach((n,i)=>{
    const angle=-Math.PI/2+(i+.5)/works.length*2*Math.PI;
    const stagger=works.length>45?(i%2?20:-20):0;
    n.position=works.length===1?{x:cx,y:cy}:{x:cx+Math.sin(angle)*((narrow?125:235)+stagger),y:cy+Math.cos(angle)*((narrow?215:145)+stagger)};
  });
  return {nodes,edges:model.edges.map(e=>({...e,data:{...e.data}})),width,height};
}
