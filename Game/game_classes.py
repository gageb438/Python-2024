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
    def __init__(self, name, damage, hits_per_round):
        self.__name = name
        self.__damage = damage
        self.__hits = hits_per_round
    
    def get_name(self):
        return self.__name
    
    def get_hits(self):
        return self.__hits

    def get_damage(self):
        return self.__damage
    
    def __str__(self):
        return f"Name: {self.__name}\nDamage: {self.__damage}\nHits per turn:{self.__hits}"

class Location():
    def __init__(self, name, desc, choices, enemies:list):
        self.__name = name
        self.__desc = desc
        self.__choices = choices
        self.__enemies = enemies
    
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

class Enemy():
    def __init__(self, name, weapon, health, max_health):
        self.__name = name
        self.__weapon = weapon
        self.__health = health
        self.__max_health = max_health
    
    # GETTER METHODS
    def get_name(self):
        return self.__name
    
    def get_weapon(self):
        return self.__weapon
    
    def get_health(self):
        return self.__health
    
    def get_max_health(self):
        return self.__max_health
    
    # MODIFIER METHODS
    def gain_health(self, gain):
        if self.__health + gain > self.__max_health:
            self.__health = self.__max_health
        else:
            self.__health += gain
    
    def lose_health(self, loss):
        if self.__health - loss <= 0:
            return "dead"
        else:
            self.__health -= loss

class Fight():
    def __init__(self, player, enemy):
        self.__player = player
        self.__enemy = enemy
        self.__p_weapon = player.get_weapon()
        self.__e_weapon = enemy.get_weapon()

    
    def run_fight(self):
        # run fight recieves no arguments
        # it runs the fights starting with the player attacking

        # initialize variables
        enemy = self.__enemy
        enemy_weapon = self.__e_weapon
        enemy_rolls = enemy_weapon.get_hits()

        player = self.__player
        player_weapon = self.__p_weapon
        player_rolls = player_weapon.get_hits()
        fight = True
        dodges = 0
        
        # start the fight
        while fight == True:
            for roll in range(player_rolls):
                choice = input(":> ")
                choice = choice.lower()
                
                if choice[0] == "run":
                    if random.randint(1,2) == 1:
                        return "ran"
                    else:
                        print("You attempt to run, but cannot make it away.")
                elif choice[0] == "dodge":
                    if random.randint(1,5) != 1:
                        print("Your dodge fails.")
                    else:
                        print("You are able to dodge 1 hit during the enemies attack phase.")
                        dodges += 1
                elif choice[0] == "attack" and choices[1] == enemy.get_name.lower():
                    print(f"You attack dealing {player_weapon.get_damage} to the {enemy.get_name()}.")
                    
                    damage = player_weapon.get_damage()
                    dead = enemy.damage(damage)
                    if dead == "dead":
                        return "enemy_dead"
                    
                    else:
                        print(f"{choice} is not recognized as a command.")
                        
                        choice = input(":> ")
                        choice.split()
                        
                        while choice[0] != "run" and choice[0] != "dodge" and choice[0] != "attack" and choice[1] != enemy.get_name():
                            print(f"{choice} not recognized as a command.")
                            choice = input(":> ")
            
            for roll in range(enemy_rolls):
                damage = enemy_weapon.get_damage()
                
                if dodges > 0:
                    print(f"{enemy.get_name()} attacks...")
                    print("You dodge the hit!")
                    dodges -= 1
                    print(f"You now have {dodges} left.")
                else:
                    if random.randint(1, 10) != 1:
                        print(f"{enemy.get_name()} attacks...")
                        print("You get hit.")
                        
                        living = player.damage(damage)
                        
                        if living == "dead":
                            return "player_dead"
                        else:
                            print(f"You are at {player.get_health()}")
                    else:
                        print(f"{enemy.get_name()} misses their attack.")
                        