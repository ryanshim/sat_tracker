// Provides orbit information outside of map.

let tle_line1 = "";
let tle_line2 = "";

function rad2deg(x) {
    return x * 180 / Math.PI;
}

function retrieve_tle(tle_data) {
    tle_line1 = tle_data[1];
    tle_line2 = tle_data[2];
    return [tle_line1, tle_line2];
}

function calc_orbit(tle_data) {
    var satrec = satellite.twoline2satrec(tle_data[0], tle_data[1]);
    var position_velocity = satellite.propagate(satrec, new Date());

    // calcaulte state vectors; earth-centered inertial (ECI) coordinates
    var positionEci = position_velocity.position;
    var velocityEci = position_velocity.velocity;

    // calculate latitude/longitude
    var time = new Date();
    var gmst = satellite.gstimeFromDate(time);
    var positionGd = satellite.eciToGeodetic(positionEci, gmst);
    var height = positionGd.height;
    var latitude = this.rad2deg(positionGd.latitude);
    var longitude = this.rad2deg(positionGd.longitude);

    if (longitude < 180) {  // for map degree conversion
        longitude += 360;
    }
    if (longitude > 180) {
        longitude -= 360;
    }

    return [positionEci, velocityEci, latitude, longitude, height];
}

function get_orbit_stats_left(tle) {

    setInterval(function() {
        document.getElementById("orbit-info-left").innerHTML = "";
        var tle_raw = this.retrieve_tle(tle);
        var stats = this.calc_orbit(tle_raw);
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

        var tle_raw = this.retrieve_tle(tle);
        var stats = this.calc_orbit(tle_raw);

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
