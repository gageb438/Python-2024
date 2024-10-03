import turtle as t

def practice_1():
    day = "Thursday"
    value = 0

    # version 1 - is using a normal string
    print("Enter a number of items sold on", day, end = '')
    value = int(input(": "))
    print("On", day, "you sold", value, "items.")

    # version 2 - using an 'f' string
    value = int(input(f"Enter a number of items sold on {day}: "))
    print(f"On {day} you sold {value} items.")

    #validate user input
    if value <= 0 and value >= 7:
        print(f"{value} is a valid value.")
    else:
        print(f"{value} is an invalid value.")
       
    count = 0 # initialize accumulator
    while count < 5: #accumulator is the condition
        print(f"Hello World")
        count += 1 # increment the accumulator
        

def parsons():
    count = 1
    MAX_COUNT = 10
    while count < MAX_COUNT:
        # this block of code is in the loop
        print(f"Counting iteration #{count}")
        count += 1 # This is the same as count = count + 1
    # this block of code is out of the loop
    print(f"Your loop ran for {count} iterations.")
    print("Goodbye")
    
def program4_1():
    # program4_1 recieves no arguments
    # asks user for sales and commission rate and repeats if requested
    # outputs total commission and whether the user wants to run it again
    
    # initializes variables
    keep_going = "y"
    
    # while loop
    while keep_going.lower() == "y":
        sales = int(input("Enter the amount of sales: "))
        comm_rate = float(input("Enter the commision rate: "))
        commission = sales * comm_rate
        # prints commission
        print(f"The commission is ${commission:,.2f}")
        
        # prompt the user to re-run
        keep_going = input("Do you want to calculate another commission? (Enter y for yes and n for no): ")
        
    print("Goodbye.")
    
    
def program4_2():
    max_temp = 102.5
    
    temp = float(input("Please input the current substance temperature in Celcius: "))
    
    while temp > max_temp:
        print("\nThe temperature is too high")
        print("Turn the thermostat down and wait for it to cool.")
        print("Then wait 5 minutes and measure again\n")
        
        temp = float(input("Please enter a new temperature in degrees Celcius: "))
        
    
    print("The temperature is acceptable.")
    print("Measure again in 15 minutes.")
    
    
def program4_3():
    # program4_1 recieves no arguments
    # asks user for sales and commission rate and repeats if requested
    # outputs total commission and whether the user wants to run it again
    
    # initializes variables
    keep_going = "y"
    
    # while loop
    while keep_going.lower() == "y":
        sales = int(input("Enter the amount of sales: "))
        comm_rate = float(input("Enter the commision rate: "))
        commission = sales * comm_rate
        # prints commission
        print(f"The commission is ${commission:,.2f}")


def program4_4():
    # program4_4 recieves no arguments
    # uses a for loop
    # prints the numbers using 1-5
    
    # prints what it does
    print("I will display the numbers 1 - 5")
    
    # prints the 5 numbers
    for num in [1, 2, 3, 4, 5]:
        print(num)
        
    # prints what it does
    print("I will display the numbers 1 - 10")
    
    # prints the 10 numbers
    for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print(num)
        

def program4_5():
    # program4_5 recieves no arguments
    # uses a for loop
    # prints the odd numbers 1 - 10
    
    # prints what it does
    print("I will output all odd numbers from 1 - 10")
    
    for num in [1, 3, 5, 7, 9]:
        print(num)
        
        
def program4_6():
    # program4_6 recieves no arguments
    # uses a for loop
    # outputs 4 names
    
    for name in ["Steve", "Tony", "Thor", "Wanda"]:
        print(name)
        

def program4_4mod():
    # program 4-4 mod recieves no arguments
    # it uses the range function
    
    for num in range(1, 10 + 1):
        print(num)
        
        
def program4_7():
    # program4_7 recieves no arguments
    # it outputs the phrase hello world 5 times
    
    for count in range(5):
        print("Hello World!")
        
        
def program4_8():
    # program4_8 recieves no arguments
    # it outputs the number 1-10 squared
    
    # prints header
    print("Number \t Square")
    print("--------------")
    
    
    # prints the number and the square
    for num in range(1, 10 + 1):
        square = (num ** 2)
        print(num, '\t', square)
        
        
