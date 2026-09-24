const json=(data,status=200,cache="public, max-age=21600")=>new Response(JSON.stringify(data),{status,headers:{"content-type":"application/json; charset=utf-8","cache-control":cache}});

const ZIP_RE=/^\d{5}$/;
const BLS_URL="https://api.bls.gov/publicAPI/v2/timeseries/data/";
const SERIES={
  WPUIP2311001:"Residential construction input goods",
  WPSID612:"Materials and components for construction"
};

function pct(a,b){
  if(!Number.isFinite(a)||!Number.isFinite(b)||b===0)return null;
  return ((a-b)/b)*100;
}

function parseSeries(series){
  const rows=(series?.data||[])
    .filter(r=>/^M(0[1-9]|1[0-2])$/.test(String(r.period||"")))
    .map(r=>({
      year:Number(r.year),
      month:Number(String(r.period).slice(1)),
      periodName:r.periodName||"",
      value:Number(String(r.value||"").replace(/,/g,""))
    }))
    .filter(r=>Number.isFinite(r.year)&&Number.isFinite(r.month)&&Number.isFinite(r.value))
    .sort((a,b)=>(b.year*100+b.month)-(a.year*100+a.month));

  const latest=rows[0];
  if(!latest)return null;
  const previous=rows[1]||null;
  const priorYear=rows.find(r=>r.year===latest.year-1&&r.month===latest.month)||null;

  return {
    seriesId:series.seriesID,
    title:SERIES[series.seriesID]||series.seriesID,
    value:latest.value,
    period:latest.periodName+" "+latest.year,
    monthOverMonthPct:previous?pct(latest.value,previous.value):null,
    yearOverYearPct:priorYear?pct(latest.value,priorYear.value):null
  };
}

async function getBlsMarketData(){
  const cache=globalThis.caches?.default;
  const cacheKey=new Request("https://homecostengine.com/__cache/bls-construction-market-v1");
  if(cache){
    const cached=await cache.match(cacheKey);
    if(cached){
      try{return await cached.json();}catch{}
    }
  }

  const now=new Date();
  const payload={
    seriesid:Object.keys(SERIES),
    startyear:String(now.getUTCFullYear()-1),
    endyear:String(now.getUTCFullYear())
  };

  const response=await fetch(BLS_URL,{
    method:"POST",
    headers:{"content-type":"application/json"},
    body:JSON.stringify(payload)
  });
  if(!response.ok)throw new Error("BLS request failed");

  const body=await response.json();
  if(body.status!=="REQUEST_SUCCEEDED")throw new Error("BLS data unavailable");

  const parsed=(body.Results?.series||[]).map(parseSeries).filter(Boolean);
  const data={
    status:"ok",
    fetchedAt:new Date().toISOString(),
    series:Object.fromEntries(parsed.map(item=>[item.seriesId,item])),
    source:{
      name:"U.S. Bureau of Labor Statistics",
      url:"https://www.bls.gov/developers/",
      frequency:"Monthly"
    }
  };

  if(cache){
    const cachedResponse=new Response(JSON.stringify(data),{
      headers:{"content-type":"application/json","cache-control":"public, max-age=43200"}
    });
    try{await cache.put(cacheKey,cachedResponse);}catch{}
  }
  return data;
}

async function lookupZip(zip){
  const response=await fetch("https://api.zippopotam.us/us/"+encodeURIComponent(zip),{
    headers:{"accept":"application/json"}
  });
  if(response.status===404)throw new Error("ZIP code not found");
  if(!response.ok)throw new Error("ZIP lookup failed");
  const body=await response.json();
  const place=body.places?.[0];
  if(!place)throw new Error("ZIP code not found");
  return {
    zip,
    city:place["place name"],
    state:place.state,
    stateCode:place["state abbreviation"],
    latitude:Number(place.latitude),
    longitude:Number(place.longitude)
  };
}

export async function onRequestGet({request}){
  const url=new URL(request.url);
  const zip=String(url.searchParams.get("zip")||"").trim();
  if(!ZIP_RE.test(zip))return json({error:"Enter a valid 5-digit U.S. ZIP code."},400,"no-store");

  let location;
  try{location=await lookupZip(zip);}
  catch(err){return json({error:err.message||"ZIP lookup failed."},404,"no-store");}

  let market;
  try{market=await getBlsMarketData();}
  catch{
    market={status:"unavailable",series:{},source:{name:"U.S. Bureau of Labor Statistics",url:"https://www.bls.gov/developers/",frequency:"Monthly"}};
  }

  return json({
    ok:true,
    location,
    market,
    methodology:{
      localAdjustment:"ZIP is used to identify city and state. The roof calculator then applies HomeCostEngine's existing state baseline.",
      marketTrend:"BLS construction indexes are national monthly trend indicators and are not local contractor quotes."
    }
  });
}

export async function onRequest(){return json({error:"Method not allowed."},405,"no-store");}
