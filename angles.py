# -*- coding: utf-8 -*-
from math import pi


def deg2grad(deg):
    """
    deg2grad(90.00) --> 100.0
    """

    return deg * (10 / 9.0)


def grad2deg(grad):
    """
    grad2deg(100.00) --> 90.0
    """

    return grad * (9 / 10.0)


def grad2rad(grad):
    """
    grad2rad(100.0) --> 1.5707963267948968
    """

    return grad * (pi / 200)


def rad2grad(rad):
    """
    rad2grad(1.5707963267948968) --> 100.0
    """

    return rad * (200 / pi)


# ======================== for 3


def decimal_deg2rad(decimal_deg):
    """
    decimal_deg(1.5707963267948968) --> 90.0
    """
    rad = (decimal_deg * pi/180)
    return rad


def rad2decimal_deg(rad):
    """
    rad2decimal_deg(1.5707963267948968) --> 90.0
    """
    dec = (rad * 180)/pi
    return dec


# ======================== for 4

def decimal_deg2dms_deg(decimal_deg):
    """
    decimal_deg2dms_deg(1.0169722222222222) --> (1, 1, 1.1)
    """

    d = int(decimal_deg)
    md = abs(decimal_deg - d) * 60
    m = int(md)
    sd = (md - m) * 60
    return (d, m, sd)


def dms_deg2decimal_deg(dms_deg):
    """
    dms_deg2decimal_deg(1, 1, 1.1) --> (1.0169722222222222)
    """

    decimal_deg = float(dms_deg[0]) + float(dms_deg[1]) / 60 + float(dms_deg[2]) / 3600
    return decimal_deg
# ======================== for 5
