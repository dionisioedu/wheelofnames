/* Cookie consent banner for Wheel Of List (shared across pages) */
(function () {
  var KEY = 'wol_consent_v1';
  try {
    if (localStorage.getItem(KEY)) return;
  } catch (e) { return; }

  var bar = document.createElement('div');
  bar.id = 'wol-consent-banner';
  bar.setAttribute('role', 'dialog');
  bar.setAttribute('aria-label', 'Cookie notice');
  bar.innerHTML =
    '<span>We use cookies to analyze traffic and to serve ads via Google AdSense. By using this site you agree to our ' +
    '<a href="/privacy-policy/">Privacy Policy</a>.</span>' +
    '<button id="wol-consent-accept" type="button">Got it</button>';
  document.body.appendChild(bar);

  document.getElementById('wol-consent-accept').addEventListener('click', function () {
    try { localStorage.setItem(KEY, String(Date.now())); } catch (e) {}
    bar.remove();
  });
})();
