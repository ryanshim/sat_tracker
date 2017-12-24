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

// Helper function that returns an image object for ammap with the previously
// travelled path, future path, and current position
function get_sat_path(desig, l1, l2) {
    var track_period = 90;  // time to track
    var images = [];
    var sat_lat = [];
    var sat_lon = [];

    for (var i = -track_period; i < track_period; i++) {
        var satrec = satellite.twoline2satrec(l1, l2);
        var time = new Date();
        var position_velocity = satellite.propagate(satrec, new Date(time.setMinutes(time.getMinutes() + i)));
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

    // create images object for ammap plotting 
    for (var j = 0; j < (track_period*2); j++) {
        if (j < track_period) {
            var color = "#00B1A9";  // traveled color
        }
        else {
            var color = "#FFCC00";  // to travel
        }

        images.push( {
            "type": "circle",
            "width": 4,
            "height": 4,
            "color": color,
            "latitude": sat_lat[j],
            "longitude": sat_lon[j]
        });
    }

    images.push( {  // push current position
        "type": "circle",
        "color": "#FF0000",
        "title": desig,
        "latitude": sat_lat[track_period],
        "longitude": sat_lon[track_period]
    });
    
    console.log(sat_lat[track_period]);
    console.log(sat_lon[track_period]);

    return images;
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

    var sat_path = this.get_sat_path(itl_desig, raw_tle[0], raw_tle[1]);

    // Map settings; default projection = mercator
    AmCharts.makeChart( "mapdiv", {
      "type": "map",
      "projection": "equirectangular",

      "dataProvider": {
        "map": "worldLow",
        "getAreasFromMap": true,
        "images": sat_path
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

