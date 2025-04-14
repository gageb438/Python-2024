import random

class Coin():
    # initialize the side up to heads
    def __init__(self):
        self.__sideup = "Heads"
    
    # toss the coin
    def toss(self):
        # if its 0, set it to heads, if its 1, set it to tails
        if random.randint(0,1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"
            
    # get the side thats up + return it
    def get_sideup(self):
        return self.__sideup