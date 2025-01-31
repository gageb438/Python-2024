#imports
import random
import time
import os

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
    TOTAL_QUESTIONS = 20
    while another.lower() == 'y':
        # prompt the user for the filename to read
        test_file = input("\nPlease enter the name of the file to read: ")
        
        if not os.path.exists(test_file):
            print(f"{test_file} not found.")
        else:
            # open the answerkey
            answer_key = open("driver_test_key.txt", "r")
            # open the test file
            test_answers = open(test_file, "r")
            
            # intialize answers key list and test_answers list
            answers = []
            user_answers = []
            # create the list with all the answers
            for line in answer_key:
                line = line.rstrip("\n")
                answers.append(line)
                
            for line in test_answers:
                line = line.rstrip("\n")
                user_answers.append(line)
            
            # create a list of wrong indexes and begin index
            wrong_indexes = []
            counter = -1
            correct = 0
            
            # check if each answer is correct
            for ans in answers:
                counter += 1
                if ans == user_answers[counter]:
                    correct += 1
                else:
                    # add wrong question number to list
                    wrong_indexes.append(counter + 1)
            
            # output message
            print("\nTest grading complete.")
            
            # output score and missed questsions
            print(f"\nYou answered {correct} questions correctly out of {TOTAL_QUESTIONS}")
            
            missed_questions = TOTAL_QUESTIONS - correct
            
            print(f"You missed {missed_questions}. The minimum you could miss to pass was 5.")
            
            if missed_questions > 5:
                print("You did not pass, study and try again.\n")
            else:
                print("\nCongratulations, you passed the exam!")
                
            if missed_questions == 0:
                print()
            else:
                print(f"Here are the questions you missed:\n{wrong_indexes}\n")
            
            another = input("Check another test? (y/n) : ")
            
            
            answer_key.close()
            test_answers.close()
            
def tic_tac_toe():
    # tic tac to plays the game
    # it calls everything to play the game

    def game_over(board):
        # game_over recieves an argument for the board
        # and checks if all plays have been made
        # without a winner
        # if so it returns true, false otherwise
            # left and right
        if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
            return False
        elif board[1][0] == board[1][1] and board[1][1] == board[1][2]:
            return False
        elif board[2][0] == board[2][1] and board[2][1] == board[2][2]:
            return False
        # up and down
        elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
            return False
        elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
            return False
        elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
            return False
        # diagnals
        elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            return False
        elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            return False
        else:
            return True


    # create the list for the board
    
    board = [["X", "X", "X"],
             ["O", "-", "-"],
             ["-", "O", "-"]]

    print(board)
    game_over(board)

    
