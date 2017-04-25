'''
Calculates the azimuth and elevation relative to the observer
Plots object position using longitudinal, latitudinal coordinates
State Vectors provided on plot

Observer can be set with LLA

Utilizes pyephem and sgp4 packages to calculate object position

TODO:
    + Use space-track api to collect TLE data                               OK
    + Create animated plot of current position (miller projection)          OK
        + Create a prediction function to show on miller projection         OK
        + Create a legend to show current LLA, State Vectors, & velocity
    + Make cli menu                                                         OK
    + convert snake_case to camelCase                                       OK
'''
from satellite import Satellite
from spaceTrackScrape import getTleData, parseTleData
from animateTrack import plotMillerProj

def main():
    satDict = {}    # empty dictionary to be populated w/ sat objects

    menu =  "1 = Scrape data from Space-Track\n" + \
            "2 = Get observer azimuth and elevation\n" + \
            "3 = Plot object current position (Miller Projection)\n" + \
            "4 = Exit program\n"
    print menu

    try:
        menuInput = int(raw_input("Enter menu ID\n>>> "))
    except ValueError:
        print "Input must be an integer\n"
        menuInput = int(raw_input("Enter menu ID\n>>> "))

    # main loop
    while menuInput != 4:
        if menuInput == 1:
            getTleData()
            print "TLE data has been saved in 'tle.txt' file\n"
            satDict = parseTleData()

        elif menuInput == 2:
            satDict = parseTleData()
            if not satDict:
                print "Satellites not populated yet. Run menu option 1 first.\n"
            else:
                satDictKey = raw_input("Enter satellite int'l designator" \
                        " (FORMAT EX: 98067A)\n>>> ")
                try:
                    satDict[satDictKey].getAzEl()
                except LookupError:
                    print "Invalid key. Input correct key.\n" 

        elif menuInput == 3:
            satDict = parseTleData()
            satDictKey = raw_input("Enter satellite int'l designator" \
                    " (FORMAT EX: 98067A)\n>>> ")
            try:
                print "Plotting current position..."
                plotMillerProj(satDict[satDictKey])
            except LookupError:
                print "Invalid key. Input correct key.\n" 

        else:
            print "Not a valid menu input"

        try:
            menuInput = int(raw_input("Enter menu ID\n>>> "))
        except ValueError:
            print "Input must be an integer\n"
            menuInput = int(raw_input("Enter menu ID\n>>> "))

    print "Exiting..."

if __name__ == '__main__':
    main()
