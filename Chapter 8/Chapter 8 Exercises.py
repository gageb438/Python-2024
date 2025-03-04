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
    
    # initalize variables
    again = True
    final_string = ""
    NUMBER_ALPHABET = ["2", "2", "2", "3", "3", "3", "4", "4", "4", "5", "5", "5", "6", "6", "6", "7", "7", "7", "8", "8", "8", "9", "9", "9", "9"]
    ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    # loop for if they make a mistake
    while again == True:
        # ask for input
        number = input("Enter a telephone number in the form of XXX-XXX-XXXX: ")
        # split to a list
        number_list = number.split("-")
        # verify it follows every rule
        if len(number_list) == 3:
            if len(number_list[0]) == 3 and len(number_list[1]) == 3 and len(number_list[2]) == 4:
                for row in number_list:
                    # get each letter
                    for letter in row:
                        if letter.lower() in ALPHABET:
                            # translate them
                            letter = letter.lower()
                            letters_index = ALPHABET.index(letter)
                            number = NUMBER_ALPHABET[letters_index]
                            # add them to final string
                            final_string += number
                        else:
                            final_string += letter
                    if row != number_list[2]:
                        # add a spacer
                        final_string += "-"
                # print final number and set again to false
                print(f"Here is your converted telephone number: {final_string}")
                again = False
                
def avg_num_words():
    # avg_num_words recieves no arguments
    # it checks the amount of words in a file
    # it also counts the sentences
    # it also checks the words per sentence
    
    # initialize variables
    outfile = open("text.txt", "r")
    sentences = 0
    words = 0
    
    # count each line in the outfile
    for line in outfile:
        # create the line, split it, get the length of the list, and add the sentences
        line = line.rstrip("\n")
        line_list = line.split(" ")
        words += len(line_list)
        sentences += 1
    
    # get the average
    average = words / sentences
    
    # output.
    print(f"The file text.txt has {words} words.")
    print(f"There are {sentences} total sentences.")
    print(f"The average number of words per sentence is: {words}")

def igpay_atinlay():
    # pig latin takes a string
    # it adds the last letter to the first
    # it then adds ay to the end
    
    # initalize variables
    final_string = ""
    
    # request input
    latinify = input("Enter a message to convert to pig latin: ")
    
    # split the string
    latinify_list = latinify.split(" ")
    
    for word in latinify_list:
        # reset the period, and check if there is one.
        period = False
        if "." in word:
            # replace period with nothing
            word = word.replace(".", "")
            period = True
        
        # get the first letter
        first_letter = word[0]
        
        # add the first letter to the end
        word += first_letter
        
        # remake the word to remove the letter at the start
        word = word[1:]
        
        # add ay to it
        word += "AY"
        
        # add a period if there was one
        if period == True:
            word += "."
        
        # add it to the final string
        final_string += word + " "
    
    # print the final string in all upercase
    print(final_string.upper())
    
def gas_prices():
    # gas prices recieves no arguments
    # it controls all functions
    # for checking gas prices per each year.
    
    
    def average_per_year():
        # average_per_year accepts no arguments
        # it calculates the average of gas prices per each year
        # then it returns them
        year_data = []
        date_list = []
        price_list = []
        average = 0
        total = 0
        
        # open the file
        outfile = open("GasPrices.txt", "r")
        
        for line in outfile:
            year_data = []
            
            year_data_temp = line.split("-")
            print(year_data_temp)
            
            year_data_temp_2 = year_data_temp[2].split(":")
            print(year_data_temp_2)
            
            year_data.append(year_data_temp[0])
            year_data.append(year_data_temp[1])
            year_data.append(year_data_temp_2[0])
            year_data.append(year_data_temp_2[1].rstrip("\n"))
            print(year_data)
            
            year = year_data[2]
            total += 
            
            
            if year != old_year:
                old_year = year
                average = 
    average_per_year()
gas_prices()
