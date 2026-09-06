/* ============================================================
   Cupboard Centre — site interactions
   Framework/behaviour mirrors the conversion reference site.
   Vanilla JS, no dependencies.
   ============================================================ */
(function () {
  'use strict';
  var doc = document;
  var on = function (el, ev, fn, o) { el && el.addEventListener(ev, fn, o || false); };
  var $ = function (s, r) { return (r || doc).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || doc).querySelectorAll(s)); };

  /* ---------- Mobile menu ---------- */
  function initMobileMenu() {
    var burger = $('.hamburger');
    var menu = $('.mobile-menu');
    if (!burger || !menu) return;
    on(burger, 'click', function () {
      var open = menu.classList.toggle('open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    $$('.m-has-sub .m-sub-toggle', menu).forEach(function (btn) {
      on(btn, 'click', function () {
        var li = btn.closest('.m-has-sub');
        var open = li.classList.toggle('open');
        btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      });
    });
    $$('.mobile-menu a').forEach(function (a) {
      on(a, 'click', function () {
        menu.classList.remove('open');
        burger.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* ---------- Generic FAQ / accordion (.faq-item) ---------- */
  function initAccordions() {
    $$('.faq-item').forEach(function (item) {
      var q = $('.faq-q', item);
      if (!q) return;
      on(q, 'click', function () { item.classList.toggle('open'); });
      q.setAttribute('role', 'button');
      q.setAttribute('tabindex', '0');
      on(q, 'keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); item.classList.toggle('open'); }
      });
    });
  }

  /* ---------- Smooth scroll to a target (data-scroll="id") ---------- */
  function initScrollButtons() {
    $$('[data-scroll]').forEach(function (btn) {
      on(btn, 'click', function (e) {
        var id = btn.getAttribute('data-scroll');
        var target = doc.getElementById(id);
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
          var field = $('input,textarea,select', target);
          if (field) setTimeout(function () { field.focus(); }, 500);
        }
      });
    });
  }

  /* ---------- "Read more" toggle on long reviews ---------- */
  function initReviewToggles() {
    $$('.rev-toggle').forEach(function (btn) {
      on(btn, 'click', function () {
        var card = btn.closest('.rev-card');
        var expanded = card.classList.toggle('rev-expanded');
        btn.textContent = expanded ? 'Read less' : 'Read more';
      });
    });
  }

  /* ---------- Review carousel (paged, 3/2/1-up responsive) ---------- */
  function perPage() {
    if (window.matchMedia('(max-width:700px)').matches) return 1;
    if (window.matchMedia('(max-width:1000px)').matches) return 2;
    return 3;
  }
  function initReviewCarousel(root) {
    var track = $('[data-track]', root);
    var slides = $$('.rev-slide', track).filter(function (s) { return s.getAttribute('aria-hidden') !== 'true'; });
    var viewport = $('.carousel-viewport', root);
    var dotsWrap = (root.closest('section') || doc).querySelector('[data-dots]');
    if (!track || !slides.length) return;
    // Hide the duplicate (aria-hidden) slides that exist only for the source site's loop
    $$('.rev-slide[aria-hidden="true"]', track).forEach(function (s) { s.style.display = 'none'; });
    var page = 0;
    function pages() { return Math.max(1, Math.ceil(slides.length / perPage())); }
    function buildDots() {
      if (!dotsWrap) return;
      dotsWrap.innerHTML = '';
      for (var i = 0; i < pages(); i++) {
        var b = doc.createElement('button');
        b.className = 'cdot' + (i === page ? ' active' : '');
        b.setAttribute('aria-label', 'Go to review page ' + (i + 1));
        (function (idx) { on(b, 'click', function () { page = idx; render(); }); })(i);
        dotsWrap.appendChild(b);
      }
    }
    function render() {
      var pp = perPage();
      if (page > pages() - 1) page = pages() - 1;
      var shift = page * viewport.offsetWidth;
      track.style.transform = 'translateX(' + (-shift) + 'px)';
      $$('.cdot', dotsWrap).forEach(function (d, i) { d.classList.toggle('active', i === page); });
    }
    on($('[data-prev]', root), 'click', function () { page = (page - 1 + pages()) % pages(); render(); });
    on($('[data-next]', root), 'click', function () { page = (page + 1) % pages(); render(); });
    var rt;
    on(window, 'resize', function () { clearTimeout(rt); rt = setTimeout(function () { buildDots(); render(); }, 150); });
    buildDots(); render();
    // autoplay
    setInterval(function () { page = (page + 1) % pages(); render(); }, 7000);
  }

  /* ---------- "Our Work" centre-mode carousel ---------- */
  function initWorkCarousel(root) {
    var track = $('[data-work-track]', root);
    var slides = $$('.work-slide', track);
    var dotsWrap = (root.closest('section') || doc).querySelector('[data-work-dots]');
    if (!track || !slides.length) return;
    var active = 0;
    function render() {
      slides.forEach(function (s, i) { s.classList.toggle('is-active', i === active); });
      var slide = slides[active];
      var vp = $('.work-viewport', root);
      var offset = slide.offsetLeft - (vp.offsetWidth - slide.offsetWidth) / 2;
      track.style.transform = 'translateX(' + (-offset) + 'px)';
      if (dotsWrap) $$('.cdot', dotsWrap).forEach(function (d, i) { d.classList.toggle('active', i === active); });
    }
    // Clicking a slide opens it in the lightbox (with prev/next + close)
    var lbImgs = slides.map(function (s) { return $('img', s); }).filter(Boolean);
    var lb = buildLightbox(lbImgs);
    slides.forEach(function (s, i) { s.style.cursor = 'zoom-in'; on(s, 'click', function () { if (lb) lb.open(i); }); });
    on($('[data-work-prev]', root), 'click', function () { active = (active - 1 + slides.length) % slides.length; render(); });
    on($('[data-work-next]', root), 'click', function () { active = (active + 1) % slides.length; render(); });
    if (dotsWrap) {
      dotsWrap.innerHTML = '';
      slides.forEach(function (s, i) {
        var b = doc.createElement('button');
        b.className = 'cdot' + (i === 0 ? ' active' : '');
        b.setAttribute('aria-label', 'Go to project ' + (i + 1));
        on(b, 'click', function () { active = i; render(); });
        dotsWrap.appendChild(b);
      });
    }
    var rt; on(window, 'resize', function () { clearTimeout(rt); rt = setTimeout(render, 150); });
    setTimeout(render, 50);
    // autoplay — keep the carousel cyclable; pause while the visitor is hovering
    var timer = setInterval(function () { active = (active + 1) % slides.length; render(); }, 5000);
    on(root, 'mouseenter', function () { clearInterval(timer); timer = null; });
    on(root, 'mouseleave', function () { if (!timer) timer = setInterval(function () { active = (active + 1) % slides.length; render(); }, 5000); });
  }

  /* ---------- Gallery filters ---------- */
  function initGalleryFilters() {
    var bar = $('.gallery-filters');
    if (!bar) return;
    var items = $$('.gallery-grid .g-item');
    $$('button', bar).forEach(function (btn) {
      on(btn, 'click', function () {
        $$('button', bar).forEach(function (b) { b.classList.remove('active'); });
        btn.classList.add('active');
        var f = btn.getAttribute('data-filter');
        items.forEach(function (it) {
          var show = f === 'all' || it.getAttribute('data-cat') === f;
          it.style.display = show ? '' : 'none';
        });
      });
    });
  }

  /* ---------- Before/After sliders ---------- */
  function initBeforeAfter() {
    $$('.ba[data-ba]').forEach(function (ba) {
      var range = $('.ba-range', ba);
      if (!range) return;
      function set(v) { ba.style.setProperty('--ba-p', v + '%'); }
      on(range, 'input', function () { set(range.value); });
      set(range.value || 50);
    });
  }

  /* ---------- Reusable lightbox ---------- */
  function buildLightbox(imgs) {
    if (!imgs.length) return null;
    var box = doc.createElement('div');
    box.className = 'lightbox';
    box.innerHTML = '<button class="lightbox-close" aria-label="Close">&times;</button>' +
      '<button class="lightbox-nav prev" aria-label="Previous">&lsaquo;</button>' +
      '<img alt="">' +
      '<button class="lightbox-nav next" aria-label="Next">&rsaquo;</button>';
    doc.body.appendChild(box);
    var big = $('img', box), idx = 0;
    function show(i) { idx = (i + imgs.length) % imgs.length; var im = imgs[idx]; big.src = im.getAttribute('data-full') || im.currentSrc || im.src; big.alt = im.alt || ''; }
    function open(i) { show(i); box.classList.add('open'); }
    function close() { box.classList.remove('open'); }
    on($('.lightbox-close', box), 'click', close);
    on($('.lightbox-nav.prev', box), 'click', function (e) { e.stopPropagation(); show(idx - 1); });
    on($('.lightbox-nav.next', box), 'click', function (e) { e.stopPropagation(); show(idx + 1); });
    on(box, 'click', function (e) { if (e.target === box) close(); });
    on(doc, 'keydown', function (e) {
      if (!box.classList.contains('open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') show(idx - 1);
      if (e.key === 'ArrowRight') show(idx + 1);
    });
    return { open: open, close: close };
  }

  /* ---------- Lightbox for gallery images ---------- */
  function initLightbox() {
    var imgs = $$('.gallery-grid .g-item img').filter(function (img) {
      return !img.closest('.ba-before');
    });
    var lb = buildLightbox(imgs);
    if (!lb) return;
    imgs.forEach(function (img, i) { img.style.cursor = 'zoom-in'; on(img, 'click', function () { lb.open(i); }); });
  }

  /* ---------- "Show more" services grid ---------- */
  function initServiceMore() {
    var btn = $('[data-svc-more]');
    if (!btn) return;
    on(btn, 'click', function () {
      $$('.svc-card.svc-hidden').forEach(function (c) { c.classList.remove('svc-hidden'); });
      btn.style.display = 'none';
    });
  }

  /* ---------- Lead / contact forms (front-end handling) ---------- */
  function initForms() {
    $$('form[data-lead]').forEach(function (form) {
      // reveal "please specify" when service = Other
      var svc = $('[data-role="service"]', form);
      var other = $('[data-role="service_other"]', form);
      if (svc && other) {
        on(svc, 'change', function () {
          other.style.display = /other/i.test(svc.value) ? '' : 'none';
        });
      }
      on(form, 'submit', function (e) {
        e.preventDefault();
        if (!form.checkValidity()) { form.reportValidity && form.reportValidity(); return; }
        var btn = $('button[type="submit"]', form);
        var name = (($('[data-role="name"]', form) || {}).value || '').trim();
        var msg = doc.createElement('div');
        msg.style.cssText = 'margin-top:14px;padding:14px 16px;border-radius:12px;background:rgba(232,30,44,.10);border:1px solid var(--green);color:var(--heading);font-size:14px;line-height:1.5';
        msg.innerHTML = '<strong>Thank you' + (name ? ', ' + name.split(' ')[0] : '') +
          '!</strong><br>Your request has reached Cupboard Centre. We’ll call you back within one business hour. For anything urgent, call <a href="tel:0846837467" style="color:var(--green);font-weight:700">084 683 7467</a>.';
        form.reset();
        if (other) other.style.display = 'none';
        if (btn) { btn.disabled = true; btn.textContent = 'Request Sent ✓'; }
        var old = form.querySelector('.lead-thanks');
        if (old) old.remove();
        msg.className = 'lead-thanks';
        form.appendChild(msg);
      });
    });
  }

  /* ---------- Cart (localStorage) ---------- */
  var CART_KEY = 'cc_cart_v1';
  var WA_NUMBER = '27846837467';
  function cartRead() { try { return JSON.parse(localStorage.getItem(CART_KEY)) || []; } catch (e) { return []; } }
  function cartWrite(items) { try { localStorage.setItem(CART_KEY, JSON.stringify(items)); } catch (e) {} cartBadge(); }
  function money(n) { return 'R' + String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g, ' '); }
  function cartBadge() {
    var n = cartRead().reduce(function (t, i) { return t + i.qty; }, 0);
    $$('[data-cart-count]').forEach(function (b) {
      b.textContent = n;
      if (n > 0) { b.hidden = false; b.removeAttribute('hidden'); } else { b.hidden = true; b.setAttribute('hidden', ''); }
    });
  }
  function cartAdd(p, qty) {
    var items = cartRead();
    var ex = null;
    items.forEach(function (i) { if (i.id === p.id) ex = i; });
    if (ex) ex.qty += qty; else items.push({ id: p.id, name: p.name, price: p.price, img: p.img, qty: qty });
    cartWrite(items);
  }
  function initAddToCart() {
    $$('[data-add-cart]').forEach(function (btn) {
      on(btn, 'click', function () {
        var buy = btn.closest('.pd-buy');
        var qInput = buy ? $('[data-qty]', buy) : null;
        var qty = qInput ? Math.max(1, parseInt(qInput.value, 10) || 1) : 1;
        cartAdd({
          id: btn.getAttribute('data-id'), name: btn.getAttribute('data-name'),
          price: parseInt(btn.getAttribute('data-price'), 10) || 0, img: btn.getAttribute('data-img')
        }, qty);
        var old = btn.textContent; btn.textContent = 'Added ✓'; btn.disabled = true;
        setTimeout(function () { btn.textContent = old; btn.disabled = false; }, 1200);
      });
    });
  }
  function initProduct() {
    var main = $('[data-pd-main]');
    $$('.pd-thumb').forEach(function (t, i) {
      if (i === 0) t.classList.add('active');
      on(t, 'click', function () {
        if (main) main.src = t.getAttribute('data-src');
        $$('.pd-thumb').forEach(function (x) { x.classList.remove('active'); });
        t.classList.add('active');
      });
    });
    $$('.pd-buy .qty-box, .product-detail .qty-box').forEach(function (box) {
      var inp = $('[data-qty]', box); if (!inp) return;
      on($('[data-qty-dec]', box), 'click', function () { inp.value = Math.max(1, (parseInt(inp.value, 10) || 1) - 1); });
      on($('[data-qty-inc]', box), 'click', function () { inp.value = (parseInt(inp.value, 10) || 1) + 1; });
    });
  }
  function renderCartItems() {
    var root = $('[data-cart-root]'); if (!root) return;
    var items = cartRead();
    var empty = $('[data-cart-empty]', root), body = $('[data-cart-body]', root);
    if (!items.length) { if (empty) empty.hidden = false; if (body) body.hidden = true; return; }
    if (empty) empty.hidden = true; if (body) body.hidden = false;
    var wrap = $('[data-cart-items]', root); wrap.innerHTML = '';
    var total = 0;
    items.forEach(function (it, idx) {
      total += it.price * it.qty;
      var el = doc.createElement('div'); el.className = 'cart-item';
      el.innerHTML = '<img src="' + it.img + '" alt=""><div><h3>' + it.name + '</h3>' +
        '<span class="ci-price">' + money(it.price) + ' each</span>' +
        '<div class="qty-box" style="margin-top:8px"><button type="button" data-dec aria-label="Decrease">−</button>' +
        '<input type="number" min="1" value="' + it.qty + '" data-q aria-label="Quantity"><button type="button" data-inc aria-label="Increase">+</button></div>' +
        '<button class="ci-remove" data-rm>Remove</button></div>' +
        '<div class="ci-line"><strong>' + money(it.price * it.qty) + '</strong></div>';
      on($('[data-dec]', el), 'click', function () { it.qty = Math.max(1, it.qty - 1); cartWrite(items); renderCartItems(); });
      on($('[data-inc]', el), 'click', function () { it.qty += 1; cartWrite(items); renderCartItems(); });
      on($('[data-q]', el), 'change', function () { it.qty = Math.max(1, parseInt(this.value, 10) || 1); cartWrite(items); renderCartItems(); });
      on($('[data-rm]', el), 'click', function () { items.splice(idx, 1); cartWrite(items); renderCartItems(); });
      wrap.appendChild(el);
    });
    var tEl = $('[data-cart-total]', root); if (tEl) tEl.textContent = money(total);
  }
  function initCart() {
    var root = $('[data-cart-root]'); if (!root) return;
    renderCartItems();
    var co = $('[data-cart-checkout]', root);
    if (co) on(co, 'click', function () {
      var items = cartRead(); if (!items.length) return;
      var total = 0, lines = items.map(function (it) { total += it.price * it.qty; return '• ' + it.name + ' x' + it.qty + ' (' + money(it.price * it.qty) + ')'; });
      var msg = "Hi Cupboard Centre, I'd like to order:\n" + lines.join('\n') + '\nTotal: ' + money(total) + '\nPlease advise on availability and delivery.';
      window.open('https://wa.me/' + WA_NUMBER + '?text=' + encodeURIComponent(msg), '_blank');
    });
  }

  /* ---------- horizontal "more services" carousel ---------- */
  function initHScroll() {
    $$('.hscroll-wrap').forEach(function (wrap) {
      var track = $('.hscroll', wrap);
      var prev = $('[data-hs-prev]', wrap), next = $('[data-hs-next]', wrap);
      if (!track) return;
      function step() {
        var card = $('.hscroll-card', track);
        return card ? card.offsetWidth + 22 : 340;
      }
      on(prev, 'click', function () { track.scrollBy({ left: -step(), behavior: 'smooth' }); });
      on(next, 'click', function () { track.scrollBy({ left: step(), behavior: 'smooth' }); });
    });
  }

  /* ---------- init all ---------- */
  function init() {
    cartBadge();
    initHScroll();
    initAddToCart();
    initProduct();
    initCart();
    initMobileMenu();
    initAccordions();
    initScrollButtons();
    initReviewToggles();
    $$('[data-carousel]').forEach(initReviewCarousel);
    $$('[data-work]').forEach(initWorkCarousel);
    initGalleryFilters();
    initBeforeAfter();
    initLightbox();
    initServiceMore();
    initForms();
  }
  if (doc.readyState === 'loading') on(doc, 'DOMContentLoaded', init);
  else init();
})();
