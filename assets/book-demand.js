/* Interest signals only. Stripe remains the source of completed orders. */
(function () {
  'use strict';
  const qa = new URLSearchParams(location.search).get('hce_qa') === '1';
  const path = location.pathname.replace(/\.html$/, '');
  const slug = document.querySelector('button[data-book]')?.dataset.book;
  const safeSlug = value => typeof value === 'string' && /^[a-z0-9-]{1,100}$/.test(value);
  const seen = new Set();
  function send(name, book) {
    if (!safeSlug(book)) return;
    const key = name + ':' + book;
    if (name !== 'book_checkout_click' && seen.has(key)) return;
    seen.add(key);
    const data = {book_slug: book, page_path: path, measurement_version: 'book_demand_v1'};
    // Never send input values, URL queries, emails, checkout IDs or payment data.
    if (qa) { console.info('[HCE book demand QA]', name, data); return; }
    if (typeof window.gtag === 'function') window.gtag('event', name, data);
  }
  if (safeSlug(slug)) send('book_detail_view', slug);
  document.addEventListener('click', function (event) {
    if (!event.isTrusted && !qa) return;
    const buy = event.target.closest('button[data-book]');
    if (buy) send('book_checkout_click', buy.dataset.book);
    const link = event.target.closest('a[href]');
    if (!link) return;
    let target;
    try { target = new URL(link.href, location.origin); } catch (_) { return; }
    if (target.origin !== location.origin) return;
    if (safeSlug(slug) && target.pathname.replace(/\.html$/, '') === path && target.hash === '#sample-pages') {
      send('book_preview_click', slug);
    }
    const match = target.pathname.match(/^\/ebooks\/([a-z0-9-]+)(?:\.html)?$/);
    if (path.startsWith('/blog/') && match) send('book_article_click', match[1]);
  });
})();
