'''
Calculates the azimuth and elevation relative to the observer
Plots object position relative to ECEF

Observer can be set with LLA

Utilizes pyephem and sgp4 packages to calculate object position

TODO:
    - Use space-track api to collect TLE data
    - Make azimuth elevation program
    - Make plotting program
    - Sanitize position data:
        - retrive data from get_SV
        - convert data list
        - send list to plot_body
    - Make cli-menu
    - convert snake_case to camelCase
'''
import ephem
import datetime
import time
import numpy as np
from state_vectors import get_SV
from spaceTrackScrape import getTleData
from azimuthElevation import getAzEl
from plot_position import plot_body

def main():
    # Start the menu
    menu = "1 = Scrape data from Space-Track\n \
            2 = Get observer azimuth and elevation\n \
            3 = Plot object orbit (ECEF)\n \
            4 = Exit program\n \
            "
    print menu
    menuInput = raw_input("Enter menu ID: ")

    while menuInput != 4:
        if menuInput == 1:
            getTleData()
            print "TLE data has been saved in 'tle.txt' file"
        elif menuInput == 2:
            timeLength = 0
            timeLength = raw_input("Enter length of time to track (seconds): ")
            getAzEl()
        elif menuInput == 3:
            timeLength = 0
            timeLength = raw_input("Enter length of time to plot (seconds): ")
            plot_body(timeLength)
        elif menuInput == 4:
            print "Exiting..."
        else:
            print "Not a valid menu input"
        menuInput = raw_input("Enter menu ID: ")


if __name__ == '__main__':
    main()
