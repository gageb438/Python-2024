# imports
import os
import random

def main():
    # main recieves no arguments
    # it prints the title and calls the functions for their questions
    # outputs the file and old results if requested

    # intialize variable
    score = 0
    TOTAL_QUESTIONS = 4 # max is 10
    if TOTAL_QUESTIONS > 10 or TOTAL_QUESTIONS < 1:
        print("Critical Error, TOTAL_QUESTIONS is configrued wrong.")
        return
    
    # ask the questions
    for question_num in range(1, TOTAL_QUESTIONS + 1):
        score += question(question_num)
    
    # print total score
    print("Quiz Completed! Your score:",score, "/", TOTAL_QUESTIONS, sep = '')
    
    # call the save prompt
    save(score)
    load()
    
def question(question_num):
    # question recieves an argument for the question number
    # it asks the user two qusetions and checks if their choices are correct
    # outputs the question and the choice input
    
    # initalize score
    score = 0
    
    # check question number and output question
    if question_num == 1:
        # question 1
        print("1. What is 20 + 30")
        print("\ta) 40\n\tb) 50\n\tc) 70")
        
        try:
            choice = input("Enter your choice (a/b/c): ")
            while choice.isnumeric() == True:
                choice = input("Enter your choice (a/b/c): ")
            while choice > "c":
                choice = input("Enter your choice (a/b/c): ")
            if choice.lower() == "b":
                print("Correct!")
                score = 1
            else:
                print("Incorrect.")
            print()
            return score
        except:
            print("Input one of the letters.")
            question(1)
    
    if question_num == 2:
        # question 2
        print("2. What is 5 + 7?")
        print("\ta) 10\n\tb) 11\n\tc) 12")
        
        try:
            choice = input("Enter your choice (a/b/c): ")
            while choice.isnumeric() == True:
                choice = input("Enter your choice (a/b/c): ")
            while choice > "c":
                choice = input("Enter your choice (a/b/c): ")
            if choice.lower() == "c":
                print("Correct!")
                score = 1
            else:
                print("Incorrect.")
            print()
            return score
        except:
            print("Input one of the letters.")
            question(2)

    if question_num == 3:
        # question 3
        print("3. What is 12 + 32?")
        print("\ta) 44\n\tb) 34\n\tc) 54")
        
        try:
            choice = input("Enter your choice (a/b/c): ")
            while choice.isnumeric() == True:
                choice = input("Enter your choice (a/b/c): ")
            while choice > "c":
                choice = input("Enter your choice (a/b/c): ")
            if choice.lower() == "a":
                print("Correct!")
                score = 1
            else:
                print("Incorrect.")
            print()
            return score
        except:
            print("Input one of the letters.")
            question(3)

    if question_num == 4:
        # question 4
        print("4. What is -12 + 46?")
        print("\ta) 46\n\tb) -34\n\tc) 34")
        
        try:
            choice = input("Enter your choice (a/b/c): ")
            while choice.isnumeric() == True:
                choice = input("Enter your choice (a/b/c): ")
            while choice > "c":
                choice = input("Enter your choice (a/b/c): ")
            if choice.lower() == "c":
                print("Correct!")
                score = 1
            else:
                print("Incorrect.")
            print()
            return score
        except:
            print("Input one of the letters.")
            question(4)

    if question_num == 5:
        # question 5
        print("5. What is -400 - 32?")
        print("\ta) -342\n\tb) -432\n\tc) -423")
        
        try:
            choice = input("Enter your choice (a/b/c): ")
            while choice.isnumeric() == True:
                choice = input("Enter your choice (a/b/c): ")
            while choice > "b":
                choice = input("Enter your choice (a/b/c): ")
            if choice.lower() == "b":
                print("Correct!")
                score = 1
            else:
                print("Incorrect.")
            print()
            return score
        except:
            print("Input one of the letters.")
            question(5)
            
    if question_num == 6:
        # question 6
        print("6. What is 109 * 177?")
        print("\ta) 19239\n\tb) 20891\n\tc) 18413")
        
        try:
            choice = input("Enter your choice (a/b/c): ")
            while choice.isnumeric() == True:
                choice = input("Enter your choice (a/b/c): ")
            while choice > "a":
                choice = input("Enter your choice (a/b/c): ")
            if choice.lower() == "a":
                print("Correct!")
                score = 1
            else:
                print("Incorrect.")
            print()
            return score
        except:
            print("Input one of the letters.")
            question(6)
            
    if question_num == 7:
        # question 7
        print("7. What is 27 / 3?")
        print("\ta) 6\n\tb) 3\n\tc) 9")
        
        try:
            choice = input("Enter your choice (a/b/c): ")
            while choice.isnumeric() == True:
                choice = input("Enter your choice (a/b/c): ")
            while choice > "c":
                choice = input("Enter your choice (a/b/c): ")
            if choice.lower() == "c":
                print("Correct!")
                score = 1
            else:
                print("Incorrect.")
            print()
            return score
        except:
            print("Input one of the letters.")
            question(7)

def save(score):
    # save recieves an argument for user score
    # it asks the user if they would like to save
    # and if they would like to display old results
    
    name = input("\nWhat is your name? : ")
    
    save = input("Would you like to save your results? (yes/no) : ")
    
    if save.lower() == "yes":
        infile = open("test_results.txt", "a")
        # write the result to the file
        infile.write(name," - ",score,"/10" + "\n", sep = '')
        # close the file
        infile.close()
        print("\nResults saved successfully.\n")

def load():
    # load recieves no arguments
    # it asks the user if they would like to load previous results
    # output previous results
    
    load = input("Would you like to load your old results? (yes/no) : ")
    
    if load.lower() == "yes":
        if os.path.exists("test_results.txt"):
            outfile = open("test_results.txt", "r")
        else:
            print("No results found")
            return
        
        # loop to print the results
        score = "A"
        print("Previous Results:")

        while score != "":
            score = outfile.readline().rstrip("\n")
            print(score)

main()
