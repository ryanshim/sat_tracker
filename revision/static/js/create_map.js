// Create a map in D3
// NOTE: using tutorial code for now
var geojson = {}

var context = d3.select('#map-container canvas')
  .node()
  .getContext('2d');

var projection = d3.geoOrthographic()
  .scale(250);

var geoGenerator = d3.geoPath()
  .projection(projection)
  .pointRadius(4)
  .context(context);

var yaw = 400;

function update() {
  projection.rotate([yaw, -30])

  context.clearRect(0, 0, 800, 600);

  context.lineWidth = 0.5;
  context.strokeStyle = '#fffaa5';

  context.beginPath();
  geoGenerator({type: 'FeatureCollection', features: geojson.features})
  context.stroke();

  // Graticule
  var graticule = d3.geoGraticule();
  context.beginPath();
  context.strokeStyle = '#ccc';
  geoGenerator(graticule());
  context.stroke();

  yaw -= 0.2
}


// REQUEST DATA
d3.json('/static/data/ne_110m_land.json', function(err, json) {
  geojson = json;
  window.setInterval(update, 100);
})

