/*
  HomeCostEngine AdSense placements.
  Keep enabled=false until AdSense approval and ad-unit IDs are ready.
  Responsive units are used; desktop layout targets are:
  top 970x250, mid 336x280, bottom 728x90.
*/
const HCE_ADSENSE_CONFIG = {
  enabled: false,
  client: "",
  slots: { top: "", mid: "", bottom: "" }
};

function loadAdSenseScript(client){
  if(!client || document.querySelector('script[data-hce-adsense]')) return;
  const script=document.createElement("script");
  script.async=true; script.crossOrigin="anonymous"; script.dataset.hceAdsense="true";
  script.src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client="+encodeURIComponent(client);
  document.head.appendChild(script);
}

function buildAdSenseUnit(position, slot){
  if(!HCE_ADSENSE_CONFIG.enabled || !HCE_ADSENSE_CONFIG.client || !slot) return null;
  const wrap=document.createElement("aside");
  wrap.className="hce-ad-slot hce-ad-"+position;
  wrap.setAttribute("aria-label","Advertisement");
  wrap.innerHTML='<div class="hce-ad-label">Advertisement</div>';
  const ins=document.createElement("ins");
  ins.className="adsbygoogle"; ins.style.display="block";
  ins.dataset.adClient=HCE_ADSENSE_CONFIG.client; ins.dataset.adSlot=slot;
  ins.dataset.adFormat="auto"; ins.dataset.fullWidthResponsive="true";
  wrap.appendChild(ins);
  requestAnimationFrame(()=>{try{(window.adsbygoogle=window.adsbygoogle||[]).push({});}catch(e){console.warn("AdSense slot could not initialize.",e);}});
  return wrap;
}

function adBand(position,slot){
  const ad=buildAdSenseUnit(position,slot); if(!ad) return null;
  const section=document.createElement("section"); section.className="hce-ad-band";
  const container=document.createElement("div"); container.className="container";
  container.appendChild(ad); section.appendChild(container); return section;
}

function injectBlogArticleAds(){
  const article=document.querySelector("main article.info-copy"); if(!article) return false;
  const firstP=Array.from(article.children).find(el=>el.tagName==="P");
  const top=buildAdSenseUnit("top",HCE_ADSENSE_CONFIG.slots.top);
  if(firstP&&top) firstP.insertAdjacentElement("afterend",top);
  const h2s=Array.from(article.children).filter(el=>el.tagName==="H2");
  const anchor=h2s[1]?.nextElementSibling||h2s[1]||h2s[0]?.nextElementSibling;
  const mid=buildAdSenseUnit("mid",HCE_ADSENSE_CONFIG.slots.mid);
  if(anchor&&mid) anchor.insertAdjacentElement("afterend",mid);
  const notice=article.querySelector(":scope > .notice");
  const bottom=buildAdSenseUnit("bottom",HCE_ADSENSE_CONFIG.slots.bottom);
  if(bottom){ if(notice) article.insertBefore(bottom,notice); else article.appendChild(bottom); }
  return true;
}

function injectSectionPageAds(){
  const main=document.querySelector("main"); if(!main) return;
  const sections=Array.from(main.children).filter(el=>el.tagName==="SECTION");
  if(!sections.length) return;
  const topBand=adBand("top",HCE_ADSENSE_CONFIG.slots.top);
  const midBand=adBand("mid",HCE_ADSENSE_CONFIG.slots.mid);
  const bottomBand=adBand("bottom",HCE_ADSENSE_CONFIG.slots.bottom);
  if(topBand) sections[0].insertAdjacentElement("afterend",topBand);
  if(midBand){
    const midIndex=Math.max(1,Math.floor(sections.length/2));
    (sections[midIndex]||sections[sections.length-1]).insertAdjacentElement("afterend",midBand);
  }
  if(bottomBand) main.appendChild(bottomBand);
}

function injectSiteAds(){
  if(!HCE_ADSENSE_CONFIG.enabled || !HCE_ADSENSE_CONFIG.client) return;
  const path=location.pathname.replace(/\/+$/,"")||"/";
  const excluded=["/privacy.html","/disclaimer.html","/contact.html","/404.html"];
  if(excluded.includes(path)) return;
  loadAdSenseScript(HCE_ADSENSE_CONFIG.client);
  const isBlogArticle=path.startsWith("/blog/") && path!=="/blog" && !path.endsWith("/index.html");
  if(isBlogArticle && injectBlogArticleAds()) return;
  injectSectionPageAds();
}

document.addEventListener("DOMContentLoaded", () => {
  injectSiteAds();
  const menuBtn = document.querySelector(".menu-btn");
  const mobile = document.querySelector(".mobile-menu");
  if(menuBtn && mobile){
    menuBtn.addEventListener("click", () => mobile.classList.toggle("open"));
  }

  const quick = document.getElementById("quickProjectForm");
  if(quick){
    quick.addEventListener("submit", (e) => {
      e.preventDefault();
      const project = document.getElementById("quickProject").value;
      const routes = {
        roofing:"/calculators/roof-replacement.html",
        concrete:"/calculators/concrete.html",
        hvac:"/calculators/hvac.html",
        painting:"/calculators/paint.html",
        flooring:"/calculators/flooring.html",
        landscaping:"/calculators/mulch.html"
      };
      location.href = routes[project] || "/calculators/";
    });
  }

  const quoteForm = document.getElementById("quoteCheck");
  if(quoteForm){
    quoteForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const quote = Number(document.getElementById("quoteAmount").value || 0);
      const typical = Number(document.getElementById("typicalAmount").value || 0);
      const out = document.getElementById("quoteMessage");
      if(!quote || !typical){ out.textContent = "Enter both amounts to compare."; return; }
      const diff = ((quote - typical)/typical)*100;
      if(Math.abs(diff) < 8) out.textContent = "This quote is close to your planning estimate.";
      else if(diff > 0) out.textContent = `This quote is about ${Math.abs(diff).toFixed(0)}% above your planning estimate.`;
      else out.textContent = `This quote is about ${Math.abs(diff).toFixed(0)}% below your planning estimate.`;
    });
  }
});