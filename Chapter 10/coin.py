import random

# class Coin simulates a coin being tossed
# note that the name of this class has a capital letter for the first
# letter, this is a standard programming convention and should be followed

class Coin():
    # a class should begin with a __init__() method
    # this method executes first, as an initialization of the class
    # the (self) paramenter is a generally accepted naming convention
    # for the paramaneter within a class, and is required
    
    # initialize the data attribute with "Heads" to indicate
    # the coun begins in a head's up position
    
    def __init__(self):
        self.__sideup = "Heads"
        
    # the toss mehod generates a random number in the range of 0 through 1
    # if the number is 0, sideup is assigned to "Heads"
    # otherwise sideup is assigned to "Tails"
    
    def toss(self):
        if random.randint(0,1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"
    
    # get sideup method returns the current state of the coin
    # or the side that is facing up
    
    def get_sideup(self):
        return self.__sideup
