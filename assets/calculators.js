const money = n => new Intl.NumberFormat("en-US",{style:"currency",currency:"USD",maximumFractionDigits:0}).format(n);
const num = id => Number(document.getElementById(id)?.value || 0);
const val = id => document.getElementById(id)?.value;
const set = (id, value) => { const el=document.getElementById(id); if(el) el.textContent=value; };

function roofCalc(){
  const area=num("area"), material=val("material"), pitch=Number(val("pitch")), stories=Number(val("stories")),
        market=Number(val("market")), tear=val("tearoff")==="yes";
  if(area<=0) return;
  const ranges={
    asphalt:[5.5,9], metal:[9,16], tile:[10,20], wood:[7,14], slate:[15,30]
  };
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
document.addEventListener("DOMContentLoaded",()=>{
  const type=document.body.dataset.calculator;
  const fn={roof:roofCalc,concrete:concreteCalc,paint:paintCalc,floor:floorCalc,mulch:mulchCalc,hvac:hvacCalc}[type];
  const form=document.getElementById("calculatorForm");
  if(form&&fn){form.addEventListener("submit",e=>{e.preventDefault();fn()}); fn();}
});