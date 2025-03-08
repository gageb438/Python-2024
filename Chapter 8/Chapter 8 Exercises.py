# imports
import random
import string

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
    
def pb_main():
    # pb main recieves no arguments
    # it handles all function calls
    # outputs the 10 most common and 10 least common powerball numbers
    
    # get the frequency and pb_frequency lists
    frequency, pb_freq = pb_frequency()
    
    # get the most common numbers
    most_common = pb_most_common(frequency, pb_freq)
    minimum_freq, minimum_pb_freq = pb_least_common(frequency, pb_freq)
    
    
def pb_frequency():
    # pb_frequency recieves no arguments
    # it checks the frequency of all numbers
    
    NUMBERS = []
    frequency = []
    PB_NUMBERS = []
    pb_freq = []
    
    # generate the lists
    for num in range(0, 69):
        NUMBERS.append(num)
        frequency.append(0)
    
    for num in range(0, 25 + 1):
        PB_NUMBERS.append(num)
        pb_freq.append(0)
    
    
    # open the file
    outfile = open("pbnumbers.txt", "r")
    
    # make each lien a list
    for line in outfile:
        line_list = line.split(" ")
        line_list[5] = line_list[5].rstrip("\n")
        
        # preset counter
        counter = -1
        
        # add the frequency to each counter list
        for number in range(0,4+1):
            num = int(line_list[number])
            num_index = NUMBERS.index(num - 1)
            frequency[int(num_index)] += 1
        # add pb frequency to pb list
        num = int(line_list[5])
        num_index = NUMBERS.index(num -1)
        pb_freq[int(num_index)] += 1
    
    # return the frequency lists
    return frequency, pb_freq

def pb_most_common(frequency, pb_freq):
    # pb_most_common recieves a list for the frequency and pb frequency
    # it returns 2 lists with the maximums
    
    # initalize variables
    maximum = 0
    maximums = []
    pb_maximums = []
    frequency_copy = []
    pb_freq_copy = []
    
    # copy frequency
    for num in frequency:
        frequency_copy.append(num)
    
    for num in pb_freq:
        pb_freq_copy.append(num)
        
    for num in range(0, 10):
        for num in frequency_copy:
            if num > maximum:
                maximum = num
            if maximum == 0:
                break
        maximum_index = frequency_copy.index(maximum)
        frequency_copy[maximum_index] = 0
        
        maximums.append(maximum_index + 1)
        
        maximum = 0
        
    for num in range(0,10):
        for num in pb_freq_copy:
            if num > maximum:
                maximum = num
            if maximum == 0:
                break
        maximum_index = pb_freq_copy.index(maximum)
        pb_freq_copy[maximum_index] = 0
        
        pb_maximums.append(maximum_index + 1)
        
        maximum = 0
        
    return maximum, pb_maximums

def pb_least_common(frequency, pb_freq):
    # pb_least_common recieves a list for the frequency and pb frequency
    # it returns 2 lists with the minimums
    
    # initalize variables
    minimum = 0
    miniums = []
    pb_minimums = []
    frequency_copy = []
    pb_freq_copy = []
    
    # copy frequency
    for num in frequency:
        frequency_copy.append(num)
    
    for num in pb_freq:
        pb_freq_copy.append(num)
        
    for num in range(0, 10):
        for num in frequency_copy:
            if num < minimum:
                minimum = num
        
        print(minimum)
        print(frequency_copy)
        minimum_index = frequency_copy.index(minimum)
        frequency_copy[minimum_index] = 69
        
        minimums.append(minimum_index + 1)
        
        minimum = 70
        
    for num in range(0,10):
        for num in pb_freq_copy:
            if num < minimum:
                minimum = num
                
        minimum_index = pb_freq_copy.index(minimum)
        pb_freq_copy[minimum_index] = 0
        
        pb_minimums.append(minimum_index + 1)
        
        minimum = 70
        
    
    print(minimums)
    print(pb_minimums)