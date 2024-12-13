# imports
import menu
import os
import random

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
        main()
    elif choice == 2:
        line_counter()
        main()
    elif choice == 3:
        average_numbers()
        main()
    elif choice == 4:
        random_number_write()
        main()
    elif choice == 5:
        random_number_read()
        main()
    elif choice == 6:
        golf_main()
        main()
    elif choice == 7:
        personal_page_generator()
        main()
    elif choice == 8:
        average_steps()
        main()
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
        lineNumber = lineNumber.rstrip("\n")
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
    infile.close()
def average_numbers(): #exercise 6
    # average numbers recieves no arguments
    # it opens the file numbers.txt to read
    # it reads and caculates the average of all the items in the file
    
    # initialize variables
    if os.path.exists("numbers.txt"):
        infile = open('numbers.txt', 'r')
    else:
        print("File is not found")
        return
    totalItems = 0
    counter = 0
    
    for lineNumber in infile:
        totalItems += int(lineNumber)
        counter += 1
    average = totalItems / counter
    print(f"There were {counter} items with an average value of {average}")
    infile.close()
    
def random_number_write(): # exercise 7
    #random_number_write recieves no arguments
    # it asks the user for an amount of numbers to write
    # and writes them to a file
    
    try:
        numbers = int(input("How many numbers would you like to write? :> "))
        while numbers < 0:
            print("Pick a number above 0.")
            numbers = int(input(":> "))
        outfile = open("ran_number_list.txt", "w")
        for number in range(numbers):
            rand_num = str(random.randint(0,500))
            outfile.write(rand_num + '\n')
        
        outfile.close()
        print("All numbers have been written to ran_number_list.txt")
    
    except Exception as exception:
        print(exception)


def random_number_read(): #exercise 8
    # random_number_read recieves no arguments
    # it reads the file ran_number_list.txt and totals the number
    # initialize variables
    
    counter = 0
    total = 0
    try:
      infile = open("ran_number_list.txt", "r")
    except Exception as exception:
        print(exception)
        return
      
    for num in infile:
        num = num.rstrip('\n')
        print(num)
        counter += 1
        total += int(num)
    
    print("The total of ", counter, " random numbers is: ", total, sep = '')
    infile.close()


def golf_main(): # exercise 10
    def display_menu():
        # display menu recieves no arguments
        # it prints the header for the golf management system
        print("Welcome to Hole in Twelve golf management system.\n" +
        "Please choose form the following commands...")
        print("\n1) Read Golf Data\n2) Append Golf Data\n3) Exit")
        
        # get the users choice 
        choice = input("\nMenu choice: ")
        
        # validate the user choice
        try:
            choice = int(choice)
            while choice < 1 or choice > 3:
                choice = input("Menu choice: ")
        except:
            print("\nPlease put in a choice on the menu.\n")
            input("Press enter to continue...\n")
            display_menu()
        
        if choice == 1:
            read_data()
            display_menu()
        elif choice == 2:
            append_data()
            display_menu()
        else:
            print("\nThank you for using Hole in Twelve golf management system. Have a great day.")
    
    def append_data():
        # append data recieves no arugments
        # it asks the users for a name and score, it then writes it to golf_data.txt
        
        # opens the file
        infile = open("golf_data.txt", "a")
        
        # ask the user for the name and score of someone
        name = input("\nName: ")
        score = input("Score: ")
        
        print()
        
        # write the data to the file
        infile.write(name + "\n")
        infile.write(score + "\n")
        
        # close the file
        infile.close()
        
    def read_data():
        # read data recieves no arguments
        # it prints out the data from golf_data.txt
        
        # check that the file exists
        if os.path.exists("golf_data.txt"):
            outfile = open("golf_data.txt", "r")
        else:
            print("\nFile not found. Returning to menu.\n")
            return()
        
        # prime the loop
        name = "temp"
        score = "temp"
        
        while name != "":
            # read the lines and print the scores out
            name = outfile.readline().rstrip("\n")
            score = outfile.readline().rstrip("\n")
            print()
            print(name)
            print(score)
            
        # close the file
        outfile.close()
        
        print("All records successfully read!\n")
        return()
    display_menu()

def personal_page_generator(): #exercise 11
    # personal page generator recieves no arguments
    # it asks the user for their name and a little bit about themselves
    # it then writes it to a file named their name .html
    # it will then open a website using it
    
    # assk for name and description
    name = input("Enter your name: ")
    desc = input("Write a short description of yourself: ")
    
    infile = open(f"{name}.html", "w")
    
    # write the page
    infile.write("<html>" + "\n")
    infile.write("<head>" + "\n")
    infile.write("</head>" + "\n")
    infile.write("<body>" + "\n")
    infile.write("\t<center>" + "\n")
    infile.write(f"\t\t<h1>{name}</h1>" + "\n")
    infile.write("\t</center>" + "\n")
    infile.write("\t<hr />" + "\n")
    infile.write(f"\t{desc}")
    infile.write("\t<hr />" + "\n")
    infile.write("</body>" +"\n")
    infile.write("</html>" + "\n")
    
    infile.close()
    
    # print closing
    print(f"Webpage saved to {name}.html")

def average_steps(): #exercise 12
    # average steps recieves no arguments
    # it uses lists to find the amount of steps from the file
    # outputs the amount of steps per month
    
    # initialize variables
    DAYS_PER_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    MONTHS = ['January\t', 'February', 'March\t', 'April\t', 'May\t', 'June\t', 'July\t', 'August\t', 'September', 'October\t', 'November', 'December']
    total = 0
    index = 0
    
    outfile = open('steps.txt', "r")
    
    #for month in MONTHS:
    for days in DAYS_PER_MONTH:
        for day in range(days):
            line = outfile.readline().rstrip("\n")
            #print(line)
            line = int(line)
            total += line
        average = total / DAYS_PER_MONTH[index]
        print(f"{MONTHS[index]}\t{average:.2f} steps")
        index +=1
        total = 0
    
main()
