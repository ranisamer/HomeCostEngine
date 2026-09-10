/* HomeCostEngine global UI, blog enhancements and AdSense */
const HCE_ADSENSE_CONFIG = {
  enabled: true,
  preview: false,
  client: "ca-pub-2351413014734308",
  slots: { top: "", mid: "", bottom: "" }
};

const HCE_BLOG_TOPICS = {
  roofing: {
    image: "https://cdn.pixabay.com/photo/2016/03/27/19/40/shingles-1283921_1280.jpg",
    imageSource: "https://pixabay.com/photos/shingles-roof-house-construction-1283921/",
    imageCredit: "Roofing photo on Pixabay",
    internal: [
      ["Roof Replacement Cost Calculator", "/calculators/roof-replacement.html"],
      ["Roofing Square Calculator", "/calculators/roofing-square.html"],
      ["Roof Pitch Calculator", "/calculators/roof-pitch.html"],
      ["Roof Replacement Cost Guide", "/guides/roof-replacement-cost.html"]
    ],
    external: [
      ["NRCA Consumer Roofing Information", "https://www.nrca.net/roofing-guidelines/consumer-information"],
      ["NRCA Roofing Resources", "https://www.nrca.net/roofing-guidelines/resources"],
      ["FEMA Home Repair and Recovery Resources", "https://www.fema.gov/emergency-managers/risk-management/building-science/homeowners"],
      ["ENERGY STAR Roof Products", "https://www.energystar.gov/products/roof_products"],
      ["OSHA Roofing Safety", "https://www.osha.gov/roofing"]
    ]
  },
  concrete: {
    image: "https://cdn.pixabay.com/photo/2014/07/31/21/20/cement-406822_1280.jpg",
    imageSource: "https://pixabay.com/photos/cement-concrete-construction-worker-406822/",
    imageCredit: "Concrete photo on Pixabay",
    internal: [
      ["Concrete Calculator", "/calculators/concrete.html"],
      ["Cubic Yard Calculator", "/calculators/cubic-yard.html"],
      ["How Many Cubic Yards Do I Need?", "/blog/how-many-cubic-yards-do-i-need.html"]
    ],
    external: [
      ["American Concrete Institute", "https://www.concrete.org/"],
      ["National Ready Mixed Concrete Association", "https://www.nrmca.org/"],
      ["Portland Cement Association", "https://www.cement.org/"],
      ["FHWA Concrete Resources", "https://www.fhwa.dot.gov/pavement/concrete/"],
      ["OSHA Concrete and Masonry Construction", "https://www.osha.gov/concrete-masonry"]
    ]
  },
  hvac: {
    image: "https://cdn.pixabay.com/photo/2021/09/08/07/20/air-conditioner-6605973_1280.jpg",
    imageSource: "https://pixabay.com/photos/air-conditioner-air-conditioning-unit-6605973/",
    imageCredit: "HVAC photo on Pixabay",
    internal: [
      ["HVAC Replacement Cost Calculator", "/calculators/hvac.html"],
      ["HVAC Repair vs Replacement", "/blog/hvac-repair-vs-replacement.html"],
      ["Heat Pump vs Central Air Cost", "/blog/heat-pump-vs-central-air-cost.html"]
    ],
    external: [
      ["ENERGY STAR: Heat & Cool Efficiently", "https://www.energystar.gov/saveathome/heating-cooling"],
      ["U.S. Department of Energy: Home Upgrades", "https://www.energy.gov/save/home-upgrades"],
      ["EPA Refrigerant Management", "https://www.epa.gov/section608"],
      ["AHRI Certified Product Directory", "https://www.ahridirectory.org/"],
      ["ASHRAE Homeowner Resources", "https://www.ashrae.org/technical-resources/free-resources"]
    ]
  },
  painting: {
    image: "https://cdn.pixabay.com/photo/2017/04/21/01/43/painter-2247395_1280.jpg",
    imageSource: "https://pixabay.com/photos/painter-paint-house-indoor-2247395/",
    imageCredit: "Interior painting photo on Pixabay",
    internal: [
      ["Paint Calculator", "/calculators/paint.html"],
      ["Interior Painting Cost Per Square Foot", "/blog/interior-painting-cost-per-square-foot.html"],
      ["How Much Does It Cost to Paint a Room?", "/blog/how-much-does-it-cost-to-paint-a-room.html"]
    ],
    external: [
      ["EPA Lead-Safe Renovation, Repair and Painting", "https://www.epa.gov/lead/steps-lead-safe-renovation-repair-and-painting"],
      ["EPA Renovation, Repair and Painting Program", "https://www.epa.gov/lead/lead-renovation-repair-and-painting-program"],
      ["EPA Indoor Air Quality", "https://www.epa.gov/indoor-air-quality-iaq"],
      ["CPSC Lead in Paint Guidance", "https://www.cpsc.gov/Safety-Education/Safety-Education-Centers/Lead"],
      ["OSHA Painting and Coating Safety", "https://www.osha.gov/etools/shipyard/general-requirements/painting"]
    ]
  },
  flooring: {
    image: "https://cdn.pixabay.com/photo/2017/02/23/02/41/wood-2091171_1280.jpg",
    imageSource: "https://pixabay.com/photos/wood-floor-wood-floor-wood-flooring-2091171/",
    imageCredit: "Flooring photo on Pixabay",
    internal: [
      ["Flooring Cost Calculator", "/calculators/flooring.html"],
      ["How Much Flooring Do I Need?", "/blog/how-much-flooring-do-i-need.html"],
      ["Vinyl Plank vs Laminate Flooring Cost", "/blog/vinyl-plank-vs-laminate-flooring-cost.html"]
    ],
    external: [
      ["National Wood Flooring Association", "https://nwfa.org/"],
      ["EPA Indoor Air Quality", "https://www.epa.gov/indoor-air-quality-iaq"],
      ["NWFA Homeowner Resources", "https://www.woodfloors.org/"],
      ["Resilient Floor Covering Institute", "https://rfci.com/"],
      ["Carpet and Rug Institute", "https://carpet-rug.org/"]
    ]
  },
  gravel: {
    image: "https://cdn.pixabay.com/photo/2020/06/10/23/27/country-side-5284614_1280.jpg",
    imageSource: "https://pixabay.com/photos/country-side-gravel-road-nature-5284614/",
    imageCredit: "Gravel road photo on Pixabay",
    internal: [
      ["Gravel Calculator", "/calculators/gravel.html"],
      ["Cubic Yard Calculator", "/calculators/cubic-yard.html"],
      ["Gravel Driveway Cost", "/blog/gravel-driveway-cost.html"]
    ],
    external: [
      ["EPA WaterSense Landscaping Tips", "https://www.epa.gov/watersense/landscaping-tips"],
      ["EPA WaterSense Outdoors", "https://www.epa.gov/watersense/outdoors"],
      ["FHWA Gravel Roads Guide", "https://www.fhwa.dot.gov/construction/pubs/ots15002.pdf"],
      ["USGS Aggregates Information", "https://www.usgs.gov/centers/national-minerals-information-center/aggregates-data"],
      ["USDA Web Soil Survey", "https://websoilsurvey.nrcs.usda.gov/"]
    ]
  },
  mulch: {
    image: "https://cdn.pixabay.com/photo/2021/06/02/14/47/mulch-6304664_1280.jpg",
    imageSource: "https://pixabay.com/photos/mulch-wood-gardening-wood-chips-6304664/",
    imageCredit: "Mulch photo on Pixabay",
    internal: [
      ["Mulch Calculator", "/calculators/mulch.html"],
      ["Cubic Yard Calculator", "/calculators/cubic-yard.html"],
      ["Mulch Cost Per Yard", "/blog/mulch-cost-per-yard.html"]
    ],
    external: [
      ["EPA WaterSense Landscaping Tips", "https://www.epa.gov/watersense/landscaping-tips"],
      ["EPA WaterSense Outdoors", "https://www.epa.gov/watersense/outdoors"],
      ["USDA Natural Resources Conservation Service", "https://www.nrcs.usda.gov/"],
      ["USDA Web Soil Survey", "https://websoilsurvey.nrcs.usda.gov/"],
      ["U.S. Forest Service Gardening Resources", "https://www.fs.usda.gov/wildflowers/Native_Plant_Materials/Native_Gardening/index.shtml"]
    ]
  },
  windows: {
    image: "https://cdn.pixabay.com/photo/2016/07/10/15/58/house-1507920_1280.jpg",
    imageSource: "https://pixabay.com/photos/house-window-home-house-window-1507920/",
    imageCredit: "Home window photo on Pixabay",
    internal: [
      ["All Home Improvement Projects", "/projects.html"],
      ["Window Replacement Cost Per Window", "/blog/window-replacement-cost-per-window.html"],
      ["Double-Pane vs Triple-Pane Windows", "/blog/double-pane-vs-triple-pane-windows.html"]
    ],
    external: [
      ["ENERGY STAR Residential Windows, Doors & Skylights", "https://www.energystar.gov/products/res_windows_doors_skylights"],
      ["U.S. Department of Energy: Home Upgrades", "https://www.energy.gov/save/home-upgrades"],
      ["National Fenestration Rating Council", "https://nfrc.org/"],
      ["DOE Energy-Efficient Windows", "https://www.energy.gov/energysaver/energy-efficient-windows"],
      ["Efficient Windows Collaborative", "https://efficientwindows.org/"]
    ]
  },
  plumbing: {
    image: "https://cdn.pixabay.com/photo/2016/11/11/12/18/boiler-1816642_1280.jpg",
    imageSource: "https://pixabay.com/photos/water-heater-boiler-maintenance-1816642/",
    imageCredit: "Water-heater photo on Pixabay",
    internal: [
      ["All Home Improvement Projects", "/projects.html"],
      ["Water Heater Repair vs Replacement", "/blog/water-heater-repair-vs-replacement.html"],
      ["How to Detect a Hidden Water Leak", "/blog/how-to-detect-hidden-water-leak.html"]
    ],
    external: [
      ["U.S. Department of Energy: Water Heating", "https://www.energy.gov/topics/water-heating"],
      ["EPA WaterSense", "https://www.epa.gov/watersense"],
      ["EPA Fix a Leak Week", "https://www.epa.gov/watersense/fix-leak-week"],
      ["CDC Drinking Water Resources", "https://www.cdc.gov/drinking-water/"],
      ["International Plumbing Code Resources", "https://www.iccsafe.org/products-and-services/i-codes/2024-i-codes/ipc/"]
    ]
  },
  general: {
    image: "https://cdn.pixabay.com/photo/2016/07/10/15/58/house-1507920_1280.jpg",
    imageSource: "https://pixabay.com/photos/house-window-home-house-window-1507920/",
    imageCredit: "Home improvement photo on Pixabay",
    internal: [
      ["Square Footage Calculator", "/calculators/square-footage.html"],
      ["Cubic Yard Calculator", "/calculators/cubic-yard.html"],
      ["All HomeCostEngine Calculators", "/calculators/"]
    ],
    external: [
      ["NIST Office of Weights and Measures", "https://www.nist.gov/pml/owm"],
      ["U.S. Department of Energy: Home Upgrades", "https://www.energy.gov/save/home-upgrades"],
      ["FTC Home Improvement Guidance", "https://consumer.ftc.gov/articles/home-improvement-scams"],
      ["HUD Healthy Homes", "https://www.hud.gov/hud-partners/healthy-homes"],
      ["EPA Indoor Air Quality", "https://www.epa.gov/indoor-air-quality-iaq"]
    ]
  }
};

