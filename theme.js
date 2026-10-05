/*!
 * theme.js — multi-theme system for Wheel of List
 * Dependency-free. Applies the stored theme synchronously at parse time to
 * avoid any flash of the wrong theme, and keeps the legacy `dark-theme`
 * class in sync for backward compatibility.
 */
(function () {
  "use strict";

  var STORAGE_KEY = "wheeloflist_theme";

  // Ordered list of themes. `dark: true` themes also get the legacy
  // `dark-theme` body class so any CSS still keyed on it keeps working.
  var THEMES = [
    { id: "light",    name: "Light",           dark: false },
    { id: "dark",     name: "Night",           dark: true  },
    { id: "neon",     name: "Neon Cyberpunk",  dark: true  },
    { id: "ocean",    name: "Deep Ocean",      dark: true  },
    { id: "sunset",   name: "Sunset",          dark: false },
    { id: "forest",   name: "Forest",          dark: true  },
    { id: "candy",    name: "Candy Pop",       dark: false },
    { id: "retro",    name: "Retro Arcade",    dark: true  },
    { id: "paper",    name: "Paper",           dark: false },
    { id: "midnight", name: "Midnight Blue",   dark: true  }
  ];

  var ids = [];
  var darkMap = {};
  for (var i = 0; i < THEMES.length; i++) {
    ids.push(THEMES[i].id);
    darkMap[THEMES[i].id] = THEMES[i].dark;
  }

  function isValid(id) {
    return Object.prototype.hasOwnProperty.call(darkMap, id);
  }

  function readStored() {
    var raw = null;
    try {
      raw = window.localStorage.getItem(STORAGE_KEY);
    } catch (e) {
      raw = null;
    }
    return isValid(raw) ? raw : "light";
  }

  function applyToBody(id) {
    if (!document.body) return false;
    var classes = document.body.classList;
    // Remove any previously applied theme-* classes.
    for (var i = ids.length - 1; i >= 0; i--) {
      classes.remove("theme-" + ids[i]);
    }
    classes.add("theme-" + id);
    // Legacy compatibility: keep `dark-theme` in sync.
    if (darkMap[id]) {
      classes.add("dark-theme");
    } else {
      classes.remove("dark-theme");
    }
    return true;
  }

  // Capture the body as soon as it exists (works whether this script is in
  // <head> or at the very start of <body>). Parse-time, no flash.
  function apply(id) {
    if (applyToBody(id)) return;
    // Body not yet parsed: retry as soon as possible.
    var observer = null;
    var done = false;
    var finish = function () {
      if (done) return;
      done = true;
      if (observer) { try { observer.disconnect(); } catch (e) {} }
      applyToBody(readStored());
    };
    if (document.readyState === "loading" && typeof MutationObserver === "function") {
      observer = new MutationObserver(function () {
        if (document.body) finish();
      });
      observer.observe(document.documentElement || document, { childList: true, subtree: true });
    }
    if (document.addEventListener) {
      document.addEventListener("DOMContentLoaded", finish, { once: true });
    }
  }

  function set(id) {
    if (!isValid(id)) id = "light";
    try {
      window.localStorage.setItem(STORAGE_KEY, id);
    } catch (e) {}
    apply(id);
    try {
      window.dispatchEvent(new CustomEvent("wol:theme", { detail: { theme: id } }));
    } catch (e) {
      // CustomEvent unsupported / very old browser: best-effort fallback.
      try {
        var ev = document.createEvent("CustomEvent");
        ev.initCustomEvent("wol:theme", true, true, { theme: id });
        window.dispatchEvent(ev);
      } catch (e2) {}
    }
  }

  window.WOLTheme = {
    list: THEMES.slice(),
    get: readStored,
    set: set
  };

  // Apply immediately at parse time (no flash).
  apply(readStored());
})();
