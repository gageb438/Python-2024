#----------------------------------------------------------------------------------------------------------------------------------
# IMPORTS
# IMPORT CLASSES, OS FOR FILE MANAGEMENT, RANDOM FOR RANDOM CHANCE IN FIGHTING INTERACTIONS AND PICKLE FOR STORING OBJECTS
import game_classes
import os
import random
import pickle

#----------------------------------------------------------------------------------------------------------------------------------
# MAIN FUNCTIONS
# MAIN HANDLES RUNNING THE GAME
# MAIN MENU GETS USERS CHOICE
def main():
    # main recieves no arguments
    # it drives the adventure game
    # it outputs all steps

    # initialize varaibles
    game_name = "The Grand Escape of Etheria"

    # print welcome
    print(f"\nWelcome to {game_name}.")

    # get user choice
    choice = main_menu()

    # translate choice to a function
    if choice == 1:
        new_save()
    elif choice == 2:
        player = load_save()
    else:
        print(f"Goodbye, thank you for playing {game_name}!")

def main_menu():
    # main menu recieves no arguments
    # it creates the main menu
    # and returns a choice

    # initialize variables
    choices = [1,2,3]
    choice = -1

    # create the menu
    print("At any point to leave, click stop at the top, and re-run it.")
    print("Each time you move to a new location it will save.")
    print("1: New Save")
    print("2: Load Save")
    print("3: Quit")

    # each time theres a wrong choice or for the first running, get the choice
    while choice not in choices:
        try:
            # get choice
            choice = int(input(":> "))
            
            # check to make sure theres gamesaves if they chose to load
            if choice == 2:
                if not os.path.exists("game_saves.dat"):
                    # if the file doesnt exist, print no saves found and reset the choic
                    choice = -1
                    print("No game saves found, please create one first.")
                else:
                    # if it does then call load save
                    load_save()
        except:
            # on exception, pass, restarting the loop
            pass
    
    # return the users choice.
    return choice

#----------------------------------------------------------------------------------------------------------------------------------
# PLAYER SAVE FUNCTIONS
# NEW SAVE CREATING A NEW SAVE, DELETE SAVE DELETING ONE AFTER LOSING, LOAD SAVE LOADING ONE
def new_save():
    # new save does not recieve any arguments
    # it creates a new save for the player
    
    # initialize valid weapons
    sword = game_classes.Weapon("Sword", 20, 1)
    dagger = game_classes.Weapon("Dagger", 10, 2)
    
    # print title
    print("---Character Creator---")

    # initialize looping variable
    good = False

    # check if the name is being used in our save file
    while good == False:
        # set good to TRUE to see if it changed
        good = True
        # get input for the name
        name = input("Please enter the name of your character (First and last if it has a last): ")

        # check if the file exists, and then load the data
        if os.path.exists("game_saves.dat"):
            file = open("game_saves.dat", "rb")
            try:
                data = pickle.load(file)
            except:
                data = {}
            
            # close the file
            file.close()

            # check if the name is being used
            if data != {}:
                for key in data:
                    if key == name:
                        print("FALSE")
                        good = False
                        
        # if good was set to false at the end of this loop, print that the name was being used and needs to be changed
        if good == False:
            print("Name already being used, pick another or modify the current one.")

    # print valid weapons
    print(sword)
    print(dagger)

    # get users choice
    weapon = input("\nWhat weapon would you like to use?\n:>")

    # validate choice
    while weapon.lower() != "sword" and weapon.lower() != "dagger":
        print(f"{weapon} does not exist.")
        weapon = input(":>")
    
    # set their weapon
    if weapon.lower() == "sword":
        weapon = sword
    else:
        weapon = dagger
    
    # generate location data
    data = generate_loc()
    # make the character
    player = game_classes.Hero(name, weapon, 100, 100, "tutorial", data)
    
    # then call main game
    tutorial(player)
    
def delete_save(player):
    # delete save recieves the player argument
    # it removes a save from the save file
    # and returns back to the main menu.
    
    # get the file data
    file = open("game_saves.dat", "rb")
    data = pickle.load(file)
    file.close()
    
    # reopen file to write
    file = open("game_saves.dat", "wb")
    
    # get the players save file and remove it
    for plr in data:
        if plr == player.get_name():
            sv = plr
    
    del data[sv]
    
    # then re-write it to the file
    pickle.dump(data, file)
    file.close()
    
    # return to the main menu
    main()
    
