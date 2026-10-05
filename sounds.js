/**
 * Wheel Of List — shared WebAudio sound module.
 *
 * Self-contained, dependency-free. Exposes window.WOLSound:
 *   play(name, opts)  -> plays a named sound (or returns a handle for 'spin')
 *   setEnabled(bool)  -> mute/unmute (persists in localStorage)
 *   isEnabled()       -> current state
 *   toggle()          -> flip state, returns new state
 *   resume()          -> resume/create the AudioContext (call from a gesture)
 *
 * No audio files: every sound is synthesized with oscillators + gain envelopes,
 * so there are zero network requests and zero 404s. All WebAudio calls are
 * wrapped in try/catch and degrade silently when WebAudio is unavailable.
 *
 * Autoplay-safe: the AudioContext is created lazily on the first play()/resume()
 * and resumed if suspended. Page code can also call resume() from the first
 * user gesture. Mute state is stored under localStorage key 'wheeloflist_sound'
 * ('0' = muted, anything else = on).
 */
(function () {
  'use strict';

  var STORAGE_KEY = 'wheeloflist_sound';
  var AudioCtx = window.AudioContext || window.webkitAudioContext;

  // One shared context for the whole page (reused by the high-rate 'tick').
  var ctx = null;
  var master = null;

  // ------------------------------------------------------------------
  // Enable / mute state (persisted)
  // ------------------------------------------------------------------
  var enabled = true;
  try {
    enabled = localStorage.getItem(STORAGE_KEY) !== '0';
  } catch (e) { /* private mode / storage blocked -> stay enabled */ }

  function persist() {
    try { localStorage.setItem(STORAGE_KEY, enabled ? '1' : '0'); } catch (e) {}
  }

  function setEnabled(bool) {
    enabled = !!bool;
    persist();
    return enabled;
  }

  function isEnabled() { return enabled; }

  function toggle() {
    enabled = !enabled;
    persist();
    return enabled;
  }

  // ------------------------------------------------------------------
  // AudioContext bootstrap
  // ------------------------------------------------------------------
  function getCtx() {
    if (ctx) return ctx;
    if (!AudioCtx) return null;
    try {
      ctx = new AudioCtx();
      master = ctx.createGain();
      master.gain.value = 0.9;
      master.connect(ctx.destination);
    } catch (e) {
      ctx = null;
      master = null;
    }
    return ctx;
  }

  function resume() {
    var c = getCtx();
    if (!c) return;
    try {
      if (c.state === 'suspended' && c.resume) c.resume().catch(function () {});
    } catch (e) {}
  }

  // Core synth primitive: an oscillator with a short gain envelope.
  // type      – 'sine' | 'square' | 'triangle' | 'sawtooth'
  // freq      – start frequency (Hz)
  // duration  – seconds
  // gain      – peak gain (0..1)
  // ramp      – optional { to: Hz, delay: seconds } exponential sweep
  // Returns the oscillator (already started) or null.
  function blip(type, freq, duration, gain, ramp, startAt) {
    var c = getCtx();
    if (!c || !master) return null;
    var t0 = (typeof startAt === 'number' ? startAt : c.currentTime);
    try {
      var osc = c.createOscillator();
      var g = c.createGain();
      osc.type = type;
      osc.frequency.setValueAtTime(freq, t0);
      if (ramp && ramp.to) {
        try {
          osc.frequency.exponentialRampToValueAtTime(
            Math.max(1, ramp.to), t0 + (ramp.delay || duration) * 0.9
          );
        } catch (e) {
          osc.frequency.linearRampToValueAtTime(Math.max(1, ramp.to), t0 + duration * 0.9);
        }
      }
      // Click-free attack + decay.
      var peak = Math.max(0.0001, gain);
      g.gain.setValueAtTime(0.0001, t0);
      g.gain.exponentialRampToValueAtTime(peak, t0 + 0.008);
      g.gain.exponentialRampToValueAtTime(0.0001, t0 + duration);
      osc.connect(g);
      g.connect(master);
      osc.start(t0);
      osc.stop(t0 + duration + 0.02);
      // Free the nodes once they have finished so repeated ticks don't leak.
      osc.onended = function () {
        try { osc.disconnect(); } catch (e) {}
        try { g.disconnect(); } catch (e) {}
      };
      return osc;
    } catch (e) {
      return null;
    }
  }

  // Short burst of filtered noise (used by the spin whoosh + dice rattle).
  function noise(duration, gain, startAt) {
    var c = getCtx();
    if (!c || !master) return;
    try {
      var frames = Math.max(1, Math.floor(c.sampleRate * duration));
      var buf = c.createBuffer(1, frames, c.sampleRate);
      var data = buf.getChannelData(0);
      for (var i = 0; i < frames; i++) {
        // Shaped noise: quieter at the edges for a soft, non-clicky burst.
        var env = 1 - Math.abs((i / frames) * 2 - 1);
        data[i] = (Math.random() * 2 - 1) * env;
      }
      var src = c.createBufferSource();
      src.buffer = buf;
      var g = c.createGain();
      g.gain.value = Math.max(0.0001, gain);
      var t0 = (typeof startAt === 'number' ? startAt : c.currentTime);
      try { g.gain.setValueAtTime(0.0001, t0); g.gain.exponentialRampToValueAtTime(Math.max(0.0001, gain), t0 + 0.02); } catch (e) {}
      src.connect(g);
      g.connect(master);
      src.start(t0);
      src.stop(t0 + duration + 0.02);
      src.onended = function () {
        try { src.disconnect(); } catch (e) {}
        try { g.disconnect(); } catch (e) {}
      };
    } catch (e) {}
  }

  // ------------------------------------------------------------------
  // Named sounds — each has a distinct character.
  // ------------------------------------------------------------------
  var players = {
    // Very short click for a wheel passing a peg. Must be cheap: one oscillator.
    tick: function () {
      blip('square', 1200, 0.03, 0.02);
    },

    // Tiny UI click for buttons.
    click: function () {
      blip('triangle', 620, 0.045, 0.05, { to: 320, delay: 0.04 });
    },

    // Bright metal ping for the coin flip.
    coin: function () {
      var c = getCtx();
      if (!c) return;
      var t = c.currentTime;
      blip('triangle', 1320, 0.28, 0.09, null, t);
      blip('sine', 1980, 0.34, 0.06, null, t + 0.01);
      blip('sine', 2640, 0.22, 0.035, null, t + 0.02);
    },

    // A couple of quick knocks for dice.
    dice: function () {
      var c = getCtx();
      if (!c) return;
      var t = c.currentTime;
      blip('square', 180, 0.045, 0.13, { to: 90, delay: 0.04 }, t);
      noise(0.03, 0.05, t);
      blip('square', 160, 0.05, 0.11, { to: 80, delay: 0.045 }, t + 0.09);
      noise(0.03, 0.045, t + 0.09);
      blip('square', 140, 0.05, 0.09, { to: 70, delay: 0.045 }, t + 0.19);
    },

    // Short low buzz for "no" / lose outcomes.
    fail: function () {
      var c = getCtx();
      if (!c) return;
      var t = c.currentTime;
      blip('sawtooth', 150, 0.32, 0.09, { to: 95, delay: 0.3 }, t);
      blip('square', 75, 0.32, 0.05, null, t);
    },

    // Short rising 3-note arpeggio (C - E - G) with a little sparkle.
    win: function () {
      var c = getCtx();
      if (!c) return;
      var t = c.currentTime;
      var notes = [523.25, 659.25, 783.99]; // C5, E5, G5
      for (var i = 0; i < notes.length; i++) {
        blip('triangle', notes[i], 0.19, 0.10, null, t + i * 0.10);
      }
      // Sparkle tail.
      blip('sine', 1046.5, 0.30, 0.05, null, t + 0.30);
      blip('sine', 1567.98, 0.26, 0.035, null, t + 0.34);
    }
  };

  // 'spin' is a longer, controllable sound: returns a handle with stop().
  function playSpin(opts) {
    var c = getCtx();
    var handle = { stop: function () {} };
    if (!c || !master) return handle;
    opts = opts || {};
    var duration = Math.max(0.3, Math.min(12, opts.duration || 4));
    try {
      var t0 = c.currentTime;

      // Descending sweep "whoosh".
      var osc = c.createOscillator();
      var og = c.createGain();
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(760, t0);
      osc.frequency.exponentialRampToValueAtTime(190, t0 + duration * 0.85);
      og.gain.setValueAtTime(0.0001, t0);
      og.gain.exponentialRampToValueAtTime(0.035, t0 + 0.15);
      og.gain.exponentialRampToValueAtTime(0.0001, t0 + duration);
      osc.connect(og); og.connect(master);
      osc.start(t0); osc.stop(t0 + duration + 0.05);

      // Soft looping noise bed.
      var frames = Math.max(1, Math.floor(c.sampleRate * duration));
      var buf = c.createBuffer(1, frames, c.sampleRate);
      var data = buf.getChannelData(0);
      for (var i = 0; i < frames; i++) {
        var p = i / frames;
        var env = Math.sin(Math.PI * Math.min(1, p * 3)) * (1 - p * 0.6);
        data[i] = (Math.random() * 2 - 1) * env;
      }
      var src = c.createBufferSource();
      src.buffer = buf;
      var ng = c.createGain();
      ng.gain.value = 0.035;
      try { ng.gain.setValueAtTime(0.0001, t0); ng.gain.exponentialRampToValueAtTime(0.035, t0 + 0.2); } catch (e) {}
      src.connect(ng); ng.connect(master);
      src.start(t0); src.stop(t0 + duration + 0.05);

      var stopped = false;
      handle.stop = function () {
        if (stopped) return;
        stopped = true;
        var now = c.currentTime;
        try { og.gain.cancelScheduledValues(now); og.gain.setValueAtTime(og.gain.value || 0.0001, now); og.gain.exponentialRampToValueAtTime(0.0001, now + 0.08); } catch (e) {}
        try { ng.gain.cancelScheduledValues(now); ng.gain.setValueAtTime(ng.gain.value || 0.0001, now); ng.gain.exponentialRampToValueAtTime(0.0001, now + 0.08); } catch (e) {}
        try { osc.stop(now + 0.1); } catch (e) {}
        try { src.stop(now + 0.1); } catch (e) {}
      };

      osc.onended = function () {
        try { osc.disconnect(); } catch (e) {}
        try { og.disconnect(); } catch (e) {}
      };
      src.onended = function () {
        try { src.disconnect(); } catch (e) {}
        try { ng.disconnect(); } catch (e) {}
      };
    } catch (e) {}
    return handle;
  }

  // ------------------------------------------------------------------
  // Public API
  // ------------------------------------------------------------------
  function play(name, opts) {
    if (!enabled) return null;
    try { resume(); } catch (e) {}
    try {
      if (name === 'spin') return playSpin(opts);
      var fn = players[name];
      if (typeof fn === 'function') { fn(opts); return true; }
    } catch (e) {}
    return null;
  }

  window.WOLSound = {
    play: play,
    setEnabled: setEnabled,
    isEnabled: isEnabled,
    toggle: toggle,
    resume: resume
  };

  // ------------------------------------------------------------------
  // Global mute toggle UI (injected here so only ONE file ships the UI).
  // ------------------------------------------------------------------
  function injectToggle() {
    if (document.getElementById('wol-sound-toggle')) return;
    var reduce = false;
    try { reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) {}

    var btn = document.createElement('button');
    btn.id = 'wol-sound-toggle';
    btn.type = 'button';
    btn.setAttribute('aria-label', 'Toggle sound');

    function style() {
      // Base position bottom-right; shift up when banners are present.
      var bottom = 16;
      try {
        if (document.getElementById('wol-consent-banner')) bottom += 72;
        var pwa = document.querySelector('.wol-pwa-banner');
        if (pwa) bottom += 72;
      } catch (e) {}
      btn.style.cssText =
        'position:fixed;right:16px;bottom:' + bottom + 'px;' +
        'width:44px;height:44px;border-radius:50%;' +
        'border:1px solid rgba(0,0,0,0.12);' +
        'background:rgba(255,255,255,0.92);color:#222;' +
        'font-size:20px;line-height:1;cursor:pointer;' +
        'box-shadow:0 2px 8px rgba(0,0,0,0.18);' +
        'z-index:1040;display:flex;align-items:center;justify-content:center;' +
        'padding:0;transition:' + (reduce ? 'none' : 'transform 0.15s ease, background 0.15s ease') + ';' +
        '-webkit-tap-highlight-color:transparent;';
      if (document.body && document.body.classList.contains('dark-theme')) {
        btn.style.background = 'rgba(40,40,44,0.92)';
        btn.style.color = '#f2f2f2';
        btn.style.borderColor = 'rgba(255,255,255,0.18)';
      }
    }

    function render() {
      var on = isEnabled();
      btn.textContent = on ? '🔊' : '🔇';
      btn.setAttribute('aria-pressed', on ? 'true' : 'false');
      btn.title = on ? 'Sound on' : 'Sound off';
    }

    btn.addEventListener('click', function () {
      toggle();
      render();
      // Play a confirmation blip only when turning sound ON.
      if (isEnabled()) { try { play('click'); } catch (e) {} }
    });
    if (!reduce) {
      btn.addEventListener('mouseenter', function () { btn.style.transform = 'scale(1.08)'; });
      btn.addEventListener('mouseleave', function () { btn.style.transform = 'scale(1)'; });
    }

    style();
    render();
    document.body.appendChild(btn);

    // Re-position after banners appear/disappear (they are injected later).
    var tries = 0;
    var iv = setInterval(function () {
      style();
      if (++tries > 12) clearInterval(iv);
    }, 1000);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectToggle);
  } else {
    injectToggle();
  }

  // Also unlock the context on the first real user gesture (autoplay policy).
  function unlock() { resume(); }
  ['pointerdown', 'keydown', 'touchstart'].forEach(function (evt) {
    try { document.addEventListener(evt, unlock, { once: true, passive: true }); } catch (e) {}
  });
})();
