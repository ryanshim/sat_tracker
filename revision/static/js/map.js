/**
 * js script to provide ammaps map plotting
 */

AmCharts.makeChart( "mapdiv", {
  /**
   * this tells amCharts it's a map
   */
  "type": "map",

  /**
   * create data provider object
   * map property is usually the same as the name of the map file.
   * getAreasFromMap indicates that amMap should read all the areas available
   * in the map data and treat them as they are included in your data provider.
   * in case you don't set it to true, all the areas except listed in data
   * provider will be treated as unlisted.
   */
  "dataProvider": {
    "map": "worldLow",
    "getAreasFromMap": true,
    "images": [
        {
            "type": "circle",
            "label": "Observer",
            "labelColor": "#64FF2E",
            "latitude": 33,
            "longitude": -117
        }
    ]
  },

  /**
   * create areas settings
   * autoZoom set to true means that the map will zoom-in when clicked on the area
   * selectedColor indicates color of the clicked area.
   */
  "areasSettings": {
    "autoZoom": true,
    "color": "#424242",
    "selectedColor": "#D3D3D3"
  },

  /**
   * let's say we want a small map to be displayed, so let's create it
   */
  "smallMap": {}
} );
