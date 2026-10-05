/**
 * Homepage enhancements: fullscreen mode + saved wheels (localStorage).
 * Loaded after script.js — interacts with the wheel only through the DOM
 * (textarea + Update button), so it stays decoupled from wheel internals.
 */
(function () {
  // ---------- Service worker + PWA install prompt ----------
  // Register a minimal service worker (network-first, cache-fallback). Guarded
  // so it never throws on browsers without support.
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', function () {
      navigator.serviceWorker.register('/sw.js').catch(function () {});
    });
  }

  // Install prompt: shown after the user's 2nd spin, only when the browser
  // offers 'beforeinstallprompt' (Chrome/Edge) and the user hasn't dismissed
  // it before. On iOS/Safari/Firefox the event never fires, so nothing shows.
  (function () {
    var DISMISS_KEY = 'wol_pwa_dismissed';
    var deferredPrompt = null;
    var spinCount = 0;
    var banner = null;
    var shown = false;

    function dismissed() {
      try { return localStorage.getItem(DISMISS_KEY) === '1'; } catch (e) { return false; }
    }

    window.addEventListener('beforeinstallprompt', function (event) {
      event.preventDefault();
      deferredPrompt = event;
      // If the user already spun twice before this event arrived, show now.
      maybeShow();
    });

    function hideBanner() {
      if (banner && banner.parentNode) banner.parentNode.removeChild(banner);
      banner = null;
    }

    function buildBanner() {
      var el = document.createElement('div');
      el.className = 'wol-pwa-banner';
      el.setAttribute('role', 'dialog');
      el.setAttribute('aria-label', 'Install Wheel Of List');

      var msg = document.createElement('span');
      msg.className = 'wol-pwa-msg';
      msg.textContent = 'Install Wheel Of List for instant access';

      var installBtn = document.createElement('button');
      installBtn.type = 'button';
      installBtn.className = 'wol-pwa-install';
      installBtn.textContent = 'Install';

      var dismissBtn = document.createElement('button');
      dismissBtn.type = 'button';
      dismissBtn.className = 'wol-pwa-dismiss';
      dismissBtn.textContent = 'Not now';

      installBtn.addEventListener('click', function () {
        var prompt = deferredPrompt;
        hideBanner();
        if (!prompt) return;
        deferredPrompt = null;
        try {
          prompt.prompt();
          if (prompt.userChoice && prompt.userChoice.then) {
            prompt.userChoice.then(function (choice) {
              if (choice && choice.outcome === 'accepted') {
                try { if (window.confettiBurst) window.confettiBurst(); } catch (e) {}
                if (window.wolAnalytics) {
                  window.wolAnalytics.track('tool_action', { tool: 'wheel', action: 'pwa_install' });
                }
              }
            }).catch(function () {});
          }
        } catch (e) {}
      });

      dismissBtn.addEventListener('click', function () {
        try { localStorage.setItem(DISMISS_KEY, '1'); } catch (e) {}
        hideBanner();
      });

      el.appendChild(msg);
      el.appendChild(installBtn);
      el.appendChild(dismissBtn);
      return el;
    }

    function maybeShow() {
      if (shown || dismissed() || !deferredPrompt || spinCount < 2) return;
      shown = true;
      banner = buildBanner();
      // Sit above the cookie notice if it is still on screen so the two
      // bottom banners never overlap.
      if (document.getElementById('wol-consent-banner')) {
        banner.classList.add('wol-pwa-banner--raised');
      }
      document.body.appendChild(banner);
    }

    window.addEventListener('wol:spin', function () {
      spinCount += 1;
      if (spinCount === 2) maybeShow();
    });
  })();

  // ---------- Feedback rating (mailto, no backend) ----------
  // Records which rating was chosen so we can see the distribution in analytics,
  // then lets the browser open the prefilled mail client.
  var feedback = document.getElementById('wolFeedback');
  if (feedback) {
    feedback.addEventListener('click', function (event) {
      var btn = event.target.closest ? event.target.closest('[data-rating]') : null;
      if (!btn) return;
      if (window.wolAnalytics) {
        window.wolAnalytics.track('tool_action', {
          tool: 'wheel',
          action: 'feedback',
          rating: btn.getAttribute('data-rating')
        });
      }
    });
  }

  // ---------- Editor tabs ----------
  var tabs = Array.prototype.slice.call(document.querySelectorAll('[data-editor-tab]'));
  tabs.forEach(function (tab) {
    tab.addEventListener('click', function () {
      tabs.forEach(function (item) {
        var selected = item === tab;
        item.classList.toggle('active', selected);
        item.setAttribute('aria-selected', selected ? 'true' : 'false');
        item.setAttribute('tabindex', selected ? '0' : '-1');
        var panel = document.getElementById(item.getAttribute('data-editor-tab'));
        if (panel) {
          panel.hidden = !selected;
          panel.classList.toggle('active', selected);
        }
      });
      // Panel heights can reflow the Bootstrap row at narrow widths; keep the
      // canvas overlays anchored to the wheel after that layout change.
      setTimeout(function () { window.dispatchEvent(new Event('resize')); }, 0);
    });
    tab.addEventListener('keydown', function (event) {
      if (event.key !== 'ArrowLeft' && event.key !== 'ArrowRight') return;
      event.preventDefault();
      var direction = event.key === 'ArrowRight' ? 1 : -1;
      var next = tabs[(tabs.indexOf(tab) + direction + tabs.length) % tabs.length];
      next.focus();
      next.click();
    });
  });

  // ---------- Fullscreen ----------
  var container = document.getElementById('wheel-container');
  var fsBtn = document.getElementById('fullscreenBtn');
  var fsShortcut = document.getElementById('fullscreenShortcut');
  if (container && fsBtn) {
    fsBtn.addEventListener('click', function () {
      try {
        if (!document.fullscreenElement) {
          (container.requestFullscreen || container.webkitRequestFullscreen).call(container);
        } else {
          (document.exitFullscreen || document.webkitExitFullscreen).call(document);
        }
      } catch (e) {}
    });
    document.addEventListener('fullscreenchange', function () {
      fsBtn.textContent = document.fullscreenElement ? '🗗' : '⛶';
      fsBtn.title = document.fullscreenElement ? 'Exit fullscreen' : 'Fullscreen';
      // Let the wheel recompute its size for the new viewport
      setTimeout(function () { window.dispatchEvent(new Event('resize')); }, 60);
    });
  }
  if (fsShortcut && fsBtn) {
    fsShortcut.addEventListener('click', function () { fsBtn.click(); });
  }

  // ---------- Saved wheels ----------
  var KEY = 'wheeloflist_saved_wheels';
  var nameInput = document.getElementById('wheelNameInput');
  var saveBtn = document.getElementById('saveWheelBtn');
  var listEl = document.getElementById('savedWheelsList');
  var namesArea = document.getElementById('namesInput');
  var updateBtn = document.getElementById('updateNames');
  if (!nameInput || !saveBtn || !listEl || !namesArea) return;

  function read() {
    try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) { return {}; }
  }
  function write(data) {
    try { localStorage.setItem(KEY, JSON.stringify(data)); } catch (e) {}
  }
  function esc(s) {
    return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;');
  }

  function render() {
    var data = read();
    var names = Object.keys(data).sort();
    if (!names.length) {
      listEl.innerHTML = '<li class="list-group-item text-muted" style="font-size:0.85rem;">No saved wheels yet — name your list and hit Save.</li>';
      return;
    }
    listEl.innerHTML = names.map(function (n) {
      return '<li class="list-group-item d-flex justify-content-between align-items-center" style="padding:6px 12px;">' +
        '<button class="btn btn-link btn-sm p-0 text-start text-decoration-none load-wheel" data-name="' + esc(n) + '" title="Load this wheel">🎡 ' + esc(n) +
        ' <span class="text-muted" style="font-size:0.78rem;">(' + data[n].length + ')</span></button>' +
        '<button class="btn btn-sm p-0 delete-wheel" data-name="' + esc(n) + '" title="Delete" style="border:none;background:none;">🗑️</button>' +
      '</li>';
    }).join('');
  }

  saveBtn.addEventListener('click', function () {
    var name = (nameInput.value || '').trim();
    var entries = namesArea.value.split('\n').map(function (s) { return s.trim(); }).filter(Boolean);
    if (!entries.length) { alert('Enter some names first, then save.'); return; }
    if (!name) { name = 'Wheel ' + new Date().toLocaleDateString(); }
    var data = read();
    data[name] = entries;
    write(data);
    if (window.wolAnalytics) window.wolAnalytics.track('wheel_save', { item_count: entries.length });
    nameInput.value = '';
    render();
  });

  listEl.addEventListener('click', function (e) {
    var loadBtn = e.target.closest('.load-wheel');
    var delBtn = e.target.closest('.delete-wheel');
    if (loadBtn) {
      var data = read();
      var entries = data[loadBtn.getAttribute('data-name')];
      if (entries) {
        namesArea.value = entries.join('\n');
        if (updateBtn) updateBtn.click();
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    } else if (delBtn) {
      var n = delBtn.getAttribute('data-name');
      if (confirm('Delete wheel "' + n + '"?')) {
        var d = read();
        delete d[n];
        write(d);
        render();
      }
    }
  });

  render();
})();
