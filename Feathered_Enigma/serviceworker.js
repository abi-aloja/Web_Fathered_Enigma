

var staticCacheName = "django-pwa-v" + new Date().getTime();
var filesToCache = [

    '/comentarios',
    '/resenas',
    '/principal',
    '/historia',
    '/offline/',
    '/static/inicio/css/fontawesome-all.min.css',
    '/static/inicio/css/main.css',
    '/static/inicio/css/noscript.css',
    '/static/inicio/webfonts/n.otf',
    '/static/inicio/webfonts/font.ttf',
    '/static/inicio/images/01.png',
    "/manifest.json",
];

// Cache on install
self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                return cache.addAll(filesToCache);
            })
    )
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("django-pwa-")))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

self.addEventListener("fetch", function(event){
    event.respondWith(
        fetch(event.request)
        .then(function(result){
            return caches.open(staticCacheName)
            .then(function(c){
                c.put(event.request.url, result.clone())
                return result;
            })  
        })

        .catch(function(e){
            return caches.match(event.request);
        })
    )
})
