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
    print("1: Exercise 2 - Sales Tax Program Mod")
    print("2: Exercise 6 - Calories")
    print("3: Exercise 7 - Stadium Seating")
    print("4: Exercise 8 - Paint Job Estimator")
    print("5: Exercise 11 - Math Quiz")
    print("6: Exercise 13 - Falling Distance")
    print("7: Exercise 21 - Rock, Paper, Scissors, Lizard, Spock")
    print("8: Exercise 23 - Turtle Graphics - Modular Snowman")
    print("9: Exercise 25 - Turtle Graphics - Checkerboard")
    
    # get input for the user choice
    choice = int(input(":> "))
    while choice < 0:
        choice = int(input(":> "))
    
    # process the menu
    if choice == 1:
        print("Calling... Sales Tax Program Mod...")
        sales_tax()
    elif choice == 2:
        print("Calling... Calories...")
        calories()
    elif choice == 3:
        print("Calling... Stadium Seating...")
        stadium_seating()
    elif choice == 4:
        print("Calling... Paint Job Estimator...")
        paint_estimator()
    elif choice == 5:
        print("Calling... Math Quiz...")
        math_quiz
    elif choice == 6:
        print("Calling... Falling Distance...")
        falling_distance
    elif choice == 7:
        print("Calling... Rock, Paper, Scissors, Lizard, Spock...")
        rock_paper_scissors()
    elif choice == 8:
        print("Calling... Modular Snowman...")
        modular_snowman()
    elif choice == 9:
        print("Calling... Checkerboard...")
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
        
