(() => {
  const money=n=>new Intl.NumberFormat("en-US",{style:"currency",currency:"USD",maximumFractionDigits:0}).format(Math.round(n||0));
  const moneyUnit=n=>new Intl.NumberFormat("en-US",{style:"currency",currency:"USD",maximumFractionDigits:0}).format(Math.round(n||0));
  const $=id=>document.getElementById(id);
  const locationData=window.HCE_STATE_RPP_2024||{states:{}};
  const projects={
    kitchen:{name:"Kitchen remodel",unit:"sq ft",qty:200,low:80,high:225,permit:850,demo:.06,mat:.54,labor:.46,timeline:"4–12 weeks",checks:["Cabinet type and installation","Countertop material and edge","Appliance allowance","Plumbing/electrical changes","Flooring and backsplash","Permit responsibility"]},
    bathroom:{name:"Bathroom remodel",unit:"sq ft",qty:60,low:150,high:400,permit:700,demo:.07,mat:.50,labor:.50,timeline:"3–8 weeks",checks:["Tile area and waterproofing","Vanity and countertop","Plumbing relocation","Shower/tub specification","Ventilation and electrical","Permit responsibility"]},
    wholehome:{name:"Whole-home renovation",unit:"sq ft",qty:1800,low:20,high:80,permit:1800,demo:.05,mat:.48,labor:.52,timeline:"2–8 months",checks:["Rooms included in scope","Structural changes","Electrical/plumbing upgrades","Finish schedule","Temporary housing","Permit and inspection plan"]},
    windows:{name:"Window replacement",unit:"window",qty:10,low:700,high:1800,permit:250,demo:.03,mat:.62,labor:.38,timeline:"1–3 days",checks:["Window size and style","Frame material","Glass package","Interior/exterior trim","Rot repair allowance","Disposal and warranty"]},
    siding:{name:"Siding replacement",unit:"sq ft",qty:1800,low:8,high:20,permit:500,demo:.08,mat:.55,labor:.45,timeline:"1–3 weeks",checks:["Siding material","Housewrap / weather barrier","Trim and soffit scope","Sheathing repair allowance","Disposal","Permit and warranty"]},
    deck:{name:"Deck addition / replacement",unit:"sq ft",qty:300,low:30,high:75,permit:500,demo:.05,mat:.58,labor:.42,timeline:"1–4 weeks",checks:["Decking material","Foundation / footings","Railings and stairs","Ledger / flashing","Lighting or electrical","Permit and inspection"]},
    basement:{name:"Basement finishing",unit:"sq ft",qty:800,low:35,high:100,permit:1200,demo:.03,mat:.48,labor:.52,timeline:"6–16 weeks",checks:["Moisture control","Egress requirements","Bathroom / plumbing scope","Electrical and HVAC","Insulation and drywall","Permit and inspections"]},
    roof:{name:"Roof replacement",unit:"sq ft",qty:2000,low:5.5,high:11,permit:400,demo:.10,mat:.48,labor:.52,timeline:"1–5 days",checks:["Roof area and pitch","Shingle / roofing system","Tear-off layers","Decking allowance","Flashing and ventilation","Disposal and warranty"]},
    waterheater:{name:"Water heater replacement",unit:"unit",qty:1,low:1300,high:3200,permit:200,demo:.03,mat:.60,labor:.40,timeline:"2–6 hours",checks:["Tank vs tankless","Fuel type","Capacity","Venting changes","Code upgrades","Old unit haul-away"]},
    panel:{name:"Electrical panel upgrade",unit:"panel",qty:1,low:2200,high:5000,permit:400,demo:.01,mat:.42,labor:.58,timeline:"1–2 days",checks:["Panel amperage","Service upgrade required","Utility coordination","Circuit corrections","Permit / inspection","Drywall repair exclusions"]},
    garagedoor:{name:"Garage door replacement",unit:"door",qty:1,low:1300,high:3200,permit:150,demo:.04,mat:.67,labor:.33,timeline:"3–8 hours",checks:["Door size","Insulation level","Window / design options","Opener included?","Track / spring replacement","Removal and warranty"]},
    driveway:{name:"Concrete driveway",unit:"sq ft",qty:600,low:8,high:18,permit:350,demo:.12,mat:.50,labor:.50,timeline:"3–7 days + cure",checks:["Slab thickness","Base preparation","Reinforcement","Old driveway removal","Drainage / grading","Finish and control joints"]}
  };

  function setBar(id,amount,total){const el=$(id);if(!el)return;el.style.width=`${Math.max(2,Math.min(100,(amount/Math.max(total,1))*100))}%`;}
  function signedPct(n){const pct=(n*100).toFixed(1);return `${n>=0?"+":""}${pct}%`;}
  function populateStates(){
    const select=$("stateCode");if(!select)return;
    Object.entries(locationData.states||{}).sort((a,b)=>a[1].name.localeCompare(b[1].name)).forEach(([code,data])=>{const option=document.createElement("option");option.value=code;option.textContent=data.name;select.appendChild(option);});
  }
  function getLocation(){
    const code=$("stateCode")?.value||"";
    const state=locationData.states?.[code];
    const rpp=state?.rpp||100;
    const stateFactor=1+((rpp/100)-1)*.65;
    const within=Number($("marketLevel")?.value)||1;
    return {code,name:state?.name||"U.S. national baseline",rpp,stateFactor,within,factor:stateFactor*within};
  }
  function updateLocationText(loc){
    const stateIndex=$("stateIndex"),detail=$("stateAdjustmentText");
    if(loc.code){
      if(stateIndex)stateIndex.textContent=`${loc.rpp.toFixed(1)} RPP • ${signedPct(loc.stateFactor-1)} model`;
      if(detail)detail.textContent=`${loc.name}: 2024 BEA RPP ${loc.rpp.toFixed(1)}. The calculator applies 65% of the state's deviation from the U.S. baseline, then your within-state market setting.`;
    }else{
      if(stateIndex)stateIndex.textContent="100.0 national baseline";
      if(detail)detail.textContent="Choose a state to apply the 2024 BEA Regional Price Parity baseline. Without a state, the calculator uses the U.S. national baseline.";
    }
  }
  function updateProjectUI(){
    const p=projects[$("projectType").value],plural=["window","unit","panel","door"].includes(p.unit)?"s":"";
    $("quantityLabel").textContent=`Project size (${p.unit}${plural})`;$("projectQuantity").value=p.qty;$("projectChecklistTitle").textContent=`${p.name} quote checklist`;$("projectChecks").innerHTML=p.checks.map(x=>`<div class="check">✓ ${x}</div>`).join("");calculate();
  }
  function calculate(){
    const p=projects[$("projectType").value],qty=Math.max(1,Number($("projectQuantity").value)||p.qty),finish=Number($("finishLevel").value)||1,loc=getLocation(),age=Number($("homeAge").value)||1,complexity=Number($("complexity").value)||1,factor=finish*loc.factor*age*complexity;
    const baseLow=qty*p.low*factor,baseHigh=qty*p.high*factor,includeDemo=$("demolition").value==="yes",demoLow=includeDemo?baseLow*p.demo*.85:0,demoHigh=includeDemo?baseHigh*p.demo*1.15:0,includePermit=$("permit").value==="auto",permitMid=includePermit?p.permit*loc.factor:0,permitLow=permitMid*.75,permitHigh=permitMid*1.35,subtotalLow=baseLow+demoLow+permitLow,subtotalHigh=baseHigh+demoHigh+permitHigh,contingencyPct=Number($("contingency").value)||0,low=subtotalLow*(1+contingencyPct),high=subtotalHigh*(1+contingencyPct),mid=(low+high)/2,baseMid=(baseLow+baseHigh)/2,demoMid=(demoLow+demoHigh)/2,contingencyMid=((subtotalLow+subtotalHigh)/2)*contingencyPct,materials=baseMid*p.mat,labor=baseMid*p.labor;
    $("estimateRange").textContent=`${money(low)} – ${money(high)}`;$("estimateMid").textContent=`Planning midpoint ${money(mid)} • ${p.name}${loc.code?` • ${loc.name}`:""}`;$("midpoint").textContent=money(mid);$("unitHeading").textContent=`Cost per ${p.unit}`;$("unitCost").textContent=`${moneyUnit(mid/qty)} / ${p.unit}`;$("timeline").textContent=p.timeline;$("contingencyAmount").textContent=money(contingencyMid);$("materialsCost").textContent=money(materials);$("laborCost").textContent=money(labor);$("demoCost").textContent=money(demoMid);$("permitCost").textContent=money(permitMid);updateLocationText(loc);
    const visibleTotal=materials+labor+demoMid+permitMid;setBar("materialsBar",materials,visibleTotal);setBar("laborBar",labor,visibleTotal);setBar("demoBar",demoMid,visibleTotal);setBar("permitBar",permitMid,visibleTotal);compareQuote(mid);
  }
  function compareQuote(mid){
    const quote=Number($("contractorQuote").value)||0;if(!quote){$("quoteComparison").textContent="Add a quote to see the percentage difference.";return;}const diff=(quote-mid)/mid*100,abs=Math.abs(diff).toFixed(0);let text="";if(Math.abs(diff)<10)text=`This quote is about ${abs}% ${diff>=0?"above":"below"} the planning midpoint. Compare scope, allowances and warranty before drawing a conclusion.`;else if(diff>=10)text=`This quote is about ${abs}% above the planning midpoint. Ask what added scope, material grade, access, code work or warranty explains the difference.`;else text=`This quote is about ${abs}% below the planning midpoint. Check for exclusions, allowances, disposal, permits, product specifications and change-order terms.`;$("quoteComparison").textContent=text;
  }
  document.addEventListener("DOMContentLoaded",()=>{
    const form=$("remodelEstimator");if(!form)return;populateStates();
    const params=new URLSearchParams(window.location.search),requested=params.get("project"),requestedState=(params.get("state")||"").toUpperCase();
    if(requested&&projects[requested])$("projectType").value=requested;if(requestedState&&locationData.states?.[requestedState])$("stateCode").value=requestedState;
    $("projectType").addEventListener("change",updateProjectUI);["projectQuantity","finishLevel","stateCode","marketLevel","homeAge","complexity","demolition","permit","contingency"].forEach(id=>{$(id)?.addEventListener("input",calculate);$(id)?.addEventListener("change",calculate);});$("contractorQuote").addEventListener("input",calculate);form.addEventListener("submit",e=>{e.preventDefault();calculate();});updateProjectUI();
  });
})();