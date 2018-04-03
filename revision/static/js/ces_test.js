// Plot position of sat on cesium map
//  - Test plotting ISS orbit path
function plot_all(positions, iss_positions) {
    // create new cesium globe
    var viewer = new Cesium.Viewer('cesiumContainer', {
        animation: false,
        timeline: false,
        skyBox: new Cesium.SkyBox({
            backgroundColor: Cesium.Color.BLACK
        })
    });

    var points = viewer.scene.primitives.add(new Cesium.PointPrimitiveCollection());
    // args format: fromDegrees(longitude, latitude, height)
    for (var i = 0; i < positions.length; i++) {
        points.add({
            position: Cesium.Cartesian3.fromDegrees(positions[i][1],
                              positions[i][0], positions[i][2]),
            pixelSize: 1.5,
            color: Cesium.Color.CYAN.withAlpha(0.5)
        });
    }

    // Add ISS path
    var polylines = viewer.scene.primitives.add(new Cesium.PolylineCollection());
    polylines.add({
        show: true,
        positions: Cesium.Cartesian3.fromDegreesArrayHeights(iss_positions),
        color: Cesium.Color.RED.withAlpha(0.5),
        width: 2 
    });
}
