// Plot position of sat on cesium map
function plot_all(positions) {
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
            position: Cesium.Cartesian3.fromDegrees(positions[i][1], positions[i][0], positions[i][2]),
            pixelSize: 1.5,
            color: Cesium.Color.CYAN.withAlpha(0.5)
        });
    }
}
