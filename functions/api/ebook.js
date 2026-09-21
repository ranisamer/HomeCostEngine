const json = (data, status=200) => new Response(JSON.stringify(data), {
  status,
  headers:{"content-type":"application/json; charset=utf-8","cache-control":"no-store"}
});

const validEmail = value => /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(String(value || "").trim());

export async function onRequestPost({request, env}){
  if(!env.BREVO_API_KEY) return json({error:"Email delivery is temporarily unavailable. You can still use the direct download link."},503);

  const origin=request.headers.get("Origin") || "";
  if(origin){
    try{
      const host=new URL(origin).hostname.replace(/^www\./,"").toLowerCase();
      const expected=String(env.SITE_HOST || "homecostengine.com").replace(/^www\./,"").toLowerCase();
      if(!(host===expected || host.endsWith(".pages.dev"))) return json({error:"Invalid request origin."},403);
    }catch{return json({error:"Invalid request origin."},403);}
  }

  let body;
  try{body=await request.json();}catch{return json({error:"Invalid request."},400);}
  if(String(body.companyWebsite || "").trim()) return json({ok:true});

  const email=String(body.email || "").trim().toLowerCase();
  if(!validEmail(email) || email.length>254) return json({error:"Please enter a valid email address."},400);

  const downloadUrl="https://homecostengine.com/assets/guides/home-project-cost-planning-guide.pdf";
  const headers={"api-key":env.BREVO_API_KEY,"content-type":"application/json","accept":"application/json"};

  if(body.marketingConsent===true && env.BREVO_LIST_ID){
    const contact=await fetch("https://api.brevo.com/v3/contacts",{
      method:"POST",headers,
      body:JSON.stringify({email,listIds:[Number(env.BREVO_LIST_ID)],updateEnabled:true,attributes:{LEAD_MAGNET:"Home Project Cost Planning Guide"}})
    });
    if(!contact.ok) console.log("Brevo ebook contact error",contact.status,await contact.text());
  }

  const senderEmail=String(env.BREVO_SENDER_EMAIL || "reports@mail.homecostengine.com").trim();
  const replyToEmail=String(env.BREVO_REPLY_TO || "reports@homecostengine.com").trim();
  const html=`<!doctype html><html><body style="margin:0;background:#f5f6f4;font-family:Arial,sans-serif;color:#102033"><div style="max-width:640px;margin:auto;padding:28px 16px"><div style="background:#102033;color:#fff;padding:30px;border-radius:20px"><div style="color:#80d3c2;font-size:12px;font-weight:800;letter-spacing:.08em">HOMECOSTENGINE FREE GUIDE</div><h1 style="font-size:30px;margin:10px 0">Your planning guide is ready</h1><p style="color:#d1dae3;line-height:1.65">Build a clearer home-project budget, compare contractor proposals and protect your contingency.</p></div><div style="background:#fff;border:1px solid #e2e7eb;border-radius:20px;padding:26px;margin-top:16px;text-align:center"><p style="line-height:1.6">Download the 14-page U.S. Home Project Cost Planning Guide below.</p><a href="${downloadUrl}" style="display:inline-block;background:#176b5b;color:#fff;text-decoration:none;font-weight:800;padding:14px 20px;border-radius:999px">Download the free PDF</a><p style="font-size:12px;color:#687687;margin-top:18px">The guide is for planning information only. Verify local prices, permits, code requirements and scope with qualified professionals.</p></div></div></body></html>`;

  const sent=await fetch("https://api.brevo.com/v3/smtp/email",{
    method:"POST",headers,
    body:JSON.stringify({sender:{name:"HomeCostEngine",email:senderEmail},to:[{email}],replyTo:{name:"HomeCostEngine",email:replyToEmail},subject:"Your free Home Project Cost Planning Guide",htmlContent:html})
  });
  if(!sent.ok){console.log("Brevo ebook send error",sent.status,await sent.text());return json({error:"We couldn't send the email right now. Please use the direct download link."},502);}
  return json({ok:true,downloadUrl,subscribed:body.marketingConsent===true});
}

export async function onRequest(){return json({error:"Method not allowed."},405);}
