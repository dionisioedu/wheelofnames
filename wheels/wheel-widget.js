/**
 * Wheel Widget — standalone canvas spinner for template pages.
 * Reads window.WHEEL_DATA = { entries: ["..."], removeDefault: false }
 * Renders into #wheel-widget. No dependency on the homepage script.js.
 */
(function () {
  var DATA = window.WHEEL_DATA || { entries: [] };
  var original = DATA.entries.slice();
  var entries = original.slice();
  var COLORS = ['#1E90FF', '#f43f5e', '#22c55e', '#f59e0b', '#8b5cf6', '#06b6d4',
                '#ef4444', '#10b981', '#e879f9', '#facc15', '#60a5fa', '#fb923c'];
  var rot = 0;
  var spinning = false;

  var root = document.getElementById('wheel-widget');
  if (!root) return;

  root.innerHTML =
    '<div class="ww-wrap">' +
      '<div class="ww-pointer" aria-hidden="true"></div>' +
      '<canvas id="wwCanvas" width="440" height="440" aria-label="Spinning wheel"></canvas>' +
    '</div>' +
    '<div class="ww-result" id="ww-result" role="status" aria-live="polite">&nbsp;</div>' +
    '<div style="text-align:center;">' +
      '<button class="btn btn-primary generator-btn" id="ww-spin" type="button">' +
        '<span class="btn-text">Spin the Wheel</span><span class="btn-icon">🎡</span>' +
      '</button>' +
    '</div>' +
    '<div class="ww-controls">' +
      '<label class="form-check-label" style="cursor:pointer;">' +
        '<input class="form-check-input" type="checkbox" id="ww-remove"' + (DATA.removeDefault ? ' checked' : '') + '> Remove winner after spin' +
      '</label>' +
      '<button class="btn btn-outline-secondary btn-sm" id="ww-reset" type="button">↺ Reset wheel</button>' +
      '<a class="btn btn-outline-primary btn-sm" id="ww-customize" href="/">✏️ Customize this wheel</a>' +
    '</div>';

  var canvas = document.getElementById('wwCanvas');
  var ctx = canvas.getContext('2d');
  var resultEl = document.getElementById('ww-result');
  var spinBtn = document.getElementById('ww-spin');

  // Build "customize in full editor" link using the homepage ?items= share format
  function b64url(str) {
    var bytes = new TextEncoder().encode(str);
    var bin = '';
    bytes.forEach(function (b) { bin += String.fromCharCode(b); });
    return btoa(bin).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/g, '');
  }
  try {
    document.getElementById('ww-customize').href = '/?items=' + b64url(original.join('\n'));
  } catch (e) {}

  function label(text, n) {
    var max = n <= 6 ? 20 : n <= 9 ? 16 : 13;
    return text.length > max ? text.slice(0, max - 1) + '…' : text;
  }

  function draw(rotDeg) {
    var n = entries.length;
    var cx = 220, cy = 220, r = 214;
    ctx.clearRect(0, 0, 440, 440);
    if (!n) return;
    var seg = 360 / n;
    var fontSize = n <= 6 ? 22 : n <= 8 ? 19 : n <= 10 ? 17 : 15;
    for (var i = 0; i < n; i++) {
      var start = (rotDeg + i * seg) * Math.PI / 180;
      var end = (rotDeg + (i + 1) * seg) * Math.PI / 180;
      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.arc(cx, cy, r, start, end);
      ctx.closePath();
      ctx.fillStyle = COLORS[i % COLORS.length];
      ctx.fill();
      ctx.strokeStyle = 'rgba(255,255,255,0.85)';
      ctx.lineWidth = 2;
      ctx.stroke();
      var mid = (rotDeg + (i + 0.5) * seg) * Math.PI / 180;
      ctx.save();
      ctx.translate(cx + Math.cos(mid) * r * 0.60, cy + Math.sin(mid) * r * 0.60);
      var ang = mid % (2 * Math.PI);
      if (ang > Math.PI / 2 && ang < 3 * Math.PI / 2) {
        ctx.rotate(mid + Math.PI); // flip text on the left side for readability
      } else {
        ctx.rotate(mid);
      }
      ctx.fillStyle = '#fff';
      ctx.font = '700 ' + fontSize + 'px Quicksand, sans-serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.shadowColor = 'rgba(0,0,0,0.35)';
      ctx.shadowBlur = 4;
      ctx.fillText(label(entries[i], n), 0, 0);
      ctx.restore();
    }
    ctx.beginPath();
    ctx.arc(cx, cy, 24, 0, Math.PI * 2);
    ctx.fillStyle = '#fff';
    ctx.fill();
    ctx.strokeStyle = '#d0d0d0';
    ctx.lineWidth = 2;
    ctx.stroke();
  }

  function winnerIndex(rotDeg) {
    var n = entries.length;
    var seg = 360 / n;
    var local = ((270 - rotDeg) % 360 + 360) % 360;
    return Math.floor(local / seg);
  }

  function easeOutCubic(t) { return 1 - Math.pow(1 - t, 3); }

  function spin() {
    if (spinning || entries.length < 2) return;
    spinning = true;
    resultEl.innerHTML = '&nbsp;';
    spinBtn.classList.add('loading');
    var duration = 3800;
    var startRot = rot;
    var delta = 4 * 360 + Math.random() * 720;
    var t0 = performance.now();
    function frame(now) {
      var t = Math.min((now - t0) / duration, 1);
      rot = (startRot + delta * easeOutCubic(t)) % 360000;
      draw(rot % 360);
      if (t < 1) { requestAnimationFrame(frame); }
      else {
        var idx = winnerIndex(rot % 360);
        var winner = entries[idx];
        resultEl.textContent = '🎉 ' + winner;
        try { if (window.confettiBurst) window.confettiBurst({ count: 120 }); } catch (e) {}
        spinBtn.classList.remove('loading');
        spinning = false;
        if (document.getElementById('ww-remove').checked) {
          setTimeout(function () {
            if (entries.length > 1) {
              entries.splice(idx, 1);
              rot = 0;
              draw(0);
              if (entries.length === 1) {
                resultEl.textContent = '🏁 Last one left: ' + entries[0];
              }
            }
          }, 1400);
        }
      }
    }
    requestAnimationFrame(frame);
  }

  document.getElementById('ww-reset').addEventListener('click', function () {
    if (spinning) return;
    entries = original.slice();
    rot = 0;
    resultEl.innerHTML = '&nbsp;';
    draw(0);
  });
  canvas.addEventListener('click', spin);
  spinBtn.addEventListener('click', spin);
  document.addEventListener('keydown', function (e) {
    if (e.code === 'Space' && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
      e.preventDefault();
      spin();
    }
  });

  draw(0);
})();
