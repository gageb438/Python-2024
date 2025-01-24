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
    
    print(f"{minimum_month} had the least rain with {minimum} inches of rain.")
    print(f"{maximum_month} had the most rain with {maximum} inches of rain.")
  
