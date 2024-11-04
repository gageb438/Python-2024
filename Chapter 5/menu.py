# imports area
import math
import turtle as t
import random

#==========================

def main():
    # main accepts no arguments
    # it will prompt the user with a menu
    # and ask the user to make a choice
    # and will call the function depending on the user choice.
    
    # declare variable for the user choice
    choice = 0
    runMain = True
    
    # output the menu
    print()
    print("Choose a program from the following options:")
    print("1: Exercise 1")
    print("2: Exercise 2")
    print("3: Exercise 3")
    print("4: Exercise 4")
    print("5: Exercise 5")
    print("6: Exercise 6")
    print("7: Exercise 7")
    print("8: Exercise 8")
    print("9: Exercise 9")
    
    # get input for the user choice
    choice = int(input(":> "))
    while choice < 1 or choice > 9:
        choice = int(input(":> "))
    
    # process the menu
    if choice == 1:
        print("Calling... Exercise 1...")
        return 1
    elif choice == 2:
        print("Calling... Exercise 2...")
        return 2
    elif choice == 3:
        print("Calling... Exercise 3...")
        return 3
    elif choice == 4:
        print("Calling... Exercise 4...")
        return 4
    elif choice == 5:
        print("Calling... Exercise 5...")
        return 5
    elif choice == 6:
        print("Calling... Exercise 6...")
        return 6
    elif choice == 7:
        print("Calling... Exercise 7...")
        return 7
    elif choice == 8:
        print("Calling... Exercise 8...")
        return 8
    elif choice == 9:
        print("Calling... Exercise 9...")
        return 9
        
    while runMain == True:
        runMain = input("Do you want to quit the program? :> ")
    if runMain == "No" or runMain == "no":
        t.clearscreen()
        main()
    else:
        print("Goodbye")
        runMain == False

#==========================