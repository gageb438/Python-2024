# imports
import random


def sum_of_digits():
    # sum of digits recieves no arguments
    # it asks the user for numbers
    # it checks if its all numbers
    # and sums up the numbers in the string
    
    # prompt for first input
    string = input("Please enter a string of single digit numbers without spaces: ")
    
    # validate it is all numbers
    while string.isdigit() != True:
        string = input("Please only enter numbers: ")
    
    # get totals
    total = 0
    for number in string:
        total += int(number)
    
    
    print(f"The sum of your string is: {total}")

def date_converter():
    # date converter recieevs no arguments
    # it asks the user for the date
    # in a certain format
    # then it checks to make sure it follows that format
    # and makes sure that it is all a valid number
    again = True

    # confirm it follows all the formatting rules
    while again == True:
        date = input("Enter a date in the format mm/dd/yyyy: ")
        date_list = date.split("/")
        if len(date_list) == 3:
            if date_list[0].isdigit() == True and date_list[1].isdigit() == True and date_list[2].isdigit() == True:
                if int(date_list[0]) < 13 and int(date_list[1]) < 32:
                    if len(date_list[0]) == 2 and len(date_list[1]) == 2 and len(date_list[2]) == 4:
                        # set again boolean to false
                        again = False
                    else:
                        print("Make sure you follow the format.")
                else:
                    print("Make sure you follow the format.")
            else:
                print("Make sure you follow the format.")
        else:
            print("Make sure you follow the format.")
    
    print('pass1')
    
    # create the list of months
    MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'Septemper', 'October', 'November', 'December']
    
    # preset variables
    month_number = int(date_list[0])
    month = ''
    done1 = False
    
    # find the month
    for month in MONTHS:
        month_index_number = MONTHS.index(month)
        if month_index_number + 1 == month_number:
            # save the real month
            real_month = month
    
    # print the ending
    print(f"The date is: {real_month} {date_list[1]}, {date_list[2]}")

    