def load_save():
    # load save recieves no arguments
    # it prints all saves
    # and loads one of the user choice

    # check if the file exists
    if os.path.exists("game_saves.dat"):
        file = open("game_saves.dat", "rb")
        
        # load the file
        try:
            data = pickle.load(file)
        except:
            # print the error and return it
            print("No saves found, create one first.")
            main()

        # if the dictionary isnt empty then it loads all
        if data != {}:
            # read the data and print each objects info
            for item in data:
                # get the character from the dictionary
                char = data[item]
                name = char.get_name()
                weapon = char.get_weapon()
                weapon_name = weapon.get_name()
                location = char.get_location()

                # print all of their stats
                print(f"\nName: {name}")
                print(f"Weapon: {weapon}")
                print(f"Location: {location}")
            
            # get the users choice
            choice = input("What save would you like to load? (NAME ONLY, CASE SENSITIVE): ")
            
            # set the blank player variable, its an integer since players are stored as srings and not integers
            player = 1
            
            # check if the player requested is correct, and then set the player object
            for item in data:
                if item == choice:
                    player = data[item]
              
            if player == 1:
                print("Player not found.")
                return
            
            # LOCATION INTERPERETER SECTION
            # get the players
            # location
            location = player.get_location()
            
            # validate and call all correct functions
            if location == "tutorial":
                tutorial(player)
            elif location == "clearing":
                clearing(player)
            elif location == "center_path":
                center_path(player)
            elif location == "left_path":
                left_path(player)
            elif location == "right_path":
                right_path(player)
            elif location == "ocean":
                ocean(player)
            elif location == "ghost_town":
                ghost_town(player)
            elif location == "forge":
                forge(player)
            elif location == "cave":
                cave(player)
            elif location == "slime_forest":
                slime_forest(player)
            elif location == "slime_boss_forest":
                slime_boss_forest(player)
            elif location == "castle":
                castle(player)
            elif location == "right_valley":
                right_valley(player)
            elif location == "left_valley":
                left_valley(player)
            elif location == "zummies_domain":
                zummies_domain(player)
            else:
                print(f"{location} not found in saved locations.")
                return
        else:
            print("No saves found, create one first.")
            main()
        


def save_game(player):
    # save game recieves an argument for the character object
    # it then adds it to a file
    # and pickles it
    
    # preset data
    data = {}
    
    # get the data
    if os.path.exists("game_saves.dat"):
        try:
            file = open("game_saves.dat", "rb")
            data = pickle.load(file)
            file.close()
        except EOFError:
            data = {}
        except Exception as error:
            print(error)
    else:
        # open and close the file if it DOESNT exist to create it
        file = open("game_saves.dat", "wb")
        data = {}
        pickle.dump(data, file)
        
        file.close()

    # check to see if there is an old file under the same name
    boolean1 = False
    for item in data:
        if item == player.get_name():
            log1 = item
            boolean1 = True
    if boolean1 == True:
        del data[log1]
    
    # add it to the data
    data[player.get_name()] = player

    # write data to the file
    file = open("game_saves.dat", "wb")
    pickle.dump(data, file)
    file.close()

    print("Game successfully saved.")

#-------------------------------------------------------
# DEATH FUNCTION
def death(player):
    # death recieves the player argment
    # it prints out that the player died
    # and their stats
    # and weapon
    # then removes it from player save.
    
    name = player.get_name()
    weapon = player.get_weapon()
    damage = weapon.get_damage()
    turns = weapon.get_hits()
    death_location = player.get_location()
    
    print("\nYou died, here is a view of your stats.")
    print(f"Name : {name}\nWeapon : {weapon.get_name()}\nDamage : {damage}\nTurns : {turns}\nDeath location: {death_location}")
    
    delete_save(player)
    print("Thank you for playing.")
    
