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

    var satrec = satellite.twoline2satrec(raw_tle[0], raw_tle[1]);  // init sat record
    var positionAndVelocity = satellite.propagate(satrec, new Date());
    
    console.log(positionAndVelocity);   // state vectors; ECEF

    var positionEci = positionAndVelocity.position;
    var gmst = satellite.gstimeFromDate(new Date());    // readme uses fn:gstime()

    var positionGd = satellite.eciToGeodetic(positionEci, gmst);

    // positionGd.lat/lon returns in rads
    var latitude = rad2deg(positionGd.latitude);
    var longitude = rad2deg(positionGd.longitude);

    console.log(latitude);
    console.log(longitude);

    // Map settings
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
            "color": "#000000"
        } ]
      },

      "areasSettings": {
        "autoZoom": true,
        "selectedColor": "#CC0000"
      },

      "smallMap": {}
    } );
}

