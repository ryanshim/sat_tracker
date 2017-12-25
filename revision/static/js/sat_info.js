// Provides orbit information outside of map.
//

var tle_line1 = "";
var tle_line2 = "";

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
    var latitude = rad2deg(positionGd.latitude);
    var longitude = rad2deg(positionGd.longitude);

    if (longitude < 180) {  // for map degree conversion
        longitude += 360;
    }
    if (longitude > 180) {
        longitude -= 360;
    }

    return [positionEci, velocityEci, latitude, longitude, height];
}

function get_orbit_stats(tle) {
    var tle_raw = this.retrieve_tle(tle);

    var stats = this.calc_orbit(tle_raw);

    var html_left = "<h5>GEODETIC</h5>" + "\n" +
                    "<p>INT'L DESIGNATOR: " + tle[0] + "<br>" + 
                    "LATITUDE: " + stats[2] + "<br>" + 
                    "LONGITUDE: " + stats[3] + "</p>" +
                    "<h5>STATE VECTORS</h5>" + 
                    "X: " + stats[0].x + "<br>" + 
                    "Y: " + stats[0].y + "<br>" +
                    "Z: " + stats[0].z + "</p>"; 

    document.getElementById("orbit-info-left").innerHTML += html_left;
}
