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
var marker1 = L.marker([41.3268505,19.8205273]).addTo(map);


// Simulation of live buses

mapMarkers1 = [];


var source = new EventSource('/topic/TOPICNAME'); //ENTER YOUR TOPICNAME HERE
source.addEventListener('message', function(e){

  console.log('Message');
  obj = JSON.parse(e.data);
  console.log(obj);

  if(obj.busline == '00001') {
    for (var i = 0; i < mapMarkers1.length; i++) {
      map.removeLayer(mapMarkers1[i]);
    }
    marker1 = L.marker([obj.latitude, obj.longitude]).addTo(map);
    mapMarkers1.push(marker1);
  }


}, false);
