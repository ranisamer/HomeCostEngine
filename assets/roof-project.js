/* One roof project, explicitly saved in this browser. No project data is sent. */
(function (root) {
  'use strict';
  const KEY = 'hce_roof_project_v1';
  const roofIds = ['area','roofState','material','pitch','stories','tearoff','market','deckArea','roofFeatures','roofPermit','roofContingency'];
  const text = (v, max) => typeof v === 'string' ? v.slice(0, max) : '';
  function amount(v, optional) {
    if (optional && (v === '' || v === null || v === undefined)) return null;
    if (typeof v !== 'number' && typeof v !== 'string') throw Error('Enter a valid dollar amount.');
    if (String(v).trim() === '') throw Error('Complete the dollar amount, or enter 0 when it is truly zero.');
    const n = Number(v);
    if (!Number.isFinite(n) || n < 0 || n > 100000000) throw Error('Use non-negative dollar amounts up to $100 million.');
    // Dollar entries have at most two decimal places.
    if (Math.abs(n * 100 - Math.round(n * 100)) > 0.00001) throw Error('Use no more than two decimal places for dollar amounts.');
    return Math.round(n * 100) / 100;
  }
  function normalize(raw) {
    if (!raw || raw.version !== 1 || typeof raw !== 'object') throw Error('This is not a supported HomeCostEngine roof project backup.');
    const name = text(raw.name, 80).trim();
    if (!name) throw Error('Give your project a name.');
    if (!Array.isArray(raw.quotes) || raw.quotes.length !== 3) throw Error('The project must contain three quote slots.');
    const quotes = raw.quotes.map((q, i) => {
      if (q === null) return null;
      if (!q || typeof q !== 'object') throw Error('Check quote ' + (i + 1) + '.');
      const price = amount(q.price), extras = amount(q.extras);
      return {name:text(q.name, 80).trim() || 'Quote ' + (i + 1), price, extras, unresolved:q.unresolved === true, notes:text(q.notes, 1000)};
    });
    const selected = String(raw.selected ?? '');
    if (selected !== '' && !['0','1','2'].includes(selected)) throw Error('Select an available quote.');
    if (selected !== '' && !quotes[Number(selected)]) throw Error('Enter the selected quote before using it in your budget.');
    const checks = Array.isArray(raw.checks) ? raw.checks.slice(0, 5).map(v => v === true) : [];
    while (checks.length < 5) checks.push(false);
    let snapshot = null;
    if (raw.snapshot !== null && raw.snapshot !== undefined) {
      const s = raw.snapshot;
      if (!s || typeof s !== 'object' || !s.inputs || typeof s.inputs !== 'object') throw Error('Invalid calculator snapshot.');
      const inputs = {};
      for (const id of roofIds) {
        if (typeof s.inputs[id] !== 'string' || s.inputs[id].length > 30) throw Error('Invalid calculator inputs in backup.');
        inputs[id] = s.inputs[id];
      }
      const mid = amount(s.mid);
      if (mid <= 0) throw Error('Invalid calculator estimate in backup.');
      snapshot = {inputs, mid, range:text(s.range, 150), savedAt:validDate(s.savedAt)};
    }
    return {version:1, name, quotes, selected, budget:amount(raw.budget, true), reserve:amount(raw.reserve), paid:amount(raw.paid), checks, snapshot, updatedAt:validDate(raw.updatedAt)};
  }
  function validDate(v) {
    if (typeof v !== 'string' || !Number.isFinite(Date.parse(v))) throw Error('Invalid saved date in backup.');
    return new Date(v).toISOString();
  }
  function empty() {
    return {version:1,name:'My roof project',quotes:[null,null,null],selected:'',budget:null,reserve:0,paid:0,checks:[false,false,false,false,false],snapshot:null,updatedAt:new Date().toISOString()};
  }
  function summary(p) {
    const quote = p.selected === '' ? null : p.quotes[Number(p.selected)];
    if (!quote) return null;
    const known = Math.round((quote.price + quote.extras) * 100) / 100;
    const cash = Math.round((known + p.reserve) * 100) / 100;
    return {known, cash, unpaid:Math.round(Math.max(0, known - p.paid) * 100) / 100,
      remaining:Math.round((cash - p.paid) * 100) / 100,
      gap:p.budget === null ? null : Math.round((p.budget - cash) * 100) / 100,
      paidAboveKnown:p.paid > known, unresolved:quote.unresolved};
  }
  const api = {KEY, normalize, empty, summary, amount};
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  if (!root.document) return;
  const doc = root.document;
  const qa = new URLSearchParams(root.location.search).get('hce_qa') === '1';
  doc.querySelectorAll('[data-project-link]').forEach(a=>{if(qa){const u=new URL(a.href,root.location.origin);u.searchParams.set('hce_qa','1');a.href=u.href;}});
  const dollars = n => new Intl.NumberFormat('en-US',{style:'currency',currency:'USD'}).format(n);
  function track(name) {
    if (qa) { root.console.info('[HCE project QA]', name); return; }
    if (typeof root.gtag === 'function') root.gtag('event',name,{funnel_version:'roof_project_v1',page_path:root.location.pathname.replace(/\.html$/,'')});
  }
  function link(path) { return path + (qa ? '?hce_qa=1' : ''); }
  function read() {
    const value = root.localStorage.getItem(KEY);
    return value === null ? null : normalize(JSON.parse(value));
  }
  function write(p) { root.localStorage.setItem(KEY, JSON.stringify(normalize(p))); }
  const roofForm = doc.getElementById('calculatorForm');
  const saveEstimate = doc.getElementById('roof-save-project');
  if (roofForm && saveEstimate) {
    const status = doc.getElementById('roof-project-save-status');
    let signature = null;
    const signatureNow = () => roofIds.map(id => doc.getElementById(id).value).join('|');
    roofForm.addEventListener('submit', () => root.setTimeout(() => {
      const mid = Number(doc.getElementById('result').textContent.replace(/[^\d.]/g,''));
      if (roofForm.checkValidity() && Number.isFinite(mid) && mid > 0 && mid <= 100000000) {
        signature = signatureNow(); saveEstimate.disabled = false;
      }
    },0));
    function stale() { if (signature !== signatureNow()) { saveEstimate.disabled = true; status.textContent = 'Calculate again before saving changed inputs.'; } }
    roofForm.addEventListener('input',stale);roofForm.addEventListener('change',stale);
    saveEstimate.addEventListener('click',() => {
      if (signature === null || signature !== signatureNow() || !roofForm.checkValidity()) return;
      try {
        let p;
        try { p = read() || empty(); } catch (_) { status.textContent = 'Saved project could not be read. Open My roof project to recover or delete it before saving.'; return; }
        if (p.snapshot && !root.confirm('Replace the saved calculator snapshot? Your saved quotes and budget will stay.')) return;
        const inputs = {};roofIds.forEach(id => { inputs[id] = doc.getElementById(id).value; });
        p.snapshot = {inputs,mid:Number(doc.getElementById('result').textContent.replace(/[^\d.]/g,'')),range:doc.getElementById('range').textContent,savedAt:new Date().toISOString()};
        p.updatedAt = new Date().toISOString();write(p);track('roof_project_saved');
        doc.getElementById('roof-restore-project').hidden = false;
        status.textContent = 'Estimate saved on this browser. Open My roof project to add quotes and a budget.';
      } catch (_) { status.textContent = 'Browser storage is unavailable or full. Your estimate was not saved. Try another browser or use the free worksheets.'; }
    });
    const restore = doc.getElementById('roof-restore-project');
    try { const p = read();restore.hidden = !p?.snapshot; } catch (_) { restore.hidden = true; }
    restore.addEventListener('click',() => {
      if (!root.confirm('Replace the calculator fields with your saved snapshot? Saved quotes and budget will stay.')) return;
      try {
        const p = read(); if (!p?.snapshot) throw Error('No snapshot');
        const entries = roofIds.map(id => [doc.getElementById(id),p.snapshot.inputs[id]]);
        // Validate every select before changing any field; stale backups cannot leave partial input state.
        if (entries.some(([el,value]) => el.tagName === 'SELECT' && !Array.from(el.options).some(o => o.value === value))) throw Error('Outdated selection');
        entries.forEach(([el,value]) => { el.value = value; });
        doc.getElementById('localZip').value = '';doc.getElementById('localMetrics').hidden = true;
        doc.getElementById('localZipStatus').textContent = 'Restored saved state-level assumptions. ZIP and live local data are not stored.';
        roofForm.requestSubmit();status.textContent = 'Saved inputs restored and recalculated using the current model. Compare with your dated snapshot; model results can change.';
      } catch (_) { status.textContent = 'This snapshot cannot be restored to the current calculator. Review or export it in My roof project.'; }
    });
  }
  const form = doc.getElementById('roof-project-form');
  if (!form) return;
  const get = id => doc.getElementById(id);
  const status = get('project-status'), error = get('project-error');
  let current = empty(), saved = null, dirty = false;
  let unreadable = false;
  function notify(message, bad) { (bad ? error : status).textContent = message;error.hidden = !bad; }
  function fill(p) {
    get('project-name').value = p.name;get('project-budget').value = p.budget ?? '';get('project-reserve').value = p.reserve;get('project-paid').value = p.paid;get('project-selected').value = p.selected;
    p.quotes.forEach((q,i) => {get('quote-name-'+i).value = q?.name || '';get('quote-price-'+i).value = q?.price ?? '';get('quote-extra-'+i).value = q?.extras ?? '';get('quote-open-'+i).checked = q?.unresolved || false;get('quote-notes-'+i).value = q?.notes || '';});
    p.checks.forEach((v,i) => { get('project-check-'+i).checked = v; });
    get('project-snapshot').textContent = p.snapshot ? 'Calculator snapshot from ' + new Date(p.snapshot.savedAt).toLocaleDateString('en-US') + ': ' + p.snapshot.inputs.area + ' sq ft; ' + p.snapshot.range + ' (midpoint ' + dollars(p.snapshot.mid) + '). This model estimate includes the calculator contingency and is not added to your quote budget.' : 'No calculator snapshot saved. Calculate your roof estimate, then choose Save estimate to My roof project.';
    current = p;dirty = false;error.hidden = true;render(p);
  }
  function collect() {
    const p = empty();p.name = get('project-name').value;p.snapshot = current.snapshot;
    p.budget = get('project-budget').value;p.reserve = get('project-reserve').value;p.paid = get('project-paid').value;p.selected = get('project-selected').value;
    p.quotes = [0,1,2].map(i => {
      const name=get('quote-name-'+i).value,price=get('quote-price-'+i).value,extras=get('quote-extra-'+i).value,notes=get('quote-notes-'+i).value,unresolved=get('quote-open-'+i).checked;
      if (!name && !price && !extras && !notes && !unresolved) return null;
      if (price.trim() === '') throw Error('Enter a total for quote '+(i+1)+', or clear that entire quote slot.');
      if (extras.trim() === '') throw Error('Enter required priced exclusions for quote '+(i+1)+'. Enter 0 only when none remain.');
      return {name,price,extras,notes,unresolved};
    });
    p.checks = [0,1,2,3,4].map(i => get('project-check-'+i).checked);
    return normalize(p);
  }
  function render(p) {
    get('project-comparison-title').textContent = p.name + ' — saved quote comparison';
    const body = get('project-comparison');body.replaceChildren();
    p.quotes.forEach(q => {
      if (!q) return;
      const tr = doc.createElement('tr');
      [q.name,dollars(q.price),dollars(q.extras),dollars(q.price+q.extras),q.unresolved?'Required costs still unpriced':'Review written scope'].forEach(value => {const td=doc.createElement('td');td.textContent=value;tr.append(td);});body.append(tr);
      if(q.notes){const notesRow=doc.createElement('tr'),td=doc.createElement('td');td.colSpan=5;td.textContent=q.name+' scope notes: '+q.notes;notesRow.append(td);body.append(notesRow);}
    });
    get('project-no-quotes').hidden = p.quotes.some(Boolean);
    const s = summary(p);const box=get('project-budget-result');box.replaceChildren();
    const line = value => {const paragraph=doc.createElement('p');paragraph.textContent=value;box.append(paragraph);};
    if (!s) {line('Choose a saved quote to calculate your project budget. No contractor is selected or recommended for you.');return;}
    line('Known scope: '+dollars(s.known)+' = quoted total + required priced exclusions. Included allowances stay inside the quote total.');
    line('Cash plan including your separate reserve: '+dollars(s.cash)+'. Already paid: '+dollars(p.paid)+'.');
    line('Known scope not yet paid: '+dollars(s.unpaid)+'. Cash still to set aside including reserve: '+dollars(Math.max(0,s.remaining))+'.');
    if (s.gap !== null) line(s.gap >= 0 ? 'Within your budget by '+dollars(s.gap)+'.' : 'Above your budget by '+dollars(-s.gap)+'.');
    if (s.paidAboveKnown) line('Paid exceeds known scope. Check for duplicate payments, a missing change order or a refund; the difference is not a saving.');
    if (s.unresolved) line('PROVISIONAL: required costs are still unpriced. This is not a complete project total.');
  }
  try {
    saved=read();fill(saved || current);
    if (saved) {notify('Opened the project saved '+new Date(saved.updatedAt).toLocaleString('en-US')+'. Changes are saved only when you press Save project.');if(Date.now()-Date.parse(saved.updatedAt)>=86400000)track('roof_project_reopened');}
  } catch (_) {unreadable=true;fill(current);notify('Saved data is unreadable or browser storage is unavailable. Nothing was deleted. Import a backup, or use Delete saved project to reset.',true);}
  function changed(e){if(e.target?.id==='project-import')return;dirty=true;notify('Unsaved changes. Save project to update the comparison and budget.');}
  form.addEventListener('input',changed);
  form.addEventListener('change',changed);
  form.addEventListener('submit',e => {
    e.preventDefault();
    try {
      if(unreadable)throw Error('Recover or delete the unreadable saved project before saving a replacement.');
      const latest=read();
      if((latest?.updatedAt || null)!==(saved?.updatedAt || null))throw Error('This project changed in another tab. Reload to use the latest saved version. Your unsaved changes here have not been saved.');
      const p=collect();write(p);const hadSecond=Boolean(saved?.quotes[1]);saved=p;fill(p);
      notify('Saved on this browser at '+new Date(p.updatedAt).toLocaleTimeString('en-US')+'. Export a backup before changing devices or clearing browser data.');
      track('roof_project_saved');if(!hadSecond && p.quotes[1])track('roof_second_quote_saved');
    } catch (e) {notify(e.message || 'Your project was not saved. Browser storage may be full or disabled.',true);}
  });
  get('project-export').addEventListener('click',() => {
    if(!saved || dirty){notify('Save your changes before exporting a backup.',true);return;}
    const blob=new Blob([JSON.stringify(saved,null,2)],{type:'application/json'});const url=URL.createObjectURL(blob),a=doc.createElement('a');a.href=url;a.download='homecostengine-roof-project.json';a.click();root.setTimeout(()=>URL.revokeObjectURL(url),1000);track('roof_project_exported');notify('Backup download requested. Keep it private; it contains your saved project.');
  });
  get('project-import').addEventListener('change',async e => {
    const file=e.target.files[0];if(!file)return;
    try {
      if(file.size>100000)throw Error('Choose a project backup smaller than 100 KB.');
      const p=normalize(JSON.parse(await file.text()));
      if((saved || dirty) && !root.confirm('Replace this browser’s saved project and unsaved changes with the backup? Export your current project first if needed.'))return;
      write(p);saved=p;unreadable=false;fill(p);notify('Backup imported and saved on this browser.');track('roof_project_imported');
    } catch(e){notify('Backup not imported. '+e.message,true);}finally{e.target.value='';}
  });
  get('project-delete').addEventListener('click',() => {
    if(!root.confirm('Delete this roof project from this browser? Export a backup first if you want to keep it.'))return;
    try{root.localStorage.removeItem(KEY);saved=null;unreadable=false;fill(empty());notify('Saved roof project deleted from this browser. Downloaded backups are not deleted.');}catch(_){notify('Browser storage could not be cleared. Use your browser site-data settings.',true);}
  });
  get('project-print').addEventListener('click',() => {if(!saved || dirty){notify('Save your project before printing the current plan.',true);return;}root.print();});
})(typeof window !== 'undefined' ? window : globalThis);
