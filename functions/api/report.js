const json = (data, status=200) =>
  new Response(JSON.stringify(data), {status,headers:{"content-type":"application/json; charset=utf-8","cache-control":"no-store"}});

const esc = (v="") => String(v).replaceAll("&","&amp;").replaceAll("<","&lt;").replaceAll(">","&gt;").replaceAll('"',"&quot;").replaceAll("'","&#039;");
const finite = (v,min=0,max=1e15) => {const x=Number(v);if(!Number.isFinite(x)) return NaN;return Math.max(min,Math.min(x,max));};
const money = v => "$" + Number(v || 0).toLocaleString("en-US",{minimumFractionDigits:0,maximumFractionDigits:0});
const number = (v,digits=2) => Number(v || 0).toLocaleString("en-US",{minimumFractionDigits:digits,maximumFractionDigits:digits});

function calculate(type, raw={}){
  if(type==="roof"){
    const area=finite(raw.area,1,1e8); if(!Number.isFinite(area)) throw new Error("Enter a valid roof area before sending the report.");
    const ranges={asphalt:[5.5,9],metal:[9,16],tile:[10,20],wood:[7,14],slate:[15,30]};
    const material=String(raw.material||"asphalt"); if(!ranges[material]) throw new Error("Choose a valid roofing material.");
    const pitch=finite(raw.pitch,.5,3), stories=finite(raw.stories,.5,3), market=finite(raw.market,.5,3);
    if(!Number.isFinite(pitch)||!Number.isFinite(stories)||!Number.isFinite(market)) throw new Error("Check the roof complexity and market selections.");
    let [lo,hi]=ranges[material]; lo*=pitch*stories*market; hi*=pitch*stories*market; if(String(raw.tearoff||"yes")==="yes"){lo+=1.15;hi+=2.35}
    const low=area*lo, high=area*hi, mid=(low+high)/2;
    return {title:"Roof Replacement Cost Report",subject:`Your roof cost estimate: ${money(low)}–${money(high)}`,url:"https://homecostengine.com/calculators/roof-replacement.html",
      summary:`Your planning range is ${money(low)} to ${money(high)}, with a midpoint of about ${money(mid)}.`,
      metrics:[["Roof area",`${Math.round(area).toLocaleString("en-US")} sq ft`],["Roofing material",material==="asphalt"?"Asphalt shingles":material.charAt(0).toUpperCase()+material.slice(1)],["Estimated range",`${money(low)} – ${money(high)}`],["Midpoint",money(mid)],["Estimated installed unit range",`${money(lo)} – ${money(hi)} / sq ft`]],
      note:"This is a budgeting range. Decking repairs, flashing, ventilation, permits, access, warranty terms and local labor can change a real contractor quote."};
  }
  if(type==="concrete"){
    const l=finite(raw.length,.01,1e6), w=finite(raw.width,.01,1e6), t=finite(raw.thickness,.01,1e4), waste=finite(raw.waste,1,2), price=finite(raw.yardPrice,0,1e7);
    if(![l,w,t,waste].every(Number.isFinite)) throw new Error("Enter valid concrete dimensions before sending the report.");
    const yards=(l*w*(t/12))/27*waste, cost=Number.isFinite(price)&&price>0?yards*price:null;
    return {title:"Concrete Calculator Report",subject:`Your concrete estimate: ${number(yards,2)} yd³`,url:"https://homecostengine.com/calculators/concrete.html",
      summary:`Your project needs about ${number(yards,2)} cubic yards of concrete including your selected waste allowance.`,
      metrics:[["Surface area",`${Math.round(l*w).toLocaleString("en-US")} sq ft`],["Thickness",`${number(t,1)} in`],["Concrete volume",`${number(yards,2)} yd³`],["Approx. 80-lb bags",Math.ceil(yards*1.35).toLocaleString("en-US")],["Material estimate",cost===null?"Price per yard not provided":money(cost)]],
      note:"Large or structural pours should be verified with the ready-mix supplier or contractor. Site conditions and ordering increments can change the final quantity."};
  }
  if(type==="hvac"){
    const sqft=finite(raw.homeSqft,100,1e7), efficiency=finite(raw.efficiency,.5,3), market=finite(raw.market,.5,3), system=String(raw.system||"central");
    const bases={central:[5500,11000],heatpump:[6500,14000],furnace:[4000,9500],ductless:[4500,12000]};
    if(!Number.isFinite(sqft)||!Number.isFinite(efficiency)||!Number.isFinite(market)||!bases[system]) throw new Error("Check your HVAC inputs before sending the report.");
    const tons=Math.max(1.5,Math.min(6,Math.ceil((sqft/600)*2)/2)); let [lo,hi]=bases[system]; const sizeFactor=.75+(tons/3)*.25;
    lo*=sizeFactor*efficiency*market; hi*=sizeFactor*efficiency*market; const mid=(lo+hi)/2;
    const systemLabel={central:"Central AC",heatpump:"Heat pump",furnace:"Furnace",ductless:"Ductless mini-split"}[system];
    return {title:"HVAC Replacement Cost Report",subject:`Your HVAC estimate: ${money(lo)}–${money(hi)}`,url:"https://homecostengine.com/calculators/hvac.html",
      summary:`Your planning range is ${money(lo)} to ${money(hi)} for the selected ${systemLabel} assumptions.`,
      metrics:[["Home size",`${Math.round(sqft).toLocaleString("en-US")} sq ft`],["System",systemLabel],["Sizing starting point",`${number(tons,1)} tons`],["Estimated range",`${money(lo)} – ${money(hi)}`],["Midpoint",money(mid)]],
      note:"This is not an HVAC load calculation. Final sizing should consider climate, insulation, windows, air leakage, ductwork and local code requirements."};
  }
  if(type==="paint"){
    const l=finite(raw.roomLength,.01,1e5), w=finite(raw.roomWidth,.01,1e5), h=finite(raw.roomHeight,.01,1e4), coats=finite(raw.coats,1,10), doors=finite(raw.doors,0,1000), windows=finite(raw.windows,0,1000), coverage=finite(raw.coverage,1,5000), price=finite(raw.gallonPrice,0,1e5);
    if(![l,w,h,coats,doors,windows,coverage].every(Number.isFinite)) throw new Error("Check your paint inputs before sending the report.");
    const area=Math.max(2*(l+w)*h - doors*21 - windows*15,0), gallons=Math.ceil(area*coats/coverage), cost=Number.isFinite(price)?gallons*price:0;
    return {title:"Paint Calculator Report",subject:`Your paint estimate: ${gallons} gallon${gallons===1?"":"s"}`,url:"https://homecostengine.com/calculators/paint.html",
      summary:`You need about ${gallons} gallon${gallons===1?"":"s"} for the entered room and coat assumptions.`,
      metrics:[["Paintable wall area",`${Math.round(area).toLocaleString("en-US")} sq ft`],["Coats",String(Math.round(coats))],["Coverage assumption",`${Math.round(coverage).toLocaleString("en-US")} sq ft / gallon`],["Estimated gallons",String(gallons)],["Estimated paint cost",money(cost)]],
      note:"Primer, ceilings, trim, textured surfaces and unusually porous surfaces can change the amount of paint required."};
  }
  if(type==="floor"){
    const area=finite(raw.floorArea,.01,1e8), waste=finite(raw.floorWaste,1,2), material=finite(raw.materialPrice,0,1e6), labor=finite(raw.laborPrice,0,1e6);
    if(![area,waste,material,labor].every(Number.isFinite)) throw new Error("Check your flooring inputs before sending the report.");
    const buy=area*waste, materialCost=buy*material, laborCost=buy*labor, total=materialCost+laborCost;
    return {title:"Flooring Cost Report",subject:`Your flooring estimate: ${money(total)}`,url:"https://homecostengine.com/calculators/flooring.html",
      summary:`Your entered assumptions produce an installed planning total of about ${money(total)}.`,
      metrics:[["Measured floor area",`${Math.round(area).toLocaleString("en-US")} sq ft`],["Purchase quantity",`${Math.round(buy).toLocaleString("en-US")} sq ft`],["Material cost",money(materialCost)],["Labor cost",money(laborCost)],["Estimated total",money(total)]],
      note:"Removal, subfloor repair, leveling, stairs, baseboards, transitions, delivery and furniture moving may be separate line items."};
  }
  if(type==="mulch"){
    const area=finite(raw.mulchArea,.01,1e9), depth=finite(raw.depth,.01,100), price=finite(raw.mulchPrice,0,1e6);
    if(!Number.isFinite(area)||!Number.isFinite(depth)) throw new Error("Check your mulch inputs before sending the report.");
    const yards=area*(depth/12)/27, cost=Number.isFinite(price)&&price>0?yards*price:null;
    return {title:"Mulch Calculator Report",subject:`Your mulch estimate: ${number(yards,2)} yd³`,url:"https://homecostengine.com/calculators/mulch.html",
      summary:`Your landscape area needs about ${number(yards,2)} cubic yards of mulch at the entered depth.`,
      metrics:[["Landscape area",`${Math.round(area).toLocaleString("en-US")} sq ft`],["Depth",`${number(depth,1)} in`],["Calculated volume",`${number(yards,2)} yd³`],["Suggested order quantity",`${Math.ceil(yards)} yd³`],["Estimated material cost",cost===null?"Price per yard not provided":money(cost)]],
      note:"Irregular beds, slopes, settling, delivery minimums and supplier rounding can change the practical order quantity."};
  }
  throw new Error("Unsupported calculator report.");
}

