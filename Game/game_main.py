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
    weapons = {"sword" : [15, 30], "battle axe" : [20, 55], "dagger" : [5, 0], "gauntlets" : [10, 20]}
    weapon = ""

    print("---Character Creator---")
    # get the name
    name = input("Please enter the name of your character (First and last if it has a last): ")
    
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
        print(f"Location: {person.get_location()}\n1")
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
        except:
            file = open("game_saves.dat", "wb")
            data = []
            file.close()
    else:
        # open and close the file if it DOESNT exist to create it
        file = open("game_saves.dat", "wb")
        data = []
        file.close()

    # check to see if the name of a save is the same as another and add it if it does
    for item in data:
        if item.get_name() == player.get_name():
            data.remove(item)
            data.append(player)
        else:
            data.append(player)

    # write it to the file
    file = open("game_saves.dat", "wb")
    pickle.dump(data, file)
    file.close()

    print("Game successfully saved.")

main()