## sat_tracker

# Dependencies
- Pyephem
- sgp4
- matplotlib
- numpy
- matplotlib Basemap
    - libgeos
- Space-Track account to download TLE data

# Description
- Calculates azimuth+elevation for observer view and plots the current position of the object, ECEF.
- Utilizes the pyephem and sgp4 packages.
- Tracking full catalog of objects from Space-Track.
- Will eventually be ported to control a satellite dish rotator controlled by a RaspberryPi for tracking and receiving data using RTLSDR's.
