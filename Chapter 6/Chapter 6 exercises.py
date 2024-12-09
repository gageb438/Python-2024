# imports
import menu
import os

def main():
    # menu recieves no arguments
    # it calls the module menu and processes the choice
    # it then calls the exercise based of the choice
    
    # get choice
    choice = menu.menu(8)
    
    # checks if it is below 0 or above 8
    try:
        while choice < 0 or choice > 8:
            choice = menu.menu(8)
    except:
        print("Please choose a number between 0 and 8.")
        main()

    if choice == 1:
        line_numbers()
    elif choice == 2:
        line_counter()
    elif choice == 3:
        average_numbers()
    elif choice == 4:
        random_number_write()
    elif choice == 5:
        random_number_read()
    elif choice == 6:
        golf_scores()
    elif choice == 7:
        personal_page_generator()
    elif choice == 8:
        average_steps()
    elif choice == 0:
        print("Goodbye.")

def line_numbers(): #exercise 3
    # line numbers recieve no arguments
    # it asks the user for the name of a file
    # it displays the contents of the file with each line precided with the line number followed by colon
    # the numbering starts and one
    
    # initialize counter
    counter = 0
    
    # asks for the file name
    infile = input("Enter the name of a file you would like to read: ")
    
    if os.path.exists(infile):
        infile = open(infile, 'r')
    else:
        print("The file does not exist.")
        return
    
    for lineNumber in infile:
        counter += 1
        print(f"{counter}:\t {lineNumber}")

def line_counter(): #exercise 4
    # line counter recieves no arguments
    # it asks for a file to read
    # it reads the maount of lines in the file
    
    # initialize variable
    counter = 0
    
    # asks for the file
    infile = input("Enter the file to read: ")
    name = infile
    
    # checks it exists
    if os.path.exists(infile):
        infile = open(infile, 'r')
    else:
        print(f"[Errno 2] No such file or directory: '{infile}'")
        return
    
    # counts the lines
    for lineNumber in infile:
        counter += 1
    
    # print the amount of lines
    print(f"{name} contains {counter} lines.")
def average_numbers(): #exercise 6
    # average numbers recieves no arguments
    # it opens the file numbers.txt to read
    # it reads and caculates the average of all the items in the file
    
    # initialize variables
    infile = open('steps.txt', 'r')
    totalItems = 0
    counter = 0
    
    for lineNumber in infile:
        totalItems += int(infile.readline())
        counter += 1
        print(totalItems)
        print(counter)
    
def random_number_write(): # exercise 7
    pass

def random_number_read(): #exercise 8
    pass

def golf_scores(): #exercise 10
    pass

def personal_page_generator(): #exercise 11
    pass

def average_steps(): #exercise 12
    pass

main()