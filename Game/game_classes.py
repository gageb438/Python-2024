class Hero():
    def __init__(self, health, health_max, weapon):
        self.__hp = health
        self.__max_hp = health_max
        self.__weapon = weapon

    # getters
    def get_hp(self):
        return self.__hp
    
    def get_max_hp(self):
        return self.__max_hp

    def get_weapon(self):
        return self.__weapon
    
    # modifiers

    # health
    def gain_hp(self, gain):
        if gain >= self.__max_hp - self.__hp:
            self.__hp = self.__max_hp
        else:
            self.__hp += gain
    
    def lose_hp(self, loss):
        if loss >= self.__hp:
            self.__hp = 0
            return False
        else:
            self.__hp -= loss
            return True
    
    def s_max_hp(self, max):
        self.__max_hp = max
    
    # weapon
    def s_weapon(self, weapon):
        self.__weapon = weapon
    


class Enemy():
    pass

class Neutral():
    pass

class Friendly():
    pass

class Item():
    pass