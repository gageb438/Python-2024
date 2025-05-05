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

    # make the character
    player = game_classes.Hero(name, weapon, 100, 100, "tutorial")
    
    # call save game with player
    # then call main game
    save_game(player)
    tutorial(player)
    

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
    main_game(player)


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

#-------------------------------------------------------
# LOCATION FUNCTIONS
def tutorial(player):
    # tutorial recieves the player argument
    # since it is a special locaion
    # it needs its own function

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

        if options[0] != "grab" and options[1] != weapon:
            # validate choice
            print(f"{option} not recognized as a command.")
            option = input(":> ")
        else:
            print(f"You grab your {weapon}.")
        
        
        # print the next area
        print(f"You advance through the cave, armed with your {weapon} and see a skeleton!")
        print("HINT: You are now faced with your first enemy and have a few options:")
        print("You can attack it by tying attack skeleton.")
        print("You can run from it by typing run")
        print("You can try to avoid its attack by typing dodge")
        
        # create the skeleton enemy and its wepaon
        s_weapon = game_classes.Weapon("Sword", 10, 1)
        skeleton = game_classes.Enemy("Skeleton", s_weapon, 50, 50)

        fight = game_classes.Fight(player, skeleton)
        fight.run_fight()
            
            



main()