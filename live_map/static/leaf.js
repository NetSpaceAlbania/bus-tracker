// tile layer for the map

var map = L.map('map').setView([41.3268505,19.8205273], 13);
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
attribution: '© <a href="https://www.mapbox.com/about/maps/">Mapbox</a> © <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> <strong><a href="https://www.mapbox.com/map-feedback/" target="_blank">Improve this map</a></strong>',
tileSize: 512,
maxZoom: 18,
zoomOffset: -1,
id: 'mapbox/streets-v11',
accessToken: 'pk.eyJ1IjoiaGFja2Vyc3BhY2VhbGJhbmlhIiwiYSI6ImNrb2E3dHczazAzeDIycG9kY2EyMjV1dncifQ.LnFZVoR69jnFIIZImLZOmw'
}).addTo(map);


// adding markers for the bus stations

var busIcon = L.icon({
    iconUrl: '/static/bus.png',
    iconSize:     [38, 39], // size of the icon
    iconAnchor:   [22, 94], // point of the icon which will correspond to marker's location
    popupAnchor:  [-3, -76] // point from which the popup should open relative to the iconAnchor
});

// todo: parse bus coordinates, read latlon and then feed them to the marker
L.marker([41.306576, 19.796567], {icon: busIcon}).addTo(map);

var busStop = L.icon({
    iconUrl: '/static/busstop.png',
    iconSize:     [39, 43], // size of the icon
    iconAnchor:   [22, 94], // point of the icon which will correspond to marker's location
    popupAnchor:  [-3, -76] // point from which the popup should open relative to the iconAnchor
});

// todo: parse coordinates from geojson, read latlon and then feed to the marker
L.marker([41.350581, 19.831421], {icon: busStop}).addTo(map);


var busline = L.marker([41.306576, 19.796567]).addTo(map);
stationMarker.bindPopup("Starting station").openPopup();

//var busline2 = L.marker([41.35, 19.83]).addTo(map);
//busline2.bindPopup("End station").openPopup(False);


// Simulation of live buses

linja1 = [];


var source = new EventSource('/topic/TOPICNAME'); //ENTER YOUR TOPICNAME HERE
source.addEventListener('message', function(e){

  console.log('Message');
  obj = JSON.parse(e.data);
  console.log(obj);

  if(obj.busline == '00001') {
    for (var i = 0; i < mapMarkers1.length; i++) {
      mymap.removeLayer(mapMarkers1[i]);
    }
    marker1 = L.marker([obj.latitude, obj.longitude]).addTo(mymap);
    mapMarkers1.push(marker1);
  }


}, false);