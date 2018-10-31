// Create a map in D3
// NOTE: using tutorial code for now
var width = 600;
var height = 400;

var svg = d3.select("#map-container").append("svg");

var projection = d3.geoMercator();

var path = d3.geoPath()
  .projection(projection);

var url = "http://enjalot.github.io/wwsd/data/world/world-110m.geojson";
d3.json(url, function(err, geojson) {
  svg.append("path")
    .attr("d", path(geojson))
})
