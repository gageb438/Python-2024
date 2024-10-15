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

#==========================

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
    
#==========================

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

#==========================

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

#==========================


def pass_arg(): # program5-6
    # pass args accepts no arguments
    # it assigns the value = 5
    # it calls show_double, passing value
    
    value = 5
    show_double(value)
    

def show_double(number):
    # show double accepts a value for a number
    # it calculates that number * 2 and prints the result
    
    result = number * 2
    print(number, "* 2 =", result)

#==========================

def volume_conversion(): # program 5-7
    # volume conversion accepts no arguments
    # it calls intro() to display a greeting
    # it prompts the user for the number of cups
    # it calls cups_to_ounces, passing the value for cups
    
    # calls greeting
    intro()
    
    # asks for the amount of cups and validates it
    cups = int(input("Please enter the number of cups to convert to ounces: "))
    while cups <= 0:
        cups = int(input("Please enter a valid number of cups to convert to ounces: "))
    
    # calls cups to ounces and passes cups on
    cups_to_ounces(cups)
    
def intro():
    # into accepts no arguments
    # it displasy a greeting message describing the program
    # and the conversion rate of cups to ounces
    print("Welcome to the cups to fluid ounces conversion program.\nFor your reference, 1 cup = 8 fluid ounces")
    
def cups_to_ounces(cups):
    # cups_to_ounces accepts a value for cups
    # it converts the number of cups to the number of ounces
    # and outputs the result
    
    # finds ounces
    ounces = cups * 8
    
    #  prints how many cups is equal to ounces
    print(cups, " cup(s) is equal to ", ounces, " fluid ounces.", sep = '')

#==========================

def show_sum(): # program 5-8
    # show sum accepts no arguments
    # it ouputs a message "The sum of 12 and 45 is"
    # it calls sum_of_numbers(num1, num2) passing the values 12 and 45
    num1 = 12
    num2 = 45
    sum_of_numbers(num1, num2)
    
def sum_of_numbers(num1, num2):
    # sume of numbers accepts two arguments for num1 and num2
    # it adds the two numbers together
    # and prints the sum
    sumof = num1 + num2
    print("The sum of ", num1, " and ", num2, " is ", sumof, sep = '')

#==========================

def get_name(): # program5-9
    # get name accepts no arguments
    # it prompts the user for their first then last name
    # it calls reverse_name(first, last) passing values
    # for first and last
    firstName = input("Please enter your first name: ")
    lastName = input("Please enter your last name: ")
    reverse_name(firstName, lastName)
    
def reverse_name(first, last):
    # reverse name accepts strings for first and last
    # it ouputs the names in reverse order
    print("Your name reversed is: ", last, " ", first, sep = '')

#==========================

def get_value(): # program 5-10
    # get value accepts no arguments
    # it assigns value = 99 and passes value to change_me
    # it ouputs a message showing the value of value in this function
    value = 99
    print("I just assigned the variable value: ", value)
    change_me(value)
    print("The value in the function get_value is still: ", value)
    
def change_me(value):
    # change me accepts an integer for value
    # it reassigns the value to 0
    # and ouputs a message with the new value in this function
    value = 0
    print("The value in the function change_me has changed to: ", value)

#==========================

def set_args(): # program5-11
    # set args accepts no arguments
    # it calls show_interest passing principal, rate, and periods as keywords
    
    show_interest(principal = 10000.0, rate = 0.01, periods = 10)
    
def show_interest(principal, rate, periods):
    # show interest accepts arguments for rate, periods, and principal
    # it calculates the interest = principal*rate*periods
    
    interest = principal * rate * periods
    print("The simple interest will be $", format(interest, '.2f'), sep = '')

#==========================

# my_value = 10 # global variable disabled to prevent issues

def show_value(): # program 5-13
    # show value recieves no arguments
    # it prints the value of global my_value
    
    print("The value of the global variable my_value is", my_value)
    
#==========================
    
# create a global variable
# number = 0 # disabled to prevent issues

def change_global(): # program 5-14
    # change_global accepts no arguments
    # it changes the value of the global variable number
    # then calls global_variables_are_bad to print the variable
    
    global number
    number = int(input("What do you want to change global to? :> "))
    global_variables_are_bad()
    
def global_variables_are_bad():
    # global variables are bad accepts no arguments
    # it prints the value of the global variable number
    
    print("The value of the global variable number was changed in change_global to the value of :", number)
    
#==========================
    
# global constant for program 5-15
CONTRIBUTION_RATE = 0.05

def pay_me(): # program5-15
    #pay me accepts no arguments
    # it prompots the user for the gross pay and the maount of bonuses
    # it calls show_pay, passing gross
    # and show_bonus, passing bonus
    gross_pay = float(input("Please enter the amount for gross pay: "))
    bonus = float(input("Please enter the amount of bonuses: "))
    
    show_pay(gross_pay)
    show_bonus(bonus)
    
def show_pay(gross_pay):
    # show pay accepts a float for gross
    # it calculates the contribution = gross * the global constant
    # it outputs the contribution for gross pay
    
    final_pay = gross_pay * CONTRIBUTION_RATE
    print("Contribution for gross pay: $", format(final_pay, ',.2f'), sep = '')
    
def show_bonus(bonus):
    # show_bonus accepts a float for a gbonus
    # it calculates the contribution = bonus * the global constant
    # it outputs the contribution for bonuses
    
    final_bonus = bonus * CONTRIBUTION_RATE
    print("Contribution for gross pay: $", format(final_bonus, ',.2f'), sep = '')
    