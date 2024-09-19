def main():
    # main acepts no arguments
    # it will prompt the user with a menu
    # and ask the user to make a choice
    # and will call the function depending on the user choice.
    
    # declare variable for the user choice
    choice = 0
    
    # output the menu
    print("Choose a program from the follopwing options:")
    print("1: Exercise 1 - Days of the week")
    print("2: Exercise 4 - Roman Numerals")
    print("3: Exercise 7 - Color Mixer")
    print("4: Exercise 8 - Hotdog Competition")
    print("5: Exercise 15 - Time Calculator")
    print("6: Exercise 16 - February Days")
    print("7: Exercise 17 - WiFi Diagnostic Tree")
    print("8: Exercise 18 - Resturant Selector")
    print("9: Exercise 19 - Hit The Target Modification")
    
    # get input for the user choice
    choice = int(input(":> "))
    
    # process the menu
    if choice == 1:
        print("Calling... Days of the week...")
        day_converter()
    elif choice == 2:
        print("Calling... Roman Numerals...")
        roman_numerals()
    elif choice == 3:
        print("Calling... Color Mixer...")
        color_mixer()
    elif choice == 4:
        print("Calling... Hotdog Competition...")
        hot_dog()
    elif choice == 5:
        print("Calling... Time Calculator...")
        time_calculator()
    elif choice == 6:
        print("Calling... February Days...")
        leap_year()
    elif choice == 7:
        print("Calling... WiFi Diagnostic Tree")
        sir_fix_alot()
    elif choice == 8:
        print("Calling... Resturant Selector...")
        can_we_just_eat()
    elif choice == 9:
        print("Calling... Hit The Target modification...")
    else:
        print("Please only input a valid choice")

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
        print("The number must be between 1-10!")
        
        
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


def hot_dog():
    # hot dog recieves no arguments
    # it asks the user for a amount of people going and how many hotdogs each person can have for a cookout.
    # outputs how much packages they need to buy and how much left over.

    # initialize variables
    hotdogPackage = 10
    bunPackage = 8

    # asks user for people going and amount each person gets
    peopleGoing = int(input("Enter the amount of people going : "))
    amountPeopleGet = int(input("Enter the amount of hotdogs each person can have : "))

    # calculates the amount of hotdogs can be eaten total
    hotdogsPossible = peopleGoing * amountPeopleGet
    
    # finds amount of hotdogs and hotdog buns needed
    hotdogsNeeded = hotdogsPossible // hotdogPackage
    hotdogsBuns = hotdogsPossible // bunPackage
    
    hotdogsNeededM = hotdogsPossible % hotdogPackage
    hotdogsBunsM = hotdogsPossible % bunPackage
    
    if hotdogsBunsM != 0:
        hotdogsBuns = hotdogsBuns + 1
    if hotdogsNeededM != 0:
        hotdogsNeeded = hotdogsNeeded + 1
    print("You need ",hotdogsBuns, " hotdog buns and ", hotdogsNeeded, " hotdogs.")
    print("With ", hotdogsNeededM, " extra hotdogs and ", hotdogsBunsM, " leftover.", sep = '')

def time_calculator():
    # time_calculator recieves no arguments
    # asks user for time in seconds
    # outputs it as days, hours, minutes, and seconds
    
    # assigns variables
    daysSecond = 86400
    hoursSeconds = 3600
    minuteSeconds = 60
    timeInSeconds = int(input("Please enter a number of seconds: "))
    
    
    if timeInSeconds > 0:
        if timeInSeconds > daysSecond:
            days = timeInSeconds // daysSecond
            timeInSeconds = timeInSeconds - (days * daysSecond)
            print("Days : ", days, sep = '')
        if timeInSeconds > hoursSeconds:
            hours = timeInSeconds // hoursSeconds
            timeInSeconds = timeInSeconds - (hours * hoursSeconds)
            print("Hours : ", hours, sep = '')
        if timeInSeconds > minuteSeconds:
            minutes = timeInSeconds // minuteSeconds
            timeInSeconds = timeInSeconds - (minutes * minuteSeconds)
            print("Minutes : ", minutes, sep = '')
        print("Seconds : ", timeInSeconds, sep = '')
    else:
        print("Invalid time entered")
    


def leap_year():
    print("")


def sir_fix_alot():
    print("f")


def can_we_just_eat():
    print("f")


def hit_the_target_mod():
    print("f")

main()
