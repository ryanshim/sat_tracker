'''
Plot object's current position over an animated surface
'''
import ephem
import datetime # include for nightshade
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def plotMillerProj(satObject):
    '''
    SET UP THE MAP
    '''
    # miller projection
    plt.figure(figsize=(9,7))
    millsMap = Basemap(projection='mill', lon_0=180)

    # plot coastlines, draw label meridians, parallels, nightshade
    millsMap.drawcoastlines(color='w')
    millsMap.drawparallels(np.arange(-90,90,30), labels=[1,0,0,0])
    millsMap.drawmeridians(np.arange(-180,180,30), labels=[0,0,0,1])
    millsMap.nightshade(datetime.datetime.utcnow(), alpha=0.2) # alpha = transparency lvl

    # fill continents 'black' (with zorder=0), color wet areas 'black'
    # color 'k' = black
    millsMap.drawmapboundary(fill_color='#1a335f')
    millsMap.fillcontinents(color='#111111', lake_color='#1a335f')

    '''
    PLOT OBJECT PATH
    '''
    # satellite object getters
    designator = satObject.getItlDesig()
    line1 = satObject.getLine1()
    line2 = satObject.getLine2()

    # plot propagated coordinates to show object path 
    lonsLats = satObject.propagatePath()
    for data in lonsLats:
        if data[0] < 0:
            data[0] += 360

        x, y = millsMap(data[0], data[1])
        millsMap.plot(x, y, 'y_', markersize=2)[0]

    '''
    PLOT OBJECT CURRENT POSITION + CREATE STATUS BOX 
    '''
    # reset x, y to plot current position
    x, y = millsMap(0,0)
    position = millsMap.plot(x, y, 'ro', markersize=5)[0]

    # create sat info text object
    satInfo = plt.text(0, 0, '', color='w')

    def init():
        satInfo.set_text('')
        position.set_data([], [])
        return position, satInfo

    def animate(i):
        # get object longitude latitude
        sat = ephem.readtle(designator, line1, line2)
        sat.compute()
        lons = np.degrees(sat.sublong)
        lats = np.degrees(sat.sublat)

        satStateVectors = satObject.getSV() # get object state vectors
        velocity = np.sqrt(satStateVectors[1][0]**2 +  # calc velocity magnitude 
                           satStateVectors[1][1]**2 +
                           satStateVectors[1][2]**2)
        
        # update text
        satInfo.set_fontsize(8)
        satInfo.set_text(' Lat: ' + str(lats) +
                         '\n Lon: ' + str(lons) +
                         '\n Velocity: ' + str(velocity) + ' (km/s)' +
                         '\n x: ' + str(satStateVectors[0][0]) +
                         '  y: ' + str(satStateVectors[0][1]) +
                         '  z: ' + str(satStateVectors[0][2]) + '\n')

        # basemap uses 0,0 as bottom left corner of plot
        if lons < 0:
            lons += 360

        x, y = millsMap(lons, lats)
        position.set_data(x, y)

        return position, satInfo

    try:
        # call the animator. blit=True  means to redraw only the 
        # parts that have been changed
        anim = animation.FuncAnimation(plt.gcf(), animate,
                                       init_func=init, frames=20,
                                       interval=500, blit=True)

        # set plot title
        plt.title("Itn'l Designator: " + designator)
        plt.show()
    except KeyboardInterrupt:
        return

