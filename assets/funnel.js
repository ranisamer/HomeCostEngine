/* Useful-action measurement through the existing GA4 tag. No input values or emails. */
(function () {
  'use strict';
  const qa = new URLSearchParams(location.search).get('hce_qa') === '1';
  const path = location.pathname.replace(/\.html$/, '');
  const concretePaths = new Set(['/blog/how-much-extra-concrete-should-i-order', '/calculators/concrete', '/ebooks/concrete-project-cost-handbook']);
  const sharedWorkbook = path === '/free-home-project-cost-planning-guide';
  const concreteFlow = concretePaths.has(path) || (sharedWorkbook && new URLSearchParams(location.search).get('hce_flow') === 'concrete');
  const trackedBooks = new Set(['roof-replacement-planning-handbook', 'concrete-project-cost-handbook']);
  const allowed = new Set(['roof_calculation', 'concrete_calculation', 'concrete_tool_open', 'concrete_book_open', 'workbook_open', 'workbook_download_click', 'roof_book_open', 'checkout_attempt', 'checkout_error']);
  function send(name) {
    if (!allowed.has(name)) return;
    // QA stays local and does not emit analytics, including synthetic interactions.
    if (qa) { console.info('[HCE funnel QA]', name); return; }
    if (typeof window.gtag !== 'function') return;
    window.gtag('event', name, {funnel_version:concreteFlow ? 'concrete_v1' : 'roof_v1', page_path:path});
  }
  document.addEventListener('click', function (event) {
    if (!event.isTrusted && !qa) return;
    const link = event.target.closest('a[href]');
    if (link) {
      let url;
      try { url = new URL(link.href, location.origin); } catch (_) { return; }
      if (url.origin !== location.origin) return;
      const target = url.pathname.replace(/\.html$/, '');
      if (target === '/free-home-project-cost-planning-guide') send('workbook_open');
      if (target === '/assets/guides/home-project-cost-planning-guide.pdf') send('workbook_download_click');
      if (target === '/ebooks/roof-replacement-planning-handbook') send('roof_book_open');
      if (target === '/calculators/concrete') send('concrete_tool_open');
      if (target === '/ebooks/concrete-project-cost-handbook') send('concrete_book_open');
      if (concreteFlow && (target === '/free-home-project-cost-planning-guide' || target === '/assets/guides/home-project-cost-planning-guide.pdf' || concretePaths.has(target))) {
        url.searchParams.set('hce_flow', 'concrete'); link.href = url.href;
      }
      // Retain QA exclusion along this internal test journey only.
      if (qa) { url.searchParams.set('hce_qa', '1'); link.href = url.href; }
    }
    const buy = event.target.closest('button[data-book]');
    if (buy && trackedBooks.has(buy.dataset.book)) send('checkout_attempt');
  });
  let calculated = false;
  document.addEventListener('submit', function (event) {
    if (event.target.id !== 'calculatorForm' || !['roof', 'concrete'].includes(document.body.dataset.calculator)) return;
    if ((!event.isTrusted && !qa) || !event.target.checkValidity()) return;
    // Calculator's own submit listener runs first; count one successful user action/page.
    queueMicrotask(function () {
      const result = document.getElementById('result');
      if (calculated || !result || !/\d/.test(result.textContent) || /NaN|Infinity/.test(result.textContent)) return;
      calculated = true;
      send(document.body.dataset.calculator === 'concrete' ? 'concrete_calculation' : 'roof_calculation');
    });
  });
  const status = document.querySelector('.book-checkout-status');
  if (status && (path === '/ebooks/roof-replacement-planning-handbook' || path === '/ebooks/concrete-project-cost-handbook')) {
    new MutationObserver(function () {
      if (status.classList.contains('error') && status.textContent.trim()) send('checkout_error');
    }).observe(status, {childList:true, subtree:true, attributes:true, attributeFilter:['class']});
  }
})();
