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

def validate_me():
    # validate me accepts no arguments
    # it takes a value from the user
    # and validates that value
    
    # create a list of possible correct answers
    answers = ["yes", "no", "maybe"]
    
    # get input from the user
    answer = input("What is your answer? : ").lower()
    
    if answer not in answers:
        print("Please only specify yes, no, or maybe.")
        
def in_list(): # program 7-2
    # in list accepts no arguments
    # it creates a list of part numbers
    # V45, V65, VF750, VFR1100, VTX1300
    # and prompts the user for a string to search for
    # and it prints if the list contains the search string
    
    # create the list
    partList = ["V45", "V65", "VF750", "VFR1100", "VTX1300"]
    
    # ask for the input
    searchPrompt = input("Enter a part to search for(Case senstive): ")
    
    if searchPrompt not in partList:
        print("Part number not found.")
    else:
        print(f"Part number {searchPrompt} was found in the list of part numbers.")

def inList(num):
    # inList accepts an integer
    # it checks to see if an element is in the list
    # if it is, it returns the index of that item
    
    # initialize the list
    myList = [1, 2, 3, 4, 5]
    
    if num in myList: 
        print("Your item is at index: ", myList.index(num))
    else:
        print(f"{num} is not in the list.")