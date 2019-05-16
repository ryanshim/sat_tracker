# Create database and table for TLE data
import sqlite3

conn = sqlite3.connect('tle.db')
c = conn.cursor()

c.execute('''CREATE TABLE tles
                (satnum text, line1 text, line2 text)''')

conn.commit()
conn.close() 
