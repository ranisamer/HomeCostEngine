import { onRequestGet as verifyPurchase } from './verify-purchase.js';

const json=(data,status=200)=>new Response(JSON.stringify(data),{status,headers:{'content-type':'application/json','cache-control':'no-store'}});
const escapeHtml=value=>String(value).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const required=['STRIPE_SECRET_KEY','STRIPE_WEBHOOK_SECRET','BREVO_API_KEY'];

// Diagnostics reveal only failure categories, never keys, signatures or raw payloads.
async function checkSignature(raw,header,configuredSecret) {
  const secret=String(configuredSecret||'').trim();
  if(!/^whsec_[A-Za-z0-9_-]+$/.test(secret))return {ok:false,code:'webhook_secret_format_invalid',status:503};
  if(!header)return {ok:false,code:'signature_header_missing',status:400};
  const fields=header.split(',').map(part=>part.trim().split('='));
  const timestamp=fields.find(([key])=>key==='t')?.[1];
  if(!/^\d+$/.test(timestamp||''))return {ok:false,code:'signature_timestamp_invalid',status:400};
  const ageSeconds=Math.round(Date.now()/1000-Number(timestamp));
  if(Math.abs(ageSeconds)>300)return {ok:false,code:'signature_timestamp_outside_tolerance',status:400,ageSeconds};
  const signatures=fields.filter(([name,value])=>name==='v1'&&/^([a-f0-9]{2}){32}$/i.test(value||''));
  if(!signatures.length)return {ok:false,code:'signature_v1_missing_or_invalid',status:400};
  const key=await crypto.subtle.importKey('raw',new TextEncoder().encode(secret),{name:'HMAC',hash:'SHA-256'},false,['verify']);
  const payload=new TextEncoder().encode(timestamp+'.'+raw);
  for(const [,value] of signatures) {
    const bytes=Uint8Array.from(value.match(/../g),v=>parseInt(v,16));
    if(await crypto.subtle.verify('HMAC',key,bytes,payload))return {ok:true};
  }
  return {ok:false,code:'signature_mismatch',status:400};
}

