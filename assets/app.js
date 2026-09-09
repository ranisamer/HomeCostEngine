/*
  HomeCostEngine AdSense placements.
  Keep enabled=false until AdSense approval and ad-unit IDs are ready.
  Responsive units are used; desktop layout targets are:
  top 970x250, mid 336x280, bottom 728x90.
*/
const HCE_ADSENSE_CONFIG = {
  enabled: false,
  preview: true, // Shows gray "Advertisement" placeholders until real AdSense IDs are added.
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
  const canServe=HCE_ADSENSE_CONFIG.enabled && HCE_ADSENSE_CONFIG.client && slot;
  if(!canServe && !HCE_ADSENSE_CONFIG.preview) return null;

  const wrap=document.createElement("aside");
  wrap.className="hce-ad-slot hce-ad-"+position+(canServe?"":" hce-ad-preview");
  wrap.setAttribute("aria-label","Advertisement");
  wrap.innerHTML='<div class="hce-ad-label">Advertisement</div>';

  if(!canServe){
    const preview=document.createElement("div");
    preview.className="hce-ad-preview-box";
    preview.innerHTML='<strong>Google AdSense placement</strong><span>Preview only — real ad will appear here after AdSense is connected.</span>';
    wrap.appendChild(preview);
    return wrap;
  }

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

  // AD #1: immediately after the first editorial/hero image.
  const firstFigure=article.querySelector(":scope > .blog-figure");
  const firstP=Array.from(article.children).find(el=>el.tagName==="P");
  const top=buildAdSenseUnit("top",HCE_ADSENSE_CONFIG.slots.top);
  const topAnchor=firstFigure||firstP;
  if(topAnchor&&top) topAnchor.insertAdjacentElement("afterend",top);

  // AD #2: around the middle of the article, after the second H2 section paragraph.
  const h2s=Array.from(article.children).filter(el=>el.tagName==="H2");
  const secondH2=h2s[1]||h2s[0];
  let midAnchor=secondH2;
  if(secondH2){
    let cursor=secondH2.nextElementSibling;
    while(cursor && cursor.tagName!=="H2"){
      midAnchor=cursor;
      if(cursor.tagName==="P") break;
      cursor=cursor.nextElementSibling;
    }
  }
  const mid=buildAdSenseUnit("mid",HCE_ADSENSE_CONFIG.slots.mid);
  if(midAnchor&&mid) midAnchor.insertAdjacentElement("afterend",mid);

  // AD #3: directly before "Sources and further reading" when present.
  const sourcesHeading=h2s.find(el=>/sources|further reading/i.test(el.textContent||""));
  const bottom=buildAdSenseUnit("bottom",HCE_ADSENSE_CONFIG.slots.bottom);
  if(bottom){
    if(sourcesHeading) article.insertBefore(bottom,sourcesHeading);
    else {
      const notice=article.querySelector(":scope > .notice");
      if(notice) article.insertBefore(bottom,notice); else article.appendChild(bottom);
    }
  }
  return true;
}

function injectCalculatorAds(){
  const main=document.querySelector("main"); if(!main) return;
  const sections=Array.from(main.children).filter(el=>el.tagName==="SECTION");
  const calcSection=sections.find(section=>section.querySelector(".calc-shell"))||sections[1]||sections[0];
  const infoSection=sections.find(section=>section!==calcSection && section.querySelector(".info-copy"))||sections[sections.length-1];

  const firstBand=adBand("top",HCE_ADSENSE_CONFIG.slots.top);
  const secondBand=adBand("bottom",HCE_ADSENSE_CONFIG.slots.bottom);
  if(firstBand&&calcSection) calcSection.insertAdjacentElement("afterend",firstBand);
  if(secondBand&&infoSection) infoSection.insertAdjacentElement("afterend",secondBand);
}

function injectHomeAds(){
  const main=document.querySelector("main"); if(!main) return;
  const sections=Array.from(main.children).filter(el=>el.tagName==="SECTION");
  if(sections.length<2) return;
  const firstBand=adBand("top",HCE_ADSENSE_CONFIG.slots.top);
  const secondBand=adBand("bottom",HCE_ADSENSE_CONFIG.slots.bottom);
  const firstAnchor=sections[Math.min(1,sections.length-1)];
  const secondAnchor=sections[Math.max(2,Math.floor(sections.length*.65))]||sections[sections.length-1];
  if(firstBand) firstAnchor.insertAdjacentElement("afterend",firstBand);
  if(secondBand) secondAnchor.insertAdjacentElement("afterend",secondBand);
}

