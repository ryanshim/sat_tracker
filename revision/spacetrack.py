'''
Scrape data using Space-Track's API

- Currently scraping full catalog from space-track 
- Space-Track recommends using Curl to access their API.
'''
from sat import Sat
import sqlite3
import subprocess
import shlex
import getpass

''' Use space-track api to obtain tle data '''
def get_tle_data():
    username = input("Enter Space-Track e-mail: ")
    password = getpass.getpass("Enter password: ")

    # FULL CATALOG FROM SPACE-TRACK
    bashCom = "curl https://www.space-track.org/ajaxauth/login -d 'identity=" + \
              username + "&password=" + password + "&query='https://www.space-track.org" \
              "/basicspacedata/query/class/tle_latest/ORDINAL/1/EPOCH/%3Enow-30/" \
              "orderby/NORAD_CAT_ID/format/tle"

    try:
        subprocess.call(shlex.split(bashCom))   # call the curl process
        output = subprocess.check_output(['bash', '-c', bashCom])
    except subprocess.CalledProcessError():
        print("Could not download TLE data\n")
        return

    # process data to insert into database
    output = output.decode('utf-8')
    output = output.split('\n')
    output = output[:-1]

    # connect to database
    conn = sqlite3.connect('./static/data/tle.db')
    c = conn.cursor()

    # extract int'l designator and insert into database
    for i in range(0, len(output), 2):
        itl_desig = output[i][9:17]
        line1 = output[i]
        line2 = output[i+1]
        row = (itl_desig, line1, line2)
        print(itl_desig)

        c.execute('INSERT INTO tles VALUES (?,?,?)', row)
        conn.commit()

    conn.close()

'''
load saved data to dictionary
Dictionary format: satDict[int'lDesignator] = Satellite object
'''
def parse_tle_data():
    satDict = {} 
    with open('tle.txt', 'r') as inFile:
        while True:
            l1 = inFile.readline()
            l2 = inFile.readline()
            if not l2:  # reached eof
                break
            # use int'l designator as key
            itlDesig = l1.split(" ")[2]
            satDict[itlDesig] = Satellite(itlDesig, l1, l2)

    return satDict

if __name__ == '__main__':
    get_tle_data()
