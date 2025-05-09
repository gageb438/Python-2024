import game_classes
import os
import random
import pickle


def main():
    # main recieves no arguments
    # it drives the adventure game
    # it outputs all steps

    # initialize varaibles
    game_name = "i couldnt find one, silly"

    print(f"Welcome to {game_name}.")
    
    choice = main_menu()

    if choice == 1:
        new_save()
    elif choice == 2:
        player = load_save()
        if player == False:
            main()
            return
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
    print("1: New Save")
    print("2: Load Save")
    print("3: Quit")

    while choice not in choices:
        try:
            # get choice
            choice = int(input(":> "))
            
            # check to make sure theres gamesaves if they chose to load
            if choice == 2:
                if not os.path.exists("game_saves.dat"):
                    choice = -1
                    print("No game saves found, please create one first.")
        except:
            # on exception, pass, restarting the loop
            pass
    
    # return the users choice.
    return choice


#-------------------------------------------------------
# PLAYER SAVE FUNCTIONS

def new_save():
    # new save does not recieve any arguments
    # it creates a new save for the player
    
    # initialize valid weapons
    sword = game_classes.Weapon("Sword", 20, 1)
    dagger = game_classes.Weapon("Dagger", 10, 2)

    print("---Character Creator---")

    # initialize looping variable
    good = False

    # check if the name is being used in our save file
    while good == False:
        # get input for the name
        name = input("Please enter the name of your character (First and last if it has a last): ")

        # check if the file exists, and then load the data
        if os.path.exists("game_saves.dat"):
            file = open("game_saves.dat", "rb")
            try:
                data = pickle.load(file)
            except:
                data = []
            
            # close the file
            file.close()

            # check if the name is being used
            if data != []:
                for item in data:
                    # preset good variable
                    good = True
                    
                    if item.get_name() == name:
                        good = False
            else:
                good = True
        else:
            # if name wasnt being used or file didnt exist, set good to true, stopping the loop from running
            good = True

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
    data = generate_locations()
    # make the character
    player = game_classes.Hero(name, weapon, 100, 100, "tutorial", data, [])
    
    # call save game with player
    # then call main game
    save_game(player)
    main_game = tutorial(player)
    
    if main_game == "death":
        death(player)
    else:
        clearing(player)
    

def load_save():
    # load save recieves no arguments
    # it prints all saves
    # and loads one of the user choice

    # check if the file exists
    if os.path.exists("inventory.dat"):
        file = open("inventory.dat", "rb")
        
        # load the file
        try:
            data = pickle.load(file)
        except:
            # print the error and return it
            print("No saves found, create one first.")
            return
        
        # read the data and print each objects info
        for item in data:
            name = item.get_name()
            weapon = item.get_weapon()
            weapon_name = weapon.get_name()
            
            print(f"\nName: {name}")
            print(f"Weapon: {weapon}")
        
        # get the users choice
        choice = input("What save would you like to load? (NAME ONLY, CASE SENSITIVE): ")
        
        # set the blank player variable
        player = 1
        
        for item in data:
            if item.get_name() == choice:
                player = item
          
        if player == 1:
            print("Player not found.")
            return
        
        tutorial(player)
        
        


def save_game(player):
    # save game recieves an argument for the character object
    # it then adds it to a file
    # and pickles it
    
    # preset data
    data = []
    
    # get the data
    if os.path.exists("game_saves.dat"):
        try:
            file = open("game_saves.dat", "rb")
            data = pickle.load(file)
            file.close()
        except EOFError:
            data = []
        except Exception as error:
            print(error)
    else:
        # open and close the file if it DOESNT exist to create it
        file = open("game_saves.dat", "wb")
        data = []
        pickle.dump(data, file)
        
        file.close()

    # check to see if there is an old file under the same name
    for item in data:
        if item.get_name() == player.get_name():
            data.remove(item)
    
    # add it to the data
    data.append(player)

    # write data to the file
    file = open("game_saves.dat", "wb")
    pickle.dump(data, file)
    file.close()

    print("Game successfully saved.")

#-------------------------------------------------------
# LOCATION FUNCTIONS
def tutorial(player):
    # tutorial recieves the player argument\
    # it creates the tutorial location

    # initalize variables
    choice = -1
    choices = ["1","2"]
    weapon = player.get_weapon().get_name()

    # print the welcome screen
    print("Welcome to the tutorial, if you would like to do it, press 1.\nIf you would like to skip it, press 2.")
    
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
            return "main_game"
        elif choice == "player_dead":
            print("Odd. You managed to die in the tutorial, either really bad luck, or your just horrible.")
            return "death"
        else:
            print("Perplexing. You might be cut out for this, good work.")
            return "main_game"
    else:
        return "main_game"  

def generate_loc():
    clearing_loc = game_classes.Location("clearing", "You are in a empty clearing.\nTo the north, there is a empty pathway.\nTo the south, there is a cluttered forest.\nThe east and west are too dense of a forest to go through.", ["north", "east", "south", "west"], [], [])
    center_path_loc = game_classes.Location("center_path", "You are in a the middle of a path.\nTo the north, there is a castle, it seems like you shouldn't be there until later.\nTo the east and west, there is more path.\nTo the south, there is a clearing.", ["north", "east", "south", "west"], [], [])
    left_path_loc = game_classes.Location("left_path", "You are in the middle of a path.\nThe north and south are blocked by dense forests.\nTo the east, there is more path.\nTo the west, there is a town, seemingly empty.", ["north", "east", "south", "west"], [], [])
    right_path_loc = game_classes.Location("right_path", "You are in the middle of a path.\nThe north and south are blocked by dense forests.\nTo the east, there is a ocean.\nTo the west, there is a path.", ["north", "east", "south", "west"], [], [])
    ocean_loc = game_classes.Location("ocean", "You are on a beach of the ocean.\nThe ocean is calming to you. It heals you back to max hp, and gives you some extra health.\nThere is nowhere to go, other than west, leading back to a path.", ["north", "east", "south", "west", [], []])
    ghost_town_loc = game_classes.Location("ghost_town", "You are in a town, it seems ancient and abandoned.\nTo the north, there is a cave.\nTo the east, there is a path.\nTo the west, there is a weapon forge.\nThe south is too dense of a forest to get through.", ["north", "east", "south", "west"], [], [])
    forge_loc = game_classes.Location("forge", "You are in a forge, abandoned by society.\nTo the east, is a town, seemingly abandoned.\nThe north, west, and south are too dense of a forest to get through.", ["north", "west", "east", "south", "forge", "smith"], [], [])
    cave_enemy_weapon = game_classes.Weapon("Sword", 10, 1)
    cave_enemy = game_classes.Enemy("skeleton", cave_enemy_weapon, 50, 50)
    cave_loc = game_classes.Location("cave", "You entered a dark cave.\nThe only way out is to the south.", ["north", "east", "south", "west"], [cave_enemy], [])
    forest_loc = game_classes.Location("forest", "You are in a dense forest.\nTheres a path to the north, leading to a clearing.\nThe west leads to more forest.\nThe east leads to more forest, its more dark and ominous than the one on the west.\nThe south leads to a valley.", [], [])
    slime_enemy_weapon = game_classes.Weapon("Goop", 5, 1)
    slime_enemy = game_classes.Enemy("Slime", slime_enemy_weapon, 50, 50)
    slime_forest_loc = game_classes.Location("slime_forest", "You are in a dense forest.\nTheres a more forest to the east.\nAll other directions are too dense to get to.", [slime_enemy], [])
    
    
    
    
def clearing(player):
    # clearing recieves the player argument
    # it is the main spawn of the game
    # it 
    pass


main()