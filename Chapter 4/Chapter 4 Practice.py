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