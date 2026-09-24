const money = n => new Intl.NumberFormat("en-US",{style:"currency",currency:"USD",maximumFractionDigits:0}).format(n);
const num = id => Number(document.getElementById(id)?.value || 0);
const val = id => document.getElementById(id)?.value;
const set = (id, value) => { const el=document.getElementById(id); if(el) el.textContent=value; };

function roofCalc(){
  const area=num("area"), material=val("material"), pitch=Number(val("pitch")), stories=Number(val("stories")),
        market=Number(val("market")), tearLayers=Number(val("tearoff")), stateCode=val("roofState"), deckArea=num("deckArea"), features=num("roofFeatures"), permit=num("roofPermit"), contingency=Number(val("roofContingency"));
  if(area<=0) return;
  const ranges={asphalt:[5.5,9], metal:[9,16], tile:[10,20], wood:[7,14], slate:[15,30]};
  const state=window.HCE_STATE_RPP_2024?.states?.[stateCode];
  const stateFactor=state?1+((state.rpp/100)-1)*.65:1;
  let [lo,hi]=ranges[material];
  lo*=pitch*stories*market*stateFactor; hi*=pitch*stories*market*stateFactor;
  const tearRates={0:[0,0],1:[1.15,2.35],2:[1.75,3.5],3:[2.5,4.75]},tear=tearRates[tearLayers]||tearRates[1];
  const baseLow=area*lo,baseHigh=area*hi,tearLow=area*tear[0],tearHigh=area*tear[1],deckLow=deckArea*3.5,deckHigh=deckArea*7,featureLow=features*250,featureHigh=features*750;
  const subtotalLow=baseLow+tearLow+deckLow+featureLow+permit,subtotalHigh=baseHigh+tearHigh+deckHigh+featureHigh+permit;
  const low=subtotalLow*(1+contingency), high=subtotalHigh*(1+contingency), mid=(low+high)/2;
  set("result",money(mid)); set("range",`${money(low)} – ${money(high)}`);
  set("unit",`${money(low/area)} – ${money(high/area)} / sq ft`);
  set("materials",`${money((baseLow+baseHigh)/2)} roof system`); set("labor",`${money((deckLow+deckHigh+featureLow+featureHigh)/2)} repairs / details`); set("other",`${money(((low-subtotalLow)+(high-subtotalHigh))/2)} contingency`);
}

function populateRoofStates(){
  const select=document.getElementById("roofState"),data=window.HCE_STATE_RPP_2024?.states;
  if(!select||!data||select.options.length>1)return;
  Object.entries(data).sort((a,b)=>a[1].name.localeCompare(b[1].name)).forEach(([code,item])=>{const option=document.createElement("option");option.value=code;option.textContent=item.name;select.appendChild(option)});
}
function concreteCalc(){
  const l=num("length"), w=num("width"), t=num("thickness"), waste=Number(val("waste")), price=num("yardPrice");
  if(l<=0||w<=0||t<=0) return;
  const yards=(l*w*(t/12))/27*waste;
  const cost=price?yards*price:0;
  set("result",`${yards.toFixed(2)} yd³`); set("range",`${Math.ceil(yards*1.35)} × 80-lb bags (approx.)`);
  set("unit",`${(l*w).toFixed(0)} sq ft surface`);
  set("materials",price?money(cost):"Add price/yd³"); set("labor","Not included"); set("other",`${((waste-1)*100).toFixed(0)}% waste`);
}
function paintCalc(){
  const l=num("roomLength"), w=num("roomWidth"), h=num("roomHeight"), coats=num("coats"),
        coverage=num("coverage")||350, price=num("gallonPrice")||45;
  if(l<=0||w<=0||h<=0) return;
  const doors=num("doors"), windows=num("windows");
  let area=2*(l+w)*h - doors*21 - windows*15;
  area=Math.max(area,0);
  const gallons=Math.ceil(area*coats/coverage);
  set("result",`${gallons} gal`); set("range",`${money(gallons*price)} estimated paint cost`);
  set("unit",`${area.toFixed(0)} sq ft paintable wall area`);
  set("materials",money(gallons*price)); set("labor","Not included"); set("other",`${coats} coat${coats===1?"":"s"}`);
}
function floorCalc(){
  const area=num("floorArea"), waste=Number(val("floorWaste")), material=num("materialPrice"), labor=num("laborPrice");
  if(area<=0) return;
  const buy=area*waste, total=buy*(material+labor);
  set("result",money(total)); set("range",`${buy.toFixed(0)} sq ft to purchase`);
  set("unit",`${money(material+labor)} / sq ft installed assumption`);
  set("materials",money(buy*material)); set("labor",money(buy*labor)); set("other",`${((waste-1)*100).toFixed(0)}% waste`);
}
function mulchCalc(){
  const area=num("mulchArea"), depth=num("depth"), price=num("mulchPrice");
  if(area<=0||depth<=0)return;
  const yards=area*(depth/12)/27;
  set("result",`${yards.toFixed(2)} yd³`); set("range",`${Math.ceil(yards)} cubic yards to order`);
  set("unit",`${depth}" depth across ${area.toFixed(0)} sq ft`);
  set("materials",price?money(yards*price):"Add price/yd³"); set("labor","Not included"); set("other","Delivery may be extra");
}
function hvacCalc(){
  const sqft=num("homeSqft"), system=val("system"), efficiency=Number(val("efficiency")), market=Number(val("market"));
  if(sqft<=0)return;
  const tons=Math.max(1.5,Math.min(6,Math.ceil((sqft/600)*2)/2));
  const bases={central:[5500,11000], heatpump:[6500,14000], furnace:[4000,9500], ductless:[4500,12000]};
  let [lo,hi]=bases[system];
  const sizeFactor=.75+(tons/3)*.25;
  lo*=sizeFactor*efficiency*market; hi*=sizeFactor*efficiency*market;
  const mid=(lo+hi)/2;
  set("result",money(mid)); set("range",`${money(lo)} – ${money(hi)}`);
  set("unit",`Approx. ${tons.toFixed(1)} ton sizing starting point`);
  set("materials",money(mid*.55)); set("labor",money(mid*.35)); set("other",money(mid*.10));
}


