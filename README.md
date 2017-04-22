# sat_tracker

## Dependencies
- Pyephem
- sgp4
- matplotlib
    - Basemap
        - libgeos
        - libgeos-dev
- numpy
- Space-Track account to download TLE data

## Description
- Calculates azimuth+elevation for observer view and plots the current position of the object, ECEF.
- Utilizes the pyephem, sgp4, and matplotlib modules.
- Full TLE catalog of tracked objects obtained from Space-Track API.
- Uses the international designator to identify the object.
    - Ex: 98067A (Last two digits of launch year [98] + launch number [067] + object classification [A])
- Will eventually be ported to control an antenna rotator controlled by a RaspberryPi for tracking and receiving data using RTLSDR's.
