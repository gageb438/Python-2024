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
    print("Choose a program from the following options:")
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
        population()
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
    
    print()
    
    # finds the amount of bugs collected
    for day in range(1, days + 1):
        print("How many bugs did you collect on day ", day, "?", sep = '', end = '')
        collected = int(input(" :> "))
        
        # validates
        while collected <= 0:
            collected = int(input("Enter a valid number of bugs you collected on day ", day, ".", sep = ''))
            
        # sets total
        total = total + collected
        
        # resets collected
        collected = 0
        
    print()
    
    print("Great job, you collected ", total, " bugs this week. You're the bug master!", sep = '')
    
    
def distance_traveled():
    # distance traveled recieves no arguments
    # it asks the user for how fast they were going and how many hours they were traveling
    # outputs the distance they will have traveled by then.
    
    # finds and validates the mph and hours traveled
    speed = int(input("Enter the speed of the vehicle in mph: "))
    
    while speed <= 0:
        speed = int(input("Enter a valid speed of the vehicle in mph: "))
    
    hours = int(input("Enter the amount of hours the vehicle traveled: "))
    
    while hours <= 0:
        hours = int(input("Enter a valid amount of hours the vehicle traveled: "))
    
    # prints header
    print("Hour \t\t Distance Traveled")
    print("----------------------------------")
    
    for hour in range(1, hours + 1):
        distance = speed * hour
        
        print(hour, "\t\t", distance)
    
    
def population():
    # population recieves no arguments
    # it asks the user for the starting population, percent of growth, and the days to calculate
    # outputs projected population each 
    
    # finds and validates starting popluation
    start = int(input("Enter the starting popluation: "))
    
    while start <= 0:
        start = int(input("Enter a valid starting popluation: "))
    
    # finds and validates daily growth
    percentGrowth = int(input("Enter the percent of daily growth: "))
    
    while percentGrowth <= 0:
        percentGrowth = int(input("Enter a valid percent of daily growth: "))
    
    # finds and validates number of days
    days = int(input("Enter the number of days to simulate: "))
    
    while days <= 0:
        days = int(input("Enter a valid number of days to simulate: "))
    
    print()
    
    # prints header
    print("Day \t\t\t Projected Population")
    print("---------------------------------------------")
    
    print("1 \t\t\t", start)
    
    for day in range(2, days + 1):
        percent = percentGrowth / 100
        projTotal = start + start * percent
        start = projTotal
        
        print(day, "\t\t\t", projTotal)
        
    
def reverse_triangle():
    # reverse triangle recieves no arguments
    # it asks for the base size of a triangle
    # and prints it backwards using a variable
    base = int(input("Enter the base size of a triangle : "))
    while base <= 0:
        base = int(input("Enter a valid base size of a triangle : "))
    
    
    # prints the triangle backwards
    for bases in range(base + 1):
        print("*" * base)
        base = base - 1
        
def stair_pattern_2():
    # stair_pattern_2 recieves no arguments
    # it asks for a amount of stairs
    # it outputs the amount of stairs with a left margin
    
    stairs = int(input("Enter the amount of stairs: "))
    while stairs <= 0:
        stairs = int(input("Enter a valid amount of stairs: "))
    
    for stair in range(stairs):
        print("@", end = '')
        for step in range(stair):
            print(" ", end = '')
        print("@")
  
  
        
def repeating_squares():
    # tortuga rcieves no arguments
    # it asks for an amount of squares to draw
    # it outputs the squares
    startingX = 300
    startingY = -300
    seperator = 10
    screenHeight = 450
    screnWidth = 450
    
    squares = int(input("Enter a amount of squares: "))
    while squares <= 0:
        squares = int(input("Enter a valid amount of squares: "))
    
    t.setup(screenHeight, screnWidth)
    t.penup()
    t.goto(startingX, startingY)
    
    for square in range(squares):
        
main()