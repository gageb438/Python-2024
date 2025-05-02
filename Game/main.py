import game_classes

# create the menu
def main_menu():
    # main menu recieves no arguments
    # it prints the main menu, gets a choice
    # and outputs
    
    # set game name because i cant pick one and stick with it
    # for the life of me
    game_name = "The binding of Anthony"
    
    # print the actual menu
    print(f"---Welcome to {game_name}---")
    print("What would you like to do?")
    print("1. New Game")
    print("2. Load Game")
    print("3. Exit")
    
    # set the choices
    choices = ["1", "2", "3"]
    choice = -1
    
    # get the choice
    while choice not in choices:
        choice = input(":> ")
    
    if choice == "1":
        new_game()
    elif choice == "2":
        load_game()
    else:
        print(f"Thank you for playing {game_name}, goodbye!")

# create new game
def new_game():
    # new game recieves no arguments
    # it creates a new player
    # and gets their choices for what they want
    
    # get the player name
    name = input("Please enter your characters name: ")
    
    # create the weapons
    sword = game_classes.Weapon("Sword", 20)
    