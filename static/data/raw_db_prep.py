import sqlite3

conn = sqlite3.connect('raw_tle.db')
c = conn.cursor()

c.execute('''CREATE TABLE raw
                (line1 text, line2 text)''')

conn.commit()
conn.close()

