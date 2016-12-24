'''
Converts longitude/latitude/altitude to
Earth-centered-Earth-fixed state vectors
'''
import datetime 
from sgp4.earth_gravity import wgs72
from sgp4.io import twoline2rv

def get_SV(tle_l1, tle_l2):
    year    = datetime.datetime.utcnow().timetuple().tm_year
    month   = datetime.datetime.utcnow().timetuple().tm_mon
    date    = datetime.datetime.utcnow().timetuple().tm_mday
    hour    = datetime.datetime.utcnow().timetuple().tm_hour
    minute  = datetime.datetime.utcnow().timetuple().tm_min
    second  = datetime.datetime.utcnow().timetuple().tm_sec
 
    satellite = twoline2rv(tle_l1, tle_l2, wgs72)
    position, velocity = satellite.propagate(year, month, date, hour, minute, second)

    return position
