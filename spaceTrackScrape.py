'''
Scrape data using Space-Track's API

- Currently scraping ISS
'''
import subprocess
import shlex
import getpass

def getTleData():

    username = raw_input("Enter Space-Track e-mail: ")
    password = getpass.getpass("Enter password: ")

    bashCom = "curl https://www.space-track.org/ajaxauth/login -d 'identity="+ username +"&password=" + password + "&query='https://www.space-track.org/basicspacedata/query/class/tle_latest/NORAD_CAT_ID/25544/ORDINAL/1--5/orderby/ORDINAL/format/tle/emptyresult/show"

    subprocess.call(shlex.split(bashCom))

    output = subprocess.check_output(['bash', '-c', bashCom])

    tleFile = open('tle.txt', 'w')
    tleFile.write(output)
    tleFile.close()
