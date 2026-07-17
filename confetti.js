/**
 * Confetti — lightweight canvas confetti burst, no dependencies.
 * Usage: window.confettiBurst(options?) — fire-and-forget celebration.
 */
(function () {
  var COLORS = ['#1E90FF', '#f43f5e', '#22c55e', '#f59e0b', '#8b5cf6', '#06b6d4', '#facc15', '#fb923c'];
  var active = null;

  function confettiBurst(opts) {
    opts = opts || {};
    var count = opts.count || 160;
    var duration = opts.duration || 2800;

    // Reuse a single canvas if bursts overlap
    var canvas = active && active.canvas;
    if (!canvas) {
      canvas = document.createElement('canvas');
      canvas.style.cssText = 'position:fixed;inset:0;width:100vw;height:100vh;z-index:3000;pointer-events:none;';
      document.body.appendChild(canvas);
    }
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    var ctx = canvas.getContext('2d');

    var W = canvas.width, H = canvas.height;
    var parts = [];
    for (var i = 0; i < count; i++) {
      var fromLeft = i % 2 === 0;
      parts.push({
        x: fromLeft ? -10 : W + 10,
        y: H * (0.2 + Math.random() * 0.3),
        vx: (fromLeft ? 1 : -1) * (4 + Math.random() * 7),
        vy: -(6 + Math.random() * 7),
        g: 0.25 + Math.random() * 0.12,
        w: 6 + Math.random() * 6,
        h: 4 + Math.random() * 4,
        rot: Math.random() * Math.PI * 2,
        vr: (Math.random() - 0.5) * 0.3,
        color: COLORS[i % COLORS.length],
        drag: 0.985 + Math.random() * 0.01
      });
    }

    var t0 = performance.now();
    if (active) { active.parts = active.parts.concat(parts); active.t0 = t0; return; }

    active = { canvas: canvas, parts: parts, t0: t0 };

    function frame(now) {
      if (!active) return;
      var elapsed = now - active.t0;
      ctx.clearRect(0, 0, W, H);
      var alive = false;
      var fade = elapsed > duration ? Math.max(0, 1 - (elapsed - duration) / 600) : 1;
      for (var j = 0; j < active.parts.length; j++) {
        var p = active.parts[j];
        p.vx *= p.drag;
        p.vy += p.g;
        p.x += p.vx;
        p.y += p.vy;
        p.rot += p.vr;
        if (p.y < H + 30) alive = true;
        ctx.save();
        ctx.translate(p.x, p.y);
        ctx.rotate(p.rot);
        ctx.globalAlpha = fade;
        ctx.fillStyle = p.color;
        ctx.fillRect(-p.w / 2, -p.h / 2, p.w, p.h);
        ctx.restore();
      }
      if (alive && fade > 0) {
        requestAnimationFrame(frame);
      } else {
        canvas.remove();
        active = null;
      }
    }
    requestAnimationFrame(frame);
  }

  window.confettiBurst = confettiBurst;
})();