function injectSectionPageAds(){
  const main=document.querySelector("main"); if(!main) return;
  const sections=Array.from(main.children).filter(el=>el.tagName==="SECTION");
  if(!sections.length) return;
  const topBand=adBand("top",HCE_ADSENSE_CONFIG.slots.top);
  const bottomBand=adBand("bottom",HCE_ADSENSE_CONFIG.slots.bottom);
  if(topBand) sections[0].insertAdjacentElement("afterend",topBand);
  if(bottomBand) main.appendChild(bottomBand);
}


function injectBlogFallbackImage(){
  const path=location.pathname.replace(/\/+$/,"");
  if(!path.startsWith("/blog/") || path==="/blog" || path.endsWith("/index.html")) return;
  const article=document.querySelector("main article.info-copy");
  if(!article || article.querySelector(".blog-figure")) return;
  const h1=document.querySelector(".page-hero h1");
  const eyebrow=document.querySelector(".page-hero .eyebrow");
  const firstP=Array.from(article.children).find(el=>el.tagName==="P");
  if(!h1 || !firstP) return;
  const title=h1.textContent.trim();
  const category=(eyebrow?.textContent||"Home Improvement").trim().toUpperCase();
  const words=title.split(/\s+/);
  const lines=[]; let line="";
  words.forEach(word=>{
    if((line+" "+word).trim().length>28){ if(line) lines.push(line); line=word; }
    else line=(line+" "+word).trim();
  });
  if(line) lines.push(line);
  const safe=s=>s.replace(/[&<>"]/g,ch=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[ch]));
  const textLines=lines.slice(0,3).map((l,i)=>'<text x="70" y="'+(175+i*62)+'" font-size="44" font-weight="800" fill="#102033">'+safe(l)+'</text>').join("");
  const svg='<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="675" viewBox="0 0 1200 675"><rect width="1200" height="675" fill="#fbfaf7"/><rect x="45" y="50" width="1110" height="575" rx="34" fill="#f2f2ed"/><rect x="760" y="105" width="330" height="455" rx="30" fill="#d8efe9"/><text x="70" y="105" font-size="20" font-weight="700" fill="#176b5b">'+safe(category)+'</text>'+textLines+'<text x="70" y="535" font-size="26" fill="#405064">HomeCostEngine</text><path d="M825 405l100-120 100 120" fill="#f0b56a" stroke="#102033" stroke-width="7"/><rect x="855" y="405" width="140" height="100" fill="#fff" stroke="#102033" stroke-width="6"/><circle cx="925" cy="455" r="22" fill="#176b5b"/></svg>';
  const figure=document.createElement("figure");
  figure.className="blog-figure";
  const img=document.createElement("img");
  img.alt=title; img.loading="lazy";
  img.src="data:image/svg+xml;charset=UTF-8,"+encodeURIComponent(svg);
  const cap=document.createElement("figcaption");
  cap.textContent="HomeCostEngine planning illustration.";
  figure.append(img,cap);
  firstP.insertAdjacentElement("afterend",figure);
}

function injectSiteAds(){
  const canServe=HCE_ADSENSE_CONFIG.enabled && HCE_ADSENSE_CONFIG.client;
  if(!canServe && !HCE_ADSENSE_CONFIG.preview) return;

  const path=location.pathname.replace(/\/+$/,"")||"/";
  const excluded=["/privacy.html","/disclaimer.html","/contact.html","/404.html"];
  if(excluded.includes(path)) return;
  if(canServe) loadAdSenseScript(HCE_ADSENSE_CONFIG.client);

  const isBlogArticle=path.startsWith("/blog/") && path!=="/blog" && !path.endsWith("/index.html");
  if(isBlogArticle && injectBlogArticleAds()) return;

  if(path.startsWith("/calculators/") && path!=="/calculators" && !path.endsWith("/index.html")){
    injectCalculatorAds();
    return;
  }

  if(path==="/"){
    injectHomeAds();
    return;
  }

  injectSectionPageAds();
}

document.addEventListener("DOMContentLoaded", () => {
  injectSiteAds();
  injectBlogFallbackImage();
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