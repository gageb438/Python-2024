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


def list_copy():
    # list copier
    # create a list
    names = ["Bob", "Mary", "Sue"]
    
    # create an empty list
    new_names = []
    
    # copy listnames to list new_names
    # this preserves both lists as unique lists
    
    for name in names:
        new_names.append(name)
    
    # print the old and new names
    print(f"Old names list: {names}")
    print(f"New names list: {new_names}")
    
    # modify the new names list and reprint the old one
    new_names.append("Jerry")

    print(f"New modified names list: {new_names}")
    
    
def barista_pay(): # program 7-7
    # barista_pay accepts no argument
    # it prompts the user for the number of employees, hours worked for each employee
    # and the hourly rate all employees are paid
    # then outputs each employee's gross pay
    
    # ask for the number of employees
    employees = int(input("How many employees do you want to calculate pay for? : "))
    
    hoursWorked = []
    counter = 0
    
    for employee in range(1, employees + 1):
        # ask for the hours worked by each worker
        hours = input(f"Enter the hours worked by employee {employee} : ")
        
        hoursWorked.append(hours)
        
    # ask for hourly rate
    hourlyRate = float(input("Enter the hourly rate for all employees: "))
    
    # print the gross pay for each employee
    for employee in employees:
        counter += 1
        print(f"Gross pay for employee {counter}: {employee * hourlyRate}")
        
def list_total(): # program 7-8
    # list total accepts no arguments
    # it creates a list of numbers [2, 4, 6, 8, 10]
    # and loops to accumulate the total of all numbers in the list
    
    # create the list
    number_list = [2, 4, 6, 8, 10]
    # create the total
    total = 0
    
    # read each number in the list
    for number in number_list:
        # add the number to the total
        total += number
    
    print(f"The sum of the numbers {number_list} is: {total}")

def list_avg():
    # list avg accepts no arguments
    # it creates a list of numbers [2.5, 7.3, 6.5, 4.0, 5.2]
    # and it calculates the average of the numbers using len
    
    # create the list and the total
    number_list = [2.5, 7.3, 6.5, 4.0, 5.2]
    total = 0
    
    for number in number_list:
        # add the number to the total
        total += number
    
    # find the length of the list and divide to find the average
    average = total / len(number_list)
    
    print(f"The average of the numbers {number_list} is: {average}")
    
def list_function(): # program 7-10
    # list function accepts no arguments
    # it creates a list [2, 4, 6, 8, 10]
    # it passes the list to get_total
    # it prints the returned total
    
    # create the list
    number_list = [2, 4, 6, 8, 10]
    
    # pass the list to get_total
    total = get_total(number_list)
    
    # print the total
    print(f"The total of {number_list} is: {total}")

def get_total(number_list):
    # get total accepts a list of numbers
    # it calculates and returns the total
    
    total = 0
    
    # find the total
    for number in number_list:
        total += number
    
    # return the total
    return total

def get_values():
    # get values accepts no arguments
    # it creates an empty list
    # and loops, prompting the user to enter a vlaue
    # and appending that value to the list
    # and to if they want to add another value
    # it returns the reference to the list
    
    values = []
    again = 'y'
    
    # get values
    while again.lower() == 'y':
        value = int(input("Input a number: "))
        
        values.append(value)
        
        again = input("Do you want to enter another number? (y/n): ")
    return values

def list_return(): #program 7-11
    # list return accepts no arguments
    # it calls get_values to create a list reference and outputs the numbers in the list
    
    # get a reference in the list
    numbers = get_values()
    
    print(f"You entered the numbers: {numbers}")


def test_calc():
    # test_calc recieves no arguments
    # it recieves scores from get_scores then gets the total
    # it averages
    # and outputs the average and lowest score
    
    # get the scores
    scores,low_score = get_scores()
    
    # find and remove the bottom score
    total = get_total(scores)
    
    # print the total scores
    print(f"The average score, with {low_score} dropped from the scores, is: {total}")
    
def get_total(scores):
    # get total recieves an argument for the scores
    # it removes the lowest score and calculates the average
    
    # remove the average
    low_score = min(scores)
    scores.remove(low_score)
    
    # output ending message
    print(f"Dropping the lowest score of {low_score}.")
    
    # calculate the average score
    for num in scores:
        total += num
    
    average = total / len(scores)
    
    return average, low_score

    
def get_scores():
    # get_score recieves no arguments
    # it asks the user for scores
    # adds them to al ist
    # and returns the list
    
    score_list = []
    cont = 'y'
    
    # ask the user for scores
    while cont.lower() == 'y':
        # ask for the score
        score = float(input("Enter a score: "))
        
        # add it to the list
        score_list.append(score)
        
        # ask for another
        cont = input("Enter another score? (y/n): ")
        
    # return the list
    return score_list

def list_writelines(): # program 7-13
    # list writelines accepts no arguments
    # it writes the entire contents of a list
    # to the file cities.txt
    
    cities = ['Kansas City', 'Lawrence', 'Wichita', 'Manhattan']
    
    try:
        # open the file
        outfile = open('cities.txt', 'w')
        
        # write the list to the file
        outfile.writelines(cities)
        
        # close the file
        print("All data written to cities.txt")
        outfile.close()
        
    except Exception as err:
        print(err)
    
def list_write(): # program 7-14
    # list writelines accepts no arguments
    # it writes the entire contents of a list
    # to the file cities.txt
    
    cities = ['Kansas City', 'Lawrence', 'Wichita', 'Manhattan']
    
    try:
        # open the file
        outfile = open('cities.txt', 'w')
        
        for city in cities:
            # write the list to the file
            outfile.write(city + '\n')
            
        # close the file
        print("All data written to cities.txt")
        outfile.close()
    
    except Exception as err:
        print(err)
        
def list_read(): # program 4-15
    # list read accepts no arguments
    # it reads from cities.txt and aggregates the data
    # to the list cities, stripping \n from each
    
    try:
        # open the file
        infile = open('cities.txt', 'r')
        
        # read the contents to a list
        cities = infile.readlines()
        
        # close the file
        infile.close()
        
    except:
        print("Error reading from file.")
    
    # initalize index
    index = 0
    
    # strip the newline and reassign it to the list
    while index < len(cities):
        cities[index] = cities[index].rstrip('\n')
        index += 1
    
    print("Here is the information read from cities.txt.")
    print(cities)
    infile.close()
    
def random_numbers(): #program 7-18
    # random numbers accepts no arguments
    # it creates a 2D list with a mximum row index of 3
    # and a maximum column index of 2
    # it uses nexted loops to fill the 2D list with a random number
    # from 1-100
    
    # constants for roww/cols loops
    ROWS = 3
    COLS = 4
    
    values = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    
    # loop to fill the list with random numbers
    for row in range(ROWS):
        for col in range (COLS):
            values[row][col] = random.randint(1,100)
    
    # print the list
    print(values)
   
