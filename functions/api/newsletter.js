const json=(data,status=200)=>new Response(JSON.stringify(data),{status,headers:{"content-type":"application/json; charset=utf-8","cache-control":"no-store"}});
const validEmail=v=>/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(String(v||"").trim());
export async function onRequestPost({request,env}){
 if(!env.BREVO_API_KEY||!env.BREVO_LIST_ID)return json({error:"Email signup is temporarily unavailable."},503);
 const origin=request.headers.get("Origin")||""; if(origin){try{const host=new URL(origin).hostname.replace(/^www\./,"").toLowerCase();const expected=String(env.SITE_HOST||"homecostengine.com").replace(/^www\./,"").toLowerCase();if(!(host===expected||host.endsWith(".pages.dev")))return json({error:"Invalid request origin."},403);}catch{return json({error:"Invalid request origin."},403);}}
 let body;try{body=await request.json();}catch{return json({error:"Invalid request."},400);}
 if(String(body.companyWebsite||"").trim())return json({ok:true});
 if(body.consent!==true)return json({error:"Please confirm that you want to receive email updates."},400);
 const email=String(body.email||"").trim().toLowerCase(); if(!validEmail(email)||email.length>254)return json({error:"Please enter a valid email address."},400);
 const headers={"api-key":env.BREVO_API_KEY,"content-type":"application/json","accept":"application/json"};
 const r=await fetch("https://api.brevo.com/v3/contacts",{method:"POST",headers,body:JSON.stringify({email,listIds:[Number(env.BREVO_LIST_ID)],updateEnabled:true,attributes:{LEAD_MAGNET:"HomeCostEngine Newsletter"}})});
 if(!r.ok){console.log("Brevo newsletter error",r.status,await r.text());return json({error:"We couldn't add you to the list right now."},502);}
 return json({ok:true});
}
export async function onRequest(){return json({error:"Method not allowed."},405);}