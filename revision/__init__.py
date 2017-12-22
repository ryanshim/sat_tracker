# Satellite Tracker Revision
#
# Revision Notes:
#   - Convert to python3
#   - Create web-based UI
#
import collections
import json
from flask import Flask, render_template, request, url_for
from .sat import Sat

app = Flask(__name__)

# Load tle data. Might need to put this in a separate function
# and imported as a module.
tle_data = {}
with app.open_resource('static/textFiles/tle.txt', 'r') as infile:
    while True:
        l1 = infile.readline()
        l2 = infile.readline() 
        if not l2:
            break
        itlDesig = l1.split(" ")[2]
        tle_data[itlDesig] = [l1, l2]

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
            desig="98067A ISS (ZARYA)", # remove later
            #desig=sat_info[0],
            lat=sat_info[1],
            lon=sat_info[2],
            tle=json.dumps(tle_raw))

