'''
Plot object's current position over an animated surface
'''
import ephem
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def plotMillerProj(satObject):

    # miller projection
    millsMap = Basemap(projection='mill', lon_0=180)

    # plot coastlines, draw label meridians and parallels
    millsMap.drawcoastlines(color='w')
    millsMap.drawparallels(np.arange(-90,90,30), labels=[1,0,0,0])
    millsMap.drawmeridians(np.arange(-180,180,30), labels=[0,0,0,1])

    # fill continents 'black' (with zorder=0), color wet areas 'black'
    # color 'k' = black
    millsMap.drawmapboundary(fill_color='#1a335f')
    millsMap.fillcontinents(color='k', lake_color='k')

    # satellite object getters
    designator = satObject.getItlDesig()
    line1 = satObject.getLine1()
    line2 = satObject.getLine2()

    # map out propogated coordinates 
    lonsLats = satObject.propogate()
    for data in lonsLats:
        if data[0] < 0:
            data[0] += 360

        x, y = millsMap(data[0], data[1])
        # yellow dot
        millsMap.plot(x, y, 'yo', markersize=2)[0]

    # reset x, y to plot current position
    # red dot
    x, y = millsMap(0,0)
    position = millsMap.plot(x, y, 'ro', markersize=5)[0]

    def init():
        position.set_data([], [])
        return position,

    def animate(i):
        sat = ephem.readtle(designator, line1, line2)
        sat.compute()
        lons = np.degrees(sat.sublong)
        lats = np.degrees(sat.sublat)

        # basemap uses 0,0 as bottom left corner of plot
        if lons < 0:
            lons += 360

        x, y = millsMap(lons, lats)

        position.set_data(x, y)
        return position,

    try:
        # call the animator. blit=True  means to redraw only the 
        # parts that have been changed
        anim = animation.FuncAnimation(plt.gcf(), animate,
                                       init_func=init, frames=20,
                                       interval=500, blit=True)

        plt.title(designator)
        plt.show()
    except KeyboardInterrupt:
        return
