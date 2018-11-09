// Calculate state vectors at t_o
function calc_sv(tle) {
    // Declare constants
    var std_grav = 3.986004418e14;    

    // Extract orbital elements
    var inclination = tle[2].substring(9,17);   // deg
    var right_ascen = tle[2].substring(18,26);  // deg
    var eccentricity = tle[2].substring(26,34); // decimal pt assumed
    var arg_perigee = tle[2].substring(34,43);  // deg
    var mean_anomaly = tle[2].substring(43,52); // deg
    var mean_motion = tle[2].substring(52,63);  // rev/day

    // Calc semi-major axis, a (m)
    mean_motion = mean_motion * (2 * Math.PI / 86400);
    var a = (Math.pow(std_grav, (1/3))) / (Math.pow(mean_motion, (2/3)));

    // Calc eccentric anomaly, EA using Newton's method
    eccentricity = Number('0.' + eccentricity);


}

// Plot position of sat on cesium map
//  - Test plotting ISS orbit path
function plot_all(positions, iss_data) {
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

    calc_sv(iss_data);

    // Add ISS path
    /*
    var polylines = viewer.scene.primitives.add(new Cesium.PolylineCollection());
    polylines.add({
        show: true,
        positions: Cesium.Cartesian3.fromDegreesArrayHeights(iss_positions),
        color: Cesium.Color.RED.withAlpha(0.5),
        width: 2 
    });
    */
}

