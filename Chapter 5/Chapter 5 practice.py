# Chapter 5 practice is where all of my practice assignments for Chapter 5 are stored.
# Imports
import math
import turtle
import random
import circle

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

my_value = 10

def show_value(): # program 5-13
    # show value recieves no arguments
    # it prints the value of global my_value
    
    print("The value of the global variable my_value is", my_value)
    
#==========================
    
# create a global variable
number = 0 # 

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
    
#==========================
    
def example_main(): # example to return values
    # main accepts no arguments
    # it passes a value to calc()
    # and outputs the result
    
    num = int(input("Enter a number from 1-10:  "))
    
    # pass num to calc
    answer = calc(num)
    
    # prints the result
    print(f"The result is: {answer}")
    
def calc(number):
    # calc accepts an argument for number
    # it performs a calculation with the number
    # and returns the calculation
    
    # perform calculation
    answer = number + 5
    
    return stuff

#==========================

def random_numbers(): # program 5-16
    # random_numbers accepts no arguments
    # it generates a random in teger from 1-10
    # output the number to the user
    
    number = random.randint(1,10)
    
    print(f"The random number is: {number}")
    
#==========================
    
def random_numbers_2(): # program 5-17
    # random numbers 2 accepts no arguments
    # it loops 5 times assigning a random integer from 1-100 to a number
    # it ouputs the random integer for each iteration
    
    for count in range(5):
        number = random.randint(1,100)
        print(f"The number is : {number}")
        
#==========================

def random_numbers_3(): # program 5-18
    # random numbers 2 accepts no arguments
    # it loops 5 times outputting a new random integer for each iteration
    
    # loop 5 times
    for count in range(5):
        print(random.randint(1,100))

#==========================
        
def dice(): # program 5-19
    # dice accepets no arguments
    # it loops until the user enters "n" or "N" to stop
    # each iteration prints two random 6-sided die rolls
    # it prompts the user to roll again (y/n)
    
    # initializes variables
    keep_going = "y"
    Min = 1
    Max = 6
    
    # starts or ends based on their input
    while keep_going == "y":
        # prints the dice numbers
        print("Rolling your dice...")
        print("Your two rolls are ", random.randint(Min,Max), " and ", random.randint(Min,Max))
        
        # asks if they want to keep going
        keep_going = input("Try your luck again? (y/n) : ")
        
        # prints seperator
        print()
        
#==========================
        
def coin_toss(): # program 5-20
    # coin toss accepts no arguments
    # it sets three named constants for heads, tails, and tosses
    # it loops for 10 tosses and uses a random integer from 1 or 2 to determine
    # if the coin flip resulted in a heads or tails, respectively
    
    # initializes variables
    heads = 1
    tails = 2
    tosses = 10
    
    # repeats finding tosses
    for toss in range(tosses):
        randomToss = random.randint(heads,tails)
        if randomToss == heads:
            print("Heads!")
        elif randomToss == tails:
            print("Tails!")
        else:
            print("An error has occurred")

#==========================
            
def total_ages(): # program 5-21
    # def total ages accepts no arguments
    # it prompts the user for two ages and passes those values to calculate_ages()
    # it uses the return value to print the total ages
    
    # get input from the user
    age1 = int(input("Please enter your age: "))
    age2 = int(input("Please enter the age of your best friend: "))
    
    # call calculate ages, passing age1 and age2 and assign the return value to total
    total = calculate_ages(age1, age2)
    
    # output the result
    print("\nTogether you are", total, "years old.")
    
def calculate_ages(age1, age2):
    # calculate ages recieves values for age1 and age2
    # it addes the two ages together
    # and returns the result
    
    # calculate the total age
    total_ages = age1 + age2
    
    # return the value
    return total_ages

#==========================

# declare global constant for program 5-22
discount_percent = 0.20

