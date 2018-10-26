# Print the TLE database for testing
import sqlite3
import ephem
import numpy as np

conn = sqlite3.connect('tle.db')
c = conn.cursor()
count = 0

'''
for row in c.execute('SELECT * FROM tles'):
    print(row)
    count += 1
'''

for row in c.execute("SELECT * FROM tles where itl_desig = '98067A'"):
    print(row)

print(count)

conn.close()

itl_desig = row[0]
line1 = row[1]
line2 = row[2]

'''
sat = ephem.readtle(itl_desig, line1, line2)
sat.compute()
lat = np.degrees(sat.sublat)
lon = np.degrees(sat.sublong)
height = sat.elevation
print(lat, lon, height)
'''
