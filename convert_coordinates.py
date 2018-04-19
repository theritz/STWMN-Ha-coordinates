"""
Module for converting horizontal (AltAz) coordinates to galactic ones, and vice versa.

This module is made for Sterrenwacht Midden-Nederland, in Amersfoort (The Netherlands) per request
of the radio astronomy group. The module is part of software to control the DIY mount and dish with which
the Milky Way is imaged in the 21cm Hydrogen-alpha line as was done almost a century ago.
Code may ofcourse be used or changed freely.

To-do:
* strip the output of SkyCoord to only output the coordinates and not all the other stuff
* have one function that figures out if horizontal, galactic coordinates or object name is put in
  and then giving back coordinates in both systems (object input) or translate one into the other
* integrate module in program for radio astronomy dish's mount
* look into running all of this under Python 3.5 because that's not working now.
"""

from astropy import units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord # High-level coordinates
from astropy.coordinates import ICRS,FK5,Galactic # Low-level frames
from astropy.coordinates import Angle, Latitude, Longitude  # Angles
from astropy.coordinates import SkyCoord, EarthLocation, AltAz

def get_object_altaz(objectname):
    """
    (str) -> str
    Gets the coordinates in AltAz for given object by using the SkyCoord library of astropy.

    >>> get_object_altaz('M33')
    <SkyCoord (AltAz: obstime=2017-02-20 09:34:31.682102, location=(3838509.4723654552, 352213.855367796, 5064539.161280073) m, pr
    essure=0.0 hPa, temperature=0.0 deg_C, relative_humidity=0, obswl=1.0 micron): (az, alt) in deg
    ( 74.30194614,  27.33490393)>
    """
    #setting time and location required for AltAz coordinates determination
    obsy_location = EarthLocation(lat=52.91044*u.deg, lon=5.242664*u.deg, height=0*u.m)
    #hardcoded STWMN coördinaten
    utcoffset = +1*u.hour
    # Eastern Daylight Time
    time = Time.now() + utcoffset
    #grabbing the input and converting to AltAz...
    objectfound = SkyCoord.from_name(objectname)
    temp_object = str(objectfound.transform_to(AltAz(obstime=time,location=obsy_location))).split('(')
    print (temp_object[-1:])
    #output moet nog gestript worden op *alleen* de coördinaten, bijv. ( 73.76294349,  42.10079281)
    #DEZE KLOPT volgens Stellarium

def gal2deg(coorA,coorB):
    """ (str, str) -> str
    Convert galactic coordinates to degrees

    >>> gal2deg(121.12334339,-21.6403587)
    <SkyCoord (AltAz: obstime=2017-02-20 09:34:31.682102, location=(3838509.4723654552, 352213.855367796, 5064539.161280073) m, pr
    essure=0.0 hPa, temperature=0.0 deg_C, relative_humidity=0, obswl=1.0 micron): (az, alt) in deg
    ( 73.76294349,  42.10079281)>
    """
    #setting time and location required for AltAz conversion
    obsy_location = EarthLocation(lat=52.91044*u.deg, lon=5.242664*u.deg, height=0*u.m) #hardcoded STWMN coördinaten
    utcoffset = +1*u.hour  # Eastern Daylight Time
    time = Time.now() + utcoffset
    #grabbing the galactic coordinates and converting to horizontal...
    c = ''
    c = SkyCoord(coorA*u.degree, coorB*u.degree, frame='galactic')
    print (c.transform_to(AltAz(obstime=time,location=obsy_location)))
    #output moet nog gestript worden op *alleen* de coördinaten, bijv. ( 73.76294349,  42.10079281)
    #DEZE KLOPT volgens Stellarium

def deg2gal(degA,degB):
    """ (str, str) -> str
    Convert degrees to galactic coordinates

    >>> deg2gal(10.625,41.2)
    <SkyCoord (Galactic): (l, b) in deg
    ( 121.12334339, -21.6403587)>
    """
    d = ''
    d = SkyCoord(ra=degA*u.degree, dec=degB*u.degree, frame='icrs')
    print (d.galactic)
    #bij deze moet de input de altaz coordinaten worden