function emailHtml(report){
  const rows=report.metrics.map(([label,value])=>`<tr><td style="padding:11px 0;color:#64748b;border-bottom:1px solid #e8edf2">${esc(label)}</td><td style="padding:11px 0;text-align:right;font-weight:800;border-bottom:1px solid #e8edf2">${esc(value)}</td></tr>`).join("");
  return `<!doctype html><html><body style="margin:0;background:#f5f6f4;font-family:Arial,sans-serif;color:#102033">
  <div style="max-width:680px;margin:0 auto;padding:28px 16px">
    <div style="background:#102033;border-radius:20px;padding:28px;color:#fff"><div style="font-size:11px;letter-spacing:.12em;color:#80d3c2;font-weight:800">HOMECOSTENGINE · PERSONALIZED PROJECT REPORT</div><h1 style="margin:10px 0 7px;font-size:30px">${esc(report.title)}</h1><p style="margin:0;color:#d1dae3;line-height:1.65">${esc(report.summary)}</p></div>
    <div style="background:#fff;border:1px solid #e2e7eb;border-radius:20px;padding:22px;margin-top:16px"><table style="width:100%;border-collapse:collapse">${rows}</table></div>
    <div style="background:#e5f3ef;border-radius:20px;padding:22px;margin-top:16px"><div style="font-size:12px;color:#176b5b;font-weight:800">WHAT THIS MEANS</div><p style="margin:8px 0 0;line-height:1.65;color:#405064">${esc(report.note)}</p></div>
    <div style="background:#fff;border:1px solid #e2e7eb;border-radius:20px;padding:22px;margin-top:16px;text-align:center"><p style="margin:0 0 16px;color:#526173">Reopen the calculator anytime and change your assumptions.</p><a href="${esc(report.url)}" style="display:inline-block;background:#176b5b;color:#fff;text-decoration:none;font-weight:800;padding:12px 18px;border-radius:10px">Open calculator</a></div>
    <p style="color:#8a98a8;font-size:11px;line-height:1.55;padding:12px 4px">This report is an estimate based on the inputs you provided and is for planning purposes only. You requested this report from HomeCostEngine.</p>
  </div></body></html>`;
}