#-------------------------------------------------------
# LOCATION FUNCTIONS
def tutorial(player):
    # tutorial recieves the player argument\
    # it creates the tutorial location

    # initalize variables
    choice = -1
    choices = ["1","2"]
    weapon = player.get_weapon().get_name()
    
    # set location
    player.set_location("tutorial")
    save_game(player)
    
    # print the welcome screen
    print("\nWelcome to the tutorial, if you would like to do it, press 1.\nIf you would like to skip it, press 2.")
    
    # get choice
    while choice not in choices:
        choice = input(":> ")
    
    if choice == "1":
        print(f"You get up after falling down a large pit, your {weapon} has fallen next to you.")
        print(f"HINT: Type grab {weapon} to pick up the weapon")

        # get the option
        option = input(":> ")
        
        # lowercase it and split it into a list
        option = option.lower()
        options = option.split(" ")
        
        # prime look
        bad = True
        
        # validate users choice
        while bad == True:
            if len(options) == 2:
                if options[0] == "grab" and options[1] == weapon.lower():
                    print(f"You grab your {weapon}.")
                    bad = False
                else:
                    print(f"{option} is not recognized as a valid command.")
                    option = input(":> ")
                    options = option.split(" ")
            elif options[0] == "look":
                print(f"You get up after falling down a large pit, your {weapon} has fallen next to you.")
                print(f"HINT: Type grab {weapon} to pick up the weapon")
                
                option = input(":> ")
                options = option.split(" ")
            else:
                print(f"{option} is not recognized as a valid command.")
                option = input(":> ")
                options = option.split(" ")


        # print the next area
        print(f"\nYou advance through the cave, armed with your {weapon} and see a skeleton!")
        print("\nHINT: You are now faced with your first enemy and have a few options:")
        print("You can attack it by tying attack skeleton.")
        print("You can run from it by typing run")
        print("You can try to avoid its attack by typing dodge")
        
        # create the skeleton enemy and its wepaon
        s_weapon = game_classes.Weapon("Sword", 10, 1)
        skeleton = game_classes.Enemy("Skeleton", s_weapon, 50, 50)

        fight = game_classes.Fight(player, skeleton)
        choice = fight.run_fight()
        
        if choice == "ran":
            print("Cowardly. Well then, lets move on to the real game.")
            clearing(player)
        elif choice == "player_dead":
            print("Odd. You managed to die in the tutorial, either really bad luck, or your just horrible.")
            death(player)
        else:
            print("Perplexing. You might be cut out for this, good work.")
            cleraing(player)
    else:
        clearing(player)

