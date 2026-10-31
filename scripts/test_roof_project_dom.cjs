// DOM adapter executes the actual feature against IDs/values parsed from source HTML.
// This is not a browser layout, accessibility-tree or production integration test.
const vm=require('node:vm'),fs=require('node:fs'),assert=require('node:assert');const code=fs.readFileSync(require('path').join(__dirname,'../assets/roof-project.js'),'utf8');let count=0;const ok=(x,m)=>{assert(x,m);count++};
class E{
 constructor(id,p={}){Object.assign(this,{id,tagName:'DIV',value:'',checked:false,hidden:false,disabled:false,children:[],listeners:{},validity:{badInput:false},_text:'',files:[]},p);this._text=p.text||'';}
 get value(){return this._value||''}set value(v){this._value=String(v)}
 addEventListener(n,f){(this.listeners[n]??=[]).push(f)} async emit(n,e={}){for(const f of this.listeners[n]||[])await f({target:this,preventDefault(){},...e})}
 get textContent(){return this._text+this.children.map(x=>x.textContent).join(' ')}set textContent(v){this._text=String(v);this.children=[]}
 replaceChildren(){this.children=[];this._text=''}append(x){this.children.push(x)}checkValidity(){return true}requestSubmit(){return this.emit('submit')}click(){this.clicked=true}focus(){}setAttribute(){}removeAttribute(){}
}
function setup(type,storage=new Map()){
 const source=fs.readFileSync(require('path').join(__dirname,type==='roof'?'../calculators/roof-replacement.html':'../projects.html'),'utf8');
 const attrs=s=>Object.fromEntries(Array.from(s.matchAll(/([\w-]+)(?:="([^"]*)")?/g),m=>[m[1],m[2]??'']));
 const schema={nodes:{},links:[]};
 for(const m of source.matchAll(/<(\w+)\b([^>]+)>/g)){
  const a=attrs(m[2]);if(a.id){
   const node={tagName:m[1].toUpperCase(),value:a.value||'',checked:'checked'in a,disabled:'disabled'in a,hidden:'hidden'in a,options:[]};
   if(m[1]==='select'){const body=source.slice(m.index+m[0].length).split('</select>')[0];node.options=Array.from(body.matchAll(/<option([^>]*)>/g),v=>{const o=attrs(v[1]);return{value:o.value||'',selected:'selected'in o}});node.value=(node.options.find(o=>o.selected)||node.options[0]||{}).value||'';}
   schema.nodes[a.id]=node;
  }
  if('data-project-link'in a)schema.links.push({href:a.href});
 }
const nodes=Object.fromEntries(Object.entries(schema.nodes).map(([id,p])=>[id,new E(id,p)]));const links=schema.links.map(l=>({...l}));const stats={events:[],confirms:0,failWrite:false};
 const localStorage={getItem:k=>storage.get(k)??null,setItem(k,v){if(stats.failWrite)throw Error('Storage full');storage.set(k,v)},removeItem:k=>storage.delete(k)};
 const document={getElementById:id=>nodes[id]||null,querySelectorAll:()=>links,createElement:t=>new E('',{tagName:t.toUpperCase()})};
 const window={document,localStorage,location:{search:'?hce_qa=1',origin:'https://homecostengine.com',pathname:type==='roof'?'/calculators/roof-replacement':'/projects.html'},console:{info:(...x)=>stats.events.push(x)},confirm:()=>{stats.confirms++;return stats.confirm!==false},setTimeout:f=>f(),print:()=>stats.printed=true};
 const U=class extends URL{};U.createObjectURL=b=>{stats.blob=b;return'blob:qa'};U.revokeObjectURL=()=>{};
 vm.runInNewContext(code,{window,URL:U,URLSearchParams,Blob,Intl,Date,Number,JSON,Error,String,Array,Object,Math,module:undefined});
 const form=nodes['roof-project-form'];return{nodes,stats,storage,links,async fill(id,value){nodes[id].value=value;if(form)await form.emit('input',{target:nodes[id]})},save:()=>form.emit('submit'),reload:()=>setup(type,storage)};
}
(async()=>{
 const key='hce_roof_project_v1';let s=setup('workspace');ok(!s.nodes['project-no-quotes'].hidden,'empty state');
 await s.fill('project-name','My roof');await s.fill('quote-name-0','A');await s.fill('quote-price-0','15000');await s.fill('quote-extra-0','1800');await s.fill('project-selected','0');await s.fill('project-reserve','1000');await s.fill('project-paid','3000');await s.fill('project-budget','20000');s.nodes['quote-open-0'].checked=true;await s.save();
 let out=s.nodes['project-budget-result'].textContent;ok(out.includes('$16,800.00')&&out.includes('$14,800.00')&&out.includes('$2,200.00'),'saved budget math');ok(out.includes('PROVISIONAL'),'unpriced scope warning');ok(s.storage.has(key),'explicit save stores');
 s=s.reload();ok(s.nodes['quote-price-0'].value==='15000','return restores');await s.fill('quote-price-1','16500');await s.fill('quote-extra-1','0');await s.save();ok(JSON.parse(s.storage.get(key)).quotes[1].extras===0,'second quote saved with explicit zero');ok(s.stats.events.some(x=>x[1]==='roof_second_quote_saved'),'QA second-quote event');
 const good=s.storage.get(key);await s.fill('quote-extra-1','');await s.save();ok(s.storage.get(key)===good,'invalid draft cannot overwrite good record');ok(!s.nodes['project-error'].hidden,'invalid error visible');await s.nodes['project-export'].emit('click');ok(!s.stats.blob,'unsaved export blocked');
 await s.fill('quote-extra-1','0');await s.save();await s.nodes['project-export'].emit('click');ok(JSON.parse(await s.stats.blob.text()).quotes[1].price===16500,'export roundtrip');
 s.stats.confirm=false;await s.nodes['project-delete'].emit('click');ok(s.storage.has(key),'cancel delete preserves');s.stats.confirm=true;const before=s.storage.get(key);await s.nodes['project-import'].emit('change',{target:{files:[{size:3,text:async()=>'{bad'}],value:''}});ok(s.storage.get(key)===before,'bad import does not destroy');
 s.stats.failWrite=true;await s.fill('project-name','Unsaved');await s.save();ok(s.storage.get(key)===before&&s.nodes['project-status'].textContent.includes('Unsaved'),'storage failure not reported saved');s.stats.failWrite=false;
 await s.nodes['project-delete'].emit('click');ok(!s.storage.has(key),'delete own record');const backup=before;await s.nodes['project-import'].emit('change',{target:{files:[{size:backup.length,text:async()=>backup}],value:''}});ok(s.storage.has(key)&&s.nodes['quote-price-1'].value==='16500','valid import restores');
 await s.fill('project-name','<img src=x onerror=alert(1)>');await s.save();ok(s.nodes['project-comparison-title'].textContent.startsWith('<img'),'user content assigned text, not HTML');
 const newer=JSON.parse(s.storage.get(key));newer.updatedAt='2099-01-01T00:00:00.000Z';s.storage.set(key,JSON.stringify(newer));await s.fill('project-name','Clobber');await s.save();ok(JSON.parse(s.storage.get(key)).updatedAt===newer.updatedAt&&s.nodes['project-error'].textContent.includes('another tab'),'concurrent tab change prevents clobber');
 const badStore=new Map([[key,'bad-json']]);const bad=setup('workspace',badStore);await bad.save();ok(badStore.get(key)==='bad-json','corrupt saved record never silently replaced');
 const roof=setup('roof',s.storage);roof.nodes.roofState.value='US';roof.nodes.roofState.options=[{value:'US'}];roof.nodes['result'].textContent='$18,000';roof.nodes['range'].textContent='$15,000–$21,000';await roof.nodes['calculatorForm'].emit('submit');ok(!roof.nodes['roof-save-project'].disabled,'calculated snapshot enabled');await roof.nodes['roof-save-project'].emit('click');let saved=JSON.parse(roof.storage.get(key));ok(saved.snapshot.mid===18000&&saved.quotes[1].price===16500,'snapshot preserves actual quotes');ok(!('localZip'in saved.snapshot.inputs),'no ZIP saved');
 roof.nodes.area.value='2400';await roof.nodes['calculatorForm'].emit('input');ok(roof.nodes['roof-save-project'].disabled,'stale save disabled');await roof.nodes['roof-restore-project'].emit('click');ok(roof.nodes.area.value==='2000','saved inputs restored after confirmation');ok(roof.nodes.localZip.value===''&&roof.nodes.localMetrics.hidden,'restore clears stale local ZIP data');ok(roof.links.every(l=>l.href.includes('hce_qa=1')),'QA stays on internal project links');
 console.log(count+' DOM-adapter assertions passed against actual feature code and parsed source IDs. No browser/layout/live test claimed.');
})().catch(e=>{console.error(e);process.exit(1)});
