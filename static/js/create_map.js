// Create a map in D3
var w = "1000";
var h = "700";

// Append svg object into map-container & init attributes
var svg = d3.select("#map-container").append("svg")
    .attr("width", w)
    .attr("height", h);

// Init a map projection
var projection = d3.geoEquirectangular();
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

// Draw continents on svg
var url = "/static/data/world-110m.geojson";
d3.json(url, function(err, geojson) {
    svg.append("path").attr("d", path(geojson));

    // Draw graticules
    svg.append("path")
        .datum(graticule)
        .attr("class", "graticule")
        .attr("d", path);

    // Draw orbit path
    // TODO: Need to draw the path as a line rather than points
    path_positions = sat_obj.calc_path();
    svg.selectAll("rect")
        .data(path_positions).enter()
        .append("rect")
        .attr("x", function (d) { return projection(d)[0]; })
        .attr("y", function (d) { return projection(d)[1]; })
        .attr("width", 5)
        .attr("height", 5)
        .attr("stroke", "yellow")

});

// Crude way of updating the circle position.
setInterval(function() {
    // Prepare satellite position data to plot
    var sat_pos_data = sat_obj.calc_position();
    var sat_lon_lat = [sat_pos_data[3], sat_pos_data[2]];   // should be passed into d3
                                                            // as [lon, lat]
    svg.selectAll("circle").remove();

    svg.selectAll("circle")
        .data([sat_lon_lat]).enter()
        .append("circle")
        .attr("cx", function (d) { return projection(d)[0]; })
        .attr("cy", function (d) { return projection(d)[1]; })
        .attr("r", "6px")
        .attr("fill", "red")

}, 2000);
