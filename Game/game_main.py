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


def new_save():
    # new save does not recieve any arguments
    # it creates a new save for the player
    
    # initialize valid weapons + damage + miss chance
    weapons = {"Sword" : [15, 30], "Battle Axe" : [20, 55], "Dagger" : [5, 0], "Gauntlets" : [10, 20]}
    weapon = ""

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
            data = pickle.load(file)
            # close the file
            file.close()

            # check if the name is being used
            for item in data:
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
    for item in weapons:
        item_data = weapons[item]
        
        print(f"\nWeapon : {item}")
        print(f"Damage : {item_data[0]}")
        print(f"Miss Chance : %{item_data[1]}")

    # get users choice
    while weapon not in weapons:
        print("\nWhat weapon would you like (with spaces if it has them)?")
        weapon = input(":> ")
    
    # lowercase the weapon for getting correct damage values with the class
    weapon = weapon.lower()
    
    # make the character
    player = game_classes.Hero(name, weapon)
    
    # call save game with player
    save_game(player)
    

def load_save():
    # load save recieves no arguments
    # it prints all saves
    # and loads one of the user choice

    # create save dictionary
    save_dict = {}

    print("Saves:")

    file = open("game_saves.dat", "rb")
    saves = pickle.load(file)   

    for person in saves:
        # print the name and add it to a dictionary
        print(f"Name: {person.get_name()}")
        print(f"Location: {person.get_location()}\n")
        # add it to the dictionary
        save_dict[person.get_name()] = person
    
    choice = input("Enter the name of the person save exactly, if it has spaces, add spaces.\n:> ")

    if choice in save_dict:
        player = save_dict[choice]
    else:
        print("No player found.")
        # return false if it doesnt exist
        return False
    
    # return player if it exists
    return player


def save_game(player):
    # save game recieves an argument for the character object
    # it then adds it to a file
    # and pickles it
    
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


def main_game(player):
    # main game recieves the player argument
    # main game loops and runs the game
    # it calls the tutorial first

    tutorial

def tutorial(player):
    # tutorial just shows the user how to interact
    # it recieves an argument for the player object
    # and returns the player
    
    def bridge_start(player):
        # bridge start recieves a player argument
        # and teachs the player how to look around and move

        # print the guide
        print("You look around, you are on a bridge, surrounded by a black fog.")
        print("The only thing that shines through the fog is a white light.")
        print("You can hear a faint voice, too quiet to make out what its saying.")
        print("You can go north and south on the bridge, the north path has the light, the south does not.")
        print("[GUIDE] Type north or south into the terminal to pick where to go.")
        
        # initialize loop
        moving = False

        while moving == False:
            choice = input(":> ")

            # set the choices
            choices = ["north", "south", "west", "east", "up", "down", "look"]
            if choice.lower() == "west" or choice.lower() == "east":
                print("You attempt to move that way, theres no where to go other than falling.")
            elif choice.lower() == "up":
                print("You reach up, theres nowhere to go.")
            elif choice.lower() == "down":
                print("You cant go down, without falling.")
            elif choice.lower() == "north":
                print("You move north.")
                moving = True
            elif choice.lower() == "south":
                print("You move south.")
                moving = True
            else:
                print("You look around, you are on a bridge, surrounded by a black fog.")
                print("The only thing that shines through the fog is a white light.")
                print("You can hear a faint voice, too quiet to make out what its saying.")
                print("You can go north and south on the bridge, the north path has the light, the south does not.")
                print("[GUIDE] Type north or south into the terminal to pick where to go.")

        if choice.lower() == "south":
            return "dark"
        else:
            return "light"
    
    def dark_bridge(player):
        # dark bridge recieves an argument for the player
        # it teaches them how to fight
        # and then lets them go back to the light bridge

        # make an enemy
        enemy = game_classes.Enemy("Skeleton", ["Sword", 10, 20], 50)

        # print that they found an enemy
        print(f"You walk along the bridge, you see a {enemy.get_name()}! He is holding a {enemy.get_weapon()}")
        print("[GUIDE] You found an enemy, to fight it, you must attack, type ATTACK into the console to fight it.")
        print("[GUIDE] Or if you don't want to, type RUN into the console.")
        print("[GUIDE] However if you choose to fight, you won't be able to run after starting.")

        # prime the loop
        run_able = True
        moving = False

        # start the loop
        while moving == False:
            # get choice and set valid choices
            choice = input(":> ")
            choice = choice.lower()
            choices = ["look", "north", "east", "south", "west", "up", "down", "attack", "run"]
            
            # get the users input if it wasnt valid
            while choice not in choices:
                print(f"{choice} not recognized as a valid command.")
                choice = input(":> ")
                choice = choice.lower()
            
            if choice == "look":
                print(f"You look around to see you and a {enemy.get_name()} on a dark bridge surrounded by fog.")
                print("Your north, east, and west seemed to be clear, but when you try to move to them, your body won't let you.")
                print("Heading south returns you back to the other bridge.")
            elif choice == "north" or choice == "west" or choice == "east":
                print("You try to move, your body wont let you.")
            elif choice == "run" or choice == "south":
                if run_able == True:
                    moving = True
                    return "ran"
                else:
                    print("You've already started this fight, no turning back now.")
            
            elif choice == "attack":
                run_able = False


    # print the welcome
    print(f"Welcone {player.get_name()}!")
    print("[GUIDE] This is the tutorial to teach you how to interact.")
    print("[GUIDE] If you would like to skip this, type SKIP in the terminal.")
    print("[GUIDE] If you would like to continue, type LOOK.")

    while choice.lower() != "skip" and choice.lower() != "look":
        print(f"{choice} not recognized as a valid command.")
        choice = input(":> ")

    # if skip, return, if they dont, show guide
    if choice.lower() == "skip":
        return player
    else:
        # get new player while walking through
        choice = bridge_start(player)
        if choice == "dark":
            # call dark bridge scene
            player = dark_bridge(player)
    


main()