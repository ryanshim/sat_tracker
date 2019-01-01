// Provides orbit information outside of map.
// NOTE: use the Sat.js class object instead of hardcoded function calculations
function get_orbit_stats_left(tle) {
    setInterval(function() {
        document.getElementById("orbit-info-left").innerHTML = "";
        var sat_obj = new Satellite(tle[1], tle[2]);
        var stats = sat_obj.calc_position();

        var html_left = "<h5>Geodetic</h5>" + "\n" +
                        "Latitude: " + stats[2].toPrecision(4) + "&deg;<br>" + 
                        "Longitude: " + stats[3].toPrecision(4) + "&deg;<br>" +
                        "Altitude: " + stats[4].toPrecision(4) + " km.</p>"; 
        document.getElementById("orbit-info-left").innerHTML += html_left;
    }, 1000);
}

function get_orbit_stats_right(tle) {
    setInterval(function() {
        document.getElementById("orbit-info-right").innerHTML = "";
        var sat_obj = new Satellite(tle[1], tle[2]);
        var stats = sat_obj.calc_position();

        var html_right_hdr = "<h5>State Vectors</h5>";

        var html_right_1 =  "POSITION:<br>" +
                            "X = " + stats[0].x.toPrecision(4) + " km." + "<br>" +
                            "Y = " + stats[0].y.toPrecision(4) + " km." + "<br>" +
                            "Z = " + stats[0].z.toPrecision(4) + " km.";

        var html_right_2 =  "VELOCITY:<br>" +
                            "V_x = " + stats[1].x.toPrecision(3) + " km/s" + "<br>" +
                            "V_y = " + stats[1].y.toPrecision(3) + " km/s" + "<br>" +
                            "V_z = " + stats[1].z.toPrecision(3) + " km/s";
        var column_open = "<div class='col-sm-4 text-left'>";
        var column_close = "</div>";

        document.getElementById("orbit-info-right").innerHTML += html_right_hdr;
        document.getElementById("orbit-info-right").innerHTML += column_open +
            html_right_1 + column_close;
        document.getElementById("orbit-info-right").innerHTML += column_open +
            html_right_2 + column_close;

    }, 1000);
}

function get_orbital_elements(tle) {
    let html_hdr = "<h5>Keplerian Elements</h5>";
    let tle_elements = "Inclination = " + tle[2].substring(8,17) + "<br>";
    tle_elements += "RA = " + tle[2].substring(18,26) + "<br>";
    tle_elements += "Eccentricity = " + tle[2].substring(27,34) + "<br>";
    tle_elements += "Arg. of perigee = " + tle[2].substring(35,43) + "<br>";
    tle_elements += "Mean anomaly = " + tle[2].substring(44,52) + "<br>";
    tle_elements += "Mean motion = " + tle[2].substring(53,64) + "<br>";

    document.getElementById("orbital-elements").innerHTML = html_hdr;
    document.getElementById("orbital-elements").innerHTML += tle_elements;
}
