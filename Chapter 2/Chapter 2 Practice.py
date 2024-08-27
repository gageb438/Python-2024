# Chapter 2 Practice


def practice1():
    # practice 1 accepts no arguments
    # it outputs a message to the user
    print("This is practice 1.")
    
    
def practice2():
    # practice 2 accepts no arguments
    # it outputs another message to the user
    print("This is practice 2.")

# hit run to use the command bar


def comment_example():
    # comment_example accepts no arguments
    # it explains how to create a function header
    # and  outputs or returns "Hello World!".
    print("Hello World!")
    
def program2_1():
    
    # program2_1 accepts no arguments
    # apostrophe output
    # it outputs 3 comments in one function.
    print ('Kate Austen')
    print ('123 Full Circle Drive')
    print ('Asheville, NC 28899')
    
    
def program2_2():
    
    # program2_2 accepts no arguments.
    # double apostrophe output.
    # it outputs 3 comments in one function.
    print ("Kate Austen")
    print ("123 Full Circle Drive")
    print ("Asheville, NC 28899")
    
    
def program2_3():
    
    # program 2_3 accepts no arguments.
    # outputs 2 comments in one function.
    print ("Don't fear!")
    print ("I'm here!")


def program2_4():
    
    # program 2_4 accepts no arguments
    # use backslash before the start and before the end quotation to ignore characters.
    print ("I read \"Hamlet\" this summer.")
    
    
def program2_7():
    
    # program 2_7 accepts no arguments
    # it uses the variable room to store the value 503
    # and prints the message to the user
    
    # assigns 503 to RoomNumber
    RoomNumber = 503
    
    
    # outputs the message to the user
    print ("I am staying in room number")
    print (RoomNumber)
    
    
    # outputs the message to the user using a second way
    print ("I am staying in room number", RoomNumber)


def program2_8():
    # program2_8 accepts no arguments
    
    # assigns a number to the variables
    TopSpeed = 160
    Distance = 300
    
    # outputs the message to the user
    print ("The top speed is:")
    print (TopSpeed)
    
    # outputs the message to the user
    print ("The distance traveled is:")
    print (Distance)
    
    
def program2_9():
    #program2_9 recieves no arguments
    
    # assigns a number to the variable
    RoomNumber = 503
    
    # outputs the message to the user
    print("I am staying in room number", RoomNumber)
    
    
def program2_10():
    # program2_10 recieves no arguments
    # it prints the amount of money and then modifies it
    # it outputs the total money at the end
    
    # assigns numbers to the variable
    AmountOfMoney = 2.75
    
    # outputs the message to the user
    print("I have", AmountOfMoney,"in my account")
    
    # re-assigns the variable
    AmountOfMoney = 99.95
    
    # outputs the message to the user
    print ("But now I have", AmountOfMoney,"in my account")
     
  
def program2_12():
    # program 2_12 recieves no arguments
    # it takes input for two strings
    # and outputs a message
    
    # asks for their first and last name
    FirstName = input("Enter your first name: ")
    LastName = input("Enter your last name: ")
    
    # outputs their first and last name
    print ("Hello", FirstName, LastName,)
    

def program2_13():
    # program 2_13 recieves no arguments
    # it takes input for 3 strings, converts 1 to float
    # and outputs the inputs
    
    # asks for name, age, and income
    # converts income to a float
    Name = input("What is your name? ")
    Age = int(input("What is your age? "))
    Income = float(input("What is your income? "))
    
    print ("Here is the data you have entered: ")
    print ("Name:",Name)
    print ("Age:",Age)
    print ("Income: $",Income)
   
   
def program2_14():
    # program2_14 recieves no arguments
    
    # Variables for money
    MoneyFromPaycheck = 3600
    MoneyFromTip = 100
    
    # Calculates total pay
    TotalSalary = float(MoneyFromTip + MoneyFromPaycheck)
    
    # Outputs total salary
    print("Your pay is: $",TotalSalary)
    
    
def program2_15():
    # program2_15 recieves no arguments
    
    # requests the user to input the price of an item
    OriginalPrice = int(input("What is the price of the item? "))
    
    # finds the amount to discount from the price
    DiscountPrice = OriginalPrice * .20
    
    # finds the total price
    TotalPrice = float(OriginalPrice - DiscountPrice)
    
    # prints the total price
    print("The sale price is $",TotalPrice)
    

def GetAverage():
    # GetAverage recieves no arguments
    
    FirstScore = float(input("Enter the first test score: "))
    SecondScore = float(input("Enter the second test score: "))
    ThirdScore = float(input("Enter the third test score: "))
    
    AverageScore = ((FirstScore + SecondScore + ThirdScore) // 3)
    
    print("The average score is: ",AverageScore)
    
    
def program2_17():
    # program2_17 recieves no arguments
    
    # requests the user for the total seconds
    seconds = float(input("Enter the number of seconds: "))
    
    # assigns variables and does equations
    total_hours = (seconds // 3600)
    minutes = (seconds // 60) % 60
    total_seconds = seconds % 60

    # returns the converted time
    print("Here is the time in hours, minutes, and seconds:")
    print("Hours: ",total_hours)
    print("Minutes: ",minutes)
    print("Seconds: ",total_seconds)
    

def program2_18():
    # program2_18 accepts no arguments
    # get the desired value
    # calculate the amount that will have to be deposited
    # output the result
    
    # get the desired future value
    future_value = float(input("Enter the desired future value: "))
    
    # get the annual interest rate
    annual_intrest = float(input("Enter the annual interest rate: "))
    
    # get the number of years that the money will grow
    number_of_years = int(input("Enter the number of years the money will grow: "))
    
    # calculate the amount needed to deposit
    amount_to_deposit = future_value / (1 + annual_intrest) ** number_of_years
    
    # output the result
    print ("You will need to deposit ",amount_to_deposit)
    

    