function squareFootageCalc(){
  const shape=val("areaShape"), a=num("areaLength"), b=num("areaWidth");
  if(a<=0)return;
  let area=0, formula="", dims="";
  if(shape==="circle"){area=Math.PI*Math.pow(a/2,2);formula="π × radius²";dims=`Diameter ${a} ft`;}
  else if(shape==="square"){area=a*a;formula="side × side";dims=`${a} ft × ${a} ft`;}
  else {if(b<=0)return;area=a*b;formula="length × width";dims=`${a} ft × ${b} ft`;}
  set("result",`${area.toFixed(2)} sq ft`);
  set("range",`${(area/9).toFixed(2)} sq yd • ${(area/43560).toFixed(4)} acres`);
  set("unit",`${(area/9).toFixed(2)} sq yd`);
  set("materials",`${(area/43560).toFixed(4)} acres`);
  set("labor",dims); set("other",formula);
}
function cubicYardCalc(){
  const l=num("cyLength"),w=num("cyWidth"),d=num("cyDepth"),waste=Number(val("cyWaste"));
  if(l<=0||w<=0||d<=0)return;
  const base=(l*w*(d/12))/27, yards=base*waste, feet=yards*27, meters=yards*.764555;
  set("result",`${yards.toFixed(2)} yd³`); set("range",`${feet.toFixed(1)} ft³ • ${meters.toFixed(2)} m³`);
  set("unit",`${feet.toFixed(1)} ft³`); set("materials",`${meters.toFixed(2)} m³`);
  set("labor",`${((waste-1)*100).toFixed(0)}%`); set("other",`${Math.ceil(yards*2)/2} yd³`);
}
function gravelCalc(){
  const length=num("gravelLength"),width=num("gravelWidth"),depth=num("gravelDepth"),density=Number(val("gravelType")),waste=Number(val("gravelWaste")),price=num("gravelPrice"),delivery=num("gravelDelivery"),prepRate=num("gravelPrepRate");
  const area=length*width;
  if(length<=0||width<=0||depth<=0)return;
  const yards=area*(depth/12)/27*waste, tons=yards*density, cost=price?tons*price:0;
  const prep=area*prepRate,total=cost+delivery+prep;
  set("result",money(total)); set("range",`${tons.toFixed(2)} tons • ${yards.toFixed(2)} cubic yards`);
  set("unit",`${area.toFixed(0)} sq ft • ${depth}\" depth`); set("materials",price?money(cost):"Add price / ton");
  set("labor",money(prep)); set("other",money(delivery));
}
function roofingSquareCalc(){
  const area=num("rsArea"),waste=Number(val("rsWaste")),bundles=num("rsBundles")||3;
  if(area<=0)return;
  const base=area/100,total=base*waste,bundleCount=Math.ceil(total*bundles);
  set("result",`${total.toFixed(2)} squares`); set("range",`${bundleCount} approximate bundles`);
  set("unit",`${base.toFixed(2)} squares`); set("materials",`${total.toFixed(2)} squares`);
  set("labor",`${bundleCount} bundles`); set("other",`${((waste-1)*100).toFixed(0)}%`);
}
function roofDeckCalc(){
  const area=num("rdArea"),waste=Number(val("rdWaste"))||1,rate=num("rdRate"),extra=num("rdExtra");
  if(area<=0||rate<0)return;
  const adjustedArea=area*waste,sheets=Math.ceil(adjustedArea/32),panelCost=sheets*rate,total=panelCost+extra;
  const lowPerSheet=64,highPerSheet=160;
  const marketLow=sheets*lowPerSheet+extra,marketHigh=sheets*highPerSheet+extra;
  set("result",money(total));
  set("range",`${sheets} × 4×8 sheets • ${money(marketLow)} – ${money(marketHigh)} broad 2026 planning band`);
  set("unit",`${money(rate)} / installed sheet`);
  set("materials",`${sheets} sheets for ${adjustedArea.toFixed(0)} sq ft incl. allowance`);
  set("labor",area?`${money(total/area)} / damaged sq ft using your rate`:"—");
  set("other",extra?money(extra):"No extra allowance");
}
function roofPitchCalc(){
  const mode=val("pitchMode")||"riseRun";
  let ratio=0,rise=0,run=12,angle=0,slope=0,mult=1,rafter=null,roofArea=null,sourceLabel="";
  if(mode==="degrees"){
    angle=num("pitchDegrees");
    if(angle<=0||angle>=89)return;
    ratio=Math.tan(angle*Math.PI/180); rise=ratio*12; run=12; sourceLabel=`${angle.toFixed(1)}° input`;
  }else if(mode==="percent"){
    slope=num("pitchPercent");
    if(slope<=0)return;
    ratio=slope/100; rise=ratio*12; run=12; angle=Math.atan(ratio)*180/Math.PI; sourceLabel=`${slope.toFixed(1)}% slope input`;
  }else if(mode==="dimensions"){
    rise=num("pitchDimRise"); run=12;
    const width=num("pitchBuildingWidth"),length=num("pitchBuildingLength"),eave=num("pitchEave"),gable=num("pitchGable");
    if(rise<0||width<=0||length<=0)return;
    ratio=rise/12; angle=Math.atan(ratio)*180/Math.PI; slope=ratio*100; mult=Math.sqrt(1+ratio*ratio);
    const halfHorizontal=(width/2)+(Math.max(0,eave)/12);
    rafter=halfHorizontal*mult;
    const roofLength=length+(2*Math.max(0,gable)/12);
    roofArea=2*rafter*roofLength;
    sourceLabel="simple gable dimensions";
  }else{
    rise=num("pitchRise"); run=num("pitchRun");
    if(run<=0||rise<0)return;
    ratio=rise/run; angle=Math.atan(ratio)*180/Math.PI; slope=ratio*100; mult=Math.sqrt(1+ratio*ratio); sourceLabel=`${rise.toFixed(1)}:${run.toFixed(1)} input`;
  }
  if(mode!=="dimensions"){
    angle=angle||Math.atan(ratio)*180/Math.PI;
    slope=slope||ratio*100;
    mult=Math.sqrt(1+ratio*ratio);
    const span=num("pitchSpan"),footprint=num("pitchFootprint");
    if(span>0) rafter=span*mult;
    if(footprint>0) roofArea=footprint*mult;
  }
  const pitch12=ratio*12;
  set("result",`${pitch12.toFixed(1)}:12`);
  set("range",`${angle.toFixed(1)}° roof angle • ${sourceLabel}`);
  set("unit",`${slope.toFixed(1)}%`);
  set("materials",`${mult.toFixed(3)}×`);
  set("labor",rafter!==null?`${rafter.toFixed(2)} ft`:"Add span or dimensions");
  set("other",roofArea!==null?`${Math.round(roofArea).toLocaleString()} sq ft`:"Add footprint or dimensions");
  set("pitchSquares",roofArea!==null?`${(roofArea/100).toFixed(2)} squares`:"—");
  set("pitchWaste",roofArea!==null?`${(roofArea/100*1.10).toFixed(2)} squares at 10% allowance`:"—");
  const category=pitch12<2?"very low slope":pitch12<4?"low slope":pitch12<=6?"moderate slope":pitch12<=9?"steep":pitch12<=12?"very steep":"very steep / specialty";
  set("pitchCategory",category);
}

