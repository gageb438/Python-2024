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
    def __init__(self, name, desc, choices, enemies:list, items:list):
        self.__name = name
        self.__desc = desc
        self.__choices = choices
        self.__enemies = enemies
        self.__items = items
    
    def get_name(self):
        return self.__name
    
    def get_choice(self):
        choice = input(":> ")
        
        # validate choice
        while choice.lower() not in self.__choices:
            print(f"{choice} not recognized as a command.")
            choice = input(":> ")
        
        return choice
    
    def __str__(self):
        return self.__desc

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

        player = self.__player
        player_weapon = self.__p_weapon
        fight = True
        dodges = 0
        
        # start the fight
        while fight == True:
            # set the player rolls
            player_rolls = player_weapon.get_hits()
            
            # do the players rolls
            while player_rolls != 0:
                print(f"\n{player.get_name()}'s roll.")
                # get users choice
                choice = input(":> ")
                choice = choice.lower()
                choices = choice.split(" ")
                
                # if the user chose to run, get a 10% chance to make it out or not
                if choices[0] == "run":
                    if random.randint(1,10) == 1:
                        return "ran"
                    else:
                        print("You attempt to run, but cannot make it away.")
                  
                # add a 1/5 chance to miss your dodge
                elif choices[0] == "dodge":
                    if random.randint(1,5) == 1:
                        print("Your dodge fails.")
                    else:
                        print("You are able to dodge 1 extra hit.")
                        dodges += 1
                        print(f"You now have {dodges} dodges.")
                
                # if the length was 2
                elif len(choices) == 2:
                    # then check if it was an attack
                    if choices[0] == "attack" and choices[1] == enemy.get_name().lower():
                        # and deal damage
                        print(f"\nYou attack dealing {player_weapon.get_damage()} damage to the {enemy.get_name()}.")
                        
                        # check if the enemy died
                        living = enemy.lose_health(player_weapon.get_damage())
                        
                        # if so, then kill it.
                        if living == "dead":
                            print(f"{enemy.get_name()} has died.")
                            
                            # set player rolls to none and stop the fight
                            # and enemy rolls
                            player_rolls = 0
                            enemy_rolls = 0
                            fight = False
                            return "enemy died"
                        # if it didn't, print its current health.
                        else:
                            print(f"The {enemy.get_name()} has {enemy.get_health()} health left.")
                    else:
                        # print error command
                        print(f"{choice} is recognized as a valid command.")
                        # add another roll because of error
                        player_rolls += 1
                else:
                    # add another roll because of an error
                    print(f"{choice} is not recognized as a valid command.")
                    player_rolls += 1
                
                # remove a roll upon completion
                player_rolls -= 1

            # do each of the enemy rolls and get them
            enemy_rolls = enemy_weapon.get_hits()
            
            while enemy_rolls != 0:
                print(f"\n{enemy.get_name()}'s roll.")
                # if they had more than 0 dodges
                if dodges > 0:
                    # print they dodged it
                    print(f"{enemy.get_name()} attacks...")
                    print("You dodge the hit!")
                    # and remove a dodge
                    dodges -= 1
                    print(f"You now have {dodges} left.")
                    # remove the roll
                    enemy_rolls -= 1
                else:
                    # theres a 1/10 chance that the enemy misses.
                    if random.randint(1, 10) != 1:
                        # if they do not miss, make them attack ,dealing the certain amount of damage
                        print(f"{enemy.get_name()} attacks...")
                        print(f"You get hit, taking {player.get_health()}.")
                        
                        # remove the amount of damage that they lost
                        living = player.damage(enemy_weapon.get_damage())
                        
                        # remove the roll for this move
                        enemy_rolls -= 1
                        # if they died then return that they died, if they didn't print their health
                        if living == "dead":
                            return "player_dead"
                        else:
                            # print their health
                            print(f"You are at {player.get_health()} health.")
                    else:
                        # print the miss chance
                        print(f"{enemy.get_name()} misses their attack.")
                        # remove the roll
                        enemy_rolls -= 1

clearing = Location("clearing", "You are in a empty clearing.\nThere is a path to the north, west, and east.\nThe south is blocked by a lot of trees.\nThe west and east are paths leading each to their own seemingly empty area.\nThe path to the north leads to a more forested area.", ["north", "west", "east", "look"], [], [])
print(clearing)
choice = clearing.get_choice()

