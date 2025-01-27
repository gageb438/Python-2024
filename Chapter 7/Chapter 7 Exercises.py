#imports
import random
import time

def lottery():
    # lottery generates 7 random numbers from 0 - 9
    # it prints them to the shell
    
    NUMBERS = 7
    numbers = []
    
    print("Generating lotto numbers...")
    
    for number in range(NUMBERS):
        numbers.append(random.randint(0,9))
    
    print("Your lotto numbers are:")
    for number in numbers:
        print(f"{number}")
        
def rainfall():
    # rainfall recieves no arguments
    # it asks the user for each rainfall each month
    
    MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    Rainfall = []
    
    for month in MONTHS:
        # ask user for the rainfall in the month
        month_rainfall = int(input(f"Enter the rainfall for {month}: "))
        
        Rainfall.append(month_rainfall)
    
    print()
    
    # find the minimum in the list and print the month along with it
    minimum = min(Rainfall)
    maximum = max(Rainfall)
    
    # find min amd max indexes
    minimum_index = Rainfall.index(minimum)
    maximum_index = Rainfall.index(maximum)
    
    # find min month and max month
    minimum_month = MONTHS[minimum_index]
    maximum_month = MONTHS[maximum_index]
    
    print()
    print(f"{minimum_month} had the least rain with {minimum} inches of rain.")
    print(f"{maximum_month} had the most rain with {maximum} inches of rain.")
    
def charge_accts():
    # charge accounts recieves no arguments
    # it checks if the account number entered is correct
    # it outputs if the number is in the list of account
    
    def isValid(account_number):
        # is valid recieves an argument for the acount number
        # it checks the account file to see if a number
        # is on the list
        account_file = open("charge_accounts.txt", "r")
        accounts = []
        go = "y"
        
        for acc in account_file:
            acc = acc.rstrip("\n")
            accounts.append(acc)
            
        account_file.close()
            
        # check if the account number is on the list
        if account_number not in accounts:
            return "invalid"
        else:
            return "valid"
    
    again = "y"
    bad = True
    
    while again == "y":
        # while they want to check another account number
        
        # ask for an account number
        account_number = input("Enter an account number: ")
        
        # check if it is a number
        while account_number.isdigit() == False:
            account_number = input("Enter an account number (numeric only): ")
        
        # check if its on the list
        on_list = isValid(account_number)
        
        if on_list == "valid":
            print("\nThe account number is valid.\n")
        else:
            print("\nThe account is invalid.\n")
        
        # ask if they want to check another
        again = input("Check another account number? (y/n) : ")
        
def drivers_exam():
    # drivers exam recieves no arguments
    # it reads a test key from a file
    another = 'y'
    
    while another = 'y':
        # prompt the user for the filename to read
        test_file = input("Please enter the name of the file to read: ")
        
        if not os.path.exists(test_file):
            print(f"{test_file} not found.")
        else:
            # check if each test answer is in the 
        
        