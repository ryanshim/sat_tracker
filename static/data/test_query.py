import sqlite3

conn = sqlite3.connect('tle.db')
c = conn.cursor()

for row in c.execute("SELECT * FROM tles WHERE itl_desig='98067A'"):
    print(row)

for row in c.execute("SELECT * FROM tles WHERE itl_desig=''"):
    print(row)
conn.close()