def sale_price(): # program 5-22
    # sale price accepts no arguments
    # it calls get regular price to get input from the user
    # it calculates the sale price by taking the regular price and subtracting the
    # return result of discount()
    # it outputs the sale price
    
    regular_price = get_regular_price()
    final_price = discount(regular_price)
    
    print("The sale price is: $", format(final_price, ',.2f'), sep = '')
def get_regular_price():
    # get regular price accepts no arguments
    # it prompts the user to input the item's regular prie
    # and returns that value
    regular_price = float(input("Please enter the regular price of the item: "))
    
    # returns the price
    return regular_price

def discount(price):
    # discount accepts an argument for the float price
    # it returns the discount @ 20% off using
    # the global constant discount_percent
    
    # finds final price
    discount_price = price * discount_percent
    final_price = price - discount_price
    
    # returns the final rpice for printing
    return final_price

#==========================

def comission_rate(): # program 5-23
    # comission rate accepts no arguments
    # it calls get-sales and get_advanced_pay
    # it calls determine_comm_rate passing sales
    # it calculates the pay and outputs the pay
    # it determines if the pay is negative and outputs if the salesperons
    # the amount the salesperson must reimburse the company for
    
    # calls functions to prompt user for sales and advanced pay
    sales = get_sales()
    advanced_pay = get_advanced_pay()
    
    # passes sales on to find the comm rate
    comm_rate = determine_comm_rate(sales)
    
    # calculates the pay and prints it
    pay = ((sales * comm_rate) - advanced_pay) + sales
    print("\nThe total pay with comission is $", format(pay, ',.2f'), sep = '')
    
    # prints how much the salesperson must pay the company if the pay is below 0
    if pay < 0:
        print("The salesperson must reimburse the company $", pay * -1, sep = '')
        
def get_sales():
    # get sales accepts no raguments
    # it prompts the user to input the total monthly sales
    # and returns the monthly sales
    
    sales = float(input("Please enter the amount of sales for the month: "))
    
    # returns sales
    return sales
def get_advanced_pay():
    # get advanced pay accepts no arguments
    # it prompts the user to enter any advanced pay, or 0 for none
    # it returns the advanced pay
    
    advanced_pay = float(input("Please enter any advanced pay you recieved (0 for none): "))
    
    return advanced_pay
def determine_comm_rate(sales):
    # determine comm rate accepts a float for sales
    # it calculates the comission rate for sales
    # and returns the calculated rate
    
    # finds commission rate
    if sales < 10000:
        comm_rate = .10
    elif sales < 14999:
        comm_rate = .12
    elif sales < 17999:
        comm_rate = .14
    elif sales < 21999:
        comm_rate = .16
    else:
        comm_rate = .18
    
    return comm_rate

#==========================

def isValid(num): # example boolean function
    # is valid accepts an integer argument
    # it will validate that the integer is > 0
    
    if num > 0:
        return True
    else:
        return False
    
#==========================
    
def get_name(): # string return example
    # get name accepts no arguments
    # it prompts the user for a name
    # and returns the name as a string
    
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    return first_name, last_name
    
def validate_even(num): # boolean return example
    # validate even accepts an integer for num
    # it tests if num is even and returns true
    
    if (num % 2) == 0:
        return True
    else:
        return False
    
#==========================
    
def square_root(): # program 5-24
    # square_root accepts no arguments
    # it prompts the user for a number and calculates square root
    # outputs a message with the square root of the number the user chose
    
    # finds the number the user wants to find the square root of
    number = float(input("Please enter a value to find the square root: "))
    
    # finds the square root
    sqRoot = float(math.sqrt(number))
    
    # prints the number and the square root
    print(f"The square root of {number} is: {sqRoot}")
    
#==========================

def hypotenuse(): # program 5-25
    # hypotenuse recieves no arguments
    # it prompts the user for two sides
    # outputs a message with the hypotenuse
    
    # finds the two sides
    side1 = float(input("Enter the length of side A: "))
    side2 = float(input("Enter the length of side B: "))
    
    length = math.hypot(side1, side2)
    
    print(f"The length of the hypotenuse is: {length}")
    
    
arar = circle.area(20)
print(arar)