document.addEventListener("DOMContentLoaded", () => {
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