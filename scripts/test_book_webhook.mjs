import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
import {webcrypto,createHmac} from 'node:crypto';
import path from 'node:path';
const root=path.resolve(import.meta.dirname,'..');
let purchase,mailCount=0,mail,failMail=false,failMarker=false,duplicateMail=false;
const env={STRIPE_SECRET_KEY:'sk_live_mock_only',STRIPE_WEBHOOK_SECRET:'whsec_mock_only',BREVO_API_KEY:'mock_only'};
const fetchMock=async(url,options={})=>{
  if(url.startsWith('https://api.brevo.com/')){
    mailCount++;mail=JSON.parse(options.body);
    if(failMail)return Response.json({code:'unavailable'},{status:503});
    if(duplicateMail)return Response.json({code:'duplicate_parameter',message:'idempotencyKey already processed'},{status:400});
    return Response.json({messageId:'mock-provider-acceptance'});
  }
  if(options.method==='POST'){
    if(failMarker)return Response.json({error:'mock failure'},{status:503});
    purchase.metadata.hce_delivery_email_sent_at=new URLSearchParams(options.body).get('metadata[hce_delivery_email_sent_at]');
    return Response.json(purchase);
  }
  return Response.json(purchase);
};
const globals={Response,Request,URL,URLSearchParams,Uint8Array,TextEncoder,crypto:webcrypto,atob,btoa,Intl,console,fetch:fetchMock};
const load=(file,extra={})=>{const ctx={...globals,...extra,exports:{}};vm.runInNewContext(fs.readFileSync(path.join(root,file),'utf8').replace(/^import .*?;\n/m,'').replace(/export async function (\w+)/g,'exports.$1 = async function $1'),ctx);return ctx.exports;};
const verify=load('functions/api/verify-purchase.js');
const hook=load('functions/api/stripe-webhook.js',{verifyPurchase:verify.onRequestGet});
function reset(){purchase={metadata:{book:'project-quote-mini-workbook'},livemode:true,payment_status:'paid',status:'complete',customer_details:{email:'owner@example.invalid'},amount_total:50,currency:'gbp'};mailCount=0;failMail=false;failMarker=false;duplicateMail=false;}
async function send({signature=true,age=0,tamper=false,type='checkout.session.completed',live=true,signingSecret=env.STRIPE_WEBHOOK_SECRET,headerOverride}={}){
  const body=JSON.stringify({type,livemode:live,data:{object:{id:'cs_live_mock',customer_email:'attacker@example.invalid'}}});
  const t=Math.floor(Date.now()/1000)-age;
  const sig=createHmac('sha256',signingSecret).update(t+'.'+body).digest('hex');
  return hook.onRequestPost({env,request:new Request('https://homecostengine.com/api/stripe-webhook',{method:'POST',headers:signature?{'stripe-signature':headerOverride??`t=${t},v1=${sig}`}:{},body:tamper?body+' ':body})});
}
reset();assert.equal((await send({signature:false})).status,400);assert.equal(mailCount,0);
assert.equal((await send({tamper:true})).status,400);assert.equal((await send({age:600})).status,400);
assert.equal((await send({live:false})).status,200);assert.equal(mailCount,0);
assert.equal((await send({type:'charge.failed'})).status,200);assert.equal(mailCount,0);
purchase.payment_status='unpaid';assert.equal((await send()).status,200);assert.equal(mailCount,0);
reset();assert.equal((await send()).status,200);assert.equal(mailCount,1);
assert.equal(mail.to[0].email,'owner@example.invalid');
assert.ok(mail.subject.includes('Project Quote Mini Workbook'));assert.ok(mail.textContent.includes('£0.50'));
assert.ok(mail.htmlContent.includes('/ebooks/success.html?session_id=cs_live_mock'));
assert.ok(!('listIds' in mail));assert.ok(purchase.metadata.hce_delivery_email_sent_at);
assert.equal((await send()).status,200);assert.equal(mailCount,1);
reset();failMail=true;assert.equal((await send()).status,503);assert.ok(!purchase.metadata.hce_delivery_email_sent_at);
reset();failMarker=true;assert.equal((await send()).status,503);const key=mail.headers.idempotencyKey;
failMarker=false;duplicateMail=true;assert.equal((await send()).status,200);assert.equal(mail.headers.idempotencyKey,key);
reset();purchase.metadata.book='unknown';assert.equal((await send()).status,200);assert.equal(mailCount,0);
reset();purchase.customer_details.email='';assert.equal((await send()).status,503);assert.equal(mailCount,0);
const readiness=await hook.onRequestGet({env:{}});assert.equal(readiness.status,503);
assert.deepEqual((await readiness.json()).missing,['STRIPE_SECRET_KEY','STRIPE_WEBHOOK_SECRET','BREVO_API_KEY']);
console.log('PASS: raw signature/timestamp; re-fetched buyer; live paid-only delivery; book/price/link; retry/deduplication; missing config; no marketing contact or external send.');