def generate_loc():
    # generate locations recieves no argument
    # it generates all of the locations
    # and returns them as a list for the player data save
    clearing_loc = game_classes.Location("clearing", "\nYou are in a empty clearing.\nTo the north, there is a empty pathway.\nTo the south, there is a cluttered forest.\nThe east and west are too dense of a forest to go through.", [], [])
    center_path_loc = game_classes.Location("center_path", "\nYou are in a the middle of a path.\nTo the north, there is a castle, it seems like you shouldn't be there until later.\nTo the east and west, there is more path.\nTo the south, there is a clearing.", [], [])
    left_path_loc = game_classes.Location("left_path", "\nYou are in the middle of a path.\nThe north and south are blocked by dense forests.\nTo the east, there is more path.\nTo the west, there is a town, seemingly empty.", [], [])
    right_path_loc = game_classes.Location("right_path", "\nYou are in the middle of a path.\nThe north and south are blocked by dense forests.\nTo the east, there is a ocean.\nTo the west, there is a path.", [], [])
    ocean_loc = game_classes.Location("ocean", "\nYou are on a beach of the ocean.\nThe ocean is calming to you. It heals you back to max hp, and gives you some extra health.\nThere is nowhere to go, other than west, leading back to a path.", [], [])
    ghost_town_loc = game_classes.Location("ghost_town", "\nYou are in a town, it seems ancient and abandoned.\nTo the north, there is a cave.\nTo the east, there is a path.\nTo the west, there is a weapon forge.\nThe south is too dense of a forest to get through.", [], [])
    forge_loc = game_classes.Location("forge", "\nYou are in a forge, abandoned by society.\nTo the east, is a town, seemingly abandoned.\nThe north, west, and south are too dense of a forest to get through.", ["forge", "smith"], [])
    cave_enemy_weapon = game_classes.Weapon("Sword", 10, 1)
    cave_enemy = game_classes.Enemy("skeleton", cave_enemy_weapon, 50, 50)
    cave_loc = game_classes.Location("cave", "\nYou entered a dark cave.\nThe only way out is to the south.", [], [cave_enemy])
    forest_loc = game_classes.Location("forest", "\nYou are in a dense forest.\nTheres a path to the north, leading to a clearing.\nThe west leads to more forest.\nThe east leads to more forest, its more dark and ominous than the one on the west.\nThe south leads to a valley.", [], [])
    slime_enemy_weapon = game_classes.Weapon("Goop", 5, 1)
    slime_enemy = game_classes.Enemy("Slime", slime_enemy_weapon, 50, 50)
    slime_forest_loc = game_classes.Location("slime_forest", "\nYou are in a dense forest.\nTheres a more forest to the east.\nAll other directions are too dense to get to.", [], [slime_enemy])
    slime_boss_weapon = game_classes.Weapon("Goop", 10, 2)
    slime_boss = game_classes.Enemy("Slime", slime_boss_weapon, 100, 100)
    slime_boss_loc = game_classes.Location("slime_boss_forest", "\nYou are in a dense forest.\nThere is more forest to the west.\nAll other directions are too dense to get to.", [], [slime_boss])
    castle_boss_weapon = game_classes.Weapon("Greatsword", 50, 1)
    castle_boss = game_classes.Enemy("Zumwalt", castle_boss_weapon, 200, 200)
    castle_loc = game_classes.Location("castle", "\nYou are in a dark castle.\nThe north leads to Etrea.\nThe south leads to a path.\nThe west and east are blocked by castle walls.", [], [castle_boss])
    right_valley_loc = game_classes.Location("right_valley", "\nYou are in the eastern part of a valley.\nTo the north, theres a forest.\nTo the east and south, there is a mountain, too tall to climb.\nTo the west, there is more valley.", [], [])
    left_valley_loc = game_classes.Location("left_valley", "\nYou are in the western part of a valley.\nTo the north, there is a forest, too dense to go through.\nTo the east there is more valley.\nTo the south, there is mountains.\nTo the west, theres a staircase, leading to a dark place.", [], [])
    zummies_weapon = game_classes.Weapon("Dark Greatsword", 50, 1)
    zummie = game_classes.Enemy("Zummie", zummies_weapon, 500, 500)
    zummies_domain_loc = game_classes.Location("zummies_domain", "\nYou are in a dark, foggy area.\nTheres no escape from this one.", [], [zummie])
    
    # RETURN ALL LOCATIONS AS DATA
    return [clearing_loc, center_path_loc, left_path_loc, right_path_loc, ocean_loc, ghost_town_loc, forge_loc, cave_loc, forest_loc, slime_forest_loc, slime_boss_loc, castle_loc, right_valley_loc, left_valley_loc, zummies_domain_loc]

def get_location(player, find):
    # get location recieves the player argument and a location to search for
    # it grabs all location data from the player
    # and checks the name of each, until it finds the right one
    # then it returns the location object
    
    # get the data
    data = player.get_data()
    
    # read the data, finding the right object
    for i in data:
        if i.get_name() == find:
            # return the right object
            return i
            
    
def zummies_domain(player):
    # zummies domain recieves the player argument
    # it is a very unbeatable boss.
    # it isnt meant to be beat, so if your looking here to see if theres a way to, dont bother
    # its litterally just to kill you quickly
    # if you manage to beat it, good for you
    
    # get the location
    location = get_location(player, "zummies_domain")
    
    # set location
    player.set_location("zummies_domain")
    save_game(player)
    
    # print the location
    print(location)
    
    # start fight
    if location.get_enemies != []:
        print("Zummie approaches you.")
        fight = game_classes.Fight(player, location.get_enemies()[0])
        outcome = fight.run_fight()
        
        if outcome == "ran":
            print(f"Zummie, Bane of the Throne: How cowardly!")
            left_valley(player)
        elif outcome == "enemy died":
            print("good work, honestly you shouldnt even see this but if you do, amazing for you i suppose.")
            location.clear_enemies()
            print("You've been healed back to max health, and gained 500 max hp.")
            player.set_max_health(500)
            player.set_health(500)
        else:
            death(player)
    else:
        choice = location.get_choice()
        
        while True:
            if choice == "north" or choice == "west" or choice == "south":
                print("An invisible barrier in the fog stops you from progressing.")
                choice = location.get_choice()
            else:
                left_valley(player)
                break
        