def program4_9():
    # program4_7 recieves no arguments
    # outputs 60- 130 kph to mph
    
    
    # initialize variables
    startSpeed = 60
    endSpeed = 131
    speedIncrement = 10
    kphMultiplier = .6214
    # prints the header
    print("KPH \t MPH")
    print("------------")
    
    # prints kph and mph
    for kph in range(startSpeed, endSpeed, speedIncrement):
        mph = kphMultiplier * kph
        print(kph, '\t', format(mph, '.1f'))
    
    
def program4_10():
    # program4_10 recieves no arguments
    # it asks the user for an amount of squares
    # prints the amount of squares
    
    # prints header
    print("This program will display a list of numbers\n(starting at 1) and their squares.")
    
    # asks for how many squares
    squares = int(input("How many squares? : "))
    
    # prints header 2
    print("Number \t Square")
    print("--------------")

    # prints the number and the square
    for num in range(1, squares + 1):
        square = (num ** 2)
        print(num, '\t', square)
    
    
def program4_11():
    # program4_11 recieves no arguments
    # it asks the user for an amount of squares
    # prints the amount of squares
    
    # prints header
    print("This program will display a list of numbers and their squares")
    
    # asks for how many squares
    start = int(input("Enter the starting number : "))
    end = int(input("Enter the ending number : "))
    
    # prints header 2
    print("Number \t Square")
    print("--------------")

    # prints the number and the square
    for num in range(start, end + 1):
        square = (num ** 2)
        print(num, '\t', square)
        
        
def program4_12():
    # program4_12 recieves no arguments
    # it asks user for 5 numbers
    # outputs the sum of all five
    
    # initializes variables
    total = 0
    number = 0
    maxNum = 5

    print("This program calculates the sum of\n5 numbers you will enter.")
    
    for count in range(0, maxNum):
        number = float(input("Please enter a number: "))
        total += number
    
    # prints total
    print("The total of your ", maxNum, " numbers is: ", format(total, '.1f'), sep = '')
    
    
def program4_13():
    # program4_13 accepts no arguments
    # it prompts the user for a lot number and loops while lot number != 0
    # it promts the user for a property value
    # and calculates the property tax
    # it ouputs the total property owed and prompts another lot
    # it outputs the total property tax and prompts for another lot
    # it outputs a program termination method
    
    # initializes variables
    lotNumber = 1
    
    propertyTax = .0065
    
    # asks for the first lot number
    
    lotNumber = int(input("Please enter a lot number (enter 0 to end): "))
    
    while lotNumber != 0:
        # finds tax
        value = float(input("Please enter the property value: "))
        tax = value * propertyTax
        
        print("Property tax: $", format(tax, '.2f'), sep = '')
        
        # asks for lot number
        lotNumber = int(input("Please enter a lot number (enter 0 to end): "))
        
    # outputs termination message
    print("Thank you for using the Cyberdyne Systems property tax calculator, all your rights reserved.")
    
    
def program4_14():
    #Gross pay accepts no arguments
    # it takes input from the user in the form of hours worked and pay rate
    # it calculates and outputs the gross pay
    
    hours = int(input("Enter the hours: "))
    
    pay_rate = int(input("Enter the hourly rate: "))
    
    gross_pay = hours * pay_rate
    
    print("Gross pay: $", format(gross_pay, ',.2f'), sep = '')
    
    
def program4_15():
    # retail no validation accepts no arguments
    # it uses a string sentinel to control the loop
    # ouytputs retail price
    
    mark_up = 1.25
    another = 'y'
    
    while another =='y' or another == 'Y':
        wholesale = float(input("Enter the wholesale cost: "))
        retail = wholesale * mark_up
        print('Retail Price: $', format(retail, ',.2f'), sep = '')
        
        another = input('Do you want to enter another item?' +
                        '(Enter Y for yes): ')
        
        
