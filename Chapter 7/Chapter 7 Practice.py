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
        
        
def list_append(): # program 7-3
    # list append accepts no arguments
    # it creates an empty list
    # and loops to append the list with input from the user
    # then prompts to continue

    # prime the list of names
    names = []
    keep_going = 'y'
    
    while keep_going.lower() == 'y':
        name = input("Enter a name: ")
        
        # adds it to the current list
        names.append(name)
        
        # prompt to continue
        keep_going = input("Add another name? (y to continue)")
        print()
    
    # output the names as entered
    print("You entered the following names: ")
    
    for name in name_list:
        print(name)
        
def list_index(): # program 7-4
    # list index accepts no arguments
    # it creates a list of three food items
    # and it prompts the user to replace one of the items
    # it searches the list for the index of the item
    # and prompts the user with a replacement of food
    
    # insert the food list
    food_list = ["Burger", "Pizza", "Hotdog"]
    
    # ask for a search
    search = input("Enter a string to search for: ")
    
    try:
        if food_list.index(search) >= 0:
            index = food_list.index(search)
            new_food = input("Item found. Enter a new food item: ")
            food_list[index] = new_food
            
    except:
        print()
        print(f"{search} was not found in the list. Check your spelling and try again")
    
    print(f"\nHere is the list: {food_list}")
    
def list_insert(): # program 7-5
    # list_insert accepts no arguments
    # it prints the original list of three names
    # it inserts a name in a list of names
    # at a specific index it prints the new list
    
    # create the starter list and print it
    name_list = ["Bruce", "Steve", "Tony"]
    print(f"Here is the list before the insert method: {name_list}")
    
    # insert the name Sam into the list
    name_list.insert(2, "Sam")
    
    # print it after the items
    print(f"Here is the list after the insert method: {name_list}")

def list_remove(): # program 7-6
    # list remove accepts no arguments
    # it creates a list of three food items
    # and it prompts the user to remove one of the items
    # it searches the list for the index of the item
    # and prompts the user with a remove of food
    
    # insert the food list
    food_list = ["Burger", "Pizza", "Hotdog"]
    
    # ask for a search
    search = input("Enter a string to search for: ")
    
    try:
        if food_list.index(search) >= 0:
            food_list.remove(search)
            print("Item removed.")
            
    except:
        print()
        print(f"{search} was not found in the list. Check your spelling and try again")
    
    print(f"\nHere is the list: {food_list}")
    