// tile layer for the map
var map = L.map('mapid').setView([41.3268505,19.8205273], 13);
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
attribution: '© <a href="https://www.mapbox.com/about/maps/">Mapbox</a> © <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> <strong><a href="https://www.mapbox.com/map-feedback/" target="_blank">Improve this map</a></strong>',
tileSize: 512,
maxZoom: 18,
zoomOffset: -1,
id: 'mapbox/streets-v11',
accessToken: 'pk.eyJ1IjoiaGFja2Vyc3BhY2VhbGJhbmlhIiwiYSI6ImNrb2E3dHczazAzeDIycG9kY2EyMjV1dncifQ.LnFZVoR69jnFIIZImLZOmw'
}).addTo(map);

// TODO: leximi i koordinatave bazuar nga ../linja1.geojson

let lat = 41.3268305
let lon = 19.8205273
var marker1 = L.marker([lat,lon]).addTo(map);

// var marker2 = L.marker([lon,lat]).addTo(map);
// var marker3 = L.marker([41.3368305,19.8305273]).addTo(map);

// TODO: perditesimi dhe projektimi i koordinatave ne menyre automatike per nje linje, marker1


// TODO: perditeso per 3 linja, marker1, 2, 3.


// LoRA network coverage
let lora_range = 30
var circle = L.circle([41.3268305,19.8205273], {
  color: 'red',
  fillColor: '#f03',
  fillOpacity: 0.3,
  radius: lora_range
}).addTo(map);


// Repeater network coverage
let repeater_range = 30
var circle = L.circle([41.3268305,19.8205273], {
  color: 'red',
  fillColor: '#f05',
  fillOpacity: 0.5,
  radius: repeater_range
}).addTo(map);


// Geojson feature
