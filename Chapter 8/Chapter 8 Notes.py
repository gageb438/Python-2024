def count_t(): #8-1
    # count_t recieves no arguments
    # it prompts the user for a word
    # and interates through each letter
    # counting the number of upper and lower case t's
    # it ouputs the total number of times it appeared in the word

    # initialize occured variable
    occured = 0

    # get input for the word
    word = input("Please enter a word: ")

    # count the times
    for letter in word:
        if letter.lower() == 't':
            occured += 1

    # output final statement.
    print(f"The letter T or t appears {occured} times in the word: {word}")

def concatenate(): #8-2
    # concatenate accpets no arguments
    # it concatenates and prints the two strings
    # Carmen and Sandiego

    # create the string
    carmen = "Where in the world is Carmen"
    print(carmen)
    print(carmen + " Sandiego")

def get_login_name(first, last, idnumber): #8-3
    # login accepts arguments for first, last, and id number.
    # it createss seperate substrings of the first 3 letters of both
    # the first name and last and last 3 characters of the id number.
    # it concatenates the strings in order of first, last, id
    # and it returns the newly generated login.

    first_slice = first[0:3]
    last_slice = last[-3:]
    last_id = idnumber[-3:]

    new_login = first_slice + last_slice + last_id
    return new_login
    
def generate_login(): #8-4
    # get login accepts no arguments
    # it prompts the user for a first name, last name, and id number
    # it passes the values to login.get_login_name()
    # and recieves the new user login.

    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    idnumber =  input("Enter your id number: ")

    # call get login name to get new login name
    login_name = get_login_name(first, last, idnumber)

    print(f"Your system login name is: {login_name}")

def string_test(): #8-5
    # string test accepts no arguments
    # it it akes input from the user in the form of a string
    # and performs a variety of tests on the string
    
    # get input
    user_string = input("Enter the string to evaluate: ")
    
    # perform string tests
    if user_string.isalnum():
        print("The string only contains alphanumeric characters.")
    if user_string.isdigit():
        print("The string only contains digits")
    if user_string.isalpha():
        print("The string only contains alpha characters.")
    if user_string.isspace():
        print("The string only contains whitespaces.")
    if user_string.islower():
        print("The string is all lowercase.")
    if user_string.isupper():
        print("The string is all uppercase.")
    
    print()
    print(f"Your string converted to all uppercase is: {user_string.upper()}")
    print(f"Your string converted to all lowercase is: {user_string.lower()}")

def valid_password(password): #8-6
    # valid password accepts a string for password
    # it tests the following conditiions
    # is password atleast 7 characters
    # does password have at least one uppercase letter
    # does password have atleast one digit (numeric)
    # if password meets all conditions is_valid is true
    # valid_password returns is_valid
    upper = 0
    lower = 0
    digit = 0

    if len(password) >= 7:
        for letter in password:
            if letter.islower():
                lower += 1
            if letter.isupper():
                upper += 1
        if lower >= 1 and upper >= 1:
            for letter in password:
                if letter.isdigit():
                    digit += 1
            if digit >= 1:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
def validate_password(): #8-7
    # validate_password accepts no arguments
    # it prompts the user for a password
    # and passes the password to login.valid_password
    # to loop while the password is invalid
    
    is_valid = False
    
    while is_valid == False:
        password = input("\nPlease enter your password: ")
        
        is_valid = valid_password(password)
        
        if is_valid == False:
            print("The password you entered is not valid. Please try again.")
        elif is_valid == True:
            print("\nPassword accepted.")