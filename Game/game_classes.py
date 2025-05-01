import random

class Hero():
    def __init__(self, name, weapon):
        weapons = {"sword" : [15, 30], "battle axe" : [20, 55], "dagger" : [5, 0], "gauntlets" : [10, 20]}
        # create the weapon save list
        weapon_save = [weapon, weapons[weapon][0], weapons[weapon][1]]
        # save all stats
        self.__weapon = weapon_save
        self.__name = name
        self.__hp = 100
        self.__max_hp = 100
        self.__location = "Spectral Bridge"

    # getter methods
    def get_name(self):
        return self.__name
    
    def get_hp(self):
        return self.__hp
    
    def get_max_hp(self):
        return self.__max_hp
    
    def get_weapon_data(self):
        return self.__weapon
    
    def get_location(self):
        return self.__location
       
    # setter methods
    def set_name(self, name):
        self.__name = name
    
    def set_hp(self, hp):
        # THIS CAN GO OVER MAX HP, MUCH BETTER TO GAIN 100000 INSTEAD
        self.__hp = hp

    def set_max_hp(self, hp):
        self.__max_hp = hp
    
    def set_location(self, place):
        self.__location = place
        
    # modifier methods
    def gain_hp(self, hp):
        if self.__hp + hp > self.__max_hp:
            self.__hp = self.__max_hp
        else:
            self.__hp += hp

    def lose_hp(self, hp):
        if self.__hp - hp <= 0:
            self.__hp = 0
            return False
        else:
            self.__hp -= hp

class Enemy():
    pass
class Location():
    def __init__(self):
        pass
class Item():
    pass

