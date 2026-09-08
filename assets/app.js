/*
  HomeCostEngine AdSense manual placements.
  Keep enabled=false until the site is approved in AdSense.
  Then add your publisher client and the three ad-unit slot IDs.
*/
const HCE_ADSENSE_CONFIG = {
  enabled: false,
  client: "",
  slots: {
    articleAfterIntro: "",
    articleMidContent: "",
    articleBeforeRelated: ""
  }
};

function loadAdSenseScript(client){
  if(!client || document.querySelector('script[data-hce-adsense]')) return;
  const script = document.createElement("script");
  script.async = true;
  script.crossOrigin = "anonymous";
  script.dataset.hceAdsense = "true";
  script.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + encodeURIComponent(client);
  document.head.appendChild(script);
}

function buildAdSenseUnit(placement, slot){
  if(!HCE_ADSENSE_CONFIG.enabled || !HCE_ADSENSE_CONFIG.client || !slot) return null;

  const wrap = document.createElement("aside");
  wrap.className = "hce-ad-slot";
  wrap.dataset.adPlacement = placement;
  wrap.setAttribute("aria-label", "Advertisement");

  const label = document.createElement("div");
  label.className = "hce-ad-label";
  label.textContent = "Advertisement";

  const ins = document.createElement("ins");
  ins.className = "adsbygoogle";
  ins.style.display = "block";
  ins.dataset.adClient = HCE_ADSENSE_CONFIG.client;
  ins.dataset.adSlot = slot;
  ins.dataset.adFormat = "auto";
  ins.dataset.fullWidthResponsive = "true";

  wrap.append(label, ins);

  requestAnimationFrame(() => {
    try{
      (window.adsbygoogle = window.adsbygoogle || []).push({});
    }catch(e){
      console.warn("AdSense slot could not initialize.", e);
    }
  });

  return wrap;
}

function injectArticleAds(){
  const path = location.pathname.replace(/\/+$/, "");
  if(!path.startsWith("/blog/") || path === "/blog" || path.endsWith("/index.html")) return;

  const article = document.querySelector("main article.info-copy");
  if(!article) return;

  const config = HCE_ADSENSE_CONFIG;
  if(!config.enabled || !config.client) return;

  loadAdSenseScript(config.client);

  // Placement 1: after the opening paragraph, visible once the reader has started the article.
  const firstParagraph = Array.from(article.children).find(el => el.tagName === "P");
  const topAd = buildAdSenseUnit("article-after-intro", config.slots.articleAfterIntro);
  if(firstParagraph && topAd) firstParagraph.insertAdjacentElement("afterend", topAd);

  // Placement 2: in the middle of the article, after the second content section.
  const h2s = Array.from(article.children).filter(el => el.tagName === "H2");
  const midAnchor = h2s[1]?.nextElementSibling || h2s[1] || h2s[0]?.nextElementSibling;
  const midAd = buildAdSenseUnit("article-mid-content", config.slots.articleMidContent);
  if(midAnchor && midAd) midAnchor.insertAdjacentElement("afterend", midAd);

  // Placement 3: after the article body, before the planning CTA / related content.
  const notice = article.querySelector(":scope > .notice");
  const endAd = buildAdSenseUnit("article-before-related", config.slots.articleBeforeRelated);
  if(endAd){
    if(notice) article.insertBefore(endAd, notice);
    else article.appendChild(endAd);
  }
}

document.addEventListener("DOMContentLoaded", () => {
  injectArticleAds();
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