reset();
assert.equal((await (await send({signature:false})).json()).code,'signature_header_missing');
assert.equal((await (await send({tamper:true})).json()).code,'signature_mismatch');
assert.equal((await (await send({age:600})).json()).code,'signature_timestamp_outside_tolerance');
assert.equal((await (await send({age:-600})).json()).code,'signature_timestamp_outside_tolerance');
assert.equal((await (await send({headerOverride:'t=bad,v1=00'})).json()).code,'signature_timestamp_invalid');
assert.equal((await (await send({headerOverride:'t='+Math.floor(Date.now()/1000)+',v1=bad'})).json()).code,'signature_v1_missing_or_invalid');
const originalSecret=env.STRIPE_WEBHOOK_SECRET;
env.STRIPE_WEBHOOK_SECRET=' \n'+originalSecret+'\r\n ';
assert.equal((await send({signingSecret:originalSecret})).status,200);
reset();env.STRIPE_WEBHOOK_SECRET='not-a-webhook-secret';
const invalid=await send();assert.equal(invalid.status,503);
const invalidBody=await invalid.text();assert.ok(!invalidBody.includes(env.STRIPE_WEBHOOK_SECRET));
assert.equal(JSON.parse(invalidBody).code,'webhook_secret_format_invalid');
assert.equal(mailCount,0);
env.STRIPE_WEBHOOK_SECRET=originalSecret;
console.log('PASS: secret boundary whitespace normalized; distinct diagnostics; stale/future/tampered/malformed headers denied; no secret disclosure.');
reset();purchase.metadata.book='smart-home-renovation-budget-blueprint';purchase.amount_total=900;
const firstBookMail=await send();assert.equal(firstBookMail.status,200);assert.equal(mailCount,1);
assert.ok(mail.subject.includes('The Smart Home Renovation Budget Blueprint'));assert.ok(mail.textContent.includes('£9.00'));
assert.ok(mail.textContent.includes('/ebooks/success.html?session_id=cs_live_mock'));
assert.equal((await send()).status,200);assert.equal(mailCount,1);
console.log('PASS: first-book signed webhook produces correct £9 thank-you and verified order link; retries deduplicate. Mock provider only.');

// Every catalog product uses the same verified transactional delivery path.
const checkoutCatalog=JSON.parse(fs.readFileSync(path.join(root,'functions/api/create-checkout-session.js'),'utf8').match(/const catalog=(\{.*?\});/s)[1]);
for(const [slug,book] of Object.entries(checkoutCatalog)){
 reset();purchase.metadata.book=slug;purchase.amount_total=book.amount||900;
 assert.equal((await send()).status,200,slug);assert.equal(mailCount,1,slug);
 assert.ok(mail.subject.includes(book.title),slug+' title');
 assert.ok(mail.textContent.includes('/ebooks/success.html?session_id=cs_live_mock'),slug+' private order URL');
 assert.ok(mail.textContent.includes(new Intl.NumberFormat('en-GB',{style:'currency',currency:'GBP'}).format(purchase.amount_total/100)),slug+' amount');
 assert.ok(mail.htmlContent.includes('positive or negative'),slug+' neutral feedback');
 assert.equal((await send()).status,200);assert.equal(mailCount,1,slug+' deduplication');
}
console.log('PASS: all 23 products (22 books + mini) thank buyer with correct title, GBP amount, private order link and neutral feedback; retries deduplicate. No external send.');
