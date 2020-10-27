const parsedJson = 'https://group4ds-bucket.s3.amazonaws.com/dataset.json'

// We create the tile layer that will be the background of our map.
let streets = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data © <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery (c) <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    accessToken: API_KEY
})

// Create the map object with center, zoom level and default layer.
let map = L.map('mapid', {
    center: [37.7749, -122.4194],
    zoom: 13,
    layers: [streets],
    preferCanvas: true
})

// Pass our map layers into our layers control and add the layers control to the map.
// L.control.layers(baseMaps).addTo(map);

// Options for our markers
var geojsonMarkerOptions = {
    radius: 2,
    fillColor: "#ff7800",
    color: "#000",
    weight: 1,
    opacity: 1,
    fillOpacity: 0.8
};

function arsonFilter(feature) {
  if (feature.properties.Category === "LARCENY/THEFT") return true
}

// Grabbing our GeoJSON data.
d3.json(parsedJson).then(function (data) {
    console.log(data);
    L.geoJson(data, {
        filter: arsonFilter,
        pointToLayer: function (feature, layer) {
            return L.circleMarker(layer, geojsonMarkerOptions);
        }
    }).addTo(map)

});



// d3.json(dataset).then(function (data) {
//     console.log(data);

//     // Creating a GeoJSON layer with the retrieved data.

//     L.geoJson(data, {
//         onEachFeature: function (feature, layer) {
//             console.log(layer);
//             // layer.bindPopup("<h2> Airport code: " + feature.properties.faa + "</h2> <hr> <h3>" + feature.properties.name + "</h3>");
//         }
//     }).addTo(map)

// });