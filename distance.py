#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import numpy as np

sin = np.sin
cos = np.cos
atan2 = np.arctan2
sqrt = np.sqrt
pi = np.pi

R = 3963.1676  # Radius of earth in miles


def distance(lat1, long1, lat2, long2):
    """
    Calculate the Haversine distance in miles between two locations based
    on their latitudes and longitudes

    Inputs
    ------

    lat1 : float
        latitude in degrees of first point
    long1 : float
        longitude in degrees of first point
    lat2: float
        latitude in degrees of second point
    long2 : float
        longitude in degrees of second point

    """
    lat1 = lat1 * pi / 180.  # convert to radians
    lat2 = lat2 * pi / 180.  # convert radians
    dlat = (lat1 - lat2)
    dlong = (long1 - long2) * pi / 180.  # difference in radians

    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlong/2)**2
    return 2 * R * atan2(sqrt(a), sqrt(1-a))
