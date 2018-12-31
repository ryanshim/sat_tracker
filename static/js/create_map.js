// Create a map in D3
var arr_tle = retrieve_tle(arr_tle);
var w = "1000";
var h = "700";

// Append svg object into map-container & init attributes
var svg = d3.select("#map-container").append("svg")
    .attr("width", w)
    .attr("height", h);

// Init a map projection
var projection = d3.geoEquirectangular();
    //.translate([w / 2, h / 2])
    //.scale(w / (2 * Math.PI));

var path = d3.geoPath().projection(projection);

// Init map graticules
var graticule = d3.geoGraticule()
    .step([10, 10]);

// Draw map border
svg.append("rect")
    .attr("x", 1)
    .attr("y", 10)
    .attr("height", (h/2) + 131)
    .attr("width", w-40)
    .style("stroke", "white")
    //.style("fill", "none")

// Draw continents on svg
var url = "http://enjalot.github.io/wwsd/data/world/world-110m.geojson";
d3.json(url, function(err, geojson) {
    svg.append("path").attr("d", path(geojson));
});

// Draw graticules
svg.append("path")
    .datum(graticule)
    .attr("class", "graticule")
    .attr("d", path);

// Crude way of updating the circle position.
setInterval(function() {
    // Prepare satellite position data to plot
    let position_data = calc_orbit(arr_tle);
    let sat_pos = [position_data[3], position_data[2]]; // should be passed into d3
                                                        // as [lon,lat]
    svg.selectAll("circle").remove();

    svg.selectAll("circle")
        .data([sat_pos]).enter()
        .append("circle")
        .attr("cx", function (d) { return projection(d)[0]; })
        .attr("cy", function (d) { return projection(d)[1]; })
        .attr("r", "6px")
        .attr("fill", "red")

}, 2000);
