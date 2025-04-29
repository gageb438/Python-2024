class Hero():
    def __init__(self, first_name, last_name, weapon):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__hp = 100
        self.__max_hp = 100
        self.__weapon = weapon
        self.__xp = 0
        self.__max_xp = 200
        self.__level = 0

    # getters
    def get_first_name(self):
        return self.__first_name
    def get_last_name(self):
        return self.__last_name
    def get_hp(self):
        return self.__hp
    def get_max_hp(self):
        return self.__max_hp
    def get_weapon(self):
        return self.__weapon
    def get_xp(self):
        return self.__xp
    def get_max_xp(self):
        return self.__xp_max
    def get_level(self):
        return self.__level
    
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
    # xp
    def gain_xp(self, xp):
        if self.__xp + xp > self.__max_xp:
            excess = (self.__xp + xp) - self.__max_xp
            self.__level += 1
            self.__xp = excess
            self.__max_xp += 200
            self.__max_hp += 2
            self.__hp = self.__max_hp

            # prevent missed xp
            while self.__xp > self.__max_xp:
                self.__xp = self.__xp - self.__max_xp
                self.__level += 1
                self.__max_xp += 200
                self.__max_hp += 2
                self.__hp = self.__max_hp
        else:
            self.__xp += xp
    
    
class Enemy():
    pass

class Neutral():
    pass

class Friendly():
    pass

class Item():
    pass
