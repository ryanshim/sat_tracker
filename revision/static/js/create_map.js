// Create a map in D3
// NOTE: using tutorial code for now
var w = "600";
var h = "400";

var svg = d3.select("#map-container").append("svg")
    .attr("width",w)
    .attr("height",h)

var projection = d3.geoMercator()
    .translate([w / 2, h / 2])
    .scale(w / (2 * Math.PI));

var path = d3.geoPath().projection(projection);

var graticule = d3.geoGraticule().step([10, 10]);

var url = "http://enjalot.github.io/wwsd/data/world/world-110m.geojson";
d3.json(url, function(err, geojson) {

    var lines = svg.selectAll('path.graticule').data([graticule()]);

    lines.enter().append('path').classed('graticule', true);
    lines.attr('d', path);
    lines.exit().remove();


    svg.append("path").attr("d", path(geojson));
});