function initRoofPitchControls(){
  const mode=document.getElementById("pitchMode");
  if(!mode)return;
  const groups={
    riseRun:document.getElementById("pitchRiseRunFields"),
    degrees:document.getElementById("pitchDegreesFields"),
    percent:document.getElementById("pitchPercentFields"),
    dimensions:document.getElementById("pitchDimensionsFields")
  };
  const update=()=>{
    Object.entries(groups).forEach(([key,el])=>{if(el)el.style.display=mode.value===key?"grid":"none"});
    roofPitchCalc();
  };
  mode.addEventListener("change",update);
  document.querySelectorAll("[data-pitch-preset]").forEach(btn=>btn.addEventListener("click",()=>{
    mode.value="riseRun";
    const rise=document.getElementById("pitchRise"),run=document.getElementById("pitchRun");
    if(rise)rise.value=btn.dataset.pitchPreset;
    if(run)run.value="12";
    update();
  }));
  update();
}
function currentCalculatorInputs(type){
  if(type==="roof") return {area:num("area"), material:val("material"), pitch:Number(val("pitch")), stories:Number(val("stories")), tearoff:Number(val("tearoff")), market:Number(val("market")), roofState:val("roofState"), deckArea:num("deckArea"), roofFeatures:num("roofFeatures"), roofPermit:num("roofPermit"), roofContingency:Number(val("roofContingency"))};
  if(type==="concrete") return {length:num("length"), width:num("width"), thickness:num("thickness"), waste:Number(val("waste")), yardPrice:num("yardPrice")};
  if(type==="hvac") return {homeSqft:num("homeSqft"), system:val("system"), efficiency:Number(val("efficiency")), market:Number(val("market"))};
  if(type==="paint") return {roomLength:num("roomLength"), roomWidth:num("roomWidth"), roomHeight:num("roomHeight"), coats:num("coats"), doors:num("doors"), windows:num("windows"), coverage:num("coverage"), gallonPrice:num("gallonPrice")};
  if(type==="floor") return {floorArea:num("floorArea"), floorWaste:Number(val("floorWaste")), materialPrice:num("materialPrice"), laborPrice:num("laborPrice")};
  if(type==="mulch") return {mulchArea:num("mulchArea"), depth:num("depth"), mulchPrice:num("mulchPrice")};
  if(type==="sqft") return {areaShape:val("areaShape"), areaLength:num("areaLength"), areaWidth:num("areaWidth")};
  if(type==="cubicyard") return {cyLength:num("cyLength"), cyWidth:num("cyWidth"), cyDepth:num("cyDepth"), cyWaste:Number(val("cyWaste"))};
  if(type==="gravel") return {gravelLength:num("gravelLength"), gravelWidth:num("gravelWidth"), gravelDepth:num("gravelDepth"), gravelType:Number(val("gravelType")), gravelWaste:Number(val("gravelWaste")), gravelPrice:num("gravelPrice"), gravelDelivery:num("gravelDelivery"), gravelPrepRate:num("gravelPrepRate")};
  if(type==="roofsquare") return {rsArea:num("rsArea"), rsWaste:Number(val("rsWaste")), rsBundles:num("rsBundles")};
  if(type==="roofdeck") return {rdArea:num("rdArea"), rdWaste:Number(val("rdWaste")), rdRate:num("rdRate"), rdExtra:num("rdExtra")};
  if(type==="roofpitch") return {pitchMode:val("pitchMode"), pitchRise:num("pitchRise"), pitchRun:num("pitchRun"), pitchDegrees:num("pitchDegrees"), pitchPercent:num("pitchPercent"), pitchSpan:num("pitchSpan"), pitchFootprint:num("pitchFootprint"), pitchDimRise:num("pitchDimRise"), pitchBuildingWidth:num("pitchBuildingWidth"), pitchBuildingLength:num("pitchBuildingLength"), pitchEave:num("pitchEave"), pitchGable:num("pitchGable")};
  if(type==="maintenance") return {homeValue:num("value"), rate:num("rate"), known:num("known")};
  if(type==="split") return {total:num("total"), labor:num("labor"), material:num("material")};
  if(type==="contingency") return {base:num("base"), rate:num("rate"), allowance:num("allow")};
  if(type==="quotes") return {quotes:[0,1,2].map(i=>({price:num(`p${i}`),allowance:num(`a${i}`),scope:num(`s${i}`),warranty:num(`w${i}`)}))};
  if(type==="toilet") return {fixture:num("fixture"), labor:num("labor"), removal:num("removal"), connections:num("connections"), valve:num("valve"), flange:num("flange"), floor:num("floor"), permit:num("permit"), tax:num("tax"), contingency:num("contingency")};
  if(type==="remodel") return {
    projectType:val("projectType"), projectName:document.querySelector("#projectType option:checked")?.textContent||"Renovation project",
    stateCode:val("stateCode"), stateName:document.querySelector("#stateCode option:checked")?.textContent||"U.S. national baseline",
    quantity:num("projectQuantity"), finishLevel:Number(val("finishLevel")), marketLevel:Number(val("marketLevel")),
    homeAge:Number(val("homeAge")), complexity:Number(val("complexity")), demolition:val("demolition"), permit:val("permit"),
    contingency:Number(val("contingency")), estimateRange:document.getElementById("estimateRange")?.textContent||"",
    midpoint:document.getElementById("midpoint")?.textContent||"", unitCost:document.getElementById("unitCost")?.textContent||"",
    timeline:document.getElementById("timeline")?.textContent||"", materials:document.getElementById("materialsCost")?.textContent||"",
    labor:document.getElementById("laborCost")?.textContent||"", demo:document.getElementById("demoCost")?.textContent||"",
    permitCost:document.getElementById("permitCost")?.textContent||"", contingencyAmount:document.getElementById("contingencyAmount")?.textContent||""
  };
  return {};
}

