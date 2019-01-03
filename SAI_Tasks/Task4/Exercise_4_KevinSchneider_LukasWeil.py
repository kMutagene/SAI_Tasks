import math

from shapely import geometry

def R (c, d, x) : 
    if (x > d) :
        return 0.
    elif (x < c) :
        return 1.
    else:
        return (d - x) / (d - c)
    
def L (a, b, x) : 
    if (x < a):
        return 0.
    elif (x > b):
        return 1.
    else:
        return (x - a) /(b - a)

def triang (a, b, m, x) : 
    if (x <= a):
        return 0.
    elif (x >= b):
        return 0.
    elif ((a < x) & (x <= m)):
        return (x - a) / (m - a)
    else:
        return (b - x) / (b - m)

def high (temp):
    return L(30., 40., temp)

def relHigh (temp):
    return triang(26., 40., 34., tmp)

def med (temp):
    return triang(16., 34., 25.)

def relLow (temp):
    return triang(8., 24., 16., temp)

def low (temp):
    return R(10., 20., temp)

memberships = [
       high,
       relHigh,
       med,
       relLow,
       low
    ]


def fuzzy (measured: dict, memberships: list, rules: list, defuzzification: list) :
    return 0


