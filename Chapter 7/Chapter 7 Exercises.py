#imports
import random
import time
import os
import menu

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
        if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != '-':
            return False
        elif board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != '-':
            return False
        elif board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] != '-':
            return False
        # up and down
        elif board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != '-':
            return False
        elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != '-':
            return False
        elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != '-':
            return False
        # diagnals
        elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != '-':
            return False
        elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != '-':
            return False
        else:
            return True
        
    def winner_check(board):
        # game_over recieves an argument for the board
        # and checks if all plays have been made
        # without a winner
        # if so it returns true, false otherwise
            # left and right
        if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != '-':
            return board[0][0]
        elif board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != '-':
            return board[1][0]
        elif board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] != '-':
            return board[2][0]
        # up and down
        elif board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != '-':
            return board[0][0]
        elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != '-':
            return board[0][1]
        elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != '-':
            return board[0][2]
        # diagnals
        elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != '-':
            return board[0][0]
        elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != '-':
            return board[0][2]
        else:
            return 'Tie'
        
    # create the list for the board
    board = [["-", "-", "-"],
             ["-", "-", "-"],
             ["-", "-", "-"]]
    x_or_o = 0
    not_over = True
    
    while not_over == True:
        x_or_o += 1
        index1 = random.randint(0,2)
        index2 = random.randint(0,2)
        while board[index1][index2] != '-':
            index1 = random.randint(0,2)
            index2 = random.randint(0,2)
        
        if x_or_o % 2 == 0:
            letter = "X"
        else:
            letter = "O"
        
        board[index1][index2] = letter
        
        not_over = game_over(board)

    winner = winner_check(board)
    if winner != 'Tie':
        print(f"Winner is {winner}")
    else:
        print("It's a draw!")

    print(board[0],"\n",board[1],"\n",board[2], sep = '')
    
def white_elephant():
    # white elephant recieves no arguments
    # it gives a random person to a random person on who they should gift
    # it outputs who can gift who
    
    # create the lists
    development_department = ["Julia", "Oliver", "Abigail"]
    hr_department = ["Camden", "Kayleigh", "Cooper", "Kerrigan"]
    sales_department = ["Avery", "Charlotte", "Elle"]
    
    # initialize lists
    givers = ["Julia", "Oliver", "Abigail", "Camden", "Kayleigh", "Cooper", "Kerrigan", "Avery", "Charlotte", "Elle"]
    recievers = ["Julia", "Oliver", "Abigail", "Camden", "Kayleigh", "Cooper", "Kerrigan", "Avery", "Charlotte", "Elle"]
    PEOPLE = ["Julia", "Oliver", "Abigail", "Camden", "Kayleigh", "Cooper", "Kerrigan", "Avery", "Charlotte", "Elle"]
    
    print("Here are the results:")
    # find who gets gifted to who
    for person in PEOPLE:
        giver = random.choice(givers)
        reciever = random.choice(recievers)
        while giver in development_department and reciever in development_department or giver in hr_department and reciever in hr_department or giver in sales_department and reciever in sales_department:
            giver = random.choice(givers)
            reciever = random.choice(recievers)
        print(f"{giver} gifts to {reciever}")
        # remove them from the list
        givers.remove(giver)
        recievers.remove(reciever)
    
def magic_8_ball():
    # magic 8 ball asks people for a qquestion
    # it reads from a file and adds the responses to a list
    # it prints the answer
    
    response = open("8_ball_responses.txt", "r")
    responses = []
    again = 'y'
    
    for res in response:
        responses.append(res)
    response.close()
    while again == 'y':
        input("\nWhat is your question? ")
        print()
        response = random.randint(0,11)
        print(responses[response])
        again = input("Do you want to ask another question? (y/n): ")
    
    print('\nBeware the prophecy... Take care.')
    
keep_going = 'y'
while keep_going == 'y':
    menu_number = menu.menu(7)
    if menu_number == 1:
        lottery()
    elif menu_number == 2:
        rainfall()
    elif menu_number == 3:
        charge_accts()
    elif menu_number == 4:
        drivers_exam()
    elif menu_number == 5:
        tic_tac_toe()
    elif menu_number == 6:
        white_elephant()
    elif menu_number == 7:
        magic_8_ball()
    
    keep_going = input("Would you like to run another program? (y/n): ")