/* Roof planning journey: estimates remain in this tab; analytics never includes inputs. */
(function () {
  'use strict';
  const params = new URLSearchParams(location.search);
  const qa = params.get('hce_qa') === '1';
  const path = location.pathname.replace(/\.html$/, '').replace(/\/$/, '');
  const roof = path === '/calculators/roof-replacement';
  const flow = roof || params.get('hce_flow') === 'roof';
  const key = 'hce_roof_benchmark_v1';
  function track(name) {
    if (qa) { console.info('[HCE roof QA]', name); return; }
    if (typeof window.gtag === 'function') window.gtag('event', name, {funnel_version:'roof_v2', page_path:path});
  }
  function benchmark() {
    try {
      const value = JSON.parse(sessionStorage.getItem(key));
      return value && Date.now() - value.time < 7200000 && value.time <= Date.now() && Number.isFinite(value.mid) && value.mid > 0 ? value : null;
    } catch (_) { return null; }
  }
  const dollars = n => new Intl.NumberFormat('en-US', {style:'currency', currency:'USD', maximumFractionDigits:0}).format(n);
  if (roof) {
    const form = document.getElementById('calculatorForm');
    const panel = document.getElementById('roof-scenarios');
    if (!form || !panel) return;
    const save = document.getElementById('roof-save-scenario');
    const compare = document.getElementById('roof-compare-scenario');
    const note = document.getElementById('roof-scenario-status');
    const currentLabel = document.getElementById('roof-current-summary');
    const next = document.getElementById('roof-next-step');
    const ids = ['area','roofState','material','pitch','stories','tearoff','market','deckArea','roofFeatures','roofPermit','roofContingency'];
    let current = null, saved = null, signature = '';
    const inputs = () => ids.map(id => document.getElementById(id).value).join('|');
    function capture() {
      const mid = Number(document.getElementById('result').textContent.replace(/[^\d.]/g, ''));
      if (!form.checkValidity() || !Number.isFinite(mid) || mid <= 0) return;
      current = {mid, range:document.getElementById('range').textContent, label:document.getElementById('material').selectedOptions[0].textContent + ', ' + Number(document.getElementById('area').value).toLocaleString('en-US') + ' sq ft', time:Date.now()};
      signature = inputs();
      currentLabel.textContent = current.label + ': ' + current.range + ' (midpoint ' + dollars(mid) + ').';
      save.disabled = false;
      compare.disabled = !saved;
      next.hidden = false;
      try { sessionStorage.setItem(key, JSON.stringify(current)); } catch (_) { /* Private modes can restrict storage. */ }
    }
    function stale() {
      if (signature && signature !== inputs()) {
        save.disabled = true; compare.disabled = true; next.hidden = true;
        currentLabel.textContent = 'Inputs changed. Calculate again to update this scenario.';
        note.textContent = saved ? 'Scenario A is saved. Calculate your new settings, then compare.' : '';
        try { sessionStorage.removeItem(key); } catch (_) {}
      }
    }
    form.addEventListener('input', stale);
    form.addEventListener('change', stale);
    form.addEventListener('submit', () => setTimeout(capture, 0));
    save.addEventListener('click', () => {
      if (!current || signature !== inputs()) return;
      saved = {...current}; compare.disabled = false;
      note.textContent = 'Scenario A saved: ' + saved.label + ', ' + saved.range + '. Change one assumption and calculate again.';
      track('roof_scenario_saved');
    });
    compare.addEventListener('click', () => {
      if (!current || !saved || signature !== inputs()) return;
      const diff = current.mid - saved.mid;
      note.textContent = 'Scenario A: ' + saved.label + ', ' + saved.range + '. Scenario B: ' + current.label + ', ' + current.range + '. Midpoint difference: ' + dollars(Math.abs(diff)) + (diff > 0 ? ' higher.' : diff < 0 ? ' lower.' : ' (unchanged).') + ' Compare full scope and material suitability with a qualified contractor.';
      track('roof_scenario_compared');
    });
    document.getElementById('roof-load-example').addEventListener('click', () => {
      const example = {area:'2000',roofState:'US',material:'asphalt',pitch:'1',stories:'1.05',tearoff:'1',market:'1',deckArea:'100',roofFeatures:'2',roofPermit:'350',roofContingency:'.10'};
      for (const [id,value] of Object.entries(example)) document.getElementById(id).value = value;
      document.getElementById('localZip').value = '';
      document.getElementById('localMetrics').hidden = true;
      document.getElementById('localZipStatus').textContent = 'Example uses the U.S. national baseline. Add your own location and measurements when ready.';
      form.requestSubmit(); track('roof_example_loaded');
    });
    document.getElementById('roof-quote-link').addEventListener('click', () => track('roof_quote_open'));
  }
  if (flow && path === '/calculators/contractor-quote-comparison') {
    const box = document.getElementById('roof-quote-context');
    box.hidden = false;
    const value = benchmark();
    document.getElementById('roof-benchmark').textContent = value ? 'Your last roof planning estimate: ' + value.range + ' (midpoint ' + dollars(value.mid) + '). This includes your selected contingency; bids may cover a different scope.' : 'Use matching roof measurements, materials, removal and repair scope for all three proposals.';
    document.getElementById('quote-compare-button').addEventListener('click', () => track('roof_quote_comparison'));
  }
  if (flow && path === '/free-home-project-cost-planning-guide') {
    document.getElementById('roof-guide-next').hidden = false;
    const status = document.getElementById('ebookStatus');
    let sent = false;
    if (status) new MutationObserver(() => {
      if (status.classList.contains('success') && !sent) { sent = true; track('workbook_request_success'); }
      if (!status.classList.contains('success')) sent = false;
    }).observe(status, {attributes:true,childList:true,subtree:true});
  }
  function connectLinks() {
    if (!flow) return;
    const targets = new Set(['/calculators/roof-replacement','/calculators/contractor-quote-comparison','/free-home-project-cost-planning-guide','/ebooks/roof-replacement-planning-handbook']);
    document.querySelectorAll('a[href]').forEach(a => {
      const url = new URL(a.href, location.origin);
      if (url.origin !== location.origin || !targets.has(url.pathname.replace(/\.html$/, ''))) return;
      url.searchParams.set('hce_flow', 'roof');
      if (qa) url.searchParams.set('hce_qa', '1');
      a.href = url.href;
    });
    if (roof) {
      const section = document.querySelector('.planning-value-section');
      if (section) section.before(document.getElementById('roof-scenarios'));
    }
  }
  connectLinks();
  document.addEventListener('DOMContentLoaded', connectLinks);
})();
