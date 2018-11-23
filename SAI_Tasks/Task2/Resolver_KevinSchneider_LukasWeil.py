import itertools

# alpha is assumed to be already negated
def resolve(knowledge: set, alpha) :
    knowledge.add(alpha)
    def loop(setSize):
        combs = itertools.combinations(knowledge,2)
        for (c1,c2) in combs:
             c = combine(c1,c2)
             print(c1)
             print(c2)
             print("Combine:")
             print(c)
             knowledge.add(c)
             if c == tuple():
                
               
                print("Found empty clause")
                return True
        if len(knowledge) == setSize:
            print("Knowledgebase saturated")
            return False
        return loop(len(knowledge))
    return loop(len(knowledge))

def combine(clause1:tuple,clause2:tuple) :
    oneNegation = True
    l = []
    for x in clause1:
        l.append(x)
    for x in clause2:
        if x in l: 
            ()
        elif -x in l and oneNegation:
            l.remove(-x)
            oneNegation <- False
        elif -x:
            ()
        else:
            l.append(x)
    return tuple(l)


W = {tuple([6 , 3 , -4 , 5]) , tuple([-3 , 6 , 2]) , tuple([-5 , -3 , 6 , -2]),
tuple([6 , 3 , 4]), tuple([6 , -4 , -5 , 3]), tuple([-3 , 6 , 5 , -1 , -2]), tuple([-6])}
H = tuple([-3 , 6 , -2 , 5 , 1])
resolve(W,H)