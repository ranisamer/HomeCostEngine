const json=(data,status=200)=>new Response(JSON.stringify(data),{status,headers:{"content-type":"application/json; charset=utf-8","cache-control":"no-store"}});

export async function onRequestPost({request,env}){
  if(!env.BREVO_API_KEY) return json({error:"Email service is not configured yet."},500);

  let body;
  try{body=await request.json();}catch{return json({error:"Invalid request."},400);}
  if(String(body.companyWebsite || "").trim()) return json({ok:true});

  const email=String(body.email || "").trim().toLowerCase();
  if(!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email) || email.length>254) return json({error:"Please enter a valid email address."},400);

  const origin=request.headers.get("Origin") || "";
  if(origin){
    try{
      const host=new URL(origin).hostname;
      const configured=String(env.SITE_HOST || "homecostengine.com").replace(/^www\./,"").toLowerCase();
      const normalized=host.replace(/^www\./,"").toLowerCase();
      if(!(normalized===configured || host.endsWith(".pages.dev"))) return json({error:"Invalid request origin."},403);
    }catch{return json({error:"Invalid request origin."},403);}
  }

  const listId=Number(env.BREVO_PRO_LIST_ID || env.BREVO_LIST_ID || 0);
  if(!listId) return json({error:"Project Pro waitlist is not configured yet."},500);

  const response=await fetch("https://api.brevo.com/v3/contacts",{
    method:"POST",
    headers:{"api-key":env.BREVO_API_KEY,"content-type":"application/json","accept":"application/json"},
    body:JSON.stringify({email,listIds:[listId],updateEnabled:true})
  });

  if(!response.ok){
    console.log("Brevo waitlist error",response.status,await response.text());
    return json({error:"We couldn't add you to the waitlist right now. Please try again shortly."},502);
  }
  return json({ok:true});
}

export async function onRequest(){return json({error:"Method not allowed."},405);}