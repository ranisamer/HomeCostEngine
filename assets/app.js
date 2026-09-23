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
      ["Roof Replacement Cost Calculator", "/calculators/roof-replacement"],
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
      ["Heat Pump vs Central Air Cost", "/blog/heat-pump-vs-central-air-cost"]
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
      ["Gravel Calculator", "/calculators/gravel"],
      ["Cubic Yard Calculator", "/calculators/cubic-yard.html"],
      ["Gravel Driveway Cost", "/blog/gravel-driveway-cost"]
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
  const calcSection=sections.find(section=>section.querySelector(".calc-shell, .hce-tool"))||sections[1]||sections[0];
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
        roofing:"/calculators/roof-replacement",
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


const HCE_BOOK_CATEGORIES=[
  ["Renovation & Remodeling","/ebooks/#renovation-remodeling","Whole-home, additions, kitchens, baths and basements."],
  ["Roofing","/ebooks/#roofing","Roof replacement planning, quantities and contractor scope."],
  ["HVAC & Home Energy","/ebooks/#hvac-home-energy","Heating, cooling, efficiency and energy upgrades."],
  ["Concrete & Outdoor","/ebooks/#concrete-outdoor-projects","Concrete, decks and landscaping projects."],
  ["Flooring & Painting","/ebooks/#flooring-painting","Interior finish quantities, labor and planning."],
  ["Home Maintenance","/ebooks/#home-maintenance","Maintenance schedules, reserves and first-time ownership."],
  ["Windows & Doors","/ebooks/#windows-doors","Replacement costs, ratings and installation scope."],
  ["Plumbing","/ebooks/#plumbing","Repair scope, water systems and quote planning."],
  ["Electrical","/ebooks/#electrical","Panel replacement, circuits, permits and upgrades."],
  ["Contractors & Quotes","/ebooks/#contractors-quotes","Compare proposals, allowances, exclusions and warranties."]
];

function ensureBooksNav(){
  document.querySelectorAll(".navlinks").forEach(nav=>{
    if(nav.querySelector(".books-nav-dropdown")) return;
    let books=nav.querySelector('a[href="/ebooks/"]');
    if(!books){
      const about=nav.querySelector('a[href="/about.html"]');
      books=document.createElement("a");
      books.href="/ebooks/";
      books.textContent="Books";
      if(about) nav.insertBefore(books,about); else nav.appendChild(books);
    }
    const details=document.createElement("details");
    details.className="nav-dropdown books-nav-dropdown";
    details.innerHTML='<summary>Books</summary><div class="nav-dropdown-menu books-dropdown-menu">'+
      HCE_BOOK_CATEGORIES.map(([label,href,desc])=>'<a href="'+href+'"><b>'+label+'</b><span>'+desc+'</span></a>').join("")+
      '<a class="nav-dropdown-all" href="/ebooks/"><b>View all books →</b></a></div>';
    books.replaceWith(details);
  });

  document.querySelectorAll(".mobile-menu").forEach(nav=>{
    if(!nav.querySelector('a[href="/ebooks/"]')){
      const about=nav.querySelector('a[href="/about.html"]');
      const a=document.createElement("a"); a.href="/ebooks/"; a.textContent="Books";
      if(about) nav.insertBefore(a,about); else nav.appendChild(a);
    }
    if(!nav.querySelector(".mobile-book-categories")){
      const wrap=document.createElement("div");
      wrap.className="mobile-book-categories";
      wrap.innerHTML=HCE_BOOK_CATEGORIES.map(([label,href])=>'<a href="'+href+'">'+label+'</a>').join("");
      const books=nav.querySelector('a[href="/ebooks/"]');
      books.insertAdjacentElement("afterend",wrap);
    }
  });
}
if(document.readyState==="loading") document.addEventListener("DOMContentLoaded",ensureBooksNav);
else ensureBooksNav();