function injectEmailReportForm(type){
  const shell=document.querySelector(".calc-shell, .hce-tool");
  if(!shell || document.querySelector(".calculator-report-form")) return;
  const labels={roof:"roof cost", concrete:"concrete", hvac:"HVAC", paint:"paint", floor:"flooring", mulch:"mulch", sqft:"square footage", cubicyard:"cubic yard", gravel:"gravel", roofsquare:"roofing square", roofdeck:"roof decking replacement cost", roofpitch:"roof pitch", remodel:"renovation cost", maintenance:"home maintenance budget", split:"labor and material split", contingency:"project contingency", quotes:"contractor quote comparison", toilet:"toilet installation cost"};
  const wrap=document.createElement("div");
  wrap.className="report-capture";
  wrap.innerHTML=`
    <div class="report-badge">FREE PERSONALIZED REPORT</div>
    <h3>Email me my ${labels[type] || "project"} report</h3>
    <p>Send this estimate and the key assumptions to your inbox so you can compare options later.</p>
    <form class="calculator-report-form" novalidate>
      <label class="report-email-label">Email address</label>
      <div class="report-email-row">
        <input name="email" type="email" autocomplete="email" placeholder="you@example.com" required>
        <button type="submit">Send my report</button>
      </div>
      <label class="report-consent">
        <input name="marketingConsent" type="checkbox">
        <span>Also send me occasional home-cost tips, calculators and product updates. I can unsubscribe anytime.</span>
      </label>
      <input class="report-honeypot" name="companyWebsite" type="text" tabindex="-1" autocomplete="off" aria-hidden="true">
      <small class="report-privacy">Your report is free. Marketing emails are optional. See our <a href="/privacy.html">Privacy Policy</a>.</small>
      <div class="report-status" data-report-status role="status" aria-live="polite"></div>
    </form>`;
  shell.appendChild(wrap);

  const form=wrap.querySelector(".calculator-report-form");
  form.addEventListener("submit",async event=>{
    event.preventDefault();
    const email=(form.elements.email?.value || "").trim();
    const status=form.querySelector("[data-report-status]");
    const button=form.querySelector('button[type="submit"]');
    status.className="report-status"; status.textContent="";
    if(!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)){
      status.classList.add("error"); status.textContent="Please enter a valid email address."; return;
    }
    button.disabled=true; button.textContent="Sending…";
    try{
      const res=await fetch("/api/report",{
        method:"POST", headers:{"Content-Type":"application/json"},
        body:JSON.stringify({
          email, reportType:type, calculatorInputs:currentCalculatorInputs(type),
          marketingConsent:form.elements.marketingConsent?.checked===true,
          companyWebsite:(form.elements.companyWebsite?.value || "").trim()
        })
      });
      let data={}; try{data=await res.json();}catch{}
      if(!res.ok) throw new Error(data.error || "Could not send your report. Please try again.");
      status.classList.add("success"); status.textContent="Report sent. Check your inbox in the next few minutes.";
      button.textContent="Sent ✓";
      setTimeout(()=>{button.disabled=false;button.textContent="Send my report";},4000);
    }catch(err){
      status.classList.add("error"); status.textContent=err.message || "Could not send your report. Please try again.";
      button.disabled=false; button.textContent="Send my report";
    }
  });
}

