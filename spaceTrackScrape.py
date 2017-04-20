'''
Scrape data using Space-Track's API

- Currently scraping full catalog from space-track 
- Space-Track recommends using Curl to access their API.
'''
from satellite import Satellite
import subprocess
import shlex
import getpass

''' Use space-track api to obtain tle data '''
def getTleData():
    username = raw_input("Enter Space-Track e-mail: ")
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
        print "Could not download TLE data\n"
        return

    tleFile = open('tle.txt', 'w')  # save the data to file
    tleFile.write(output)
    tleFile.close()

'''
load saved data to dictionary
Dictionary format: satDict[int'lDesignator] = Satellite object
'''
def parseTleData():
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

