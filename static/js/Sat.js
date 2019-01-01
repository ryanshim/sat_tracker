// Satellite class to be instantiated when Flask passes tle arguments
class Satellite {
    constructor(line1, line2) {
        this.line1 = line1;
        this.line2 = line2;
        this.position_data = []
    }

    // Calculate orbit for the satellite
    calc_position() {
        var satrec = satellite.twoline2satrec(this.line1, this.line2);
        var position_velocity = satellite.propagate(satrec, new Date());

        // State vectors; Earth-centered inertial (ECI) coordinates
        var positionEci = position_velocity.position;
        var velocityEci = position_velocity.velocity;

        // Calc latitude/longitude
        var time = new Date();
        var gmst = satellite.gstimeFromDate(time);
        var positionGd = satellite.eciToGeodetic(positionEci, gmst);
        var height = positionGd.height;
        var latitude = this.rad2deg(positionGd.latitude);
        var longitude = this.rad2deg(positionGd.longitude);

        // For map degree conversion
        if (longitude < 180) {
            longitude += 360;
        }
        else if (longitude > 180) {
            longitude -= 360;
        }

        this.position_data = [positionEci, velocityEci, latitude, longitude, height];
        return this.position_data;
    }
    
    /* 
     * Calculate range of positions for path plotting
     * This function will only be called once when the document is ready.
     * TODO: Refactor this function to call calc_position() function. Need to 
     * refactor calc_position() to determine if date will be provided.
     */
    calc_path() {
        var path_points = []
        // get a range of dates
        var now = new Date();
        var date_range = [];
        for (var i = -60; i < 60; i += 2) {
            date_range.push(new Date(now.getTime() + i*60000));
        }

        for (var i = 0; i < date_range.length; i++) {
            var satrec = satellite.twoline2satrec(this.line1, this.line2);
            //var position_velocity = satellite.propagate(satrec, new Date());
            var position_velocity = satellite.propagate(satrec, date_range[i]);

            // State vectors; Earth-centered inertial (ECI) coordinates
            var positionEci = position_velocity.position;
            var velocityEci = position_velocity.velocity;

            // Calc latitude/longitude
            //var time = new Date();
            var gmst = satellite.gstimeFromDate(date_range[i]);
            var positionGd = satellite.eciToGeodetic(positionEci, gmst);
            var height = positionGd.height;
            var latitude = this.rad2deg(positionGd.latitude);
            var longitude = this.rad2deg(positionGd.longitude);

            // For map degree conversion
            if (longitude < 180) {
                longitude += 360;
            }
            else if (longitude > 180) {
                longitude -= 360;
            }
            path_points.push([longitude, latitude]);
        }
        return path_points;
    }

    // Radians to degrees conversion
    rad2deg(x) {
        return x * 180 / Math.PI;
    }
}
