// In the template file, we first call the get_info() to retrieve the
// variables from Flask. The call to make_map() to create an instance
// of the ammap chart.
//
// The position of the object is currently calculated through the backend
// using PyEphem. Will probably need to migrate to the js library equivalent
// found at: https://github.com/shashwatak/satellite-js

// Variable declarations
var itl_desig = "test";
var lat = "";
var lon = "";

// Helper function to retrieve data from Flask backend
function get_info(info) {
    itl_desig = info[0];
    lat = info[1];
    lon = info[2];
    console.log(info);
}

// Creates an instance of an Ammap chart
function make_map() {
    AmCharts.makeChart( "mapdiv", {
      "type": "map",

      "dataProvider": {
        "map": "worldLow",
        "getAreasFromMap": true,
        "images": [ {
            "title": itl_desig,
            "latitude": lat,
            "longitude": lon,
            "type": "circle",
            "color": "#000000"
        } ]
      },

      "areasSettings": {
        "autoZoom": true,
        "selectedColor": "#CC0000"
      },

      /**
       * let's say we want a small map to be displayed, so let's create it
       */
      "smallMap": {}
    } );
}

