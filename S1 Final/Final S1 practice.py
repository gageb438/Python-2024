# imports
import os
import random

def main():
    # main recieves no arguments
    # it prints the title and calls the functions for their questions
    # outputs the file and old results if requested

    # intialize variable
    score = 0
    
    # ask the questions
    for question_num in range(1, 10):
        score += question(question_num)
    
    # print total score
    print(f"Quiz Completed! Your score: {score}/10")
    
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
            q1_choice = input("Enter your choice (a/b/c): ")
            while q1_choice.isnumeric() == True:
                q1_choice = input("Enter your choice (a/b/c): ")
            while q1_choice > "c":
                q1_choice = input("Enter your choice (a/b/c): ")
            if q1_choice.lower() == "b":
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
            q2_choice = input("Enter your choice (a/b/c): ")
            while q2_choice.isnumeric() == True:
                q2_choice = input("Enter your choice (a/b/c): ")
            while q2_choice > "c":
                q1_choice = input("Enter your choice (a/b/c): ")
            if q2_choice.lower() == "c":
                print("Correct!")
                score = 1
            else:
                print("Incorrect.")
            print()
            return score
        except:
            print("Input one of the letters.")
            question(2)

def save(score):
    # save recieves an argument for user score
    # it asks the user if they would like to save
    # and if they would like to display old results
    
    name = input("\nWhat is your name? : ")
    
    save = input("Would you like to save your results? (yes/no) : ")
    
    if save.lower() == "yes":
        infile = open("test_results.txt", "a")
        # write the result to the file
        infile.write(f"{name} - {score}/10" + "\n")
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