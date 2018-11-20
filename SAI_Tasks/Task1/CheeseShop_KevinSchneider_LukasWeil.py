import math
import random

def initStock() :
    RedLeicesterAmnt    = random.randint(0,20)
    TilsitAmnt          = random.randint(0,20)
    RedWindsorAmnt      = random.randint(0,20)
    GruyereAmnt         = random.randint(0,20)
    EmmentalAmnt        = random.randint(0,20)
    stock = {
        "RedLeicester" : RedLeicesterAmnt,
        "Tilsit" : TilsitAmnt,
        "RedWindsor" : RedWindsorAmnt,
        "Gruyere" : GruyereAmnt,
        "Emmental" : EmmentalAmnt
        }
    return  stock

class store :

    def __init__(self):
        self.stock = initStock()
    def ask(self,cheeseType) :
        if cheeseType in self.stock:
            return self.stock[cheeseType] != 0
        else :
            return False
    def buy(self,cheeseType) :
        if cheeseType in self.stock:
            if self.stock[cheeseType] != 0 :
                self.stock[cheeseType] = self.stock[cheeseType] - 1
                return True
            else :
                raise ValueError("could not find {} in the store" .format(cheeseType))
        else :
            raise ValueError("could not find {} in the store" .format(cheeseType))


def main () :
    cheeseTypes =  [   
        "RedLeicester",
        "Tilsit" ,
        "RedWindsor", 
        "Gruyere" ,
        "Emmental" ]
    myStore = store()
    while True :
        buyType = random.choice(cheeseTypes)
        print("Customer: i want to buy {}" .format(buyType))
        if myStore.ask(buyType):
            print ("Me, an intellectual: we have {} in stock" .format(buyType))
            myStore.buy(buyType)
            print ("Customer: k thx bye")
        else:
            print ("Me, an intellectual: we don't have {} in stock" .format(buyType))
            print ("Customer: REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
            myStore.buy(buyType)

main()