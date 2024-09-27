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