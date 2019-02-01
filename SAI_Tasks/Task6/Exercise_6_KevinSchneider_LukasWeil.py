import networkx as nx
import math
import numpy as np
import matplotlib.pyplot as plt
import copy


defaultActions = ["S1","S2","B1","B2","S1B1"]

def S1(state) :
    if state[2] == 0 :
        return tuple(np.add(state,(1,0,1)))
    else :
        return tuple(np.add(state,(-1,0,-1)))

def S2(state) :
    if state[2] == 0 :
        return tuple(np.add(state,(2,0,1)))
    else :
        return tuple(np.add(state,(-2,0,-1)))

def B1(state) :
    if state[2] == 0 :
        return tuple(np.add(state,(0,1,1)))
    else :
        return tuple(np.add(state,(0,-1,-1)))

def B2(state) :
    if state[2] == 0 :
        return tuple(np.add(state,(0,2,1)))
    else :
        return tuple(np.add(state,(0,-2,-1)))

def S1B1(state) :
    if state[2] == 0 :
        return tuple(np.add(state,(1,1,1)))
    else :
        return tuple(np.add(state,(-1,-1,-1)))

class Path:
    def __init__(self):
        self.actions = []
        self.states = []
    def addAction(self,action):
        self.actions.append(action)
    def addState(self,state):
        self.states.append(state)


def performAction(act,state):
    if act == "S1":     return S1(state)
    if act == "S2":     return S2(state)
    if act == "B1":     return B1(state)
    if act == "B2":     return B2(state)
    if act == "S1B1":   return S1B1(state)
    else: raise ValueError("could not find action {}" .format(str))

#determine if state is legal
def isLegalState (state) :
    sherriffs = state[0]
    bandits = state[1]
    boat = state[2]
    if sherriffs <= 3 and bandits <= 3 and sherriffs >= 0 and bandits >=0 and bandits+sherriffs <= 6 and (boat == 1 or boat == 0):
        return True
    else :
        return False

#determine if state is deadly
def isDeadlyState(state):
    sherriffs = state[0]
    bandits = state[1] 
    if sherriffs < bandits and sherriffs > 0:
        return True
    else :
        return False

def findNewPaths(path): 
    newPossiblePaths = []
    for action in defaultActions:
        newPath = copy.deepcopy(path)
        oldState = newPath.states[-1]
        newState = performAction(action,oldState)
        #print (action,newState)
        if newState in newPath.states: 
            #print("true")
            ()
        else: 
            if isLegalState(newState):
                #print("false")
                newPath.addAction(action)
                newPath.addState(newState)
                newPossiblePaths.append(newPath)
    return newPossiblePaths

startPath = Path()

#create all paths from a start state
def allPaths (startState) :
    finishedPaths = []
    paths = []        
    newPath = Path()
    newPath.addState((startState))
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
                if newPath.states[-1] == (0,0,0) or isDeadlyState(newPath.states[-1]) :
                    finishedPaths.append(newPath)
                    newPaths.remove(newPath)
                else:
                    paths.append(newPath)
    print("Done")
    if finishedPaths: 
        for p in finishedPaths:
            print(p.states)
        print ("found {} paths".format(len(finishedPaths)))
        return finishedPaths
    else: print("no results")

#all paths starting from original state
allPossibilites = allPaths((3,3,1))

#add tree depth for better visualization
def addDepth (tree):
    result = []
    for path in tree:
        paths = path.states
        tmp = []
        for i in range(0,len(paths)-1):
            #print(i)
            tmp.append((i,paths[i]))
        result.append(tmp)
    return result

#add paths to a network and return the network
def addPaths(paths):
    nodeSet = set()
    for path in paths:
        pathSet = set(path)
        nodeSet = nodeSet.union(pathSet)
    graph = nx.digraph.DiGraph()
    for node in sorted(nodeSet):
        graph.add_node(node)
    for path in paths:
        graph.add_path(path)
    print(sorted(nodeSet))
    return graph

#state tree result
sT = addPaths(a)

#write graphml for visualization
nx.write_graphml(sT,"C:/Users/Kevin/Desktop/SearchTreee.graphml")

#Visualization done in Cytoscape.
