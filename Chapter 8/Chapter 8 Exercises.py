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

def morse_code():
    # mores_code recieves no arguments
    # it translates text and numbers to morse code
    ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    MORSE_ALPHABET = ['•-', '-•••', '-•-•', '-••', '•', '••-•', '--•', '••••', '••', '•---', '-•-', '•-••', '--','-•', '---', '•--•', '--•-', '•-•', '•••', '-', '••-', '•••-', '•--', '-••-', '-•--', '--••','•----', '••---', '•••---', '••••-', '•••••', '-••••', '--•••', '---••', '----•', '-----']
    
    input_string = "@"
    
    # prompt user for morse code string
    while input_string.isalnum() == False:
        print("No spaces, or special characters, only letters and numbers.")
        input_string = input("Enter a message to encode to morse code: ")
    
    # check each letter and convert it
    for letter in input_string:
        if letter in ALPHABET:
            letters_index = ALPHABET.index(letter)
            morse_letter = MORSE_ALPHABET[letters_index]
            
            print(morse_letter, end = ' ')
            
def phone_converter():
    # phone_converted recieves no arguments
    # it makes sure they follow the argument for the telephone number
    
    again == True
    
    while again == True:
        number = input("Enter a telephone number in the form of XXX-XXX-XXXX: ")
        number_list = list.split("-")
        if len(number_list) == 3:
            if number_list[0].isdigit() == True and number_list[1].isdigit() == True and number_list[2].isdigit() == True:
                if len(number_list[0]) == 3 and len(number_list[1]) == 3 and len(number_list[2]) == 3:
                    #####################################################
    