function blogTopicForPath(path=""){
  const s=String(path).toLowerCase();
  if(/water-heater|toilet|water-leak|plumb/.test(s)) return "plumbing";
  if(/window/.test(s)) return "windows";
  if(/hvac|heat-pump|seer|air-condition|ac-repair|furnace/.test(s)) return "hvac";
  if(/paint/.test(s)) return "painting";
  if(/floor|vinyl|laminate/.test(s)) return "flooring";
  if(/gravel/.test(s)) return "gravel";
  if(/mulch|landscap/.test(s)) return "mulch";
  if(/concrete|cubic-yard|slab|patio|ready-mix/.test(s)) return "concrete";
  if(/roof|shingle|attic-ventilation/.test(s)) return "roofing";
  return "general";
}

function ensureBlogEnhancementStyles(){
  if(document.getElementById("hce-blog-enhancement-styles")) return;
  const style=document.createElement("style");
  style.id="hce-blog-enhancement-styles";
  style.textContent=`
    .article-cover.hce-photo-cover{position:relative;overflow:hidden;padding:0;height:180px;background:#dfe5e1;display:block}
    .article-cover.hce-photo-cover img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block;transition:transform .25s ease}
    .article:hover .article-cover.hce-photo-cover img{transform:scale(1.03)}
    .article-cover.hce-photo-cover .blog-card-label{position:absolute;left:0;right:0;bottom:0;z-index:2;padding:36px 18px 14px;color:#fff;background:linear-gradient(180deg,transparent,rgba(8,25,40,.84));font-size:.76rem;font-weight:850;letter-spacing:.05em;text-transform:uppercase;text-shadow:0 1px 2px rgba(0,0,0,.35)}
    .blog-figure.hce-external-photo img{width:100%;aspect-ratio:16/9;object-fit:cover;background:#eef1ef}
    .blog-figure.hce-external-photo figcaption a{color:var(--accent);text-decoration:underline;text-underline-offset:2px}
    .seo-link-panel{margin:36px 0 22px;padding:22px;border:1px solid var(--line);border-radius:18px;background:#f5faf8}
    .seo-link-panel>h2{font-size:1.55rem!important;margin:0 0 9px!important}
    .seo-link-panel>p{margin:0 0 18px!important}
    .seo-link-grid{display:grid;grid-template-columns:1fr 1fr;gap:20px}
    .seo-link-panel h3{font-size:1rem!important;margin:0 0 8px!important;letter-spacing:-.02em}
    .seo-link-panel ul{margin:0;padding-left:20px}
    .seo-link-panel li{margin:7px 0;color:var(--ink-2)}
    .seo-link-panel a{color:var(--accent);text-decoration:underline;text-underline-offset:2px;font-weight:700}
    @media(max-width:650px){.seo-link-grid{grid-template-columns:1fr}.article-cover.hce-photo-cover{height:190px}}
  `;
  document.head.appendChild(style);
}

