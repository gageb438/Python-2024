import random
import os

'''
HELPER STRINGS -- Feel free to copy these lines to aid in your printouts:


Press Enter when you are ready to begin...

You encountered ___

Enter:  '1' to use your ___
        '2' to run away
Your choice: ___

Press Enter to continue...

You won the fight!

You lost the fight...

You ran away.

You made it to the other town!

You left the game.
'''

# Write your functions here

def game_loop():
    
    print("\nWelcome adventurer.")
    
    # get the name and weapon here
    name = get_name()
    weapon = get_weapon()
    
    print("\nHello,", name)
    print("Welcome to The Legend of Python!")
    print("Before you is a path that you must take to reach the next town.")
    print("However, there are monsters roaming the path up ahead, and you")
    print("must be prepared to battle!")
    print("I see you have your trusty ", weapon, ". You will need it.", sep="")
    
    # get input to continue
    enter = input("Press Enter when you are ready to begin...")
    
    while enter != "":
        enter = input("Press Enter when you are ready to begin...")
    
    for num in range(3):
        encounter(weapon)
    
    game_over(name,weapon)

def main():
    
    print("Game Menu")
    print("Enter '1' to start the game")
    print("Enter '2' to see the previous adventurer's stats")
    print("Enter '3' to quit the game")
    
    # start coding here
    
    # initalize variable
    choice = int(input("Your choice: "))
    
    while choice < 1 or choice > 3:
        try:
            while choice > 3 or choice < 1:
                print("Invalid input.")
                choice = int(input("Your choice: "))
        except:
            print("Invalid input.")
            
    if choice == 1:
        game_loop()
    elif choice == 2:
        previous_adventurer()
    elif choice == 3:
        print("\nYou left the game.")
        return
    
def get_name():
    # get name recieves no arguments
    # it asks the user for their name and returns it to game_loop
    
    # ask for the users name
    name = input("What is your name?: ")
    
    # return their name
    return name


def get_weapon():
    # get weapon receives no arguments
    # it asks the user for their name and returns it to game_loop
    
    # ask for weapon
    weapon = input("What is your weapon?: ")
    
    # return their weapon
    return weapon


def encounter(weapon):
    # encounter recieves an argument for the user weapon
    # it picks a random encounter by a 1 and 3 chance for each
    
    monster = random.randint(1,3)
    
    if monster == 1:
        # read the monster one file
        outfile = open("monsterOne.txt", "r")
    elif monster == 2:
        # read the monster two file
        outfile = open("monsterTwo.txt", "r")
    else:
        # read the monster three file
        outfile = open("monsterThree.txt", "r")
        
    # print out what they encountered
    # and read the file to find the monster encounter
    encounter_header = outfile.readline()
    encounter_bio = outfile.readline()
    
    print(f"\nYou've encountered {encounter_header}\n{encounter_bio}")
    
    # close the file
    outfile.close()
        
    # ask the user if they want to fight or run
    print(f"Enter:\t'1' to use your {weapon}\n\t'2' to run away")
    
    # initalize choice
    choice = 3
    
    # check use choice
    # and validate
    while choice != 1 or choice != 2:
        try:
            choice = int(input("Your choice: "))
            if choice == 1 or choice == 2:
                break
            else:
                print("Invalid input")
        except:
            print("Invalid input")
    
    # find user win chance if they chose to fight if they chose to run print exiting message
    if choice == 1:
        win_chance = random.randint(1,5)
        
        if win_chance == 3:
            print("You lost the fight...")
        else:
            print("You won the fight!")
    else:
        print("You ran away")

    enter_cont = "a"
    while enter_cont != "":
        enter_cont = input("Press Enter to continue... ")
    

def game_over(name, weapon):
    # game over recieves an argument for user name and weapon
    # it will congratulate user for reaching the end and save their name
    # and weapon to a file
    
    print("\nYou made it to the other town!")
    # open file
    infile = open("previousAdventurer.txt", "w")
    
    # write name and weapon
    infile.write(name + "\n")
    infile.write(weapon + "\n")
    
    # close the file
    infile.close()
    
def previous_adventurer():
    # previous adventurer recieves no arguments
    # it calls the previous adventurers name and waepon
    # it then prints them
    
    # checks if the file exists
    if os.path.exists("previousAdventurer.txt"):
        outfile = open("previousAdventurer.txt", "r")
    else:
        print("\nNo previous adventurer found. Looks like you are the first one.\n")
        main()
    
    name = outfile.readline().rstrip("\n")
    weapon = outfile.readline().rstrip("\n")
    
    # print name and weapon
    print(f"\nName: {name}")
    print(f"Weapon: {weapon}\n")
    
    main()
    
main()






















