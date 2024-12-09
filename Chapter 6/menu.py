# imports
import turtle as t

#==========================

def menu(exercise):
    # main accepts an argument for how many exercises are wanted
    # it will prompt the user with a menu
    # and ask the user to make a choice
    # and will call the function depending on the user choice.
    
    # declare variable for the user choice
    choice = 0
    
    # output the menu
    print()
    print("Choose a program from the following options.")
    for exerciseNumber in range(1, exercise + 1):
        print(f"{exerciseNumber}: Exercise {exerciseNumber}")
    print("0: Exit")
    # get input for the user choice
    choice = int(input(":> "))
    while choice < 1 or choice > exercise:
        choice = int(input(":> "))
    print()
        
    print(f"Calling... Exercise {choice}...")
    print()
    return choice

#==========================