function makeExternalPhoto(topic, title){
  const figure=document.createElement("figure");
  figure.className="blog-figure hce-external-photo";
  const img=document.createElement("img");
  img.src=topic.image;
  img.alt=title ? `${title} — project photo` : "Home improvement project photo";
  img.loading="lazy";
  img.decoding="async";
  img.referrerPolicy="no-referrer";
  img.addEventListener("error",()=>{img.style.display="none";figure.classList.add("image-failed")},{once:true});
  const cap=document.createElement("figcaption");
  cap.append("Illustrative photo: ");
  const a=document.createElement("a");
  a.href=topic.imageSource;
  a.target="_blank";
  a.rel="noopener noreferrer";
  a.textContent=topic.imageCredit;
  cap.appendChild(a);
  figure.append(img,cap);
  return figure;
}

function enhanceBlogCards(){
  const cards=document.querySelectorAll('.article[href^="/blog/"]');
  cards.forEach(card=>{
    const cover=card.querySelector(".article-cover");
    if(!cover || cover.classList.contains("hce-photo-cover")) return;
    const topic=HCE_BLOG_TOPICS[blogTopicForPath(card.getAttribute("href"))]||HCE_BLOG_TOPICS.general;
    const label=(cover.textContent||"Home improvement guide").trim();
    const title=(card.querySelector("h3")?.textContent||label).trim();
    cover.textContent="";
    cover.classList.add("hce-photo-cover");
    const img=document.createElement("img");
    img.src=topic.image;
    img.alt=title;
    img.loading="lazy";
    img.decoding="async";
    img.referrerPolicy="no-referrer";
    const span=document.createElement("span");
    span.className="blog-card-label";
    span.textContent=label;
    img.addEventListener("error",()=>{img.remove();cover.classList.add("image-failed")},{once:true});
    cover.append(img,span);
  });
}

