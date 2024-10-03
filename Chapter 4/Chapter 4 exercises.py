# imports
import math
import turtle as t

def main():
    # main acepts no arguments
    # it will prompt the user with a menu
    # and ask the user to make a choice
    # and will call the function depending on the user choice.
    
    # declare variable for the user choice
    choice = 0
    
    # output the menu
    print("Choose a program from the follopwing options:")
    print("1: Exercise 1 - Bug Collector")
    print("2: Exercise 4 - Distance Traveled")
    print("3: Exercise 13 - Population")
    print("4: Exercise 14 - Reverse Triangle")
    print("5: Exercise 15 - Stair Pattern 2")
    print("6: Exercise 16 - Repeating Square")
    print("7: Exercise 18 - Hypnotic Pattern")
    
    # get input for the user choice
    choice = int(input(":> "))
    while choice <= 0:
        choice = int(input(":> "))
    
    # process the menu
    if choice == 1:
        print("Calling... Bug Collector...")
        bug_collector()
    elif choice == 2:
        print("Calling... Distance Traveled...")
        distance_traveled()
    elif choice == 3:
        print("Calling... Population...")
        popluation()
    elif choice == 4:
        print("Calling... Reverse Triangle...")
        reverse_triangle()
    elif choice == 5:
        print("Calling... Stair Pattern 2...")
        stair_pattern_2()
    elif choice == 6:
        print("Calling... Repeating Square...")
        repeating_squares()
    elif choice == 7:
        print("Calling... Hypnotic Pattern...")
        hypnotic_pattern()
    
        
        
def bug_collector():
    # bug_collector recieves no arguments
    # it asks user for how many bugs they have collected each day
    # outputs total bugs
    
    # initialize variables
    total = 0
    days = 5
    # prints header
    print("Welcome to the Bug Masteres bug collection system.")
    
    # finds the amount of bugs collected
    for day in range(days + 1):
        collected = int(input("How many bugs did you collect on day ", day, "?", sep = ''))
        
        # validates
        while collected <= 0:
            collected = int(input("Enter a valid number of bugs you collected on day ", day, ".", sep = ''))
            
        # sets total
        total = total + collected
        
        # resets collected
        collected = 0
    
    print("Great job, you collected ", total, " bugs this week. You're the bug master!", sep = '')
    