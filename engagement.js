/**
 * Privacy-safe engagement events for Wheel Of List.
 *
 * Events are sent only after the existing cookie consent has been accepted.
 * This helper accepts a small allowlist of categorical/numeric parameters and
 * never reads or transmits wheel entries, winners, free text or saved names.
 */
(function () {
  'use strict';

  var CONSENT_KEY = 'wol_consent_v1';
  var MEASUREMENT_ID = 'G-XV614N2RLR';
  var EVENT_PARAMS = {
    wheel_spin_start: ['item_count'],
    wheel_result: ['item_count', 'remaining_count'],
    wheel_items_update: ['item_count'],
    wheel_save: ['item_count'],
    wheel_share: ['method'],
    wheel_image_download: [],
    theme_change: ['theme'],
    tool_navigation: ['tool', 'source'],
    template_open: ['template', 'source'],
    tool_action: ['tool', 'action']
  };
  var NUMERIC_PARAMS = { item_count: true, remaining_count: true };
  var CATEGORY_PATTERN = /^[a-z0-9_-]{1,40}$/;

  function hasConsent() {
    try { return !!localStorage.getItem(CONSENT_KEY); } catch (e) { return false; }
  }

  function safeParams(eventName, params) {
    var output = { send_to: MEASUREMENT_ID };
    var allowed = EVENT_PARAMS[eventName] || [];
    params = params || {};
    allowed.forEach(function (key) {
      var value = params[key];
      if (NUMERIC_PARAMS[key]) {
        var number = Number(value);
        if (Number.isFinite(number)) output[key] = Math.max(0, Math.min(10000, Math.round(number)));
        return;
      }
      value = String(value || '').toLowerCase();
      if (CATEGORY_PATTERN.test(value)) output[key] = value;
    });
    return output;
  }

  function track(eventName, params) {
    if (!Object.prototype.hasOwnProperty.call(EVENT_PARAMS, eventName)) return false;
    if (!hasConsent() || typeof window.gtag !== 'function') return false;
    try {
      window.gtag('event', eventName, safeParams(eventName, params));
      return true;
    } catch (e) {
      return false;
    }
  }

  window.wolAnalytics = { track: track, hasConsent: hasConsent };

  var TOOL_PATHS = {
    '/': 'wheel',
    '/coin-flip/': 'coin_flip',
    '/random-number/': 'random_number',
    '/dice-roller/': 'dice_roller',
    '/yes-no-wheel/': 'yes_no_wheel',
    '/team-generator/': 'team_generator',
    '/random-letter/': 'random_letter',
    '/raffle-picker/': 'raffle_picker',
    '/tournament/': 'tournament',
    '/tools/': 'tools_hub',
    '/wheels/': 'wheel_templates'
  };
  var TOOL_ACTIONS = {
    'flip-btn': 'flip',
    'reset-stats': 'reset_stats',
    'generate-btn': 'generate',
    'clear-history-btn': 'clear_history',
    'roll-btn': 'roll',
    'clear-history-dice': 'clear_history',
    'spin-btn': 'spin',
    'tg-generate': 'generate_teams',
    'tg-reshuffle': 'reshuffle',
    'tg-copy': 'copy',
    'rl-generate': 'generate_letter',
    'rl-clear': 'clear_history',
    'rp-draw': 'draw',
    'rp-copy': 'copy',
    'tb-create': 'create_bracket',
    'tb-randall': 'randomize_remaining',
    'tb-copy': 'copy',
    'tb-new': 'new_bracket',
    'ww-spin': 'spin',
    'ww-reset': 'reset'
  };

  function sourceFor(element) {
    if (element.closest('.tool-card')) return 'card';
    if (element.closest('.dropdown-menu')) return 'menu';
    if (element.closest('footer')) return 'footer';
    return 'navigation';
  }

  function toolForCurrentPath() {
    return TOOL_PATHS[window.location.pathname] ||
      (window.location.pathname.indexOf('/wheels/') === 0 ? 'wheel_template' : 'unknown');
  }

  document.addEventListener('click', function (event) {
    var button = event.target.closest('button[id]');
    if (button && TOOL_ACTIONS[button.id]) {
      track('tool_action', { tool: toolForCurrentPath(), action: TOOL_ACTIONS[button.id] });
    }

    var link = event.target.closest('a[href]');
    if (!link) return;
    var url;
    try { url = new URL(link.href, window.location.href); } catch (e) { return; }
    if (url.origin !== window.location.origin) return;
    var templateMatch = url.pathname.match(/^\/wheels\/([a-z0-9-]+)\/$/);
    if (templateMatch) {
      track('template_open', { template: templateMatch[1].replace(/-/g, '_'), source: sourceFor(link) });
    } else if (TOOL_PATHS[url.pathname]) {
      track('tool_navigation', { tool: TOOL_PATHS[url.pathname], source: sourceFor(link) });
    }
  });
})();
