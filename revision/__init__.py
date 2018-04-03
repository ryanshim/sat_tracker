# Satellite Tracker Revision
#
# Revision Notes:
#
import sqlite3
import collections
import json
from flask import Flask, render_template, request, url_for
from .sat import Sat

# for ISS tracking
import ephem
import datetime
import numpy as np

app = Flask(__name__)

# Cesium Globe page
@app.route('/', methods=['GET', 'POST'])
def ces_track():
    iss_positions = []
    positions = []
    error_count = 0

    conn = sqlite3.connect('./static/data/tle.db')
    c = conn.cursor()

    for row in c.execute('SELECT * FROM tles'):
        sat = Sat(row[0], row[1], row[2])
        try:
            lat, lon, height = sat.get_position()
        except:
            error_count += 1
            pass
        positions.append([lat, lon, height])

    # Retrieve ISS tle
    iss_tle = []
    for row in c.execute("SELECT * FROM tles WHERE itl_desig = '98067A  '"):
        iss_tle = row
    
    conn.close()
    print(error_count)

    # Get points to plot ISS path
    base = datetime.datetime.today()
    t_delta = [base - datetime.timedelta(minutes=x) for x in range(-30, 90)]

    # Compute iss orbit positions
    iss = ephem.readtle(iss_tle[0], iss_tle[1], iss_tle[2])
    for time in t_delta:
        iss.compute(time)
        iss_positions.append(np.degrees(iss.sublong))
        iss_positions.append(np.degrees(iss.sublat))
        iss_positions.append(iss.elevation)

    return render_template('cesium_test.html', 
            pos_arr=json.dumps(positions),
            iss_pos=json.dumps(iss_positions))

'''
# Main landing page
@app.route('/')
def homepage():
    return render_template('main.html',
            title = 'SAT TRACKER',
            temp = 'SAT SELECTION PAGE',
            tle = tle_data)

# Tracking page
@app.route('/tracking/', methods=['GET', 'POST'])
def tracking():
    itl_desig = request.form['itl_desig']

    #sat = Sat(itl_desig, tle_data[itl_desig][0], tle_data[itl_desig][1])
    sat = Sat("98067A", tle_data["98067A"][0], tle_data["98067A"][1])   # track iss for test

    latitude, longitude = sat.get_position()
    
    sat_info = [itl_desig, latitude, longitude]

    tle_raw = sat.get_satrec()

    return render_template('track.html',
            #desig="98067A ISS (ZARYA)", # remove later
            #desig=sat_info[0],
            #lat=sat_info[1],
            #lon=sat_info[2],
            tle=json.dumps(tle_raw))
'''

