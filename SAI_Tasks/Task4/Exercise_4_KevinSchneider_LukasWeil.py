
import math

from shapely import geometry

from matplotlib import pyplot

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

# Membership functions for C and T

def high (**kwargs):
    return {"high" : L(30., 40., kwargs["temp"])}

def relHigh (**kwargs):
    return {"relHigh" : triang(25., 43., 34., kwargs["temp"])}

def med (**kwargs):
    return {"med" : triang(16., 34., 25., kwargs["temp"])}

def relLow (**kwargs):
    return {"relLow" : triang(7., 25., 16., kwargs["temp"])}

def low (**kwargs):
    return {"low" : R(10., 20., kwargs["temp"])}

# Membership functions for dT

def increasing (**kwargs):
    return {"increasing" : L(0.,0.77,kwargs["dT"])}

def decreasing (**kwargs):
    return {"decreasing" : R(-0.77,0.,kwargs["dT"])}

def stable (**kwargs):
    return {"stable" : triang(-0.77, 0.77, 0.,kwargs["dT"])}

#list of all membership functions
memberships = [
       high,
       relHigh,
       med,
       relLow,
       low,
       increasing,
       decreasing,
       stable
    ]

# shapes of the membership functions

shapes = {
    "highShape" : geometry.Polygon([(30.,0.),(40.,1.),(50.,1.),(50.,0.)]),
    "relHighShape" : geometry.Polygon([(25.,0.),(34,1.),(43.,0.)]),
    "medShape" : geometry.Polygon([(16.,0.),(25.,1.),(34.,0.)]),
    "relLowShape" : geometry.Polygon([(7.,0.),(16.,1.),(25.,0.)]),
    "lowShape" : geometry.Polygon([(0.,1.),(10.,1.),(20.,0.),(0.,0.)])
    }

#Fuzzy rules of the system

def R1 (**kwargs) :
    res = min(kwargs["high"],kwargs["increasing"])
    return {"C_low" : res}

def R2 (**kwargs):
    res = min(kwargs["relHigh"],kwargs["stable"])
    return {"C_relLow" : res}

def R3 (**kwargs):
    res = min(kwargs["med"],kwargs["stable"])
    return {"C_med" : res}

def R4 (**kwargs):
    res = min(kwargs["relLow"],kwargs["decreasing"])
    return {"C_relHigh" : res}

def R5 (**kwargs):
    res = min(kwargs["low"],kwargs["decreasing"])
    return {"C_high" : res}

#list of rules
rules = [
    R1,
    R2,
    R3,
    R4,
    R5
    ]


# helper function to cut from shape
def cutOffShapeAt(c,targetShape):
    full = geometry.Polygon([(0.,1),(50.,1.),(50.,c),(0.,c)])
    res = targetShape.difference(full)
    return res

#functions to de-fuzzify variables

def defuzzifyHigh (**kwargs):
    return cutOffShapeAt(kwargs["C_high"],kwargs["highShape"])

def defuzzifyRelHigh (**kwargs):
    return cutOffShapeAt(kwargs["C_relHigh"],kwargs["relHighShape"])

def defuzzifyMed (**kwargs):
    return cutOffShapeAt(kwargs["C_med"],kwargs["medShape"])

def defuzzifyRelLow (**kwargs):
    return cutOffShapeAt(kwargs["C_relLow"],kwargs["relLowShape"])

def defuzzifyLow (**kwargs):
    return cutOffShapeAt(kwargs["C_low"],kwargs["lowShape"])

# list of defuzzifications
defuzzifications = [
    defuzzifyHigh,
    defuzzifyRelHigh,
    defuzzifyMed,
    defuzzifyRelLow,
    defuzzifyLow
    ]

def fuzzy (measured: dict, memberships: list, rules: list, defuzzification: list, showPlot) :
    fig = pyplot.figure(1, figsize=(5,5), dpi=90)
    membershipValues = {}
    for m in memberships:
        res = m(**measured)
        print(res)
        membershipValues = {**membershipValues, **res}
    fuzzyControls = {}
    for r in rules:
        res = r(**membershipValues)
        print(res)
        fuzzyControls = {**fuzzyControls, **res}
    shapeRes = []
    for d in defuzzification:
        res = d(**fuzzyControls, **shapes)
        shapeRes.append(res)
    result = shapeRes.pop(0)
    for s in shapeRes:
        result = s.union(result)
    centroid = result.centroid.x
    
    x,y = result.exterior.xy
    ax = fig.add_subplot(111)
    ax.plot(x, y, color='#6699cc', alpha=0.7,
        linewidth=3, solid_capstyle='round', zorder=2)
    ax.set_title('Polygon')
    if (showPlot) :
        pyplot.show(fig)
    return {"C" : centroid}



#measured variables
measured = {
    "temp"  : 18. ,
    "dT"    : -0.5
    }


#calling the function returns the real value of the control variable
fuzzy(measured,memberships,rules,defuzzifications,True)

