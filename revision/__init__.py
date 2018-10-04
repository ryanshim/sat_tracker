# Satellite Tracker Revision
#
# Revision Notes:
#
import sqlite3
import collections
import json
from flask import Flask, render_template, request, url_for
#from .sat import Sat

app = Flask(__name__)

# Main landing page
@app.route('/')
def homepage():
    return render_template('main.html',
            title = 'SATELLITE TRACKING',
            intl_desig ="",
            tle_l1 = "",
            tle_l2 = "")


# Handle Intl Designator Search
@app.route('/track', methods=['GET','POST'])
def intl_desig_search():
    if request.method == 'POST':
        desig = request.form.get('intl_desig_input')

        # Search for satellite in db by international designator
        conn = sqlite3.connect('./static/data/tle.db')
        c = conn.cursor()
        query = "SELECT * FROM tles WHERE itl_desig = '" + desig + "'"
        for row in c.execute(query):
            l1 = row[1]
            l2 = row[2]
        conn.close()

        # Strip the carriage return
        l1 = l1[:-1]
        l2 = l2[:-1]

        return render_template('main.html',
                title = 'SATELLITE TRACKING',
                intl_desig = desig,
                tle_l1 = l1,
                tle_l2 = l2)






















'''
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
    iss_data = []
    for row in c.execute("SELECT * FROM tles WHERE itl_desig = '98067A  '"):
        iss_data = row
    
    conn.close()
    print(error_count)

    return render_template('cesium_test.html', 
            pos_arr=json.dumps(positions),
            iss_tle=json.dumps(iss_data))
'''

'''
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

