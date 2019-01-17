import copy
defaultActions = ["f3", "f4", "e3","e4","pu34","pu43","pa34","pa43"]

def f3(x, y):
    return x,3
def f4(x, y):
    return 4,y
def e3(x, y):
    return x,0
def e4(x, y):
    return 0,y
def pu34(x,y):
    if (x+y) > 4 : return (4,(y-(4-x)))
    else : return((x+y),0)
def pu43(x,y):
    if (x+y) > 3 : return((x-(3-y)),3)
    else: return (0,(x+y))
def pa34(x,y):
    if (x+y) > 4: return (4,0)
    else: return((x+y),0)
def pa43(x,y):
    if (x+y) > 3: return (0,3)
    else: return (0,(x+y))

def performAction(act,x,y):
    if act == "f3": return f3(x,y)
    if act == "f4": return f4(x,y)
    if act == "e3": return e3(x,y)
    if act == "e4": return e4(x,y)
    if act == "pu34": return pu34(x,y)
    if act == "pu43": return pu43(x,y)
    if act == "pa34": return pa34(x,y)
    if act == "pa43": return pa43(x,y)
    else: raise ValueError("could not find action {}" .format(str))

class Path:
    def __init__(self):
        self.actions = []
        self.states = []
    def addAction(self,action):
        self.actions.append(action)
    def addState(self,state):
        self.states.append(state)

def findNewPaths(path): 
    newPossiblePaths = []
    for action in defaultActions:
        newPath = copy.deepcopy(path)
        oldX,oldY = newPath.states[-1]
        newState = performAction(action,oldX,oldY)
        #print (action,newState)
        if newState in newPath.states: 
            #print("true")
            ()
        else: 
            #print("false")
            newPath.addAction(action)
            newPath.addState(newState)
            newPossiblePaths.append(newPath)
    return newPossiblePaths
    #RückgabeWert alle Pfade die nicht redundante JugFüllWerte erzeugen

def calcErrorOfFillup(path):
    error = 0
    for i in range(0,len(path.actions)):
        act = path.actions[i]
        x,y = path.states[i]
        if act == "f3": error += 3 - y
        if act == "f4": error += 4 - x
    return error

class JugProblemSolver:  
    def __init__(self,initial4G,initial3G):
        self.finishedPaths = []
        self.x = initial4G
        self.y = initial3G
    def solve(self,final4G,final3G):
        paths = []        
        newPath = Path()
        newPath.addState((self.x,self.y))
        paths.append(newPath)        
        while(paths):
            newPaths = []
            for path in paths:
                nps = findNewPaths(path)
                for n in nps:
                   newPaths.append(n)
                paths.remove(path) 
            if newPaths:
                for newPath in newPaths:
                    if newPath.states[-1] == (final4G,final3G):
                        self.finishedPaths.append(newPath)
                        newPaths.remove(newPath)
                    else:
                        paths.append(newPath)
        print("Done")
        if self.finishedPaths: print(len(self.finishedPaths)," results")
        else: print("no results")
    def ReturnBestResult(self):
        sortedRes = sorted(self.finishedPaths, key=calcErrorOfFillup)
        return sortedRes[0]
    def ReturnWorstResult(self):
        sortedRes = sorted(self.finishedPaths, key=calcErrorOfFillup,reverse = True)
        return sortedRes[0]

def waterjug(start,finish):
    init3g,init4g = start
    finish3g,finish4g = finish
    solver = JugProblemSolver(init3g,init4g)
    solver.solve(finish3g,finish4g)
    return solver.ReturnBestResult().actions

waterjug((0,0),(2,0))