const HCE_VALUE_GUIDES={
  roof:{title:"Turn this roof estimate into a quote-ready plan",intro:"Use the range as a screening benchmark, then compare written scopes—not just totals.",diy:"DIY is generally limited to measuring, photographing damage and collecting product preferences. Roofing work involves fall, structural and weatherproofing risks.",pro:"Hire a qualified roofing contractor for tear-off, deck inspection, flashing, ventilation and code or permit decisions.",checks:["Confirm measured roof area, pitch and waste","Request matching material and warranty specifications","Separate tear-off, deck repairs, permits and disposal"],links:[["Compare contractor quotes","/calculators/contractor-quote-comparison.html"],["Roof replacement checklist","/blog/roof-replacement-checklist.html"],["Choose a roofing contractor","/blog/how-to-choose-roofing-contractor.html"]]},
  roofdeck:{title:"Turn the decking allowance into a controlled change order",intro:"Decking is often concealed until tear-off, so the best budget uses a documented quantity and a written per-sheet rate rather than an undefined wood allowance.",diy:"Homeowners can review photos, panel counts, contract terms and invoices from the ground. Open-roof work, structural assessment and sheathing installation are high-risk tasks.",pro:"Use a qualified roofing contractor for deck inspection and replacement. Structural framing damage, code questions or unusual conditions may require additional professional review.",checks:["Get the installed per-sheet rate in writing before tear-off","Require photos or marked quantities for replaced panels","Separate sheathing from rafter, fascia, mold and interior repair"],links:[["Roof decking replacement guide","/blog/roof-decking-replacement-cost.html"],["Roof replacement cost calculator","/calculators/roof-replacement.html"],["Compare contractor quotes","/calculators/contractor-quote-comparison.html"]]},
  concrete:{title:"Plan the order before the truck arrives",intro:"Volume is only the starting point. Confirm subgrade, forms, reinforcement, access and delivery minimums before ordering.",diy:"Small non-structural pads may be manageable if you can prepare forms, place and finish concrete safely before it sets.",pro:"Consider a concrete contractor for structural slabs, difficult access, drainage-sensitive work, large pours or projects requiring permits.",checks:["Verify compacted base and finished thickness","Ask about short-load, delivery and pumping fees","Confirm reinforcement, joints, slope and curing plan"],links:[["Cubic yard calculator","/calculators/cubic-yard.html"],["Ready-mix vs bags","/blog/ready-mix-concrete-vs-bags.html"],["Concrete cost per yard","/blog/concrete-cost-per-yard-explained.html"]]},
  hvac:{title:"Convert the HVAC range into comparable proposals",intro:"Equipment price alone is not a complete system quote. Sizing, ductwork, electrical work and commissioning can materially change cost.",diy:"Homeowners can document comfort problems, filter size, equipment age and utility use. Refrigerant and electrical work should not be treated as DIY tasks.",pro:"Use a licensed HVAC professional for load calculations, equipment selection, refrigerant handling, permits and startup testing.",checks:["Ask for Manual J or documented sizing assumptions","Compare efficiency ratings and exact model numbers","Separate duct, electrical, thermostat and permit work"],links:[["HVAC repair vs replacement","/blog/hvac-repair-vs-replacement.html"],["SEER2 explained","/blog/seer2-explained-for-homeowners.html"],["Compare contractor quotes","/calculators/contractor-quote-comparison.html"]]},
  paint:{title:"Build a practical painting shopping list",intro:"The gallon estimate helps with purchasing, while prep condition and number of color changes usually drive labor.",diy:"DIY can make sense for accessible interiors when you have time for patching, masking, sanding and multiple coats.",pro:"Hire a professional for high walls, damaged surfaces, exterior access, lead-safe work or a tight completion schedule.",checks:["Confirm wall condition and primer needs","Keep the same product and sheen assumptions","Add trim, ceilings, repairs and protection separately"],links:[["Room painting cost guide","/blog/how-much-does-it-cost-to-paint-a-room.html"],["Painting labor cost","/blog/painting-labor-cost-per-square-foot.html"],["Compare contractor quotes","/calculators/contractor-quote-comparison.html"]]},
  floor:{title:"Use the flooring total to compare full installed scope",intro:"Material price is only one part of a flooring project. Subfloor repairs, transitions, stairs and furniture moving are common differences between quotes.",diy:"Click-lock flooring in a simple empty room may suit an experienced DIYer who can prepare the subfloor and plan transitions.",pro:"Consider an installer for glue-down products, tile, stairs, moisture issues, complex layouts or warranty-sensitive work.",checks:["Verify measured area and waste percentage","Include removal, underlayment and subfloor preparation","Match trim, transitions, stairs and furniture scope"],links:[["Flooring waste guide","/blog/how-much-flooring-waste-should-i-add.html"],["Flooring cost per sq ft","/blog/flooring-cost-per-square-foot.html"],["Compare contractor quotes","/calculators/contractor-quote-comparison.html"]]},
  gravel:{title:"Turn the gravel estimate into an order-ready driveway plan",intro:"Use the total as a planning baseline, then verify the layer design, delivered tonnage and site-preparation scope with local suppliers and installers.",diy:"Refreshing a small, stable surface may be manageable with safe equipment access. Building a new driveway base requires grading, drainage and compaction decisions that affect long-term performance.",pro:"Consider an experienced driveway or excavation contractor for soft subgrade, drainage problems, steep slopes, culvert work, major excavation or limited truck access.",checks:["Confirm compacted depth and whether multiple aggregate layers are required","Ask the supplier to verify tons per cubic yard and delivered-load fees","Separate excavation, fabric, grading, drainage and compaction in every quote"],links:[["Driveway gravel quantity guide","/blog/how-much-gravel-do-i-need-for-a-driveway"],["Gravel driveway cost per square foot","/blog/gravel-driveway-cost"],["Compare contractor quotes","/calculators/contractor-quote-comparison.html"]]},
  remodel:{title:"Move from a state-adjusted budget to a bid package",intro:"This range is a planning baseline. A useful contractor comparison requires the same drawings, finish assumptions and exclusions for every bidder.",diy:"Homeowners can define priorities, collect product selections and document existing conditions. Trade work may require permits and licensed professionals.",pro:"Use qualified professionals when work affects structure, electrical, plumbing, HVAC, waterproofing or code compliance.",checks:["Write one scope and give it to every bidder","Separate allowances from fixed-price work","Keep contingency owner-controlled until changes are approved"],links:[["Compare contractor quotes","/calculators/contractor-quote-comparison.html"],["Project contingency calculator","/calculators/project-contingency.html"],["Worked project examples","/project-cost-examples.html"]]},
  quotes:{title:"Investigate the differences before choosing",intro:"The lowest number is not automatically the best value. Normalize scope, allowances, qualifications and contract terms first.",diy:"You can organize proposals and verify that each bidder answered the same scope. Avoid making a decision from the score alone.",pro:"For major or technical projects, an independent designer, engineer or construction professional can help review scope and risk.",checks:["Verify license, insurance and references","Clarify exclusions, allowances and change orders","Compare payment schedule, warranty and completion terms"],links:[["Project contingency calculator","/calculators/project-contingency.html"],["Home improvement glossary","/home-improvement-glossary.html"],["Cost methodology","/cost-methodology.html"]]},
  maintenance:{title:"Turn the annual reserve into a home maintenance plan",intro:"A reserve works best when it is divided into predictable upkeep, near-term replacements and emergency cash.",diy:"Routine inspections, filter changes and simple seasonal upkeep can reduce surprises when performed safely.",pro:"Use qualified trades for electrical, gas, roofing, structural, refrigerant and other regulated or high-risk work.",checks:["List equipment age and expected replacement year","Separate annual upkeep from capital replacements","Review the reserve after major repairs or renovations"],links:[["Project contingency calculator","/calculators/project-contingency.html"],["Home improvement glossary","/home-improvement-glossary.html"],["All cost guides","/guides/"]]},
  contingency:{title:"Keep uncertainty separate from known scope",intro:"A contingency is not permission to overspend. It is an owner-controlled reserve for documented surprises and approved changes.",diy:"You can maintain the change log, request supporting prices and track the remaining reserve throughout the project.",pro:"For complex work, a designer or construction professional can review whether a proposed change is necessary and reasonably priced.",checks:["Do not mix allowances with contingency","Document every draw from the reserve","Reforecast the remaining budget after each change"],links:[["Compare contractor quotes","/calculators/contractor-quote-comparison.html"],["Worked project examples","/project-cost-examples.html"],["Cost methodology","/cost-methodology.html"]]},
  split:{title:"Use the split to test what a proposal includes",intro:"Labor and material percentages are planning assumptions, not universal rules. Scope, access and product selection can shift the mix.",diy:"Use the split to ask clearer questions about product allowances, crew time and excluded work.",pro:"Ask the contractor to explain major cost categories without requiring disclosure of private payroll or supplier terms.",checks:["Confirm percentages add up to 100%","Separate allowances and owner-supplied items","Check permits, disposal, overhead and warranty coverage"],links:[["Compare contractor quotes","/calculators/contractor-quote-comparison.html"],["Project contingency calculator","/calculators/project-contingency.html"],["Home improvement glossary","/home-improvement-glossary.html"]]},
  default:{title:"Use this result as a planning checkpoint",intro:"Recheck measurements and assumptions before purchasing materials or comparing contractor proposals.",diy:"DIY suitability depends on safety, access, tools, experience and local code requirements—not cost alone.",pro:"Use a qualified professional for regulated, structural, electrical, gas, roofing or other high-risk work.",checks:["Verify measurements and units","Add waste, delivery and project-specific extras","Compare the same scope across local quotes"],links:[["Compare contractor quotes","/calculators/contractor-quote-comparison.html"],["Project contingency calculator","/calculators/project-contingency.html"],["All planning tools","/calculators/"]]}
};

