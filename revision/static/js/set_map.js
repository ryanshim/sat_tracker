// In the template file, we first call the get_info() to retrieve the
// variables from Flask. The call to make_map() to create an instance
// of the ammap chart.
//
// The position of the object is currently calculated through the backend
// using PyEphem. Will probably need to migrate to the js library equivalent
// found at: https://github.com/shashwatak/satellite-js

// Variable declarations
var tle_line1 = "";
var tle_line2 = "";
var satrec = "";

// Helper function to retrieve tle data from backend
function get_tle(tle_data) {
    tle_line1 = tle_data[1];
    tle_line2 = tle_data[2];
    return [tle_line1, tle_line2];
}

function get_sat_path(l1, l2) {
    var sat_lat = new Array(8);
    var sat_lon = new Array(8);
    var time = new Date();

    // each time step is 1 min; propagate for 1 hr
    for (i = 0; i < 8; i++) {
        time = new Date(time.setMinutes(time.getMinutes() + i));
        var satrec = satellite.twoline2satrec(l1, l2);
        var position_velocity = satellite.propagate(satrec, time);
        var positionEci = position_velocity.position;
        var gmst = satellite.gstimeFromDate(time);
        var positionGd = satellite.eciToGeodetic(positionEci, gmst);
        var latitude = rad2deg(positionGd.latitude);
        var longitude = rad2deg(positionGd.longitude);

        if (longitude < 180) {  // for map degree conversion
            longitude += 360;
        }
        if (longitude > 180) {
            longitude -= 360;
        }

        sat_lat.push(latitude);
        sat_lon.push(longitude);
    }
    return [sat_lat, sat_lon];
}

// Conversion functions
function deg2rad(degrees) {
    return degrees * (Math.PI / 180);
}

function rad2deg(rads) {
    return rads * (180 / Math.PI);
}

// Creates an instance of an Ammap chart
function make_map(tle) {
    var raw_tle = this.get_tle(tle);
    var itl_desig = raw_tle[0].substring(9, 16);
    var lats_lons = this.get_sat_path(raw_tle[0], raw_tle[1]);

    // process array
    lats_lons[0] = lats_lons[0].slice(8, 16);
    lats_lons[1] = lats_lons[1].slice(8, 16);
    latitude = lats_lons[0][0];
    longitude = lats_lons[1][0];

    console.log(lats_lons);
    console.log(latitude);
    console.log(longitude);

    // Map settings; default projection = mercator
    AmCharts.makeChart( "mapdiv", {
      "type": "map",

      "dataProvider": {
        "map": "worldLow",
        "getAreasFromMap": true,
        "images": [ {
            "title": itl_desig,
            "latitude": latitude,
            "longitude": longitude,
            "type": "circle",
            "color": "#CC0000"
        } ],

        "lines": [ {
            "latitudes": lats_lons[0],
            "longitudes": lats_lons[1],
            "color": "#FFCC00"
        } ]
      },

      "areasSettings": {
        "autoZoom": true,
        "color": "#000000",
        "outlineColor": "#FFFFFF",
        "selectedColor": "#CC0000"
      },

      "smallMap": {}
    } );
}

