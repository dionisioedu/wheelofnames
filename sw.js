/*
 * Minimal service worker for Wheel Of List.
 *
 * Strategy: network-first, cache-fallback.
 *   - On install we precache the app shell ('/' and '/manifest.json').
 *   - Every same-origin GET request is fetched from the network first; the
 *     fresh response is written back into the cache. If the network fails
 *     (offline / flaky connection) we fall back to the cached copy so the
 *     site keeps working offline while always preferring fresh content when
 *     online.
 *
 * A fetch handler is also required for Chrome to consider the app installable
 * and to fire 'beforeinstallprompt'.
 */

var CACHE_NAME = 'wol-cache-v1';
var PRECACHE_URLS = ['/', '/manifest.json'];

self.addEventListener('install', function (event) {
  event.waitUntil(
    caches.open(CACHE_NAME).then(function (cache) {
      return cache.addAll(PRECACHE_URLS);
    }).then(function () {
      return self.skipWaiting();
    })
  );
});

self.addEventListener('activate', function (event) {
  event.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(
        keys.map(function (key) {
          if (key !== CACHE_NAME) return caches.delete(key);
        })
      );
    }).then(function () {
      return self.clients.claim();
    })
  );
});

self.addEventListener('fetch', function (event) {
  var request = event.request;

  // Only handle same-origin GET requests; let everything else pass through.
  if (request.method !== 'GET') return;
  var url = new URL(request.url);
  if (url.origin !== self.location.origin) return;

  event.respondWith(
    fetch(request)
      .then(function (response) {
        // Cache a copy of the fresh response for offline fallback.
        if (response && response.status === 200 && response.type === 'basic') {
          var copy = response.clone();
          caches.open(CACHE_NAME).then(function (cache) {
            cache.put(request, copy);
          });
        }
        return response;
      })
      .catch(function () {
        // Offline: serve the cached copy when we have one.
        return caches.match(request).then(function (cached) {
          return cached || caches.match('/');
        });
      })
  );
});
