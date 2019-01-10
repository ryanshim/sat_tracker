""" Utility functions to calculate an object's Keplerian orbital elements to
state vectors. Algorithms are from the textbook "Orbital Mechanics for
Engineering Students" by Curtis and "KEPLERIAN Orbit Elements --> Cartesian
State Vectors" by Rene Schwarz
"""
import math
import numpy as np

# CONSTANTS
STDGRAV = 3.986004418e14

def calc_SV(tle):
    """ Returns state vectors given Keplerian elements from TLE.
    :param l1: TLE line 1
    :param l2: TLE line 2
    """
    # Extract orbital elements and convert to radians
    inclination = math.radians(float(tle[1][9:17]))     # rad
    right_ascen = math.radians(float(tle[1][18:26]))    # rad 
    eccentricity = format_eccentricity(tle[1][26:34])   # decimal pt assumed
    arg_perigee = math.radians(float(tle[1][34:43]))    # rad 
    mean_anomaly = math.radians(float(tle[1][43:52]))   # rad 
    mean_motion = float(tle[1][52:63])                  # rev/day


    # Calc semi-major axis, a in meters
    mean_motion = mean_motion * (2 * np.pi / 86400) # convert from rev/day to rad/s
    a = (math.pow(STDGRAV, (1/3))) / (math.pow(mean_motion, (2/3)))

    # Calc mean anomaly
    MA = calc_MA(mean_anomaly, a, 0)
    print("MEAN ANOMALY: {}".format(MA))

    # Calc eccentric anomaly, EA using Newton's method
    EA = calc_EA(eccentricity, MA, 1.0e-8)
    print("ECCENTRIC ANOMALY: {}".format(EA))
    
    # Calc true anomaly
    TA = calc_TA(EA, eccentricity)
    print("TRUE ANOMALY: {}".format(TA))

    # Calc angular momentum
    h = calc_h(eccentricity, a)
    print("ANGULAR MOMENTUM: {}".format(h))

def calc_MA(M_o, a, t_o, t=None):
    """ Return the mean anomaly given a time difference.
    :param M_o: initial mean anomaly (degrees)
    :param a: semi-major axis (meters)
    :param t_o: initial time
    :param t: final time
    """
    if t == None or t == t_o:   # calc for current time
        return M_o

    delta_t = 86400 * (t - t_o) # time difference
    M = M_o + (delta_t * math.sqrt(STDGRAV / math.pow(a, 3)))

    return M
    
def calc_EA(e, M, tol):
    """ Return the eccentric anomaly by solving Kepler's equation using
    Newton's method.
    :param e: eccentricity
    :param M: mean anomaly
    :param tol: error tolerance (i.e. tangent precision)
    """
    # Select a starting value for E
    if M < math.pi:
        E = M + e/2
    else:
        E = M - e/2

    # Iterate on Kepler's equation until E is determined to be within
    # the error tolerance.
    ratio = 1
    while math.fabs(ratio) > tol:
        ratio = (E - e*math.sin(E) - M) / (1 - e*math.cos(E))
        E = E - ratio

    return E

def calc_TA(EA, e):
    """ Return the true anomaly derived from the given eccentric anomaly.
    :param EA: eccentric anomaly
    :param e: eccentricity
    """
    y = math.sqrt(1+e) * math.sin(EA/2)
    x = math.sqrt(1-e) * math.cos(EA/2)

    if x > 0:
        return 2 * math.atan(y/x)
    elif y >= 0 and x < 0:
        return 2 * (math.atan(y/x) + math.pi)
    elif y < 0 and x < 0:
        return 2 * (math.atan(y/x) - math.pi)
    elif y > 0 and x == 0:
        return 2 * (math.pi / 2)
    elif y < 0 and x == 0:
        return 2 * -(math.pi / 2)
    elif y == 0 and x == 0:
        return None
    return None

def calc_h(e, a):
    """ Return the angular momentum given the eccentricity and the semi-major
    axis using the angular momentum equation.
    :param e: eccentricity
    :param a: semi-major axis
    """
    return math.sqrt(STDGRAV * a * (1-math.pow(e, 2)))

def format_eccentricity(e):
    """ Decimal point assumed in TLE after the 0's. Format and convert
    to floating point. Since orbits are elliptical, the eccentricity will
    always be greater than zero but less than one.
    :param e: eccentricity
    """
    e = float(e)
    while e > 1:
        e /= 10
    return e

def calc_vectors():
    """ WIP: Return the position and velocity vectors, r and p, from calculated
    orbital elements. Orbit lies in the perifocal frame and needs to be
    transformed to the geocentric equatorial frame using the calssical Euler
    angle sequence. [R_3(W)][R_1(i)][R_3(w)]
    """
    h = 80000
    e = 1.4
    i = math.radians(30)
    ra = math.radians(40)
    arg_p = math.radians(60)
    ta = math.radians(30)

    # rp unit: km
    rp = (math.pow(h, 2) / 398600) * \
         (1 / (1 + e * math.cos(ta))) * \
         np.matrix([[math.cos(ta)], [math.sin(ta)], [0]])

    # vp unit: km/s
    vp = (398600 / h) * (np.matrix([[-math.sin(ta)],
                                    [e + math.cos(ta)],
                                    [0]]))

    # Euler angle sequence
    R3_W = np.matrix([[math.cos(ra), math.sin(ra), 0],
                      [-math.sin(ra), math.cos(ra), 0],
                      [0, 0, 1]])

    R1_i = np.matrix([[1, 0, 0],
                      [0, math.cos(i), math.sin(i)],
                      [0, -math.sin(i), math.cos(i)]])

    R3_w = np.matrix([[math.cos(arg_p), math.sin(arg_p), 0],
                      [-math.sin(arg_p), math.cos(arg_p), 0],
                      [0, 0, 1]])

    Q_pX = (R3_w * R1_i * R3_W).transpose()

    r = Q_pX * rp
    v = Q_pX * vp
    print(r)
    print(v)


calc_vectors()

# TEST ISS TLE
#line1 = "1 25544U 98067A   19008.04344106  .00001791  00000-0  34727-4 0  9995"
#line2 = "2 25544  51.6421  77.8266 0002386 253.7712 175.9272 15.53746625150376"
#calc_SV([line1, line2])