function injectPlanningValue(type){
  if(document.querySelector(".planning-value-section")) return;
  const tool=document.querySelector(".calc-shell, .hce-tool");
  const calcSection=tool?.closest("section");
  if(!calcSection) return;
  const guide=HCE_VALUE_GUIDES[type]||HCE_VALUE_GUIDES.default;
  const section=document.createElement("section");
  section.className="section planning-value-section";
  section.innerHTML=`<div class="container planning-value">
    <div class="planning-value-head"><span class="eyebrow">YOUR NEXT STEPS</span><h2>${guide.title}</h2><p>${guide.intro}</p></div>
    <div class="planning-value-grid">
      <article><h3>DIY planning</h3><p>${guide.diy}</p></article>
      <article><h3>When to call a professional</h3><p>${guide.pro}</p></article>
      <article class="planning-checks"><h3>Before you request quotes</h3><ul>${guide.checks.map(item=>`<li>${item}</li>`).join("")}</ul></article>
    </div>
    <nav class="planning-links" aria-label="Related planning resources">${guide.links.map(([label,href])=>`<a href="${href}">${label}<span aria-hidden="true">→</span></a>`).join("")}</nav>
    <p class="planning-disclaimer">Planning guidance only. Verify measurements, permits, code requirements, product specifications and site conditions with qualified local professionals.</p>
  </div>`;
  calcSection.insertAdjacentElement("afterend",section);
}

document.addEventListener("DOMContentLoaded",()=>{
  const type=document.body.dataset.calculator;
  if(type==="roof")populateRoofStates();
  if(type==="roofpitch")initRoofPitchControls();
  const fn={roof:roofCalc,concrete:concreteCalc,paint:paintCalc,floor:floorCalc,mulch:mulchCalc,hvac:hvacCalc,sqft:squareFootageCalc,cubicyard:cubicYardCalc,gravel:gravelCalc,roofsquare:roofingSquareCalc,roofdeck:roofDeckCalc,roofpitch:roofPitchCalc}[type];
  const form=document.getElementById("calculatorForm");
  if(form&&fn){form.addEventListener("submit",e=>{e.preventDefault();fn()}); fn();}
  if(type){injectEmailReportForm(type);injectPlanningValue(type);}
});