def clearing(player):
    # clearing recieves the player argument
    # it is the main spawn of the game
    
    # get the clearing location from the player save
    location = get_location(player, "clearing")
    
    player.set_location("clearing")
    save_game(player)
    
    # print the description
    print(location)
    
    # get choice
    choice = location.get_choice()
    while True:
        if choice == "east" or choice == "west":
            print("It's too dense for you to get through.")
            choice = location.get_choice()
        elif choice == "north":
            center_path(player)
            break
        elif choice == "south":
            forest(player)
            break
def forest(player):
    # forest recieves the player argument
    # it generates the forest location
    
    # get the location
    location = get_location(player, "forest")
    
    player.set_location("forest")
    save_game(player)
    
    # print the location
    print(location)
    
    # get the choice
    choice = location.get_choice()
    while True:
        if choice == "east":
            slime_boss(player)
            break
        elif choice == "west":
            slime_forest(player)
            break
        elif choice == "north":
            clearing(player)
            break
        elif choice == "south":
            right_valley(player)
            break

def slime_boss_forest(player):
    # slime boss recieves the player argument
    # it is to the left of the forest
    
    # get the location from the player save
    location = get_location(player, "slime_boss_forest")
    
    player.set_location("slime_boss_forest")
    save_game(player)
    
    # print the location
    print(location)
    
    # get the enemies
    if location.get_enemies() != []:
        enemy = location.get_enemies()
        
        fight = game_classes.Fight(player, enemy[0])
        print("A slime approaches and engages you.")
        outcome = fight.run_fight()
        
        # get the outcome and fix
        if outcome == "ran":
            forest(player)
        elif outcome == "enemy died":
            location.clear_enemies()
            
            print("Killing an enemy restored you to max hp, you also gained a +20 hp increase.")
            max_health = player.get_max_health()
            max_health += 20
            player.set_max_health(max_health)
            player.heal(200000)
            
            print(f"Good job winning, your current health is at {player.get_health()} and your max health is at {player.get_max_health()}.")
        else:
            death(player)
    
    # get choice
    choice = location.get_choice()
    while True:
        if choice == "north" or choice == "west" or choice == "south":
            print("The forests are too dense to pass through.")
            choice = location.get_choice()
        else:
            forest(player)
            break
def slime_forest(player):
    # slime enemy recieves the player argument
    # it is to the left of the forest
    
    # get the location from the player save
    location = get_location(player, "slime_forest")
    player.set_location("slime_forest")
    save_game(player)
    
    # print the location
    print(location)
    if location.get_enemies() != []:
        enemy = location.get_enemies()
        
        fight = game_classes.Fight(player, enemy[0])
        outcome = fight.run_fight()
        
        if outcome == "ran":
            forest(player)
        elif outcome == "enemy died":
            location.clear_enemies()
            
            print("Killing an enemy restored you to max hp, you also gained a +20 hp increase.")
            max_health = player.get_max_health()
            max_health += 20
            player.set_max_health(max_health)
            player.heal(200000)
            
            print(f"Good job winning, your current health is at {player.get_health()} and your max health is at {player.get_max_health()}.")
        else:
            death(player)
    
    # get choice
    choice = location.get_choice()
    while True:
        if choice == "north" or choice == "west" or choice == "south":
            print("The forests are too dense to pass through.")
            choice = location.get_choice()
        else:
            forest(player)
            break
          
def center_path(player):
    # center path recieves the player argument
    # it is above the main spawn
    
    # get the center path location from the player save
    location = get_location(player, "center_path")
    player.set_location("center_path")
    save_game(player)
    
    # print the location
    print(location)
    
    # get choice
    choice = location.get_choice()
    
    if choice == "north":
        castle(player)
    elif choice == "south":
        clearing(player)
    elif choice == "east":
        right_path(player)
    elif choice == "west":
        left_path(player)

def left_path(player):
    # left path recieves the player argument
    # it is to the left of the center path
    
    # get the left path location from the player save
    location = get_location(player, "left_path")
    player.set_location("left_path")
    save_game(player)
    
    # print the location
    print(location)
    
    # get the choice
    choice = location.get_choice()
    
    while True:
        if choice == "north" or choice == "south":
            print("The forest is too dense for your to pass through.")
            choice = location.get_choice()
        elif choice == "east":
            center_path(player)
            break
        elif choice == "west":
            ghost_town(player)
            break