function buildSeoLinkPanel(topic){
  const panel=document.createElement("aside");
  panel.className="seo-link-panel";
  panel.setAttribute("aria-label","Related tools and trusted resources");
  const current=location.pathname.replace(/\/+$/,"");
  const internal=topic.internal.filter(([,href])=>href.replace(/\/+$/,"")!==current).slice(0,3);
  const internalHtml=internal.map(([label,href])=>`<li><a href="${href}">${label}</a></li>`).join("");
  const externalHtml=topic.external.slice(0,5).map(([label,href])=>`<li><a href="${href}" target="_blank" rel="noopener noreferrer">${label} ↗</a></li>`).join("");
  panel.innerHTML=`<h2>Related tools & trusted resources</h2><p>Continue planning with HomeCostEngine tools and verify important project details with independent industry or government resources.</p><div class="seo-link-grid"><div><h3>On HomeCostEngine</h3><ul>${internalHtml}</ul></div><div><h3>Independent external resources</h3><ul>${externalHtml}</ul></div></div>`;
  return panel;
}

function enhanceBlogArticle(){
  const article=document.querySelector("main article.info-copy");
  if(!article) return;
  const topic=HCE_BLOG_TOPICS[blogTopicForPath(location.pathname)]||HCE_BLOG_TOPICS.general;
  const title=(document.querySelector(".page-hero h1")?.textContent||document.title||"Home improvement guide").trim();
  let figure=article.querySelector(":scope > .blog-figure");
  const shouldReplace=figure && (()=>{
    const src=figure.querySelector("img")?.getAttribute("src")||"";
    return !src || src.startsWith("data:") || src.endsWith(".svg") || src.includes("/assets/blog/");
  })();
  if(shouldReplace){
    figure.replaceWith(makeExternalPhoto(topic,title));
  } else if(!figure){
    const firstP=Array.from(article.children).find(el=>el.tagName==="P");
    if(firstP) firstP.insertAdjacentElement("afterend",makeExternalPhoto(topic,title));
  }
  if(!article.querySelector(".seo-link-panel")){
    const panel=buildSeoLinkPanel(topic);
    const h2s=Array.from(article.children).filter(el=>el.tagName==="H2");
    const sourcesHeading=h2s.find(el=>/sources|further reading|references/i.test(el.textContent||""));
    const notice=article.querySelector(":scope > .notice");
    if(sourcesHeading) article.insertBefore(panel,sourcesHeading);
    else if(notice) article.insertBefore(panel,notice);
    else article.appendChild(panel);
  }
}

