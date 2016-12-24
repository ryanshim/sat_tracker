'''
Calculates the azimuth and elevation relative to the observer
Plots object position relative to ECEF

Observer can be set with LLA

Utilizes pyephem and sgp4 packages to calculate object position

TODO:
    - Use space-track api to collect TLE data
    - Sanitize position data:
        - retrive data from get_SV
        - convert data list
        - send list to plot_body
    - Plot position data
'''
import ephem
import datetime
import time
import numpy as np
import plot_position
from state_vectors import get_SV

def main():
    # read TLE data from file
    with open('tle.txt', 'r') as inFile:
        name = inFile.readline()
        line1 = inFile.readline()
        line2 = inFile.readline()

    # set observer position
    obs = ephem.Observer()
    obs.lat = np.radians(33.66946)
    obs.long = np.radians(-117.82311)
    obs.elev = 26.78 # meters

    iss = ephem.readtle(name, line1, line2)

    '''
    # calculate observer view direction
    count = 0
    while count < 1000:
        obs.date = datetime.datetime.utcnow() 
        iss.compute(obs)
        print 'TIME: %s  AZ: %f  EL: %f\n' % \
                (obs.date, np.degrees(iss.az), np.degrees(iss.alt))
        count += 1
        time.sleep(5)
    '''

    # get positions for given time
    print "Retrieving body positions..."
    posData = []
    timeLength = 300 
    count = 1
    while count <= timeLength: 
        r_cur = get_SV(line1, line2)
        print "Count:", count, " Data: ", r_cur
        posData.append(list(r_cur))
        time.sleep(1)
        count += 1

    # plot positions on graph
    plot_position.plot_body(posData)

if __name__ == '__main__':
    main()
