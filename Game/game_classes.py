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
        self.__data = {}

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

    # use swing
    def swing(self):
        damage = self.__weapon[1]
        miss_chance = self.__weapon[2]
        
        miss = random.randint(0, 100)
        if miss <= miss_chance:
            return "miss"
        else:
            return damage
    
    def add_data(self, key, data):
        self.__data[key] = data
    
    def get_data(self):
        return self.__data
        
class Enemy():
    def __init__(self, name, weapon, health):
        # WEAPON MUST BE FORMATTED LIKE
        # weapon = [weapon, damage, miss]
        self.__name = name
        self.__weapon = weapon[0]
        self.__damage = weapon[1]
        self.__miss = weapon[2]
        self.__max_hp = health
        self.__hp = health

    def swing(self):
        # get their dice roll
        chance = random.randint(1,100)
        
        # if their miss chance was greater than or equal to the roll return a miss
        if self.__miss >= chance:
            return "miss"
        else:
            # if it wasnt, return the damage
            return self.__damage
    
    def lose_hp(self, damage):
        if self.__hp - damage <= 0:
            return False
        else:
            self.__hp -= damage
    
    def gain_hp(self, gain):
        if self.__hp + gain > self.__max_hp:
            self.__hp = self.__max_hp
        else:
            self.__hp += gain

    def get_name(self):
        return self.__name
    
    def get_hp(self):
        return self.__hp
    
    def get_weapon(self):
        return self.__weapon

class Location():
    def __init__(self):
        pass
class Item():
    pass

