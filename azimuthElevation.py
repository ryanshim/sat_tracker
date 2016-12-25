'''
Get Azimuth and Elevation for user defined time interval

Add user defined long/lat/alt (LLA)
'''
import ephem
import datetime
import time
import numpy as np

def getAzEl(timeInterval):
    # read TLE data from file
    with open('tle.txt', 'r') as inFile:
        name = "ISS (ZARYA)"
        line1 = inFile.readline()
        line2 = inFile.readline()

    # set observer position
    obs = ephem.Observer()
    obs.lat = np.radians(33.66946)
    obs.long = np.radians(-117.82311)
    obs.elev = 26.78 # meters

    # read the tle data
    iss = ephem.readtle(name, line1, line2)

    # calculate observer view direction
    count = 1 
    while count <= timeInterval:
        obs.date = datetime.datetime.utcnow()
        iss.compute(obs)
        print 'TIME: %s  AZ: %f  EL: %f\n' % \
                (obs.date, np.degrees(iss.az), np.degrees(iss.alt))
        count += 1
        time.sleep(1)

