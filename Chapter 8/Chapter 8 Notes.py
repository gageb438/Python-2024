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
        if word.lower() = 't':
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

