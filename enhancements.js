/**
 * Homepage enhancements: fullscreen mode + saved wheels (localStorage).
 * Loaded after script.js — interacts with the wheel only through the DOM
 * (textarea + Update button), so it stays decoupled from wheel internals.
 */
(function () {
  // ---------- Fullscreen ----------
  var container = document.getElementById('wheel-container');
  var fsBtn = document.getElementById('fullscreenBtn');
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
