'''
Plots object's current position over surface
on orthographic projection of Earth
'''
from mpl_toolkits.mplot3d import Axes3D
from state_vectors import get_SV
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.animation as animation

def plot_body(posData):

    # create mpl figure
    fig = plt.figure(figsize=plt.figaspect(1))
    ax = fig.add_subplot(111, projection='3d', aspect=1)

    # plot earth surface
    max_radius = 0
    earth_radius = 6371 # km
    max_radius = max(max_radius, earth_radius)
    coefs = (1, 1, 1)
    rx, ry, rz = [earth_radius/np.sqrt(coef) for coef in coefs]
    u = np.linspace(0, 2*np.pi, 100)
    v = np.linspace(0, np.pi, 100)

    # cartesian coordinates that correspond to spherical angles
    # matrix outer multiplication
    x = rx * np.outer(np.cos(u), np.sin(v))
    y = ry * np.outer(np.sin(u), np.sin(v))
    z = rz * np.outer(np.ones_like(u), np.cos(v))

    # draw Earth
    ax.plot_surface(x, y, z, rstride=4, cstride=4, color='g', antialiased=True)

    # plot positions in recorded file
    '''
    r_cur = get_SV(line1, line2)
    sat_x = r_cur[0]
    sat_y = r_cur[1]
    sat_z = r_cur[2]
    '''
    for data in posData:
        ax.plot([data[0]], [data[1]], [data[2]], 'bo')


    #ax.plot([sat_x], [sat_y], [sat_z], 'bo')

    plt.show()
