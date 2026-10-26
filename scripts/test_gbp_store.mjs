import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
import path from 'node:path';
const root = path.resolve(import.meta.dirname, '..');
const read = p => fs.readFileSync(path.join(root,p),'utf8');
let stripeSession, posted;
const mockFetch = async (url, options={}) => {
  if(options.method==='POST') { posted=new URLSearchParams(options.body); return Response.json({url:'https://checkout.stripe.com/mock',id:'cs_test_mock'}); }
  return Response.json(stripeSession);
};
const context = {exports:{}, Response, Request, URL, URLSearchParams, Uint8Array, atob, btoa, console, fetch:mockFetch};
function load(p, extras={}) {
  const code=read(p).replace(/^import .*?;\n/m,'').replace(/export async function (\w+)/g,'exports.$1 = async function $1');
  const ctx={...context,...extras,exports:{}}; vm.runInNewContext(code,ctx); return ctx.exports;
}
const checkout=load('functions/api/create-checkout-session.js');
const verify=load('functions/api/verify-purchase.js');
const download=load('functions/api/download-mini-guide.js',{verifyPurchase:verify.onRequestGet});
const catalog=JSON.parse(read('functions/api/create-checkout-session.js').match(/const catalog=(\{.*?\});/s)[1]);
const env={STRIPE_SECRET_KEY:'mock-only-not-a-key'};
for(const [slug,book] of Object.entries(catalog)) {
  const request=new Request('https://homecostengine.com/api/create-checkout-session',{method:'POST',body:JSON.stringify({book:slug,amount:1,currency:'usd'})});
  assert.equal((await checkout.onRequestPost({request,env})).status,200);
  assert.equal(posted.get('line_items[0][price_data][currency]'),'gbp');
  assert.equal(posted.get('line_items[0][price_data][unit_amount]'),String(book.amount||900));
  assert.equal(posted.get('adaptive_pricing[enabled]'),'false');
  assert.equal(posted.get('line_items[0][price_data][tax_behavior]'),'inclusive');
  const html=read('ebooks/'+slug+'.html');
  const price='£'+((book.amount||900)%100===0?String((book.amount||900)/100):((book.amount||900)/100).toFixed(2));
  assert.ok(html.includes(price),slug+' visible price');
  const sellingPanels=[...html.matchAll(/<section[^>]*class="[^"]*ebook-(?:top-buy-panel|bottom-buy)[^"]*"[^>]*>[\s\S]*?<\/section>/g)].map(m=>m[0]);
  assert.ok(sellingPanels.length>0||slug==='project-quote-mini-workbook',slug+' selling panels found');
  assert.ok(sellingPanels.every(panel=>!/\bUSD\b|\$\d/.test(panel)),slug+' no USD selling price');
  for(const m of html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g))check(JSON.parse(m[1]),book);
}
assert.equal(Object.keys(catalog).length,22);
const request=new Request('https://homecostengine.com/api/download-mini-guide?session_id=cs_test_mock');
stripeSession={metadata:{book:'project-quote-mini-workbook'},payment_status:'unpaid',status:'open'};
assert.equal((await download.onRequestGet({request,env})).status,402);
stripeSession={metadata:{book:'roof-replacement-planning-handbook'},payment_status:'paid',status:'complete'};
assert.equal((await download.onRequestGet({request,env})).status,403);
stripeSession={metadata:{book:'project-quote-mini-workbook'},payment_status:'paid',status:'complete'};
const response=await download.onRequestGet({request,env});
assert.equal(response.status,200);assert.equal(response.headers.get('content-type'),'application/pdf');
const bytes=Buffer.from(await response.arrayBuffer());
assert.ok(bytes.subarray(0,5).toString()==='%PDF-');
assert.deepEqual(bytes,fs.readFileSync(path.join(root,'output/pdf/project-quote-mini-workbook.pdf')));
assert.equal(response.headers.get('cache-control'),'private, no-store');
assert.equal((await download.onRequestGet({request:new Request('https://homecostengine.com/api/download-mini-guide'),env})).status,400);
// Existing paid USD orders remain downloadable.
stripeSession={metadata:{book:'roof-replacement-planning-handbook'},payment_status:'paid',status:'complete',currency:'usd'};
assert.equal((await verify.onRequestGet({request,env})).status,200);
for(const file of fs.readdirSync(path.join(root,'ebooks')).filter(p=>p.endsWith('.html'))) {
  const html=read('ebooks/'+file);
  for(const m of html.matchAll(/<script([^>]*)>([\s\S]*?)<\/script>/g)) {
    if(m[1].includes('application/ld+json'))JSON.parse(m[2]);
    else if(m[2].trim()) new vm.Script(m[2]);
  }
}
const library=read('ebooks/index.html');
const data=JSON.parse(library.match(/<script type="application\/ld\+json">(.*?)<\/script>/s)[1]);
function check(obj, book) {
  if(!obj||typeof obj!=='object')return;
  const slug=obj.url?.split('/').at(-1).replace('.html','');
  book=catalog[slug]||book;
  if(obj['@type']==='Offer'){assert.equal(obj.priceCurrency,'GBP');assert.equal(Number(obj.price),(book.amount||900)/100);}
  for(const v of Object.values(obj))check(v,book);
}
check(data);
assert.ok(!read('index.html').includes('projectSliderTitle'));
assert.ok(read('ebooks/project-quote-mini-workbook.html').includes('data-mini-workbook="true"'));
console.log('PASS: 22 GBP prices; fixed currency; schema/inline JS; paid/unpaid/invalid/wrong-product PDF; legacy paid orders; carousel removed. No real payment performed.');
