
var albmap = L.map('mapid').setView([41.3268505,19.8205273], 13);
 
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
attribution: '© <a href="https://www.mapbox.com/about/maps/">Mapbox</a> © <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> <strong><a href="https://www.mapbox.com/map-feedback/" target="_blank">Improve this map</a></strong>',
tileSize: 512,
maxZoom: 18,
zoomOffset: -1,
id: 'mapbox/streets-v11',
accessToken: 'pk.eyJ1IjoiaGFja2Vyc3BhY2VhbGJhbmlhIiwiYSI6ImNrb2E3dHczazAzeDIycG9kY2EyMjV1dncifQ.LnFZVoR69jnFIIZImLZOmw'
}).addTo(albmap);

// adding markers for the bus stations
var stationMarker = L.marker([41.306576, 19.796567]).addTo(albmap);
stationMarker.bindPopup("First station marker").openPopup();

var stationMarker2 = L.marker([41.350581, 19.831421]).addTo(albmap);
stationMarker2.bindPopup("Last station marker").openPopup();

// adding a standalone popup

var popup = L.popup()
    .setLatLng([41.33, 19.83])
    .setContent("Selitë-Kristal-Qendër-Stacioni i Trenit-Allias")
    .openOn(albmap);

    // Map Events

    var popup = L.popup();

    function onMapClick(e) {
        popup
            .setLatLng(e.latlng)
            .setContent("Koodrinata e zgjedhur eshte: " + e.latlng.toString())
            .openOn(albmap);
    }
    
    albmap.on('click', onMapClick);


// representing a GeoJSON