def program4_16():
    # retail with validation accepts no arguments
    # it uses a string sentinel to control the loop
    # ouytputs retail price
    
    mark_up = 1.25
    another = 'y'
    
    while another =='y' or another == 'Y':
        wholesale = float(input("Enter the wholesale cost: "))
        while wholesale <= 0:
            wholesale = float(input("Enter a valid cost: "))
        retail = wholesale * mark_up
        print('Retail Price: $', format(retail, ',.2f'), sep = '')
        
        another = input('Do you want to enter another item?' +
                        '(Enter Y for yes): ')
    
    
def program4_17():
    # program4_17 recieves no arguments
    # takes the amount of students and amount of scores per student
    # looping to find the average
    
    # initialize variables
    total = 0.0
    
    # number of students
    students = int(input("Enter the amount of students : "))
    
    # validate
    while students <= 0:
        students = input("Enter a valid amount of students : ")
        
    tests = int(input("Enter the amount of tests per student : "))
    
    # validate
    while tests <= 0:
        tests = input("Enter a valid amount of tests : ")
        
    print()
    
    for student in range(1, students + 1):
        
        # prints the title
        print("Student number", student)
        print("-----------------")
        
        for test in range(1, tests + 1):
            print("Test number", test, end = '')
            score = float(input(": "))
            total += score
        print()
        averageTests = total / tests
        print("The average for student number", student, "is: ", format(averageTests, '.2f'), '\n')
        
        # reset variables
        total = 0.0


def program4_18():
    # program4_18 recieves no arguments
    # it asks for rows and columns
    # outputs art
    
    # finds rows and validates
    rows = int(input("Enter the number of rows to print: "))
    while rows <=0:
        rows = int(input("Enter a valid number of rows to print: "))
    
    # finds columns and validates
    columns = int(input("Enter the number of columns to print: "))
    while columns <=0:
        columns = int(input("Enter a valid number of columns to print: "))
        
    for row in range(rows):
        
        for column in range(columns):
            print("*", end = '')
        print()
    print("Art finished")
    

def program4_19():
    # program4_19 recieves no arguments
    # it asks for the base of a triangle
    # outputs art of a triangle
    
    # initializes variables
    base = 0
    
    # finds base and validates
    base = int(input("Enter the base size of a triangle : "))
    while base <= 0:
        base = int(input("Enter a valid base size of a triangle : "))
    
    for length in range(1, base + 1):
        for column in range(length):
            print("*", end = '')
        print()
    
    
def program4_20():
    # program4_20 recieves no arguments
    # it asks for the number of stairs
    # outputs the art of the amount of stairs
    
    stairs = int(input("Enter the amount of stairs: "))
    while stairs <= 0:
        stairs = int(input("Enter a valid amount of stairs: "))
    
    for stair in range(stairs):
        for step in range(stair):
            print(" ", end = '')
        print("\\")
        


def program4_21():
    # program4_21 recieves no arguments
    # it draws that amount of squares
    
    numCircles = int(input("Enter the number of circles: "))
    while numCircles <= 0:
        numCircles = int(input("Enter a valid number of circles: "))
    
    startingRad = 20
    offset = 10
    animationSpeed = 0
    
    t.speed(animationSpeed)
    t.hideturtle()
    
    radius = startingRad
    
    for circle in range(numCircles):
        t.circle(radius)
        
        xcor = t.xcor()
        ycor = t.ycor()
        
        radius = radius + offset
        
        t.penup()
        t.goto(xcor, ycor - offset)
        t.pendown()
    
    t.done()
    
    
def program4_22():
    # program4_22 recieves no arguments
    # it asks for a amount of circles
    # and draws the amount of circles.
    
    # initialize variables
    numCircles = 36
    radius = 100
    angle = 10
    speed = 0
    
    t.speed(speed)
    
    for circle in range(numCircles):
        t.circle(radius)
        t.left(angle)
        
        
        
def program4_23():
    # program4_23 recieves no arguments
    # it draws a starburst
    
    startX = -200
    startY = 0
    numLines = 36
    lineLength = 400
    angle = 170
    
    t.speed(100)
    t.hideturtle()
    t.penup()
    t.goto(startX, startY)
    t.pendown()
    
    for x in range(numLines):
        t.forward(lineLength)
        t.left(angle)
    
    t.done()