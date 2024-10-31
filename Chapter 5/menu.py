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
    while choice < 0:
        choice = int(input(":> "))
    
    # process the menu
    if choice == 1:
        print("Calling... Exercise 1...")
        sales_tax()
    elif choice == 2:
        print("Calling... Exercise 2...")
        calories()
    elif choice == 3:
        print("Calling... Exercise 3...")
        stadium_seating()
    elif choice == 4:
        print("Calling... Exercise 4...")
        paint_estimator()
    elif choice == 5:
        print("Calling... Exercise 5...")
        math_quiz
    elif choice == 6:
        print("Calling... Exercise 6...")
        falling_distance
    elif choice == 7:
        print("Calling... Exercise 7...")
        rock_paper_scissors()
    elif choice == 8:
        print("Calling... Exercise 8...")
        modular_snowman()
    elif choice == 9:
        print("Calling... Exercise 9...")
        checkerboard()
    
    while runMain == True:
        runMain = input("Do you want to quit the program? :>")
    if runMain == "No" or runMain == "no":
        t.clearscreen()
        main()
    else:
        print("Goodbye")
        runMain == False

#==========================