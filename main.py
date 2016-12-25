'''
Calculates the azimuth and elevation relative to the observer
Plots object position relative to ECEF

Observer can be set with LLA

Utilizes pyephem and sgp4 packages to calculate object position

TODO:
    - Use space-track api to collect TLE data
    - Record historical orbit path
    - Create animated plot of current position (miller projection)
    - Create a prediction function 
    - Sanitize position data:
        - retrive data from get_SV
        - convert data list
        - send list to plot_body
    - Make cli-menu
    - convert snake_case to camelCase
'''
from state_vectors import get_SV
from spaceTrackScrape import getTleData
from azimuthElevation import getAzEl
from plot_position import plot_body

def main():
    menu =  '''
            1 = Scrape data from Space-Track\n \
            2 = Get observer azimuth and elevation\n \
            3 = Plot object orbit (ECEF)\n \
            4 = Plot object position (Miller Projection)\n \
            5 = Exit program\n
            '''
    print menu
    menuInput = input("Enter menu ID: ")

    # main loop
    while menuInput != 5:
        if menuInput == 1:
            getTleData()
            print "TLE data has been saved in 'tle.txt' file"
        elif menuInput == 2:
            timeLength = 0
            timeLength = input("Enter length of time to track (seconds): ")
            getAzEl(timeLength)
        elif menuInput == 3:
            timeLength = 0
            timeLength = input("Enter length of time to plot (seconds): ")
            plot_body(timeLength)
        elif menuInput == 4:
            #plotMillerProj()
            continue
        else:
            print "Not a valid menu input"
        menuInput = input("Enter menu ID: ")

    print "Exiting..."

if __name__ == '__main__':
    main()
