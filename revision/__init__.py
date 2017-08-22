# Satellite Tracker Revision
#
# Revision Notes:
#   - Convert to python3
#   - Create web-based UI
#   - Integrate RPi servo control
#
import collections
import ephem
from flask import Flask, render_template

app = Flask(__name__)

# Main landing page
@app.route('/')
def homepage():

    tleData = {}

    # read the tle data
    with app.open_resource('static/textFiles/tle.txt', 'r') as f:
        while True:
            l1 = f.readline()
            l2 = f.readline()
            if not l2:
                break

            itlDesig = l1.split(" ")[2]

            tleData[itlDesig] = [l1, l2]

    return render_template('main.html',
            title = 'SAT TRACKER',
            temp = 'SAT SELECTION PAGE',
            tle = tleData)

# Tracking page
@app.route('/tracking/')
def tracking():
    return render_template('track.html')

