'''
Satellite class: creates Satellite object when instantiated
    Member variables:
        satNum
        line1
        line2
    Member functions:
        getAzEl
'''
import sys
import select
import ephem
import datetime
import time 
import numpy as np

class Satellite:
    def __init__(self, itlDesig, line1, line2):
        self.itlDesig = itlDesig 
        self.line1 = line1 
        self.line2 = line2 

    def printSatelliteInfo(self):
        print self.itlDesig, " ", self.line1, " ", self.line2

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






