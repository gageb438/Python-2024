# Chapter 5 practice is where all of my practice assignments for Chapter 5 are stored.
# Imports
import math
import turtle
import random
#==========================

def message(): # program 5-1
    # function message accepts no arguments
    # it outputs "I am Iron Man"
    
    # prints the message
    print("I am Iron Man.")


def main_5_2(): # program 5-2
    # main_5_2 accepts no arguments
    # it prints "I am inevitable"
    # calls the procedure message()
    # then prints "only one way to win"
    
    # prints the message and calls the function message()
    print("I am inevitable.")
    message()
    print("Only one way to win...")


def acme_dryer(): # program 5-3
    # acme_dryer recieves no arguments
    # it prints steps to disassemble a dryer
    # outputs goodbye message at the end
    
    def greeting():
        # greeting recieves no arguments
        # it prints the greeting and requests the user to input a step.
        print("Hello welcome to the Acme Dryer disassembly guide.")
        print("Please enter a step number below. 0 to exit.")
        
    def goodbye():
        # goodbye recieves no arguments
        # it prints the goodbye message
        print("Goodbye, thank you for using the Acme Dryer Disassembly guide.")
    
    def step1():
        # step1 recieves no arguments
        # it prints step 1
        print("Unplug the dryer and move it away from the wall")
    
    def step2():
        # step 2 recieves no arugments
        # it prints step 2
        print("Remove the six screws from the back of the dryer")
        
    def step3():
        # step 3 recieves no arguments
        # it prints step 3
        print("Remove the back panel")
    
    def step4():
        # step 4 recieves no arguments
        # it prints step 4
        print("Pull the top of the dryer straight up")
        
    def step5():
        # step 5 recieves no raguments
        # it prints step 5
        print("Pull the front dryer off.")
   
    def question():
        # question recieves no arguments
        # it requests for the step number
        # outputs the step and calls the question again
        # if 0 is entered prints a goodbye.
        greeting()
        stepNumber = int(input(":> "))
        
        while stepNumber < 0 or stepNumber > 5:
            stepNumber = int(input("Enter a valid step number :> "))
            
        if stepNumber == 1:
            step1()
            question()
        elif stepNumber == 2:
            step2()
            question()
        elif stepNumber == 3:
            step3()
            question()
        elif stepNumber == 4:
            step4()
            question()
        elif stepNumber == 5:
            step5()
            question()
        elif stepNumber == 0:
            goodbye()
        
    # starts the function
    print()        
    question()
    
    
def bad_scope(): # program5-4
    # bad local accepts no arguments
    # it calls procedure get_name() to get someones name
    # then outputs am essage using that name
    #NOTE: The scope of the variable "name" in get_name will not
    # allow this function to access this variable
    
    get_name()
    print("Hello", name) # this will throw an exception
    

def get_name():
    # get name accepts no arguments
    # it prompts the user to get their name
    
    name = input("Enter your name: ")


def bird_calculator(): # program5-5
    # bird_calculator accepts no arguments
    # it calls the function texas()
    # then calls the function kansas()
    
    def texas():
        # texas accepts no arguments
        # it assigns the variable birds = 5000
        # then outputs a message "There are <birds> in Texas.")
        birds = 5000
        print("There are ", birds, " birds in Texas.", sep = '')
        
    def kansas():
        # kansas accepts no arguments
        # it assigns the variable birds = 8000
        # then outputs a message "There are <birds> in Kansas.")
        birds = 8000
        print("There are ", birds, " birds in Kansas.", sep = '')
    
    texas()
    kansas()
        