export async function onRequestPost(context){
  const {request,env}=context;
  if(!env.BREVO_API_KEY || !env.BREVO_SENDER_EMAIL) return json({error:"Email service is not configured yet."},500);

  const origin=request.headers.get("Origin") || "";
  if(origin){
    try{
      const host=new URL(origin).hostname;
      const configuredHost=String(env.SITE_HOST || "homecostengine.com").replace(/^www\./,"").toLowerCase();
      const normalized=host.replace(/^www\./,"").toLowerCase();
      if(!(normalized===configuredHost || host.endsWith(".pages.dev"))) return json({error:"Invalid request origin."},403);
    }catch{return json({error:"Invalid request origin."},403);}
  }

  let body; try{body=await request.json();}catch{return json({error:"Invalid request."},400);}
  if(String(body.companyWebsite || "").trim()) return json({ok:true});

  const email=String(body.email || "").trim().toLowerCase();
  if(!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email) || email.length>254) return json({error:"Please enter a valid email address."},400);

  let report; try{report=calculate(String(body.reportType || ""),body.calculatorInputs || {});}catch(err){return json({error:err.message || "Please check your calculator inputs."},400);}

  const headers={"api-key":env.BREVO_API_KEY,"content-type":"application/json","accept":"application/json"};

  if(body.marketingConsent===true && env.BREVO_LIST_ID){
    const contactResp=await fetch("https://api.brevo.com/v3/contacts",{method:"POST",headers,body:JSON.stringify({email,listIds:[Number(env.BREVO_LIST_ID)],updateEnabled:true})});
    if(!contactResp.ok) console.log("Brevo contact error",contactResp.status,await contactResp.text());
  }

  const mailResp=await fetch("https://api.brevo.com/v3/smtp/email",{method:"POST",headers,body:JSON.stringify({
    sender:{name:"HomeCostEngine",email:env.BREVO_SENDER_EMAIL},to:[{email}],
    replyTo:{name:"HomeCostEngine",email:env.BREVO_REPLY_TO || env.BREVO_SENDER_EMAIL},
    subject:report.subject,htmlContent:emailHtml(report)
  })});
  if(!mailResp.ok){console.log("Brevo send error",mailResp.status,await mailResp.text());return json({error:"We couldn't send the report right now. Please try again shortly."},502);}
  return json({ok:true,subscribed:body.marketingConsent===true});
}
export async function onRequest(){return json({error:"Method not allowed."},405);}