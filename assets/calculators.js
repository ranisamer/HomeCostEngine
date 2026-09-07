const money = n => new Intl.NumberFormat("en-US",{style:"currency",currency:"USD",maximumFractionDigits:0}).format(n);
const num = id => Number(document.getElementById(id)?.value || 0);
const val = id => document.getElementById(id)?.value;
const set = (id, value) => { const el=document.getElementById(id); if(el) el.textContent=value; };

function roofCalc(){
  const area=num("area"), material=val("material"), pitch=Number(val("pitch")), stories=Number(val("stories")),
        market=Number(val("market")), tear=val("tearoff")==="yes";
  if(area<=0) return;
  const ranges={asphalt:[5.5,9], metal:[9,16], tile:[10,20], wood:[7,14], slate:[15,30]};
  let [lo,hi]=ranges[material];
  lo*=pitch*stories*market; hi*=pitch*stories*market;
  if(tear){lo+=1.15;hi+=2.35}
  const low=area*lo, high=area*hi, mid=(low+high)/2;
  set("result",money(mid)); set("range",`${money(low)} – ${money(high)}`);
  set("unit",`${money(lo)} – ${money(hi)} / sq ft`);
  set("materials",money(mid*.44)); set("labor",money(mid*.39)); set("other",money(mid*.17));
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
  const area=num("gravelArea"),depth=num("gravelDepth"),density=Number(val("gravelType")),waste=Number(val("gravelWaste")),price=num("gravelPrice");
  if(area<=0||depth<=0)return;
  const yards=area*(depth/12)/27*waste, tons=yards*density, cost=price?tons*price:0;
  set("result",`${yards.toFixed(2)} yd³`); set("range",`${tons.toFixed(2)} estimated tons`);
  set("unit",`${yards.toFixed(2)} yd³`); set("materials",`${tons.toFixed(2)} tons`);
  set("labor",price?money(cost):"Add price / ton"); set("other",`${((waste-1)*100).toFixed(0)}%`);
}
function roofingSquareCalc(){
  const area=num("rsArea"),waste=Number(val("rsWaste")),bundles=num("rsBundles")||3;
  if(area<=0)return;
  const base=area/100,total=base*waste,bundleCount=Math.ceil(total*bundles);
  set("result",`${total.toFixed(2)} squares`); set("range",`${bundleCount} approximate bundles`);
  set("unit",`${base.toFixed(2)} squares`); set("materials",`${total.toFixed(2)} squares`);
  set("labor",`${bundleCount} bundles`); set("other",`${((waste-1)*100).toFixed(0)}%`);
}
function roofPitchCalc(){
  const rise=num("pitchRise"),run=num("pitchRun");
  if(run<=0||rise<0)return;
  const ratio=rise/run, pitch12=ratio*12, angle=Math.atan(ratio)*180/Math.PI, slope=ratio*100, mult=Math.sqrt(1+ratio*ratio);
  set("result",`${pitch12.toFixed(1)}:12`); set("range",`${angle.toFixed(1)}° roof angle`);
  set("unit",`${angle.toFixed(1)}°`); set("materials",`${slope.toFixed(1)}%`);
  set("labor",`${mult.toFixed(3)}×`); set("other",`${pitch12.toFixed(1)}:12`);
}

function currentCalculatorInputs(type){
  if(type==="roof") return {area:num("area"), material:val("material"), pitch:Number(val("pitch")), stories:Number(val("stories")), tearoff:val("tearoff"), market:Number(val("market"))};
  if(type==="concrete") return {length:num("length"), width:num("width"), thickness:num("thickness"), waste:Number(val("waste")), yardPrice:num("yardPrice")};
  if(type==="hvac") return {homeSqft:num("homeSqft"), system:val("system"), efficiency:Number(val("efficiency")), market:Number(val("market"))};
  if(type==="paint") return {roomLength:num("roomLength"), roomWidth:num("roomWidth"), roomHeight:num("roomHeight"), coats:num("coats"), doors:num("doors"), windows:num("windows"), coverage:num("coverage"), gallonPrice:num("gallonPrice")};
  if(type==="floor") return {floorArea:num("floorArea"), floorWaste:Number(val("floorWaste")), materialPrice:num("materialPrice"), laborPrice:num("laborPrice")};
  if(type==="mulch") return {mulchArea:num("mulchArea"), depth:num("depth"), mulchPrice:num("mulchPrice")};
  if(type==="sqft") return {areaShape:val("areaShape"), areaLength:num("areaLength"), areaWidth:num("areaWidth")};
  if(type==="cubicyard") return {cyLength:num("cyLength"), cyWidth:num("cyWidth"), cyDepth:num("cyDepth"), cyWaste:Number(val("cyWaste"))};
  if(type==="gravel") return {gravelArea:num("gravelArea"), gravelDepth:num("gravelDepth"), gravelType:Number(val("gravelType")), gravelWaste:Number(val("gravelWaste")), gravelPrice:num("gravelPrice")};
  if(type==="roofsquare") return {rsArea:num("rsArea"), rsWaste:Number(val("rsWaste")), rsBundles:num("rsBundles")};
  if(type==="roofpitch") return {pitchRise:num("pitchRise"), pitchRun:num("pitchRun")};
  return {};
}

function injectEmailReportForm(type){
  const shell=document.querySelector(".calc-shell");
  if(!shell || document.querySelector(".calculator-report-form")) return;
  const labels={roof:"roof cost", concrete:"concrete", hvac:"HVAC", paint:"paint", floor:"flooring", mulch:"mulch", sqft:"square footage", cubicyard:"cubic yard", gravel:"gravel", roofsquare:"roofing square", roofpitch:"roof pitch"};
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

document.addEventListener("DOMContentLoaded",()=>{
  const type=document.body.dataset.calculator;
  const fn={roof:roofCalc,concrete:concreteCalc,paint:paintCalc,floor:floorCalc,mulch:mulchCalc,hvac:hvacCalc,sqft:squareFootageCalc,cubicyard:cubicYardCalc,gravel:gravelCalc,roofsquare:roofingSquareCalc,roofpitch:roofPitchCalc}[type];
  const form=document.getElementById("calculatorForm");
  if(form&&fn){form.addEventListener("submit",e=>{e.preventDefault();fn()}); fn(); injectEmailReportForm(type);}
});