'''
Satellite class: creates Satellite object when instantiated
    Member variables:
        satNum
        line1
        line2
    Member functions:
        memberVarGetters
        get_SV (state vectors)
        getAzEl
'''
import ephem
import datetime
import time 
import numpy as np
from sgp4.earth_gravity import wgs72
from sgp4.io import twoline2rv

class Satellite:
    def __init__(self, itlDesig, line1, line2):
        self.itlDesig = itlDesig 
        self.line1 = line1 
        self.line2 = line2 

    def getItlDesig(self):
        return self.itlDesig

    def getLine1(self):
        return self.line1

    def getLine2(self):
        return self.line2

    # computes state vectors of this satellite
    def get_SV(self):
        # get current utc time
        year    = datetime.datetime.utcnow().timetuple().tm_year
        month   = datetime.datetime.utcnow().timetuple().tm_mon
        date    = datetime.datetime.utcnow().timetuple().tm_mday
        hour    = datetime.datetime.utcnow().timetuple().tm_hour
        minute  = datetime.datetime.utcnow().timetuple().tm_min
        second  = datetime.datetime.utcnow().timetuple().tm_sec

        satObject = twoline2rv(self.line1, self.line2, wgs72)   # compute sat object
        position, velocity = satObject.propogate(year, month, date,
                                                 hour, minute, second)

        return position

    # comput+outputs az, el until ctrl+c
    def getAzEl(self):
        obs = ephem.Observer()
        obs.lat = np.radians(input("Enter observer latitude (deg): "))
        obs.long = np.radians(input("Enter observer longitude (deg): "))
        obs.elev = input("Enter observer altitude (meters): ")

        sat = ephem.readtle(self.itlDesig, self.line1, self.line2)

        while True:
            try:
                obs.date = datetime.datetime.utcnow()
                sat.compute(obs)
                print 'TIME: %s  AZ: %f  EL: %f\n' % \
                        (obs.date, np.degrees(sat.az), np.degrees(sat.alt))
                time.sleep(1)
            except KeyboardInterrupt:
                break

