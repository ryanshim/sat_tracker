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

    // Calculate range of positions for path plotting
    // This function will only be called once when the document is ready
    calc_path() {
        // get a range of dates
        let now = new Date();
        let date_range = [];

        //now.setMinutes(now.getMinutes() + 10);
        let current_minute = now.getMinutes();

        for (var i = 0; i < 10; i++) {
            now.setMinutes(current_minute + 1);
            console.log(now);
            //date_range.push(now);
        }

        console.log(date_range);
    }

    // Radians to degrees conversion
    rad2deg(x) {
        return x * 180 / Math.PI;
    }
}

/*
let l1 = "1 25544U 98067A 18312.66294476 .00003824 00000-0 65431-4 0 9999";
let l2 = "2 25544 51.6413 18.7523 0004902 25.1869 73.9258 15.53933410140984";
iss = new Satellite(l1, l2);
iss.calc_path();
*/