def ghost_town(player):
    # ghost town recieves the player argument
    # it is to the left of the left path!!
    
    # get the location from player save
    location = get_location(player, "ghost_town")
    player.set_location("ghost_town")
    save_game(player)
    
    # print the location
    print(location)
    
    # get the choice
    choice = location.get_choice()
    
    while True:
        if choice == "north":
            cave(player)
            break
        elif choice == "east":
            left_path(player)
            break
        elif choice == "west":
            forge(player)
            break
        elif choice == "south":
            print("The forest is too dense for you to pass through.")
            choice = location.get_choice()

def forge(player):
    # forge recieves the player argument
    # it is to the left of the ghost town
    
    # get the location from the player save
    location = get_location(player, "forge")
    player.set_location("forge")
    save_game(player)
    
    # print the location
    print(location)
    print("HINT: Type smith or forge to use the forge.")
    
    # get the choice
    choice = location.get_choice()
    
    
    while True:
        if choice == "north" or choice == "south" or choice == "west":
            print("The forest is too dense for you to pass through.")
            choice = location.get_choice()
        elif choice == "east":
            ghost_town(player)
            break
        elif choice == "forge" or choice == "smith":
            # PRINT THE SPECIAL SMITHING GUI
            print("Welcome to the forge.")
            print("What would you like to make?\n")
            
            # make all the weapons
            greatsword = game_classes.Weapon("Greatsword", 40, 1)
            longsword = game_classes.Weapon("Longsword", 20, 2)
            battle_axe = game_classes.Weapon("Battle Axe", 30, 1)
            glaive = game_classes.Weapon("Glaive", 10, 4)
            sticks_and_stones = game_classes.Weapon("Sticks and stones", 1, 1)
            
            weapons = [greatsword, longsword, battle_axe, glaive, sticks_and_stones]
            
            for weapon in weapons:
                name = weapon.get_name()
                damage = weapon.get_damage()
                turns = weapon.get_hits()
                
                print(f"Name: {name}\nDamage: {damage}\nTurns: {turns}")
            
            # get the users choice
            inpu = input("What would you like to smith (leave or quit to stop forging): ")
            options = ["greatsword", "longsword", "battle axe", "glaive", "sticks and stones", "leave", "quit"]
            
            while inpu not in options:
                print(f"{choice} not recognized as a command.")
                inpu = input("What would you like to smith (leave or quit to stop forging): ")
            
            if inpu == "leave" or inpu == "quit":
                choice = location.get_choice()
            else:
                print(f"Forging...")
                
                # find the proper weapon
                if inpu.lower() == "greatsword":
                    player.set_weapon(greatsword)
                elif inpu.lower() == "longsword":
                    player.set_weapon(longsword)
                elif inpu.lower() == "battle axe":
                    player.set_weapon(battle_axe)
                elif inpu.lower() == "glaive":
                    player.set_weapon(glaive)
                elif inpu.lower() == "sticks and stones":
                    player.set_weapon(sticks_and_stones)
                
                # print fixed weapon
                print(f"Forged. Your weapon is now set to {player.get_weapon().get_name()}.")
                
                # get the users choice again
                choice = location.get_choice()

def cave(player):
    # cave recieves the player argument
    # it creates the cave scene
    
    # get the location
    location = get_location(player, "cave")
    player.set_location("cave")
    save_game(player)
    
    # print it
    print(location)
    
    # due to this having an enemy, the moment you are thrown in, you get put in to a fight.
    enemies = location.get_enemies()
    
    if enemies != []:
        # start the fight if there were enemies
        print("A skeleton approaches you, and engages you.")
        fight = game_classes.Fight(player, enemies[0])
        outcome = fight.run_fight()
        
        if outcome == "ran":
            ghost_town(player)
        elif outcome == "enemy died":
            # since they won! get them to full hp and gain 20 extra
            print("Killing an enemy restored you to max hp, you also gained a +20 hp increase.")
            max_health = player.get_max_health()
            max_health += 20
            player.set_max_health(max_health)
            player.heal(200000)
            
            print(f"Good job winning, your current health is at {player.get_health()} and your max health is at {player.get_max_health()}.")
            location.clear_enemies()
        else:
            death(player)
    
    # get the choice
    choice = location.get_choice()
    
    while True:
        if choice == "north" or choice == "west" or choice == "east":
            print("Too many rocks, no point in trying to break through.")
        elif choice == "south":
            ghost_town(player)
            break

