(()=>{
  const zipInput=document.getElementById("localZip");
  const button=document.getElementById("localZipButton");
  const status=document.getElementById("localZipStatus");
  const metrics=document.getElementById("localMetrics");
  if(!zipInput||!button||!status)return;

  const byId=id=>document.getElementById(id);
  const fmtPct=value=>{
    if(value===null||value===undefined||!Number.isFinite(Number(value)))return "—";
    const n=Number(value);
    return (n>0?"+":"")+n.toFixed(1)+"%";
  };

  function setBusy(isBusy){
    button.disabled=isBusy;
    button.textContent=isBusy?"Loading local data…":"Use ZIP data";
  }

  async function loadLocalData(){
    const zip=String(zipInput.value||"").trim();
    if(!/^\d{5}$/.test(zip)){
      status.className="local-zip-status error";
      status.textContent="Enter a valid 5-digit U.S. ZIP code.";
      if(metrics)metrics.hidden=true;
      return;
    }

    setBusy(true);
    status.className="local-zip-status";
    status.textContent="Loading ZIP location and latest construction-market data…";

    try{
      const response=await fetch("/api/local-cost?zip="+encodeURIComponent(zip),{headers:{"accept":"application/json"}});
      const data=await response.json().catch(()=>({}));
      if(!response.ok)throw new Error(data.error||"Could not load local data.");

      const loc=data.location||{};
      const stateSelect=byId("roofState");
      if(stateSelect&&loc.stateCode){
        stateSelect.value=loc.stateCode;
        stateSelect.dispatchEvent(new Event("change",{bubbles:true}));
      }

      const residential=data.market?.series?.WPUIP2311001;
      const construction=data.market?.series?.WPSID612;

      byId("localPlace").textContent=[loc.city,loc.state].filter(Boolean).join(", ")||zip;
      byId("localStateApplied").textContent=loc.stateCode?"State baseline applied: "+loc.stateCode:"State baseline applied";
      byId("localResidentialIndex").textContent=residential?residential.value.toFixed(1):"Unavailable";
      byId("localResidentialTrend").textContent=residential
        ? fmtPct(residential.yearOverYearPct)+" vs. year ago"
        : "BLS feed temporarily unavailable";
      byId("localConstructionIndex").textContent=construction?construction.value.toFixed(1):"Unavailable";
      byId("localConstructionTrend").textContent=construction
        ? fmtPct(construction.yearOverYearPct)+" vs. year ago"
        : "BLS feed temporarily unavailable";

      const periods=[residential?.period,construction?.period].filter(Boolean);
      byId("localDataDate").textContent=periods.length?"Latest available: "+periods[0]:"Latest BLS release unavailable";
      if(metrics)metrics.hidden=false;

      status.className="local-zip-status success";
      status.textContent="Location loaded. Your state baseline has been applied automatically.";
      window.HCE_LOCAL_COST_SNAPSHOT=data;
    }catch(err){
      status.className="local-zip-status error";
      status.textContent=err.message||"Could not load local data.";
      if(metrics)metrics.hidden=true;
    }finally{
      setBusy(false);
    }
  }

  button.addEventListener("click",loadLocalData);
  zipInput.addEventListener("keydown",event=>{
    if(event.key==="Enter"){
      event.preventDefault();
      loadLocalData();
    }
  });

  const preset=new URLSearchParams(location.search).get("zip");
  if(/^\d{5}$/.test(String(preset||""))){
    zipInput.value=preset;
    loadLocalData();
  }
})();
