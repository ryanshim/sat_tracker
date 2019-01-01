# Satellite Tracker Revision
#
# Revision Notes:
#
from flask import Flask, render_template, request, url_for
from .str_filter import *
import sqlite3
import collections
import json

app = Flask(__name__)

# Main landing page
@app.route('/')
def homepage():
    return render_template('main.html',
            title = 'SATELLITE TRACKING',
            intl_desig = '',
            tle_l1 = '',
            tle_l2 = '')

# Handle Intl Designator Search
# TODO: Fix the tle entries in the db that don't have an intl desig.'
#       It's breaking the code.
@app.route('/track', methods=['GET','POST'])
def intl_desig_search():
    if request.method == 'POST':
        desig = request.form.get('intl_desig_input')
        l1 = ""
        l2 = ""

        # Convert any alpha chars to upper
        desig = upper_char(desig)

        # Search for satellite in db by international designator
        conn = sqlite3.connect('./static/data/tle.db')
        c = conn.cursor()
        try:
            query = "SELECT * FROM tles WHERE itl_desig = '" + desig + "'"
            for row in c.execute(query):
                l1 = row[1]
                l2 = row[2]
        except Exception:
            print("SQL Query Error:")
        conn.close()
        print(l1, l2)

        # Strip the carriage return
        l1 = l1[:-1]
        l2 = l2[:-1]
        tle_data = [desig, l1, l2]

        return render_template('main.html',
                title = 'TRACKING',
                intl_desig = desig,
                tle_l1 = l1,
                tle_l2 = l2)