def right_path(player):
    # right path recieves the player argument
    # it generates the right path scene
    
    # get the location
    location = get_location(player, "right_path")
    player.set_location("right_path")
    save_game(player)
    
    # print the location
    print(location)
    
    # get the choice
    choice = location.get_choice()
    
    # translate the choice and move the player
    while True:
        if choice == "north" or choice == "south":
            print("The forest is too dense for you to pass through.")
        elif choice == "east":
            ocean(player)
            break
        elif choice == "west":
            center_path(player)
            break

def right_valley(player):
    # right valley recieves the player argument
    # it generates the right valley location
    
    # get the location
    location = get_location(player, "right_valley")
    player.set_location("right_valley")
    save_game(player)
    
    # print the location
    print(location)
    
    # get the choice
    choice = location.get_choice()
    
    # translate the choice and move the player
    while True:
        if choice == "north":
            forest(player)
            break
        elif choice == "south" or choice == "east":
            print("The mountain blocks your path.")
            choice = location.get_choice()
        elif choice == "west":
            left_valley(player)
            break

def left_valley(player):
    # left valley recieves the player argument
    # it generates the left valley location
    
    # get the location
    location = get_location(player, "left_valley")
    player.set_location("left_valley")
    save_game(player)
    
    # print the location
    print(location)
    
    # get the choice
    choice = location.get_choice()
    
    # translate it and move the player
    while True:
        if choice == "north":
            print("The forest is too dense to pass through.")
            choice = location.get_choice()
        elif choice == "south":
            print("The mountain is blocking your path.")
            choice = location.get_choice()
        elif choice == "west":
            zummies_domain(player)
            break
        elif choice == "east":
            right_valley(player)
            break
    
def ocean(player):
    # ocean recieves the player argument
    # it generates the player scene
    
    # get thel ocation
    location = get_location(player, "ocean")
    player.set_location("ocean")
    save_game(player)
    
    # print the location
    print(location)
    
    # up max hp and heal to max
    max_hp = player.get_max_health()
    max_hp += 20
    print("You gained +20 max health.")
    
    player.set_max_health(max_hp)
    player.heal(20000000)
    
    # print the health
    print(f"Your health is now at {player.get_health()} out of {player.get_max_health()}.")
    
    # get the choice
    choice = location.get_choice()
    
    # translate the choice and move the player
    while True:
        if choice == "east":
            print("That leads to an advance of ocean, no reason to go there.")
            choice = location.get_choice()
        elif choice == "south" or choice == "north":
            print("That leads to a advance of beach, no reason to go there.")
            choice = location.get_choice()
        else:
            right_path(player)
            break
        
def castle(player):
    # castle recieves the player argument
    # it is the final locatino in the game
    # and it has the final boss
    # and after that, it leads you to the credits.
    
    # get location
    location = get_location(player, "castle")
    player.set_location("castle")
    save_game(player)
    
    # get the locations enemies
    enemies = location.get_enemies()
    
    # make sure bro wasnt dead by the time we got there
    if enemies != []:
        # start the fight
        print("Zumwalt approaches you...")
        fight = game_classes.Fight(player, enemies[0])
        outcome = fight.run_fight()
        
        # validate outcomes
        if outcome == "ran":
            print("A voice bellows behind you:")
            print("Zumwalt, King of Etheria: Cowardly!")
            print("As he yells, the clouds darken.")
            print("Lightning starts striking near you.")
            print("Lightning hits you, killing you on the spot.")
            death(player)
        elif outcome == "enemy dead":
            location.clear_enemies()
            print("Zumwalt, King of Etheria: You've bested me in combat. I will allow you to pass.")
            print("Lightning strikes Zumwalt and he dies, with a thud.")
        else:
            death(player)
            
    # get the choice
    choice = location.get_choice()
    
    while True:
        if choice == "east" or choice == "west":
            print("The castle walls are too tall to climb or get around.")
            choice = location.get_choice()
        elif choice == "south":
            center_path(player)
            break
        else:
            print("Thank you for playing")
            print("You win!")
            death(player)
            main()
            break
          
main()
