import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';
const code=fs.readFileSync('assets/book-demand.js','utf8');
function run({qa=false,blog=false}={}){
 const events=[],logs=[],handlers={};
 const slug='home-energy-upgrade-savings-planner';
 const location={origin:'https://homecostengine.com',pathname:blog?'/blog/is-home-energy-audit-worth-it':'/ebooks/'+slug,search:qa?'?hce_qa=1&email=private@example.com':'?session_id=cs_private'};
 const document={querySelector:()=>blog?null:{dataset:{book:slug}},addEventListener:(n,f)=>handlers[n]=f};
 vm.runInNewContext(code,{URL,URLSearchParams,location,document,window:{gtag:(...a)=>events.push(a)},console:{info:(...a)=>logs.push(a)}});
 const click=(type,href,trusted=true)=>handlers.click({isTrusted:trusted,target:{closest:s=>s==='button[data-book]'?(type==='buy'?{dataset:{book:slug}}:null):s==='a[href]'?(href?{href}:null):null}});
 return {events,logs,click,slug};
}
let s=run();assert.equal(s.events[0][1],'book_detail_view');
s.click('buy',null,false);assert.equal(s.events.length,1);
s.click('preview','https://homecostengine.com/ebooks/'+s.slug+'#sample-pages');s.click('preview','https://homecostengine.com/ebooks/'+s.slug+'#sample-pages');assert.equal(s.events.filter(e=>e[1]==='book_preview_click').length,1);
s.click('buy');assert.equal(s.events.at(-1)[1],'book_checkout_click');
assert(!JSON.stringify(s.events).includes('cs_private'));
assert(s.events.every(e=>Object.keys(e[2]).sort().join(',')==='book_slug,measurement_version,page_path'));
s=run({qa:true});s.click('buy',null,false);assert.equal(s.events.length,0);assert(s.logs.length>0);assert(!JSON.stringify(s.logs).includes('private@example'));
s=run({blog:true});s.click('link','https://homecostengine.com/ebooks/'+s.slug+'.html#sample-pages');assert.equal(s.events[0][1],'book_article_click');s.click('link','https://external.example/ebooks/fake');assert.equal(s.events.length,1);
console.log('PASS: product/preview/checkout/article signals; preview dedup; synthetic exclusion; QA never emits GA; custom payload excludes queries and private data.');
