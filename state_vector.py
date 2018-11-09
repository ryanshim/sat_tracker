import math
import numpy as np

def calc_sv(l1, l2):
    # Declare constants
    std_grav = 3.986004418e14

    # Extract orbital elements
    inclination = tle[2][9:17]      # deg
    right_ascen = tle[2][18:26]     # deg
    eccentricity = tle[2][26:34]    # decimal pt assumed
    arg_perigee = tle[2][34:43]     # deg
    mean_anomaly = tle[2][43:52]    # deg
    mean_motion = tle[2][52:63]     # rev/day

    # Calc semi-major axis, a in meters
    mean_motion = mean_motion * (2 * np.pi / 86400)
    a = (math.pow(std_grav, (1/3))) / (math.pow(mean_motion, (2/3)))

    # Calc eccentric anomaly, EA using Newton's method
