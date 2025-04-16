# all classes for the game

class Hero():
    def __init__(self, name, health, health_max, mana, mana_max, power_xp, power_xp_max, inventory):
        self.__name = name
        self.__health = health
        self.__health_max = health_max
        self.__mana = mana
        self.__mana_max = mana_max
        self.__power_xp = power_xp
        self.__power_xp_max = power_xp_max
        self.__inventory = inventory
    
    #--getters--#
    def get_name(self):
        return self.__name
    
    def get_health(self):
        return self.__health
    
    def get_max_health(self):
        return self.__health_max
    
    def get_mana(self):
        return self.__mana
    
    def get_max_mana(self):
        return self.__mana_max
    
    def get_power_xp(self):
        return self.__power_xp
    
    def get_max_power_xp(self):
        return self.__max_power_xp
    
    def get_inventory(self):
        return self.__inventory
    
    #--modifiers--#
    
    # healths
    def lose_health(self, loss):
        if self.__health <= loss:
            return "Dead"
        else:
            self.__health -= loss
            
    def gain_health(self, gain):
        if self.__health + gain > self.__health_max:
            self.__health = self.__health_max
        else:
            self.__health += gain
            
    # manas
    def lose_mana(self, loss):
        if self.__mana <= loss:
            self.__mana = 0
        else:
            self.__mana -= loss
            
    def gain_mana(self, gain):
        if self.__mana + gain >= self.__mana_max:
            self.__mana = self.__mana_max
        else:
            self.__mana += gain
    
class Enemy():
    pass

class Neutral():
    pass

class Friendly():
    pass

class Item():
    pass