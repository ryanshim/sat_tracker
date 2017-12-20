# Satellite Class
# Currently return the longitude and latitude of selected object
import ephem
import datetime
import time
import numpy as np

class Sat:
    def __init__(self, itlDesig, line1, line2):
        self.itlDesig = itlDesig
        self.line1 = line1
        self.line2 = line2

    # Returns the class attributes as a list
    def get_satrec(self):
        return [self.itlDesig, self.line1, self.line2]

    # Returns the object's current latitudinal and longitudinal coordinates
    def get_position(self):
        sat = ephem.readtle(self.itlDesig, self.line1, self.line2)
        sat.compute()   # date ommitted; uses now()
        latitude = np.degrees(sat.sublat)
        longitude = np.degrees(sat.sublong)
        return latitude, longitude
