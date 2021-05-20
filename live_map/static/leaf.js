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

// adding markers for the bus stations
var marker1 = L.marker([41.3268305,19.8205273]).addTo(map);

// var marker2 = L.marker([lon,lat]).addTo(map);
// var marker3 = L.marker([41.3368305,19.8305273]).addTo(map);

// LoRA network coverage

var circle = L.circle([41.3268305,19.8205273], {
  color: 'red',
  fillColor: '#f03',
  fillOpacity: 0.5,
  radius: 3
}).addTo(map);


// Geojson feature


// Simulation of live buses
