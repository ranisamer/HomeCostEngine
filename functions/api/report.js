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
    const pitch=finite(raw.pitch,.5,3),stories=finite(raw.stories,.5,3),market=finite(raw.market,.5,3),tearLayers=finite(raw.tearoff,0,3),deckArea=finite(raw.deckArea,0,1e7),features=finite(raw.roofFeatures,0,100),permit=finite(raw.roofPermit,0,1e7),contingency=finite(raw.roofContingency,0,.5);
    if(![pitch,stories,market,tearLayers,deckArea,features,permit,contingency].every(Number.isFinite)) throw new Error("Check the roof scope and market selections.");
    const stateFactors={AL:.927,AK:1.015,AZ:1.004,AR:.915,CA:1.070,CO:1.020,CT:1.023,DE:.999,DC:1.064,FL:1.022,GA:.976,HI:1.065,ID:.971,IL:1.000,IN:.957,IA:.920,KS:.935,KY:.936,LA:.923,ME:.981,MD:1.032,MA:1.037,MI:.975,MN:.991,MS:.915,MO:.940,MT:.965,NE:.936,NV:1.000,NH:1.027,NJ:1.057,NM:.949,NY:1.051,NC:.963,ND:.928,OH:.953,OK:.921,OR:1.022,PA:.984,RI:1.015,SC:.959,SD:.926,TN:.947,TX:.981,UT:.993,VT:.987,VA:1.007,WA:1.046,WV:.932,WI:.962,WY:.953};
    const stateCode=String(raw.roofState||"US").toUpperCase(),stateFactor=stateFactors[stateCode]||1,tearRates={0:[0,0],1:[1.15,2.35],2:[1.75,3.5],3:[2.5,4.75]},tear=tearRates[Math.round(tearLayers)]||tearRates[1];
    let [lo,hi]=ranges[material];lo*=pitch*stories*market*stateFactor;hi*=pitch*stories*market*stateFactor;
    const baseLow=area*lo,baseHigh=area*hi,tearLow=area*tear[0],tearHigh=area*tear[1],deckLow=deckArea*3.5,deckHigh=deckArea*7,featureLow=features*250,featureHigh=features*750,subtotalLow=baseLow+tearLow+deckLow+featureLow+permit,subtotalHigh=baseHigh+tearHigh+deckHigh+featureHigh+permit,low=subtotalLow*(1+contingency),high=subtotalHigh*(1+contingency),mid=(low+high)/2;
    return {title:"Roof Replacement Cost Report",subject:`Your roof cost estimate: ${money(low)}–${money(high)}`,url:"https://homecostengine.com/calculators/roof-replacement",
      summary:`Your planning range is ${money(low)} to ${money(high)}, with a midpoint of about ${money(mid)}.`,
      metrics:[["Roof area",`${Math.round(area).toLocaleString("en-US")} sq ft`],["Location",stateCode==="US"?"U.S. national baseline":stateCode],["Roofing material",material==="asphalt"?"Asphalt shingles":material.charAt(0).toUpperCase()+material.slice(1)],["Tear-off layers",String(Math.round(tearLayers))],["Deck repair allowance",`${Math.round(deckArea).toLocaleString("en-US")} sq ft`],["Roof details",`${Math.round(features)} skylight / chimney / complex features`],["Permit allowance",money(permit)],["Contingency",`${number(contingency*100,0)}%`],["Estimated range",`${money(low)} – ${money(high)}`],["Midpoint",money(mid)],["Estimated unit range",`${money(low/area)} – ${money(high/area)} / sq ft`]],
      note:"This is a budgeting range. Verify measured roof area, decking, flashing, ventilation, underlayment, permits, access, warranty terms and local labor in written contractor proposals."};
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

  if(type==="sqft"){
    const shape=String(raw.areaShape||"rectangle"),a=finite(raw.areaLength,.01,1e9),b=finite(raw.areaWidth,.01,1e9);
    if(!Number.isFinite(a)) throw new Error("Check your area measurements.");
    let area=0;
    if(shape==="circle") area=Math.PI*Math.pow(a/2,2);
    else if(shape==="square") area=a*a;
    else { if(!Number.isFinite(b)) throw new Error("Enter a valid width."); area=a*b; }
    return {title:"Square Footage Report",subject:`Your area: ${number(area,2)} sq ft`,url:"https://homecostengine.com/calculators/square-footage.html",summary:`Your calculated area is ${number(area,2)} square feet.`,metrics:[["Shape",shape],["Square feet",`${number(area,2)} sq ft`],["Square yards",`${number(area/9,2)} sq yd`],["Acres",number(area/43560,4)]],note:"For irregular spaces, split the project into simple shapes and add the results."};
  }
  if(type==="cubicyard"){
    const l=finite(raw.cyLength,.01,1e7),w=finite(raw.cyWidth,.01,1e7),d=finite(raw.cyDepth,.01,1e5),waste=finite(raw.cyWaste,1,2);
    if(![l,w,d,waste].every(Number.isFinite)) throw new Error("Check your cubic-yard inputs.");
    const base=(l*w*(d/12))/27,yards=base*waste;
    return {title:"Cubic Yard Report",subject:`Your volume: ${number(yards,2)} yd³`,url:"https://homecostengine.com/calculators/cubic-yard.html",summary:`Your project volume is about ${number(yards,2)} cubic yards including waste.`,metrics:[["Cubic yards",`${number(yards,2)} yd³`],["Cubic feet",`${number(yards*27,1)} ft³`],["Cubic meters",`${number(yards*.764555,2)} m³`],["Waste allowance",`${number((waste-1)*100,0)}%`]],note:"Supplier order increments, compaction and site conditions can change the practical order quantity."};
  }
  if(type==="gravel"){
    const length=finite(raw.gravelLength,.01,1e6),width=finite(raw.gravelWidth,.01,1e6),depth=finite(raw.gravelDepth,.01,1e4),density=finite(raw.gravelType,.5,3),waste=finite(raw.gravelWaste,1,2),price=finite(raw.gravelPrice,0,1e7),delivery=finite(raw.gravelDelivery,0,1e8),prepRate=finite(raw.gravelPrepRate,0,1e5);
    if(![length,width,depth,density,waste,price,delivery,prepRate].every(Number.isFinite)) throw new Error("Check your gravel driveway inputs.");
    const area=length*width,yards=area*(depth/12)/27*waste,tons=yards*density,material=tons*price,prep=area*prepRate,total=material+delivery+prep;
    return {title:"Gravel Driveway Cost Report",subject:`Your gravel driveway estimate: ${money(total)}`,url:"https://homecostengine.com/calculators/gravel",summary:`Your ${number(area,0)} sq ft driveway planning estimate is ${money(total)} for about ${number(tons,2)} tons of gravel.`,metrics:[["Driveway size",`${number(length,0)} ft × ${number(width,0)} ft`],["Planned depth",`${number(depth,1)} in`],["Cubic yards",`${number(yards,2)} yd³`],["Estimated tons",number(tons,2)],["Material",money(material)],["Delivery",money(delivery)],["Site preparation / labor",money(prep)],["Planning total",money(total)]],note:"This is a planning estimate based on one compacted layer. Confirm the layer design, compaction factor, supplier density, delivery access, drainage and site conditions locally."};
  }
  if(type==="roofsquare"){
    const area=finite(raw.rsArea,1,1e9),waste=finite(raw.rsWaste,1,2),bundles=finite(raw.rsBundles,1,20);
    if(![area,waste,bundles].every(Number.isFinite)) throw new Error("Check your roofing-square inputs.");
    const base=area/100,total=base*waste,bundleCount=Math.ceil(total*bundles);
    return {title:"Roofing Square Report",subject:`Your roofing quantity: ${number(total,2)} squares`,url:"https://homecostengine.com/calculators/roofing-square.html",summary:`Your roof needs about ${number(total,2)} roofing squares including waste.`,metrics:[["Roof area",`${number(area,0)} sq ft`],["Base squares",number(base,2)],["Squares with waste",number(total,2)],["Approx. bundles",String(bundleCount)]],note:"Bundle counts vary by shingle product. Verify packaging and waste requirements before ordering."};
  }
  if(type==="roofdeck"){
    const area=finite(raw.rdArea,1,1e9),waste=finite(raw.rdWaste,1,2),rate=finite(raw.rdRate,0,1e6),extra=finite(raw.rdExtra,0,1e8);
    if(![area,waste,rate,extra].every(Number.isFinite)) throw new Error("Check your roof decking inputs.");
    const adjustedArea=area*waste,sheets=Math.ceil(adjustedArea/32),panelCost=sheets*rate,total=panelCost+extra;
    const marketLow=sheets*64+extra,marketHigh=sheets*160+extra;
    return {title:"Roof Decking Replacement Cost Report",subject:`Your roof decking allowance: ${money(total)}`,url:"https://homecostengine.com/calculators/roof-decking-replacement-cost.html",summary:`Your inputs produce a planning allowance of ${money(total)} for about ${sheets} standard 4×8 panels.`,metrics:[["Damaged / replacement area",`${number(area,0)} sq ft`],["Allowance factor",`${number((waste-1)*100,0)}%`],["Estimated 4×8 sheets",String(sheets)],["Your installed rate",`${money(rate)} / sheet`],["Extra allowance",money(extra)],["Planning total",money(total)],["Broad 2026 reference band",`${money(marketLow)} – ${money(marketHigh)}`]],note:"The broad reference band derives from current published installed ranges around $2–$5 per square foot, equivalent to roughly $64–$160 for a 32-square-foot panel. Use your contractor’s written unit rate for project decisions and verify what the rate includes."};
  }
  if(type==="roofpitch"){
    const mode=String(raw.pitchMode||"riseRun");
    let ratio=0,rise=0,run=12,angle=0,slope=0,mult=1,rafter=null,roofArea=null;
    if(mode==="degrees"){
      angle=finite(raw.pitchDegrees,.01,88.9);
      if(!Number.isFinite(angle)) throw new Error("Check your roof angle.");
      ratio=Math.tan(angle*Math.PI/180); rise=ratio*12;
    }else if(mode==="percent"){
      slope=finite(raw.pitchPercent,.01,10000);
      if(!Number.isFinite(slope)) throw new Error("Check your slope percentage.");
      ratio=slope/100; rise=ratio*12; angle=Math.atan(ratio)*180/Math.PI;
    }else if(mode==="dimensions"){
      rise=finite(raw.pitchDimRise,0,1000);
      const width=finite(raw.pitchBuildingWidth,.01,100000),length=finite(raw.pitchBuildingLength,.01,100000),eave=finite(raw.pitchEave,0,10000),gable=finite(raw.pitchGable,0,10000);
      if(![rise,width,length,eave,gable].every(Number.isFinite)) throw new Error("Check your building dimensions.");
      ratio=rise/12; angle=Math.atan(ratio)*180/Math.PI; slope=ratio*100; mult=Math.sqrt(1+ratio*ratio);
      const halfHorizontal=(width/2)+(eave/12),roofLength=length+(2*gable/12);
      rafter=halfHorizontal*mult; roofArea=2*rafter*roofLength;
    }else{
      rise=finite(raw.pitchRise,0,100000); run=finite(raw.pitchRun,.01,100000);
      if(!Number.isFinite(rise)||!Number.isFinite(run)) throw new Error("Check your rise and run.");
      ratio=rise/run; angle=Math.atan(ratio)*180/Math.PI;
    }
    slope=slope||ratio*100; mult=Math.sqrt(1+ratio*ratio);
    if(mode!=="dimensions"){
      const span=finite(raw.pitchSpan,0,100000),footprint=finite(raw.pitchFootprint,0,1e9);
      if(Number.isFinite(span)&&span>0) rafter=span*mult;
      if(Number.isFinite(footprint)&&footprint>0) roofArea=footprint*mult;
    }
    const pitch12=ratio*12;
    const metrics=[["Pitch",`${number(pitch12,1)}:12`],["Angle",`${number(angle,1)}°`],["Slope",`${number(slope,1)}%`],["Pitch / area multiplier",`${number(mult,3)}×`]];
    if(rafter!==null) metrics.push(["Approx. rafter / slope length",`${number(rafter,2)} ft`]);
    if(roofArea!==null){metrics.push(["Approx. roof surface",`${number(roofArea,0)} sq ft`]);metrics.push(["Roofing squares",number(roofArea/100,2)]);}
    return {title:"Roof Pitch & Area Report",subject:`Your roof pitch: ${number(pitch12,1)}:12`,url:"https://homecostengine.com/calculators/roof-pitch.html",summary:`Your roof pitch is approximately ${number(pitch12,1)}:12, or ${number(angle,1)} degrees, with a ${number(mult,3)}× area multiplier.`,metrics,note:"Use roof pitch as one input in material and cost planning. Complex roofs, hips, valleys, dormers and uneven overhangs should be measured by roof plane. Do not access an unsafe roof to improve an online estimate."};
  }
  if(type==="heatcompare"){
    const hpInstall=finite(raw.hpInstall,0,1e8),acInstall=finite(raw.acInstall,0,1e8),furnaceInstall=finite(raw.furnaceInstall,0,1e8),hpAnnual=finite(raw.hpAnnual,0,1e7),traditionalAnnual=finite(raw.traditionalAnnual,0,1e7),years=finite(raw.comparisonYears,1,25),incentive=finite(raw.hpIncentive,0,1e8);
    if(![hpInstall,acInstall,furnaceInstall,hpAnnual,traditionalAnnual,years,incentive].every(Number.isFinite)) throw new Error("Check your heat pump and AC comparison inputs.");
    const hpNet=Math.max(0,hpInstall-Math.min(hpInstall,incentive)),traditionalInstall=acInstall+furnaceInstall,hpTotal=hpNet+hpAnnual*years,traditionalTotal=traditionalInstall+traditionalAnnual*years,difference=Math.abs(hpTotal-traditionalTotal),winner=hpTotal===traditionalTotal?"Both options":hpTotal<traditionalTotal?"Heat pump":"Central AC plus furnace";
    return {title:"Heat Pump vs AC Cost Report",subject:`Your ${number(years,0)}-year HVAC comparison`,url:"https://homecostengine.com/blog/heat-pump-vs-central-air-cost",summary:`${winner} has the lower modeled ${number(years,0)}-year total by ${money(difference)} under your assumptions.`,metrics:[["Heat pump net installed cost",money(hpNet)],["AC plus furnace installed cost",money(traditionalInstall)],["Heat pump annual operation",money(hpAnnual)],["AC plus heating annual operation",money(traditionalAnnual)],["Heat pump ownership total",money(hpTotal)],["AC plus furnace ownership total",money(traditionalTotal)],["Modeled difference",money(difference)]],note:"This simple comparison does not forecast energy-price changes, financing, maintenance, equipment life or replacement timing. Confirm equipment suitability, climate performance and matching scope with qualified local contractors."};
  }
  if(type==="maintenance"){
    const value=finite(raw.homeValue,1,1e9),rate=finite(raw.rate,0,10),known=finite(raw.known,0,1e9);
    if(![value,rate,known].every(Number.isFinite)) throw new Error("Check your maintenance budget inputs.");
    const annual=value*rate/100+known,monthly=annual/12;
    return {title:"Home Maintenance Budget Report",subject:`Your annual maintenance reserve: ${money(annual)}`,url:"https://homecostengine.com/calculators/home-maintenance-budget.html",summary:`Your planning reserve is ${money(annual)} per year, or about ${money(monthly)} per month.`,metrics:[["Estimated home value",money(value)],["Planning rate",`${number(rate,1)}%`],["Known annual maintenance",money(known)],["Annual reserve",money(annual)],["Monthly set-aside",money(monthly)]],note:"This percentage method is a starting point. Home age, climate, system condition and deferred maintenance can materially change the amount needed."};
  }
  if(type==="split"){
    const total=finite(raw.total,1,1e12),laborPct=finite(raw.labor,0,100),materialPct=finite(raw.material,0,100);
    if(![total,laborPct,materialPct].every(Number.isFinite)||laborPct+materialPct>100) throw new Error("Check the estimate and percentage shares.");
    const otherPct=100-laborPct-materialPct;
    return {title:"Labor and Material Cost Split Report",subject:`Your project cost split: ${money(total)}`,url:"https://homecostengine.com/calculators/labor-material-split.html",summary:`Your ${money(total)} estimate has been separated into labor, materials and other costs.`,metrics:[["Total estimate",money(total)],["Labor",`${money(total*laborPct/100)} (${number(laborPct,1)}%)`],["Materials",`${money(total*materialPct/100)} (${number(materialPct,1)}%)`],["Other / overhead",`${money(total*otherPct/100)} (${number(otherPct,1)}%)`]],note:"Actual cost structures vary by trade and contractor. Use this split for planning and compare written scope, specifications, exclusions and allowances."};
  }
  if(type==="contingency"){
    const base=finite(raw.base,1,1e12),rate=finite(raw.rate,0,100),allowance=finite(raw.allowance,0,1e12);
    if(![base,rate,allowance].every(Number.isFinite)) throw new Error("Check your contingency inputs.");
    const reserve=base*rate/100,total=base+allowance+reserve;
    return {title:"Project Contingency Report",subject:`Your planning budget: ${money(total)}`,url:"https://homecostengine.com/calculators/project-contingency.html",summary:`Your total planning budget is ${money(total)}, including a ${money(reserve)} contingency reserve.`,metrics:[["Base estimate",money(base)],["Known allowances",money(allowance)],["Contingency rate",`${number(rate,1)}%`],["Contingency reserve",money(reserve)],["Total planning budget",money(total)]],note:"Keep contingency separate from known allowances. Release it only for documented changes or unexpected conditions."};
  }
  if(type==="toilet"){
    const fixture=finite(raw.fixture,0,1e7),labor=finite(raw.labor,0,1e7),removal=finite(raw.removal,0,1e7),connections=finite(raw.connections,0,1e7),valve=finite(raw.valve,0,1e7),flange=finite(raw.flange,0,1e7),floor=finite(raw.floor,0,1e7),permit=finite(raw.permit,0,1e7),taxRate=finite(raw.tax,0,20),contingencyRate=finite(raw.contingency,0,30);
    if(![fixture,labor,removal,connections,valve,flange,floor,permit,taxRate,contingencyRate].every(Number.isFinite)) throw new Error("Check your toilet installation inputs before sending the report.");
    const tax=(fixture+connections)*taxRate/100,known=fixture+labor+removal+connections+permit+tax,repairs=valve+flange+floor,typical=known+repairs,contingency=typical*contingencyRate/100,high=typical+contingency;
    return {title:"Toilet Installation Cost Report",subject:`Your toilet installation plan: ${money(typical)}`,url:"https://homecostengine.com/calculators/toilet-installation-cost.html",summary:`Your entered scope produces a ${money(typical)} typical planning total and a ${money(high)} high plan with contingency.`,metrics:[["Fixture and connections",money(fixture+connections+tax)],["Labor, removal and permit",money(labor+removal+permit)],["Valve allowance",money(valve)],["Flange allowance",money(flange)],["Floor repair allowance",money(floor)],["Known subtotal",money(known)],["Typical with repair allowances",money(typical)],["Contingency reserve",`${money(contingency)} (${number(contingencyRate,0)}%)`],["High planning amount",money(high)]],note:"Repair allowances are not proof that work is required. Confirm fixture compatibility, concealed conditions, permits and every added line item in a written local proposal."};
  }
  if(type==="quotes"){
    const quotes=Array.isArray(raw.quotes)?raw.quotes.slice(0,3):[];
    if(quotes.length!==3) throw new Error("Enter all three contractor quotes.");
    const metrics=[];quotes.forEach((q,i)=>{const price=finite(q.price,0,1e12),allowance=finite(q.allowance,0,1e12),scope=finite(q.scope,1,5),warranty=finite(q.warranty,1,5);if(![price,allowance,scope,warranty].every(Number.isFinite))throw new Error("Check the contractor quote inputs.");metrics.push([`Quote ${String.fromCharCode(65+i)}`,`${money(price)} total • ${money(Math.max(0,price-allowance))} less allowances • scope ${scope}/5 • warranty ${warranty}/5`]);});
    return {title:"Contractor Quote Comparison Report",subject:"Your contractor quote comparison",url:"https://homecostengine.com/calculators/contractor-quote-comparison.html",summary:"Your three quotes are organized below so you can compare price, allowances, scope completeness and warranty clarity.",metrics,note:"The lowest price or highest score is not automatically the best contractor. Verify licensing, insurance, references, exclusions, payment terms and written scope."};
  }
  if(type==="remodel"){
    const clean=(v,max=120)=>String(v||"").replace(/[<>]/g,"").slice(0,max);
    const qty=finite(raw.quantity,1,1e8);if(!Number.isFinite(qty)||!clean(raw.estimateRange)) throw new Error("Build your renovation budget before sending the report.");
    return {title:"Home Renovation Cost Report",subject:`Your ${clean(raw.projectName,60)} estimate: ${clean(raw.estimateRange,80)}`,url:"https://homecostengine.com/calculators/remodeling-cost.html",summary:`Your planning range for ${clean(raw.projectName,60).toLowerCase()} in ${clean(raw.stateName,80)} is ${clean(raw.estimateRange,80)}.`,metrics:[["Project",clean(raw.projectName,80)],["Location",clean(raw.stateName,80)],["Project size",number(qty,0)],["Estimated range",clean(raw.estimateRange,80)],["Planning midpoint",clean(raw.midpoint,60)],["Unit cost",clean(raw.unitCost,60)],["Typical timeline",clean(raw.timeline,60)],["Materials",clean(raw.materials,60)],["Labor",clean(raw.labor,60)],["Demolition / disposal",clean(raw.demo,60)],["Permit allowance",clean(raw.permitCost,60)],["Contingency",clean(raw.contingencyAmount,60)]],note:"This is a state-adjusted planning model, not a contractor quote. Compare itemized local bids with matching scope, allowances, exclusions and warranty terms."};
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
  const senderEmail=String(env.BREVO_SENDER_EMAIL || "reports@mail.homecostengine.com").trim();
  const replyToEmail=String(env.BREVO_REPLY_TO || "reports@homecostengine.com").trim();
  if(!env.BREVO_API_KEY) return json({error:"Email service is temporarily unavailable. Please try again shortly."},503);

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
    sender:{name:"HomeCostEngine",email:senderEmail},to:[{email}],
    replyTo:{name:"HomeCostEngine",email:replyToEmail},
    subject:report.subject,htmlContent:emailHtml(report)
  })});
  if(!mailResp.ok){console.log("Brevo send error",mailResp.status,await mailResp.text());return json({error:"We couldn't send the report right now. Please try again shortly."},502);}
  return json({ok:true,subscribed:body.marketingConsent===true});
}
export async function onRequest(){return json({error:"Method not allowed."},405);}
