'''
Scrape data using Space-Track's API

- Currently scraping full catalog from space-track 
- Space-Track recommends using Curl to access their API.
'''
from satellite import Satellite
import subprocess
import shlex
import getpass

def getTleData():

    username = raw_input("Enter Space-Track e-mail: ")
    password = getpass.getpass("Enter password: ")

    # ISS (ZARYA)
    #bashCom = "curl https://www.space-track.org/ajaxauth/login -d 'identity="+ username +"&password=" + password + "&query='https://www.space-track.org/basicspacedata/query/class/tle_latest/NORAD_CAT_ID/25544/ORDINAL/1--5/orderby/ORDINAL/format/tle/emptyresult/show"

    # FULL CATALOG FROM SPACE-TRACK
    bashCom = "curl https://www.space-track.org/ajaxauth/login -d 'identity="+ username +"&password=" + password + "&query='https://www.space-track.org/basicspacedata/query/class/tle_latest/ORDINAL/1/EPOCH/%3Enow-30/orderby/NORAD_CAT_ID/format/tle"


    subprocess.call(shlex.split(bashCom))

    output = subprocess.check_output(['bash', '-c', bashCom])

    tleFile = open('tle.txt', 'w')
    tleFile.write(output)
    tleFile.close()

def parseTleData():
    satList = []
    with open('tle.txt', 'r') as inFile:
        while True:
            l1 = inFile.readline()
            l2 = inFile.readline()
            satNum = l1[9:16]
            satList.append(Satellite(satNum, l1, l2))
            if not l2:
                break
    return satList

