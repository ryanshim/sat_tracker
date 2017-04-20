'''
Plots object's current position over surface
on orthographic projection of Earth
'''
import time
#from state_vectors import get_SV
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

def plotBody(satObject):
    # create mpl figure
    fig = plt.figure(figsize=plt.figaspect(1))
    ax = fig.add_subplot(111, projection='3d', aspect=1)

    # plot earth surface
    maxRadius = 0
    earthRadius = 6371 # km
    maxRadius = max(maxRadius, earthRadius)
    coefs = (1, 1, 1)
    rx, ry, rz = [earthRadius/np.sqrt(coef) for coef in coefs]
    u = np.linspace(0, 2*np.pi, 100)
    v = np.linspace(0, np.pi, 100)

    # cartesian coordinates that correspond to spherical angles
    # matrix outer multiplication
    x = rx * np.outer(np.cos(u), np.sin(v))
    y = ry * np.outer(np.sin(u), np.sin(v))
    z = rz * np.outer(np.ones_like(u), np.cos(v))

    # draw Earth
    ax.plot_surface(x, y, z, rstride=4, cstride=4, color='g', antialiased=True)

    # get satellite data
    designator = satObject.ItlDesig()
    line1 = satObject.getLine1()
    line2 = satObject.getLine2()

    print "Position in state vector format..."
    posData = []
    count = 1
    while count <= timeInterval:
        r_cur = get_SV(line1, line2)
        print "Time +", count, "Seconds :: State Vectors:", r_cur
        posData.append(list(r_cur))
        count += 1
        time.sleep(1)

    for data in posData:
        ax.plot([data[0]], [data[1]], [data[2]], 'bo')
        
    plt.show()
