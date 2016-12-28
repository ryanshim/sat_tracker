'''
Plot object's current position over an animated surface
'''
import ephem
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def plotMillerProj():

    # miller projection
    millsMap = Basemap(projection='mill', lon_0=180)

    # plot coastlines, draw label meridians and parallels
    millsMap.drawcoastlines()
    millsMap.drawparallels(np.arange(-90,90,30), labels=[1,0,0,0])
    millsMap.drawmeridians(np.arange(-180,180,30), labels=[0,0,0,1])

    # fill continents 'coral' (with zorder=0), color wet areas 'aqua'
    millsMap.drawmapboundary(fill_color='aqua')
    millsMap.fillcontinents(color='coral', lake_color='aqua')

    x, y = millsMap(0,0)
    position = millsMap.plot(x, y, 'ro', markersize=5)[0]


    # read the tle from file
    with open("tle.txt", "r") as inFile:
        name = "ISS (ZARYA)"
        line1 = inFile.readline()
        line2 = inFile.readline()


    def init():
        position.set_data([], [])
        return position,

    def animate(i):
        # compute longitude and latitude
        iss = ephem.readtle(name, line1, line2)
        iss.compute()
        lons = np.degrees(iss.sublong)
        lats = np.degrees(iss.sublat)

        x, y = millsMap(lons, lats)

        position.set_data(x, y)
        return position,

    # call the animator. blit=True  means to redraw only the parts that have been changed
    anim = animation.FuncAnimation(plt.gcf(), animate, init_func=init, frames=20, interval=500, blit=True)

    plt.show()
