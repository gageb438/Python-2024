# the hero class initializes a new hero object
# with name, health, power, mana, weapon

class Hero:
    def __init__(self, name, health, power, mana, weapon):
        # constructor for the hero class
        
        # set all the attributes
        self.__name = name
        self.__health = health
        self.__power = power
        self.__mana = mana
        self.__weapon = weapon
    
    #--getters--#
    def get_name(self):
        return self.__name
    
    def get_health(self):
        return self.__health
    
    def get_power(self):
        return self.__power
    
    def get_mana(self):
        return self.__mana
    
    def get_weapon(self):
        return self.__weapon
    
    #--getters--#
    def set_name(self, name):
        self.__name = name
    
    def set_health(self, health):
        self.__health = health
        
    def set_power(self, power):
        self.__power = power
    
    def set_mana(self, mana):
        self.__mana = mana
    
    def set_weapon(self, weapon):
        self.__weapon = weapon
    
    #--losers--#
        
    def lose_health(self, loss):
        if self.__health <= loss:
            print("You died.")
            self.__health = 0
        else:
            self.__health -= loss
    
    def lose_mana(self, loss):
        if self.__mana <= loss:
            print("You are out of mana.")
            self.__mana = 0
        else:
            self.__mana -= loss
    
    #--gainers--#
    
    def gain_health (self, gain):
        self.__health += gain
    
    def gain_mana(self, gain):
        self.__mana += gain
    
    
        
    