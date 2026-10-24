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
async function send({signature=true,age=0,tamper=false,type='checkout.session.completed',live=true}={}){
  const body=JSON.stringify({type,livemode:live,data:{object:{id:'cs_live_mock',customer_email:'attacker@example.invalid'}}});
  const t=Math.floor(Date.now()/1000)-age;
  const sig=createHmac('sha256',env.STRIPE_WEBHOOK_SECRET).update(t+'.'+body).digest('hex');
  return hook.onRequestPost({env,request:new Request('https://homecostengine.com/api/stripe-webhook',{method:'POST',headers:signature?{'stripe-signature':`t=${t},v1=${sig}`}:{},body:tamper?body+' ':body})});
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
