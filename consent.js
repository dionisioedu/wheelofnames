/* Cookie consent banner for Wheel Of List (shared across pages) */
(function () {
  var KEY = 'wol_consent_v1';
  try {
    if (localStorage.getItem(KEY)) return;
  } catch (e) { return; }

  var bar = document.createElement('div');
  bar.setAttribute('role', 'dialog');
  bar.setAttribute('aria-label', 'Cookie notice');
  bar.style.cssText = 'position:fixed;bottom:0;left:0;right:0;z-index:2000;background:#212529;color:#fff;padding:14px 18px;display:flex;flex-wrap:wrap;gap:12px;align-items:center;justify-content:center;font-size:14px;box-shadow:0 -2px 10px rgba(0,0,0,.3);';
  bar.innerHTML =
    '<span style="max-width:720px;">We use cookies to analyze traffic and to serve ads via Google AdSense. By using this site you agree to our ' +
    '<a href="/privacy-policy/" style="color:#8ab4f8;">Privacy Policy</a>.</span>' +
    '<button id="wol-consent-accept" style="background:#3369e8;color:#fff;border:0;border-radius:6px;padding:8px 22px;font-weight:600;cursor:pointer;">Got it</button>';
  document.body.appendChild(bar);

  document.getElementById('wol-consent-accept').addEventListener('click', function () {
    try { localStorage.setItem(KEY, String(Date.now())); } catch (e) {}
    bar.remove();
  });
})();
