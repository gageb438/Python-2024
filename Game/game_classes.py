import random

class Hero():
    def __init__(self, name, weapon, health, max_health, location):
        self.__name = name
        self.__weapon = weapon
        self.__health = health
        self.__max_health = max_health
        self.__location = location
    
    # get items
    def get_name(self):
        return self.__name
    
    def get_health(self):
        return self.__health
    
    def get_max_health(self):
        return self.__max_health
    
    def get_weapon(self):
        return self.__weapon
    
    def get_location(self):
        return self.__location
    
    # setters
    def set_health(self, health):
        self.__health = health
    
    def set_max_health(self, health):
        self.__max_health = health
    
    def set_weapon(self, weapon):
        self.__weapon = weapon
        
    def set_location(self, location):
        self.__location = location
    
    
    # modifiers
    def heal(self, heal):
        # HEAL DOES NOT GO OVER HEALTH CAP
        if self.__health + heal > self.__max_health:
            self.__health = self.__max_health
        else:
            self.__health += heal
    
    def damage(self, damage):
        if self.__health - damage <= 0:
            return "dead"
        else:
            self.__health -= damage
    
    
class Weapon():
    def __init__(self, name, damage):
        self.__name
        self.__damage = damage
    
    def get_name(self):
        return self.__name
    
    def get_damage(self):
        return self.__damage

class Location():
    def __init__(self, name, desc, choices):
        self.__name = name
        self.__desc = desc
        self.__choices = choices
    
    def get_name(self):
        return self.__name
    
    def get_choice(self):
        choice = input(":> ")
        
        # validate choice
        while choice.lower() not in choices:
            print(f"{choice} not recognized as a command.")
            choice = input(":> ")
        
        return choice
    
    
    def __str__(self):
        print(desc)
    