
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

def high (**kwargs):
    return L(30., 40., kwargs["temp"])

def relHigh (**kwargs):
    return triang(25., 43., 34., kwargs["temp"])

def med (**kwargs):
    return triang(16., 34., 25., kwargs["temp"])

def relLow (**kwargs):
    return triang(7., 25., 16., kwargs["temp"])

def low (**kwargs):
    return R(10., 20., kwargs["temp"])

low(temp=1.)

memberships = [
       high,
       relHigh,
       med,
       relLow,
       low
    ]

measured = {
    "temp"  : 18. ,
    "dT"    : -0.5
    }

test = [{"temp" : 0., "soos" : saas}, {"temp":18.}, {"temp" : 25.}, {"temp" : 32.}, {"temp" : 50.} ]
a = test[1]
high(**measured)

for f in memberships:
    for t in test:
        res = f(**t)
        print('t={:f} res={:f}'.format(t["temp"],res))



def fuzzy (measured: dict, memberships: list, rules: list, defuzzification: list) :
    return 0


