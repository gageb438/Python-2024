# imports
import random
import string

def encrypt():
    # encrypt takes a file, reads its contents, and encrypts it all in a new
    
    # create the key
    key = {'a': 's', 'b': 'O', 'c': 'Y', 'd': 'p', 'e': 'd', 'f': 'v', 'g': 'S', 'h': 'E', 'i': 'K', 'j': 'Q', 'k': 'k', 'l': 'w', 'm': 'f', 'n': 'V', 'o': 'A', 'p': 'e', 'q': 'a', 'r': 'q', 's': 'G', 't': 'y', 'u': 'l', 'v': 'I', 'w': 'n', 'x': 'i', 'y': 'H', 'z': 'u', 'A': 'c', 'B': 'r', 'C': 'h', 'D': 't', 'E': 'W', 'F': 'b', 'G': 'Z', 'H': 'j', 'I': 'T', 'J': 'P', 'K': 'g', 'L': 'R', 'M': 'J', 'N': 'L', 'O': 'z', 'P': 'C', 'Q': 'o', 'R': 'B', 'S': 'F', 'T': 'U', 'U': 'm', 'V': 'N', 'W': 'M', 'X': 'D', 'Y': 'X', 'Z': 'x', " ": " ", "\n" : "\n"}
    file = open("storage_file.txt", "r")
    encoded_file = open("encoded_file.txt", "w")
    
    # encode the file
    for line in file:
        encoded_line = ""
        
        for letter in line:
            encoded_line += key[letter]
        
        encoded_file.write(encoded_line)
    # close the files
    file.close()
    encoded_file.close()
def decrypt():
    # decrypt takes a file, reads it contents, and decrypts it in a new file
    
    # create the key
    key = {'a': 's', 'b': 'O', 'c': 'Y', 'd': 'p', 'e': 'd', 'f': 'v', 'g': 'S', 'h': 'E', 'i': 'K', 'j': 'Q', 'k': 'k', 'l': 'w', 'm': 'f', 'n': 'V', 'o': 'A', 'p': 'e', 'q': 'a', 'r': 'q', 's': 'G', 't': 'y', 'u': 'l', 'v': 'I', 'w': 'n', 'x': 'i', 'y': 'H', 'z': 'u', 'A': 'c', 'B': 'r', 'C': 'h', 'D': 't', 'E': 'W', 'F': 'b', 'G': 'Z', 'H': 'j', 'I': 'T', 'J': 'P', 'K': 'g', 'L': 'R', 'M': 'J', 'N': 'L', 'O': 'z', 'P': 'C', 'Q': 'o', 'R': 'B', 'S': 'F', 'T': 'U', 'U': 'm', 'V': 'N', 'W': 'M', 'X': 'D', 'Y': 'X', 'Z': 'x', " ": " ", "\n" : "\n"}
    decoded_file = open("decoded_file.txt", "w")
    encoded_file = open("encoded_file.txt", "r")
    reversed_key = {}
    
    # create reversed key
    for item in key:
        temp_item = key[item]
        
        reversed_key[temp_item] = item
    
    # decode the file
    for line in encoded_file:
        decoded_line = ""
        
        for letter in line:
            decoded_line += reversed_key[letter]
        
        decoded_file.write(decoded_line)
        
    # close the files
    decoded_file.close()
    encoded_file.close()
    
def unique_words():
    # unique_words accepts no arguments
    # it reads the amount of unique words in text.txt
    
    # initialize set variable
    uniques = set()
    
    # open the file
    file = open("text.txt", "r")
    
    # read each line in the text file
    for line in file:
        # break it into a list
        words = line.split(" ")
        for word in words:
            # make sure theres not a newline in the word
            if "\n" in word:
                word = word.rstrip("\n")
            
            # add the word to the set
            uniques.add(word)
    # close the file
    file.close()
    
    print(f"There are {len(uniques)} unique word(s) in the file.")
    
def world_series():
    # world series recieves no arguments
    # it counts the number of wins per team in each year
    # then it tallies them up
    # and asks the user for the year and it will say the year they won
    # and how many times they've one
    
    # initialize variables
    STARTING_YEAR = 1903
    ENDING_YEAR = 2008
    year_counter = STARTING_YEAR
    selected_team = "none"
    winners = dict()
    file = open("WorldSeries.txt", "r")
    bad = True
    
    
    # read the file to create
    for line in file:
        # rstrip the line
        line = line.rstrip("\n")
        # make sure the world series was played that year
        if "World Series Not Played in" not in line:
            # check if it is already in the dictionary, if so add 1
            if line in winners:
                wins = winners[line]
                wins += 1
                winners[line] = wins
            # if not, set the wins to 1
            else:
                winners[line] = 1
    
    # while user inputs a bad input
    while bad == True:
        try:
            # ask for input
            year = int(input(f"Enter a year to find the winner of (YEARS {STARTING_YEAR} TO {ENDING_YEAR} ARE VALID): "))
            
            # validate it
            if year > ENDING_YEAR or year < STARTING_YEAR:
                print(f"Enter a team between valid years of {STARTING_YEAR} and {ENDING_YEAR}.")
            else:
                # set it to be a good input
                bad = False
        except:
            # output error
            print("Enter only numbers.")
            
            
    #close and reopen file to start reading from beginning
    file.close()
    file = open("WorldSeries.txt", "r")
    
    # read each line and check if it is the right year
    for line in file:
        if int(year_counter) == int(year):
            # print it was not played that year
            if "World Series Not Played in" in line:
                line = line.rstrip("\n")
                print(f"The {line}.")
                break
            
            # print the team that won and their win times.
            else:
                selected_team = line.rstrip("\n")
                times_team_won = winners[selected_team]
        
                print(f"The team {selected_team}, has won {times_team_won} time starting in {STARTING_YEAR}, ending in {ENDING_YEAR}.")
                break
        else:
            # add to year counter to keep track of year if it was not correct.
            year_counter += 1