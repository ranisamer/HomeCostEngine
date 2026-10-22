(function (root, factory) {
  'use strict';
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  if (root && root.document) {
    root.HCEConcrete = api;
    if (root.document.readyState === 'loading') root.document.addEventListener('DOMContentLoaded', api.init);
    else api.init();
  }
})(typeof window !== 'undefined' ? window : null, function () {
  'use strict';
  const STORAGE_KEY = 'hce_concrete_plan_v2';
  const ceil = n => Math.ceil(n - 8 * Number.EPSILON * Math.max(1, Math.abs(n)));
  function number(value, name, min, max) {
    if (typeof value !== 'number' || !Number.isFinite(value) || value < min || value > max) throw new RangeError(name);
    return value;
  }
  function calculate(plan) {
    if (!Array.isArray(plan.zones) || plan.zones.length < 1 || plan.zones.length > 8) throw new RangeError('Use between one and eight rectangular sections.');
    const sections = plan.zones.map((zone, i) => {
      const length = number(zone.length, 'Enter a positive length for every section.', 0.01, 10000);
      const width = number(zone.width, 'Enter a positive width for every section.', 0.01, 10000);
      const thickness = number(zone.thickness, 'Enter a positive concrete thickness for every section.', 0.01, 240);
      return { label: 'Section ' + (i + 1), length, width, thickness, area: length * width, cubicFeet: length * width * thickness / 12 };
    });
    const slabFeet = sections.reduce((sum, section) => sum + section.cubicFeet, 0);
    let edgeFeet = 0;
    if (plan.edge.enabled) {
      const first = sections[0];
      const width = number(plan.edge.width, 'Enter the inside perimeter edge width in inches.', 0.01, 12000) / 12;
      const depth = number(plan.edge.depth, 'Total edge depth must be at least the first slab thickness.', first.thickness, 240);
      if (2 * width >= Math.min(first.length, first.width)) throw new RangeError('The edge width must be less than half the first section’s shorter side.');
      // The inner rectangle removes the corner overlap. Only depth below the slab is added.
      const ringArea = first.area - (first.length - 2 * width) * (first.width - 2 * width);
      edgeFeet = ringArea * (depth - first.thickness) / 12;
    }
    const allowance = number(plan.allowance, 'Choose an allowance from 0% to 30%.', 0, 30);
    const increment = number(plan.increment, 'Choose a supplier increment from 0 to 10 cubic yards.', 0, 10);
    const yieldFeet = number(plan.bagYield, 'Enter a positive product yield in cubic feet per bag.', 0.001, 10);
    const yardPrice = plan.yardPrice === null ? null : number(plan.yardPrice, 'Enter a nonnegative quoted price per cubic yard.', 0, 100000);
    const delivery = number(plan.delivery, 'Delivery and short-load charges cannot be negative.', 0, 1000000);
    const placement = number(plan.placement, 'Placement charges cannot be negative.', 0, 1000000);
    const netFeet = slabFeet + edgeFeet;
    const scenario = pct => {
      const allowanceFeet = netFeet * pct / 100;
      const planningFeet = netFeet + allowanceFeet;
      const planningYards = planningFeet / 27;
      const orderYards = increment ? ceil(planningYards / increment) * increment : planningYards;
      return { allowance: pct, allowanceFeet, planningFeet, planningYards, orderYards, roundingYards: Math.max(0, orderYards - planningYards), bags: ceil(planningFeet / yieldFeet), materialCost: yardPrice === null ? null : orderYards * yardPrice, deliveredCost: yardPrice === null ? null : orderYards * yardPrice + delivery + placement };
    };
    return { sections, slabFeet, edgeFeet, netFeet, netYards: netFeet / 27, area: sections.reduce((sum, s) => sum + s.area, 0), ...scenario(allowance), scenarios: [...new Set([5, 10, 15, allowance])].sort((a, b) => a - b).map(scenario) };
  }
  function init() {
    const form = document.getElementById('calculatorForm');
    if (!form || document.body.dataset.planner !== 'concrete-v2' || form.dataset.ready) return;
    form.dataset.ready = 'true';
    const byId = id => document.getElementById(id);
    const text = (id, value) => { const el = byId(id); if (el) el.textContent = value; };
    const fmt = n => new Intl.NumberFormat('en-US', { maximumFractionDigits: 3 }).format(n);
    const dollars = n => new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 2 }).format(n);
    const readNumber = id => Number(byId(id).value);
    const actions = Array.from(document.querySelectorAll('[data-concrete-action]'));
    let last = null;
    let lastInputKey = null;
    const inputKey = () => JSON.stringify(Array.from(form.querySelectorAll('input')).map(input => [input.id, input.type === 'checkbox' ? input.checked : input.value, input.disabled, input.validity.valid]));
    function read() {
      return { version: 2, zones: Array.from(form.querySelectorAll('[data-concrete-zone]')).map(zone => ({ length: Number(zone.querySelector('[data-dimension="length"]').value), width: Number(zone.querySelector('[data-dimension="width"]').value), thickness: Number(zone.querySelector('[data-dimension="thickness"]').value) })), edge: { enabled: byId('edgeEnabled').checked, width: readNumber('edgeWidth'), depth: readNumber('edgeDepth') }, allowance: readNumber('waste'), increment: readNumber('orderIncrement'), bagYield: readNumber('bagYield'), yardPrice: byId('yardPrice').value.trim() === '' ? null : readNumber('yardPrice'), delivery: readNumber('deliveryFee'), placement: readNumber('placementFee') };
    }
    function edgeState() {
      const enabled = byId('edgeEnabled').checked;
      byId('edgeFields').hidden = !enabled;
      byId('edgeWidth').disabled = !enabled;
      byId('edgeDepth').disabled = !enabled;
    }
    function dirty() {
      const key = inputKey();
      if (key === lastInputKey) return;
      lastInputKey = key;
      last = null;
      actions.forEach(button => button.disabled = true);
      text('result', 'Update your plan');
      text('range', 'Inputs changed. Calculate again before using or saving the result.');
      text('concreteStatus', 'Inputs changed. Recalculate to refresh the breakdown.');
      byId('concreteDetail').hidden = true;
      document.querySelector('.concrete-detail-grid').hidden = true;
      byId('concreteExport').value = '';
      document.querySelector('.concrete-summary-details').dataset.printSummary = '';
      byId('calculatorError').textContent = '';
    }
    function addZone(values) {
      const zones = form.querySelectorAll('[data-concrete-zone]');
      if (zones.length >= 8) return;
      const zone = document.createElement('fieldset');
      zone.className = 'concrete-zone';
      zone.dataset.concreteZone = '';
      const n = zones.length + 1;
      zone.innerHTML = '<legend>Section ' + n + '</legend><div class="concrete-zone-grid">' + [['length', 'Length (ft)', 10000], ['width', 'Width (ft)', 10000], ['thickness', 'Thickness (in)', 240]].map(([key, label, max]) => '<div class="field"><label for="section-' + n + '-' + key + '">' + label + '</label><input id="section-' + n + '-' + key + '" data-dimension="' + key + '" type="number" min="0.01" max="' + max + '" step="any" required value="' + (key === 'thickness' ? 4 : 10) + '"></div>').join('') + '</div><button class="concrete-text-button" type="button" data-remove-zone>Remove this section</button>';
      if (values) for (const key of ['length', 'width', 'thickness']) zone.querySelector('[data-dimension="' + key + '"]').value = values[key];
      byId('concreteZones').appendChild(zone);
      byId('addConcreteZone').disabled = form.querySelectorAll('[data-concrete-zone]').length >= 8;
      return zone;
    }
    function refreshZoneNames() {
      form.querySelectorAll('[data-concrete-zone]').forEach((zone, index) => {
        zone.querySelector('legend').textContent = 'Section ' + (index + 1) + (index === 0 ? ' · main slab' : '');
        zone.querySelectorAll('[data-dimension]').forEach(input => {
          const id = 'section-' + (index + 1) + '-' + input.dataset.dimension;
          zone.querySelector('label[for="' + input.id + '"]')?.setAttribute('for', id);
          input.id = id;
        });
      });
      byId('addConcreteZone').disabled = form.querySelectorAll('[data-concrete-zone]').length >= 8;
    }
    function summary(plan, result) {
      const lines = ['HOME COST ENGINE — CONCRETE PLANNING WORKSHEET', new Date().toLocaleDateString('en-US'), 'https://homecostengine.com/calculators/concrete', '', 'DIMENSIONS (NON-OVERLAPPING RECTANGLES)'];
      result.sections.forEach(s => lines.push(s.label + ': ' + s.length + ' ft × ' + s.width + ' ft × ' + s.thickness + ' in = ' + fmt(s.cubicFeet / 27) + ' yd³'));
      if (plan.edge.enabled) lines.push('First section perimeter edge: ' + plan.edge.width + ' in wide, ' + plan.edge.depth + ' in TOTAL depth; added volume below slab = ' + fmt(result.edgeFeet / 27) + ' yd³');
      lines.push('', 'QUANTITY', 'Net measured volume: ' + fmt(result.netYards) + ' yd³', 'Chosen allowance: ' + plan.allowance + '% = ' + fmt(result.allowanceFeet / 27) + ' yd³', 'Quantity before supplier rounding: ' + fmt(result.planningYards) + ' yd³', 'Supplier increment entered: ' + plan.increment + ' yd³ (0 means no rounding)', 'Ready-mix quantity after rounding: ' + fmt(result.orderYards) + ' yd³', 'Alternative bag quantity: ' + result.bags + ' bags at ' + plan.bagYield + ' ft³/bag, based on unrounded quantity including allowance.', '', 'QUOTED COST INPUTS', plan.yardPrice === null ? 'No concrete rate entered; cost is incomplete.' : 'Material: ' + fmt(result.orderYards) + ' yd³ × ' + dollars(plan.yardPrice) + ' = ' + dollars(result.materialCost), 'Delivery / short-load charges: ' + dollars(plan.delivery), 'Pump / placement charges: ' + dollars(plan.placement));
      if (result.deliveredCost !== null) lines.push('Entered material + fees subtotal: ' + dollars(result.deliveredCost));
      lines.push('', 'CONFIRM WITH YOUR SUPPLIER', '[ ] Final form dimensions, thickness and edge design', '[ ] Product / mix specification, reinforcement and local requirements', '[ ] Minimum order, increment, truck access and delivery timing', '[ ] Waiting time, washout, returns, tax and all quoted fees', '', 'Excluded: excavation, aggregate base, forms, reinforcement, finishing labor, permits and tax unless explicitly included in your entered fees. This is a quantity and quote worksheet, not an engineering design or an order placed with a supplier.');
      return lines.join('\n');
    }
    function render() {
      if (!form.checkValidity()) { dirty(); form.reportValidity(); return false; }
      let plan, result;
      try { plan = read(); result = calculate(plan); }
      catch (error) { dirty(); text('calculatorError', error.message); byId('calculatorError').focus(); return false; }
      last = { plan, result };
      lastInputKey = inputKey();
      actions.forEach(button => button.disabled = false);
      byId('concreteDetail').hidden = false;
      document.querySelector('.concrete-detail-grid').hidden = false;
      text('result', fmt(result.orderYards) + ' yd³');
      text('range', plan.increment ? 'Ready-mix quantity after rounding to your entered increment' : 'Planning quantity; no supplier rounding applied');
      text('netVolume', fmt(result.netYards) + ' yd³');
      text('slabVolume', fmt(result.slabFeet / 27) + ' yd³');
      text('edgeVolume', fmt(result.edgeFeet / 27) + ' yd³');
      text('allowanceVolume', fmt(result.allowanceFeet / 27) + ' yd³ (' + plan.allowance + '%)');
      text('beforeRounding', fmt(result.planningYards) + ' yd³');
      text('roundingVolume', fmt(result.roundingYards) + ' yd³');
      text('metricVolume', fmt(result.orderYards * 0.764554857984) + ' m³');
      text('bagCount', result.bags.toLocaleString('en-US') + ' bags');
      text('bagNote', 'At ' + plan.bagYield + ' ft³ per bag; uses quantity with allowance, before ready-mix rounding.');
      text('materialCost', result.materialCost === null ? 'Add your quoted rate' : dollars(result.materialCost));
      text('quotedFees', dollars(plan.delivery + plan.placement));
      text('deliveredCost', result.deliveredCost === null ? 'Incomplete — no material rate' : dollars(result.deliveredCost));
      const sectionBody = byId('sectionBreakdown'); sectionBody.textContent = '';
      result.sections.forEach(s => {
        const row = document.createElement('tr');
        for (const value of [s.label, s.length + ' × ' + s.width + ' ft · ' + s.thickness + ' in', fmt(s.cubicFeet / 27) + ' yd³']) { const cell = document.createElement('td'); cell.textContent = value; row.appendChild(cell); }
        sectionBody.appendChild(row);
      });
      const scenarios = byId('concreteScenarios'); scenarios.textContent = '';
      result.scenarios.forEach(s => {
        const row = document.createElement('tr'); if (s.allowance === plan.allowance) row.className = 'is-selected';
        for (const value of [s.allowance + '%' + (s.allowance === plan.allowance ? ' · selected' : ''), fmt(s.planningYards) + ' yd³', fmt(s.orderYards) + ' yd³', s.deliveredCost === null ? 'Rate not entered' : dollars(s.deliveredCost)]) { const cell = document.createElement('td'); cell.textContent = value; row.appendChild(cell); }
        scenarios.appendChild(row);
      });
      byId('concreteExport').value = summary(plan, result);
      document.querySelector('.concrete-summary-details').dataset.printSummary = byId('concreteExport').value;
      text('calculatorError', '');
      text('concreteStatus', 'Plan calculated. Review the measured volume, chosen allowance and supplier rounding separately.');
      return true;
    }
    function applySaved(plan) {
      calculate(plan); // Validate stored data before touching the form.
      form.querySelectorAll('[data-concrete-zone]').forEach((zone, i) => { if (i) zone.remove(); });
      const first = form.querySelector('[data-concrete-zone]');
      for (const key of ['length', 'width', 'thickness']) first.querySelector('[data-dimension="' + key + '"]').value = plan.zones[0][key];
      plan.zones.slice(1).forEach(addZone);
      byId('edgeEnabled').checked = plan.edge.enabled;
      for (const [id, value] of Object.entries({ edgeWidth: plan.edge.width, edgeDepth: plan.edge.depth, waste: plan.allowance, orderIncrement: plan.increment, bagYield: plan.bagYield, yardPrice: plan.yardPrice === null ? '' : plan.yardPrice, deliveryFee: plan.delivery, placementFee: plan.placement })) byId(id).value = value;
      edgeState(); refreshZoneNames(); render();
    }
    form.addEventListener('submit', event => { event.preventDefault(); render(); });
    form.addEventListener('input', dirty);
    form.addEventListener('change', () => { edgeState(); dirty(); });
    form.addEventListener('click', event => { const button = event.target.closest('[data-remove-zone]'); if (button) { button.closest('[data-concrete-zone]').remove(); refreshZoneNames(); dirty(); } });
    byId('addConcreteZone').addEventListener('click', () => { const zone = addZone(); dirty(); zone?.querySelector('input').focus(); });
    byId('saveConcretePlan').addEventListener('click', () => {
      if (!last) return;
      try { localStorage.setItem(STORAGE_KEY, JSON.stringify(last.plan)); byId('restoreConcretePlan').disabled = false; byId('clearConcretePlan').disabled = false; text('concreteStatus', 'Saved on this browser only. Use Restore saved plan on your next visit.'); }
      catch (_) { text('concreteStatus', 'This browser could not save the plan. Download the worksheet instead.'); }
    });
    byId('restoreConcretePlan').addEventListener('click', () => {
      try { const plan = JSON.parse(localStorage.getItem(STORAGE_KEY)); if (!plan || plan.version !== 2) throw new Error('Invalid plan'); applySaved(plan); text('concreteStatus', 'Your saved plan was restored. Recheck supplier prices and measurements.'); }
      catch (_) { text('concreteStatus', 'No valid saved plan is available. Your current inputs have not been replaced.'); }
    });
    byId('clearConcretePlan').addEventListener('click', () => {
      try { localStorage.removeItem(STORAGE_KEY); byId('restoreConcretePlan').disabled = true; byId('clearConcretePlan').disabled = true; text('concreteStatus', 'Saved plan removed from this browser.'); }
      catch (_) { text('concreteStatus', 'This browser could not remove the saved plan.'); }
    });
    byId('downloadConcretePlan').addEventListener('click', () => {
      if (!last) return;
      const url = URL.createObjectURL(new Blob([byId('concreteExport').value], { type: 'text/plain;charset=utf-8' }));
      const a = document.createElement('a'); a.href = url; a.download = 'homecostengine-concrete-plan.txt'; document.body.appendChild(a); a.click();
      // Keep the blob alive while the browser hands the download to its file service.
      setTimeout(() => { a.remove(); URL.revokeObjectURL(url); }, 30000);
      text('concreteStatus', 'Worksheet download requested. Keep it with your supplier quote.');
    });
    byId('printConcretePlan').addEventListener('click', () => {
      if (!last) return;
      const details = document.querySelector('.concrete-summary-details');
      const wasOpen = details.open; details.open = true;
      window.addEventListener('afterprint', () => { details.open = wasOpen; }, { once: true });
      window.print();
    });
    byId('copyConcretePlan').addEventListener('click', async () => {
      if (!last) return;
      try { await navigator.clipboard.writeText(byId('concreteExport').value); text('concreteStatus', 'Worksheet copied. Paste it into your own project notes.'); }
      catch (_) { byId('concreteExport').focus(); byId('concreteExport').select(); text('concreteStatus', 'Select and copy the worksheet text below.'); }
    });
    try { const saved = JSON.parse(localStorage.getItem(STORAGE_KEY)); if (saved && saved.version === 2) { calculate(saved); byId('restoreConcretePlan').disabled = false; byId('clearConcretePlan').disabled = false; } } catch (_) {}
    edgeState();
    byId('concreteNoScript').hidden = true;
    render(); // Default examples are never sent as conversion events.
  }
  return { calculate, init };
});
