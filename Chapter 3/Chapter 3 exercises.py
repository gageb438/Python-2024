def day_converter():
    # day converter recieves no arguments
    # asks the user for a number form 1-7 and converts it to spanish.
    # prints an error message if it isnt in value of 1-7. outputs what day it is in spanish.
    
    # asks for the day number
    dayNumber = int(input("Enter a number 1-7 for the day: "))
    
    # prints the day in spanish or an error message.
    if dayNumber == 1:
        print("The day is lunes")
    elif dayNumber == 2:
        print("The day is martes")
    elif dayNumber == 3:
        print("The day is miercoles")
    elif dayNumber == 4:
        print("The day is jueves")
    elif dayNumber == 5:
        print("The day is viernes")
    elif dayNumber == 6:
        print("The day is sabado")
    elif dayNumber == 7:
        print("The day is domingo")
    else:
        print("The day number must be between 1 and 7!")
            

def roman_numerals():
    # roman numerals recieves no arguments
    # asks the user for a number 1-10 and converts it to roman numerals
    # outputs a roman numeral or an error
    
    dayNumber = int(input("Input a number 1-10 which you would like converted to Roman Numerals : "))
    
    if dayNumber == 1:
        print("The Roman Numeral is : I")
    elif dayNumber == 2:
        print("The Roman Numeral is : II")
    elif dayNumber == 3:
        print("The Roman Numeral is : III")
    elif dayNumber == 4:
        print("The Roman Numeral is : IV")
    elif dayNumber == 5:
        print("The Roman Numeral is : V")
    elif dayNumber == 6:
        print("The Roman Numeral is : VI")
    elif dayNumber == 7:
        print("The Roman Numeral is : VII")
    elif dayNumber == 8:
        print("The Roman Numeral is : VIII")
    elif dayNumber == 9:
        print("The Roman Numeral is : IX")
    elif dayNumber == 10:
        print("The Roman Numeral is : X")
    else:

def color_mixer():
    # color_mixer recieves no arguments
    # it asks the user for two colors to mix and mixes them
    # outputs what color they got from mixing the two.

    primary1 = "nil"
    primary2 = "nil"
    
    # asks for the first color
    primary1 = input("Please enter the first primary color to mix (lowercase): ")
    
    # asks for a second color
    primary2 = input("Please enter the second primary color to mix: ")

    # validates it is a primary color
    
    if primary1 == "red" or "yellow" or "blue" and primary2 == "red" or "yellow" or "blue":
        if primary1 == "red" and primary2 == "red":
            print("The new color is red.")
        elif primary1 == "red" and primary2 == "blue" or primary1 == "blue" and primary2 == "red":
            print("The new color is purple.")
        elif primary1 == "red" and primary2 == "yellow" or primary1 == "yellow" and primary2 == "yellow":
            print("The new color is orange.")
        elif primary1 == "blue" and primary2 == "blue":
            print("The new color is blue.")
        elif primary1 == "blue" and primary2 == "yellow" or primary1 == "yellow" and primary2 == "blue":
            print("The new color is green.")
        elif primary1 == "yellow" and primary2 == "yellow":
            print("The new color is yellow.")
        else:
            print("Error, color combination not found or not two primary colors")
