import fs from 'node:fs';
import vm from 'node:vm';
import path from 'node:path';
import assert from 'node:assert/strict';
const root=path.resolve(import.meta.dirname,'..');
const read=f=>fs.readFileSync(path.join(root,f),'utf8');
let purchase,posted;
const fetchMock=async(url,options={})=>{
 if(options.method==='POST'){posted=new URLSearchParams(options.body);return Response.json({url:'https://checkout.stripe.com/mock',id:'cs_live_mock_only'});}
 return Response.json(purchase);
};
const globals={Request,Response,URL,URLSearchParams,Uint8Array,atob,btoa,console,fetch:fetchMock};
function load(file,extras={}){const ctx={...globals,...extras,exports:{}};vm.runInNewContext(read(file).replace(/^import .*?;\n/m,'').replace(/export async function (\w+)/g,'exports.$1 = async function $1'),ctx);return ctx.exports;}
const verify=load('functions/api/verify-purchase.js');
const book=load('functions/api/download-deck-guide.js',{verifyPurchase:verify.onRequestGet});
const mini=load('functions/api/download-mini-guide.js',{verifyPurchase:verify.onRequestGet});
const checkout=load('functions/api/create-checkout-session.js');
const env={STRIPE_SECRET_KEY:'mock_only_not_a_credential'};
const slug='deck-outdoor-living-cost-planner';
const request=new Request('https://homecostengine.com/api/download-deck-guide?session_id=cs_live_mock_only');
purchase={metadata:{book:slug},payment_status:'unpaid',status:'open'};
assert.equal((await book.onRequestGet({request,env})).status,402);
purchase.payment_status='paid';assert.equal((await book.onRequestGet({request,env})).status,402);
purchase.status='complete';purchase.metadata.book='project-quote-mini-workbook';
assert.equal((await book.onRequestGet({request,env})).status,403);
assert.equal((await mini.onRequestGet({request,env})).status,200);
purchase.metadata.book=slug;
assert.equal((await mini.onRequestGet({request,env})).status,403);
const entitlement=await (await verify.onRequestGet({request,env})).json();
assert.equal(entitlement.downloadUrl,'/api/download-deck-guide?session_id=cs_live_mock_only');
const delivered=await book.onRequestGet({request,env});assert.equal(delivered.status,200);
assert.equal(delivered.headers.get('content-type'),'application/pdf');
assert.equal(delivered.headers.get('cache-control'),'private, no-store');
assert.equal(delivered.headers.get('x-robots-tag'),'noindex, nofollow');
assert.deepEqual(Buffer.from(await delivered.arrayBuffer()),fs.readFileSync(path.join(root,'output/deck-outdoor-living-cost-planner.pdf')));
assert.equal((await book.onRequestGet({request:new Request('https://homecostengine.com/api/download-deck-guide'),env})).status,400);
assert.equal((await book.onRequestGet({request,env:{}})).status,503);
assert.equal((await book.onRequest()).status,405);
for(const s of [slug,'project-quote-mini-workbook']){
 const r=await checkout.onRequestPost({request:new Request('https://homecostengine.com/api/create-checkout-session',{method:'POST',body:JSON.stringify({book:s,amount:1,currency:'usd'})}),env});assert.equal(r.status,200);
 assert.equal(posted.get('line_items[0][price_data][currency]'),'gbp');assert.equal(posted.get('adaptive_pricing[enabled]'),'false');
 assert.equal(posted.get('line_items[0][price_data][unit_amount]'),s===slug?'1099':'50');
 if(s===slug)assert.match(posted.get('line_items[0][price_data][product_data][description]'),/64-page/);
}
for(const f of ['ebooks/'+slug+'.html','ebooks/index.html']){
 const html=read(f);for(const m of html.matchAll(/<script([^>]*)>([\s\S]*?)<\/script>/g)){
  if(m[1].includes('application/ld+json')){const schema=JSON.parse(m[2]);if(schema['@type']==='Book'){assert.equal(schema.numberOfPages,64);assert.equal(schema.offers.priceCurrency,'GBP');assert.equal(schema.offers.price,'10.99');}}
  else if(m[2].trim())new vm.Script(m[2]);
 }
}
for(const f of ['assets/app.js','assets/ebook-preview.js'])new vm.Script(read(f));
const html=read('ebooks/'+slug+'.html');assert.ok(!html.includes('104'));assert.ok(!html.includes('4.8'));assert.ok(html.includes('data-real-pdf-preview="true"'));assert.ok(html.includes('id="buy-book"'));
console.log('PASS: paid/complete/right-product PDF equals reviewed artifact; missing/unpaid/wrong-product denial; mini regression; server-controlled £10.99 GBP/64-page checkout; schema/JS/real samples. No external payment or email.');
