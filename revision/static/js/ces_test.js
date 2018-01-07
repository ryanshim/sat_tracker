// Plot position of sat on cesium map

// Conversion functions
function deg2rad(degrees) {
    return degrees * (Math.PI / 180);
}

function rad2deg(rads) {
    return rads * (180 / Math.PI);
}

function get_tle(tle_data) {
    tle_line1 = tle_data[1];
    tle_line2 = tle_data[2];
    return [tle_line1, tle_line2];
}

function plot_all(positions) {
    // create new cesium globe
    var viewer = new Cesium.Viewer('cesiumContainer', {
        animation: false,
        timeline: false
    });
    
    var points = viewer.scene.primitives.add(new Cesium.PointPrimitiveCollection());

    // args format: fromDegrees(longitude, latitude, height)
    for (var i = 0; i < positions.length; i++) {
        points.add({
            position: Cesium.Cartesian3.fromDegrees(positions[i][1], positions[i][0], positions[i][2]),
            pixelSize: 2.0,
            color: Cesium.Color.CYAN
        });
    }
}