function enhanceBlog(){
  const path=location.pathname.replace(/\/+$/,"")||"/";
  if(path!=="/blog" && !path.startsWith("/blog/")) return;
  ensureBlogEnhancementStyles();
  enhanceBlogCards();
  if(path!=="/blog" && !path.endsWith("/index.html")) enhanceBlogArticle();
}

function loadAdSenseScript(client){
  if(!client || document.querySelector('script[src*="pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"]')) return;
  const script=document.createElement("script");
  script.async=true;
  script.crossOrigin="anonymous";
  script.dataset.hceAdsense="true";
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
  ins.className="adsbygoogle";
  ins.style.display="block";
  ins.dataset.adClient=HCE_ADSENSE_CONFIG.client;
  ins.dataset.adSlot=slot;
  ins.dataset.adFormat="auto";
  ins.dataset.fullWidthResponsive="true";
  wrap.appendChild(ins);
  requestAnimationFrame(()=>{try{(window.adsbygoogle=window.adsbygoogle||[]).push({});}catch(e){console.warn("AdSense slot could not initialize.",e);}});
  return wrap;
}

function adBand(position,slot){
  const ad=buildAdSenseUnit(position,slot);
  if(!ad) return null;
  const section=document.createElement("section");
  section.className="hce-ad-band";
  const container=document.createElement("div");
  container.className="container";
  container.appendChild(ad);
  section.appendChild(container);
  return section;
}

function injectBlogArticleAds(){
  const article=document.querySelector("main article.info-copy");
  if(!article) return false;
  const firstFigure=article.querySelector(":scope > .blog-figure");
  const firstP=Array.from(article.children).find(el=>el.tagName==="P");
  const top=buildAdSenseUnit("top",HCE_ADSENSE_CONFIG.slots.top);
  const topAnchor=firstFigure||firstP;
  if(topAnchor&&top) topAnchor.insertAdjacentElement("afterend",top);
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

document.addEventListener("DOMContentLoaded",()=>{
  enhanceBlog();
  injectSiteAds();

  const menuBtn=document.querySelector(".menu-btn");
  const mobile=document.querySelector(".mobile-menu");
  if(menuBtn&&mobile){
    menuBtn.addEventListener("click",()=>mobile.classList.toggle("open"));
  }

  const quick=document.getElementById("quickProjectForm");
  if(quick){
    quick.addEventListener("submit",e=>{
      e.preventDefault();
      const project=document.getElementById("quickProject").value;
      const routes={
        roofing:"/calculators/roof-replacement.html",
        concrete:"/calculators/concrete.html",
        hvac:"/calculators/hvac.html",
        painting:"/calculators/paint.html",
        flooring:"/calculators/flooring.html",
        landscaping:"/calculators/mulch.html"
      };
      location.href=routes[project]||"/calculators/";
    });
  }

  const quoteForm=document.getElementById("quoteCheck");
  if(quoteForm){
    quoteForm.addEventListener("submit",e=>{
      e.preventDefault();
      const quote=Number(document.getElementById("quoteAmount").value||0);
      const typical=Number(document.getElementById("typicalAmount").value||0);
      const out=document.getElementById("quoteMessage");
      if(!quote||!typical){out.textContent="Enter both amounts to compare.";return;}
      const diff=((quote-typical)/typical)*100;
      if(Math.abs(diff)<8) out.textContent="This quote is close to your planning estimate.";
      else if(diff>0) out.textContent=`This quote is about ${Math.abs(diff).toFixed(0)}% above your planning estimate.`;
      else out.textContent=`This quote is about ${Math.abs(diff).toFixed(0)}% below your planning estimate.`;
    });
  }
});