export async function onRequestPost({request,env}) {
  if(required.some(name=>!env[name]))return json({error:'Transactional delivery is not configured.'},503);
  const raw=await request.text();
  if(raw.length>262144)return json({error:'Event too large.'},413);
  const signature=await checkSignature(raw,request.headers.get('stripe-signature')||'',env.STRIPE_WEBHOOK_SECRET);
  if(!signature.ok)return json({error:'Invalid signature.',code:signature.code,...(signature.ageSeconds!==undefined?{ageSeconds:signature.ageSeconds}:{}),revision:'signature-diagnostics-1'},signature.status);
  let event;
  try{event=JSON.parse(raw);}catch{return json({error:'Invalid event.'},400);}
  if(!['checkout.session.completed','checkout.session.async_payment_succeeded'].includes(event.type))return json({received:true,ignored:true});
  if(String(env.STRIPE_SECRET_KEY).startsWith('sk_live_')&&event.livemode!==true)return json({received:true,ignored:true});
  const id=event.data?.object?.id;
  if(!/^cs_[A-Za-z0-9_]+$/.test(id||''))return json({error:'Invalid session.'},400);

  // Never fulfill from a redirect, browser-supplied amount or unverified event payload.
  const verification=await verifyPurchase({env,request:new Request('https://homecostengine.com/api/verify-purchase?session_id='+encodeURIComponent(id))});
  if(verification.status===402)return json({received:true,pending:true});
  if(verification.status===400)return json({received:true,ignored:true});
  if(!verification.ok)return json({error:'Purchase lookup failed; retry delivery.'},503);
  const purchase=await verification.json();
  if(String(env.STRIPE_SECRET_KEY).startsWith('sk_live_')&&purchase.livemode!==true)return json({received:true,ignored:true});
  if(purchase.emailDeliveryAcceptedAt)return json({received:true,alreadyAccepted:true});
  const email=purchase.customerEmail;
  if(!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email||''))return json({error:'Paid order has no deliverable email.'},503);
  const orderUrl='https://homecostengine.com/ebooks/success.html?session_id='+encodeURIComponent(id);
  const title=escapeHtml(purchase.title);
  const money=typeof purchase.amountTotal==='number'&&purchase.currency?new Intl.NumberFormat('en-GB',{style:'currency',currency:purchase.currency.toUpperCase()}).format(purchase.amountTotal/100):'';
  // Stable UUID per session: provider deduplication supplements the persistent Stripe metadata marker.
  const hash=Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256',new TextEncoder().encode('hce-book-'+id)))).map(b=>b.toString(16).padStart(2,'0')).join('');
  const uuid=hash.slice(0,8)+'-'+hash.slice(8,12)+'-4'+hash.slice(13,16)+'-a'+hash.slice(17,20)+'-'+hash.slice(20,32);
  const message={
    sender:{name:'HomeCostEngine',email:String(env.BREVO_SENDER_EMAIL||'reports@mail.homecostengine.com').trim()},
    replyTo:{name:'HomeCostEngine',email:String(env.BREVO_REPLY_TO||'reports@homecostengine.com').trim()},
    to:[{email}],
    subject:'Thank you - your '+purchase.title+' is ready',
    headers:{idempotencyKey:uuid},
    tags:['book-order'],
    textContent:'Thank you for your purchase.\n\nYour book: '+purchase.title+(money?'\nPaid: '+money:'')+'\n\nDownload your PDF from your private order page:\n'+orderUrl+'\n\nSave the PDF and keep this link private. Start with the contents and choose the section that matches your next project decision. If you need help, reply to this email. You can also reply with honest feedback, positive or negative; no reward or positive rating is requested. This is an order delivery email, not a marketing subscription.\nHomeCostEngine',
    htmlContent:'<!doctype html><html><body style="background:#f3f6f6;color:#172c3a;font-family:Arial,sans-serif;padding:24px"><div style="max-width:600px;margin:auto;background:white;border-radius:16px;padding:30px"><p style="color:#166d70;font-weight:bold">HOMECOSTENGINE · YOUR ORDER</p><h1>Thank you for your purchase!</h1><p>Your payment has been confirmed. Your digital book is ready:</p><h2>'+title+'</h2>'+(money?'<p>Paid: <strong>'+escapeHtml(money)+'</strong></p>':'')+'<p><a href="'+orderUrl+'" style="display:inline-block;background:#166d70;color:white;text-decoration:none;padding:14px 22px;border-radius:8px">Download your book</a></p><p>The link opens your private order page and PDF download. Save your PDF and keep this link private.</p><h3>Start with your next decision</h3><p>Save a copy of the PDF, open the contents and choose the section that matches the next decision on your project.</p><p>Need help? Reply to this email and we will help with your order.</p><p>After reading, you are welcome to reply with honest feedback, positive or negative. We do not require a positive rating or offer a reward. Feedback is not published as a customer review without your permission.</p><p style="font-size:12px;color:#526372">For personal use only. This transactional email delivers your purchase; it does not subscribe you to marketing.</p></div></body></html>'
  };
  let sent;
  try{sent=await fetch('https://api.brevo.com/v3/smtp/email',{method:'POST',headers:{'api-key':env.BREVO_API_KEY,'content-type':'application/json','accept':'application/json'},body:JSON.stringify(message)});}catch{return json({error:'Email provider unavailable; retry delivery.'},503);}
  let result={};try{result=await sent.json();}catch{}
  if(!sent.ok&&!(result.code==='duplicate_parameter'&&/idempotenc/i.test(result.message||'')))return json({error:'Email was not accepted; retry delivery.'},503);
  const params=new URLSearchParams();params.set('metadata[hce_delivery_email_sent_at]',new Date().toISOString());
  const marked=await fetch('https://api.stripe.com/v1/checkout/sessions/'+encodeURIComponent(id),{method:'POST',headers:{authorization:'Basic '+btoa(String(env.STRIPE_SECRET_KEY)+':'),'content-type':'application/x-www-form-urlencoded'},body:params});
  if(!marked.ok)return json({error:'Email accepted but delivery marker failed; retry reconciliation.'},503);
  // Provider acceptance is not a verified inbox delivery. No contacts/list API is called.
  return json({received:true,emailAccepted:true});
}

export async function onRequestGet({env}) {
  const missing=required.filter(name=>!env[name]);
  return json({revision:'signature-diagnostics-1',configured:missing.length===0,missing,mode:'transactional book delivery',note:'Configuration does not establish webhook registration or inbox delivery.'},missing.length?503:200);
}
export async function onRequest(){return json({error:'Method not allowed.'},405);}

