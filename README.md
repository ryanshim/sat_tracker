# sat_tracker

![alt text](https://github.com/ryanshim/sat_tracker/blob/master/sats.png)

## Dependencies
- satellite.js
- Space-Track account to download TLE data

## Description
- Simple web-based utility to track satellites using Flask and satellite.js.
    - Currently, objects are searchable using their international designator
    - Ex: 98067A (Last two digits of launch year [98] + launch number [067] + object classification [A])
- Full TLE catalog of tracked objects obtained from Space-Track API.
