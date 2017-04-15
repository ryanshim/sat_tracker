'''
Calculates the azimuth and elevation relative to the observer
Plots object position relative to ECEF

Observer can be set with LLA

Utilizes pyephem and sgp4 packages to calculate object position

TODO:
    + Use space-track api to collect TLE data                               OK
    + Record historical orbit path
    + Create animated plot of current position (miller projection)
        - Closing graph does not close out of animate loop
    + Create a prediction function 
    + Make cli menu                                                         OK
    + convert snake_case to camelCase
'''
from satellite import Satellite
from state_vectors import get_SV
from spaceTrackScrape import getTleData, parseTleData
from azimuthElevation import getAzEl
from plot_position import plot_body
from animateTrack import plotMillerProj

def main():
    satList = []

    menu =  "1 = Scrape data from Space-Track\n" + \
            "2 = Get observer azimuth and elevation\n" + \
            "3 = Plot object orbit (ECEF)\n" + \
            "4 = Plot object current position (Miller Projection)\n" + \
            "5 = Exit program\n"
            
    print menu
    menuInput = input("Enter menu ID: ")

    # main loop
    while menuInput != 5:
        if menuInput == 1:
            getTleData()
            print "TLE data has been saved in 'tle.txt' file"
            satList = parseTleData()

        elif menuInput == 2:
            #timeLength = 0
            #timeLength = input("Enter length of time to track (seconds): ")
            #getAzEl(timeLength)
            '''
            with open('tle.txt', 'r') as inFile:
                l1 = inFile.readline()
                l2 = inFile.readline()
                satNum = l1[9:16]
            print satNum
            sat = Satellite(satNum, l1, l2)
            sat.getAzEl()
            '''
            if not satList:
                print "Satellites not populated yet. Run menu option 1 first.\n"
            else:
                satList[0].getAzEl()

        elif menuInput == 3:
            timeLength = 0
            timeLength = input("Enter length of time to plot (seconds): ")
            plot_body(timeLength)
        elif menuInput == 4:
            print "Plotting current position..."
            plotMillerProj()
            continue
        else:
            print "Not a valid menu input"
        menuInput = input("Enter menu ID: ")

    print "Exiting..."

if __name__ == '__main__':
    main()
