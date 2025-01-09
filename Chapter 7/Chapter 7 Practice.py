# imports
import random

def isValid(value):
    # isValid is a boolean function that will return true if all characters
    # in the string are numeric, otherwise it will return false
    
    return value.isnumeric()

def forReview():
    # for Review accepts no arguments
    # it prompts the user for a start and end value
    # and loops from the start to the end, adding the values together
    
    # get input from the user
    start = int(input("Enter a starting value: "))
    end = int(input("Enter an ending value, greater than the starting value: "))
    total = 0
    if end > start:
        for num in range(start, end + 1):
            total += num 
        print(f"Your total is: {total}")
    else:
        print("Ending value must be greater than the starting value")

def sales_list(): # program 7-1
    # sales list accepts no arguments
    # it creates a list NUM_DAYS long
    # and loops to accept input from the user
    # adding that input to the list
    
    NUM_DAYS = 5
    sales = [0] * NUM_DAYS
    index = 0
    
    # print the header
    print("Enter the sales for each day")
    
    # loop to ask the user for each one
    while index < NUM_DAYS:
        sales[index] = float(input((f"Day #{index + 1}: ")))
        
        index += 1
        
    # print the values
    print("\nHere are the values you entered\n")
    
    for sale in sales:
        print(format(sale, '.2f'))