function hceBookPageCount(){
  const text=(document.body?.innerText||"");
  const m=text.match(/\b(\d{2,3})[- ]page\b/i)||text.match(/\b(\d{2,3}) pages\b/i);
  return m?m[1]:"";
}
function hceBookPrice(){
  return (document.querySelector(".book-price")?.textContent||document.querySelector(".ebook-card h2")?.textContent||"").trim();
}
function hceFirstModules(){
  return Array.from(document.querySelectorAll(".ebook-chapter-list li")).slice(0,3).map(li=>li.textContent.replace(/^\s*\d+\.\s*/,"").trim());
}
function makeBookFeatureIcon(symbol,label,value){
  const item=document.createElement("div");
  item.className="ebook-feature-icon";
  item.innerHTML='<span class="ebook-feature-symbol" aria-hidden="true">'+symbol+'</span><span><b>'+label+'</b><small>'+value+'</small></span>';
  return item;
}
function enhanceEbookDetail(){
  const path=location.pathname;
  if(!path.startsWith("/ebooks/") || path==="/ebooks/" || path.endsWith("/ebooks/index.html")) return;
  const h1=document.querySelector("main h1");
  if(!h1 || document.querySelector(".ebook-product-enhanced")) return;
  document.body.classList.add("ebook-product-enhanced");
  const pageCount=hceBookPageCount();
  const price=hceBookPrice();
  const mobileCover=document.querySelector(".mobile-book-cover");
  const desktopCover=document.querySelector(".desktop-book-cover,.ebook-cover-link");
  const coverAnchor=mobileCover||desktopCover;
  const heroLead=h1.parentElement?.querySelector(".lead");
  const topList=h1.parentElement?.querySelector(".ebook-checks");
  const firstSection=document.querySelector(".book-expanded-content") || document.querySelector("main .section.alt .info-copy");

  // Rating / trust strip: stars are deliberately unrated until verified reader reviews exist.
  if(coverAnchor && !coverAnchor.nextElementSibling?.classList?.contains("ebook-rating-strip")){
    const rating=document.createElement("div");
    rating.className="ebook-rating-strip";
    rating.innerHTML='<span class="ebook-stars" aria-label="No verified rating yet">☆☆☆☆☆</span><strong>New release</strong><span>Verified reader reviews open</span>';
    coverAnchor.insertAdjacentElement("afterend",rating);
  }

  // Product feature icons under the intro/cover.
  const iconRow=document.createElement("div");
  iconRow.className="ebook-feature-row";
  iconRow.append(
    makeBookFeatureIcon("▤","Pages",pageCount?pageCount+" pages":"Digital guide"),
    makeBookFeatureIcon("⇩","Format","PDF instant download"),
    makeBookFeatureIcon("▦","Extras","Printable worksheets")
  );
  if(mobileCover){
    const rating=mobileCover.nextElementSibling;
    (rating?.classList.contains("ebook-rating-strip")?rating:mobileCover).insertAdjacentElement("afterend",iconRow);
  }else if(heroLead){
    heroLead.insertAdjacentElement("afterend",iconRow);
  }

  // Add a secondary preview CTA in the purchase card.
  const buyBtn=document.querySelector(".book-buy-button,.buy-book");
  if(buyBtn && !document.querySelector(".ebook-preview-jump")){
    const previewBtn=document.createElement("a");
    previewBtn.href="#sample-pages";
    previewBtn.className="btn secondary full ebook-preview-jump";
    previewBtn.textContent="View 3 Sample Pages";
    buyBtn.insertAdjacentElement("afterend",previewBtn);
  }

  // Sales copy block similar to the cleaner mobile product layout.
  if(firstSection && !document.querySelector(".ebook-about-panel")){
    const about=document.createElement("section");
    about.className="section ebook-about-panel";
    const listItems=topList?Array.from(topList.querySelectorAll("li")).slice(0,6).map(li=>'<li>'+li.textContent.trim()+'</li>').join(""):"";
    about.innerHTML='<div class="container ebook-about-grid"><div><span class="eyebrow">About this book</span><h2>'+h1.textContent.trim()+'</h2><p class="lead">'+(heroLead?.textContent.trim()||"A practical HomeCostEngine field guide for smarter project planning.")+'</p></div><div class="ebook-whats-inside"><h3>What’s inside</h3><ul class="ebook-value-list">'+(listItems||'<li>Project planning guidance</li><li>Printable worksheets</li><li>Contractor quote checks</li><li>Internal calculator links</li>')+'</ul></div></div>';
    const heroSection=h1.closest("section");
    heroSection?.insertAdjacentElement("afterend",about);
  }

  // A safe 3-page preview built from the book's real first planning modules, without exposing the paid PDF.
  if(!document.getElementById("sample-pages")){
    const modules=hceFirstModules();
    const first=modules[0]||"Project scope and existing conditions";
    const second=modules[1]||"Measurements, materials and allowances";
    const third=modules[2]||"Contractor quote and decision check";
    const preview=document.createElement("section");
    preview.id="sample-pages";
    preview.className="section alt ebook-sample-section";
    preview.innerHTML='<div class="container"><div class="section-head"><div><span class="eyebrow">Free preview</span><h2>Read 3 sample planning pages.</h2></div><p>These previews reflect the early planning pages and worksheet style used in the full guide. The complete PDF stays protected behind checkout.</p></div><div class="ebook-sample-grid">'+
      '<article class="ebook-sample-page"><span>Sample page 1</span><h3>'+first+'</h3><p>Start by separating verified facts from assumptions. Record the existing condition, the result you want, and anything that still needs field confirmation before you compare prices.</p><ul><li>Define included and excluded scope</li><li>Record measurements and product requirements</li><li>Flag permit, access and restoration questions</li></ul></article>'+
      '<article class="ebook-sample-page"><span>Sample page 2</span><h3>'+second+'</h3><p>Use the worksheet to turn a general idea into written scope. Keep owner selections, contractor responsibilities and allowances visible instead of burying them in one total.</p><div class="sample-lines"><i></i><i></i><i></i><i></i><i></i></div></article>'+
      '<article class="ebook-sample-page"><span>Sample page 3</span><h3>'+third+'</h3><p>Normalize proposals before comparing the bottom line. Check quantities, exclusions, warranty, cleanup, permits and the conditions that could trigger a change order.</p><div class="sample-checks"><b>✓ Same scope?</b><b>✓ Allowances clear?</b><b>✓ Warranty stated?</b><b>✓ Change-order rules?</b></div></article>'+
    '</div><div class="ebook-preview-cta"><span>'+ (price?price+" • ":"") +'Instant PDF after secure checkout</span><a class="btn" href="#'+(buyBtn?.id||"top")+'" onclick="window.scrollTo({top:0,behavior:\'smooth\'});return false;">Get the full guide →</a></div></div>';
    const questions=Array.from(document.querySelectorAll("main section")).find(s=>/Questions & updates/i.test(s.textContent||""));
    if(questions) questions.insertAdjacentElement("beforebegin",preview); else document.querySelector("main")?.appendChild(preview);
  }

  // Honest review block: no fabricated review count or score.
  if(!document.querySelector(".ebook-review-section")){
    const review=document.createElement("section");
    review.className="section ebook-review-section";
    review.innerHTML='<div class="container ebook-review-card"><div><span class="eyebrow">Reader reviews</span><h2>Verified reviews will appear here.</h2><div class="ebook-stars ebook-stars-large">☆☆☆☆☆</div><p>We do not publish invented ratings. Once verified purchasers send feedback, their reviews can be displayed here.</p></div><a class="btn secondary" href="mailto:reports@homecostengine.com?subject='+encodeURIComponent("HomeCostEngine book review: "+h1.textContent.trim())+'">Share your review →</a></div>';
    const main=document.querySelector("main");
    main?.appendChild(review);
  }
}
function enhanceEbookLibrary(){
  const path=location.pathname.replace(/\/+$/,"");
  if(path!=="/ebooks" && !path.endsWith("/ebooks/index.html")) return;
  document.body.classList.add("ebook-library-enhanced");
  document.querySelectorAll(".book-card").forEach(card=>{
    if(card.querySelector(".book-card-rating")) return;
    const h2=card.querySelector("h2");
    const pageTxt=card.querySelector(".book-card-actions span")?.textContent.trim()||"Digital PDF";
    const rating=document.createElement("div");
    rating.className="book-card-rating";
    rating.innerHTML='<span aria-hidden="true">☆☆☆☆☆</span><small>New release</small>';
    h2?.insertAdjacentElement("afterend",rating);
    const features=document.createElement("div");
    features.className="book-card-mini-features";
    features.innerHTML='<span>▤ '+pageTxt+'</span><span>⇩ Instant PDF</span>';
    rating.insertAdjacentElement("afterend",features);
  });
}
function enhanceEbookStorefront(){
  enhanceEbookLibrary();
  enhanceEbookDetail();
}
if(document.readyState==="loading") document.addEventListener("DOMContentLoaded",enhanceEbookStorefront);
else enhanceEbookStorefront();


/* Load the reusable interactive ebook preview system. */
(function(){
  if(!location.pathname.startsWith("/ebooks")) return;
  const css=document.createElement("link"); css.rel="stylesheet"; css.href="/assets/ebook-preview.css?v=20260923-1"; document.head.appendChild(css);
  const js=document.createElement("script"); js.src="/assets/ebook-preview.js?v=20260923-1"; js.defer=true; document.head.appendChild(js);
})();
