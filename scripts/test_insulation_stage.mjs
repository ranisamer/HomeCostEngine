import fs from 'node:fs';import vm from 'node:vm';import assert from 'node:assert/strict';import path from 'node:path';
const root=path.resolve(import.meta.dirname,'..'), read=f=>fs.readFileSync(path.join(root,f),'utf8');
const fixture=JSON.parse(read('books/drafts/insulation-integration.json'));
const augment=s=>s.replace(/const catalog=(\{.*?\});/s,(_,raw)=>{const c=JSON.parse(raw);c[fixture.slug]={...fixture};return 'const catalog='+JSON.stringify(c)+';';});
let purchase,posted;const fetchMock=async(u,o={})=>o.method==='POST'?(posted=new URLSearchParams(o.body),Response.json({id:'cs_live_mock',url:'https://checkout.stripe.com/mock'})):Response.json(purchase);
function load(f,extra={}){const ctx={Response,Request,URL,URLSearchParams,Uint8Array,atob,btoa,fetch:fetchMock,exports:{},...extra};vm.runInNewContext(augment(read(f)).replace(/^import .*?;\n/m,'').replace(/export async function (\w+)/g,'exports.$1 = async function $1'),ctx);return ctx.exports;}
const env={STRIPE_SECRET_KEY:'mock_only'},request=new Request('https://homecostengine.com/api/download-insulation-workbook?session_id=cs_live_mock');
const verify=load('functions/api/verify-purchase.js'),route=load('books/drafts/insulation-download.js',{verifyPurchase:verify.onRequestGet}),checkout=load('functions/api/create-checkout-session.js');
purchase={metadata:{book:fixture.slug},status:'open',payment_status:'unpaid'};assert.equal((await route.onRequestGet({request,env})).status,402);
purchase.payment_status='paid';assert.equal((await route.onRequestGet({request,env})).status,402);
purchase.status='complete';purchase.metadata.book='project-quote-mini-workbook';assert.equal((await route.onRequestGet({request,env})).status,403);
purchase.metadata.book=fixture.slug;const res=await route.onRequestGet({request,env});assert.equal(res.status,200);assert.equal(res.headers.get('cache-control'),'private, no-store');assert.deepEqual(Buffer.from(await res.arrayBuffer()),fs.readFileSync(path.join(root,'output/pdf/'+fixture.slug+'.pdf')));
assert.equal((await route.onRequestGet({request:new Request('https://homecostengine.com/api/download-insulation-workbook'),env})).status,400);
await checkout.onRequestPost({request:new Request('https://homecostengine.com/api/create-checkout-session',{method:'POST',body:JSON.stringify({book:fixture.slug,amount:1,currency:'usd'})}),env});
assert.equal(posted.get('line_items[0][price_data][currency]'),'gbp');assert.equal(posted.get('line_items[0][price_data][unit_amount]'),'799');
assert.ok(!read('functions/api/create-checkout-session.js').includes(fixture.slug));
console.log('PASS: isolated staged £7.99 checkout/paid+complete matching PDF/denials; live catalogs unmodified; no requests sent.');
