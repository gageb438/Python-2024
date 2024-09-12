def example1():
    # exmaple1 accepts no arguments
    # it takes input from the user
    # and outputs a response based on the input
    
    choice = int(input("Enter 1 to continue..."))
    
    if choice == 1:
        # then this code will run
        print("Continuing...")
        # and this will run
        print("Continuing...")
        # and this
        print("and... continuing...")
    # if they entered anything anything other than 1 the code below will run
    else:
        print("You did not enter 1")
        print("Terminating the program")
    
    # this will run no matter what happens
    print("The program has completed")
    

def test_average():
    # test_average accepts no arguments
    # asks the user for test scores and averages them
    # outputs the average score and a congratulations if it is over 95.
    
    # assigns all 3 scores
    firstScore = float(input("Enter the first score: "))
    secondScore = float(input("Enter the second score: "))
    thirdScore = float(input("Enter the third score: "))
    highScore = 95.00
    # finds the average score
    averageScore = ((firstScore + secondScore + thirdScore) / 3)
    
    # prints the average score
    print("The average score is: %", format(averageScore, '.2f'), sep = '')
    
    # if the average score is greater than or equal to 95.00 it prints "Congratulations!" "Thats a high score!"
    if averageScore > highScore:
        print("Congratulations!")
        print("Thats a high score!")
        

def auto_repair_payroll():
    # auto repair payroll recieves no arguments
    # asks for the number of hours and pay rate, if they worked more than 40 hours they get overtime.
    # outputs their total pay
    
    overtimeNumber = 40
    hoursWorked = float(input("Enter the number of hours worked: "))
    hourlyPay = float(input("Enter your hourly pay: "))
    
    if hoursWorked > overtimeNumber:
        # finds the amount of hours of overtime worked
        overtimeHours = hoursWorked - overtimeNumber
        
        # calculates overtime pay and normal pay
        
        grossPay = (overtimeHours * (hourlyPay * 1.5)) + overtimeNumber * hourlyPay
    else:
        # calculates gross pay
        grossPay = hoursWorked * hourlyPay
    # prints your gross pay
    print(f"Your gross pay is: ${grossPay:,.2f}")


def password_verifier():
    # password_verifier accepts no arguments
    # asks the user for a password
    # outputs whether the password is correct or not
    
    # prints notice
    print("Case sensitive")
    
    # asks the user for their password
    userPassword = input("Please enter the password: ")
    
    # outputs whether the userpassword is accepted
    if userPassword == "prospero":
        print("Password accepted.")
    else:
        print("Password is invalid.")
        
        
def sort_names():
    # sort_names recieves no arguments
    # asks the user for two names
    # outputs them organized alphabetically
    firstNames = input("Enter the first name (last, first): ")
    secondNames = input("Enter the second name (last, first): ")
    
    print("Here are the names, sorted alphabetically.")
    
    if firstNames < secondNames:
        print(firstNames)
        print(secondNames)
    else:
        print(secondNames)
    

def loan_qualifier():
    # loan_qualifier recieves no arguments
    # asks the user for their salary and how long they have been at their job
    # outputs whether they qualify for a loan or not.
    
    # asks for the salary and the years
    salary = float(input("Enter your annual salary: "))
    years = float(input("Enter the number of year at your current job: "))
    qualifiedSalary = 30000
    
    # if their salary is 30000 checks for if they worked for 2 years
    if salary >= qualifiedSalary:
        if years >= 2:
            print("You qualify for the loan.")
        else:
            print("You must have been at your current job for a minimum of 2 years")
    else:
        print("Your salary must be atleast $", format(qualifiedSalary, '.2f'), sep = '')
        
        
def grader():
    # grader receives no arguments
    # asks the user for the grade
    # prints whether they got a grade a - f
    # asks the user for there test score
    gradeA = 90
    gradeB = 80
    gradeC = 70
    gradeD = 60

    testScore = float(input("Enter your test score: "))
    
    # checks if it is less than 0 and outputs an error message if true
    if testScore < 0:
        print("Error! Your score can not be lower than 0...")
    else:
        # finds their test grade and prints it.
        if testScore >= gradeA:
            print("Your grade is an A.")
        else:
            if testScore >= gradeB:
                print("Your grade is B.")
            else:
                if testScore >= gradeC:
                    print("Your grade is C.")
                else:
                    if testScore >= gradeD:
                        print("Your grade is D")
                    else:
                        print("Your grade is F")
                        
def grader2():
    # grader receives no arguments
    # asks the user for the grade
    # prints whether they got a grade a - f
    # asks the user for there test score
    gradeA = 90
    gradeB = 80
    gradeC = 70
    gradeD = 60

    testScore = float(input("Enter your test score: "))
    
    if testScore < 0:
        print("Error! Your score can not be lower than 0...")
    elif testScore >= gradeA:
        print("Your grade is A")
    elif testScore >= gradeB:
        print("Your grade is B")
    elif testScore >= gradeC:
        print("Your grade is C")
    elif testScore >= gradeD:
        print("Your grade is D")
    else:
        print("Your grade is F")
        
        
def loan_qualifier_v2():
    # loan_qualifier recieves no arguments
    # asks the user for their salary and how long they have been at their job
    # outputs whether they qualify for a loan or not.
    
    # asks for the salary and the years
    salary = float(input("Enter your annual salary: "))
    years = float(input("Enter the number of year at your current job: "))
    qualifiedSalary = 30000
    minimum_years = 2
    
    # if their salary is 30000 checks for if they worked for 2 years
    if salary >= qualifiedSalary and minimum_years >= 2:
        print("You qualify for the loan.")
    else:
        print("You do not qualify for the loan")
        

def loan_qualifier_v3():
    # loan_qualifier recieves no arguments
    # asks the user for their salary and how long they have been at their job
    # outputs whether they qualify for a loan or not.
    
    # asks for the salary and the years
    salary = float(input("Enter your annual salary: "))
    years = float(input("Enter the number of year at your current job: "))
    qualifiedSalary = 30000
    minimum_years = 2
    
    # if their salary is 30000 checks for if they worked for 2 years
    if salary >= qualifiedSalary or minimum_years >= 2:
        print("You qualify for the loan.")
    else:
        print("You do not qualify for the loan")
        
        
def is_valid():
    # is valid checks to see if a value is within a certain range
    # and it outputs "Within range" if it is and "outside range" if it
    # it isn't
    
    # declare flag variable
    valid = False
    
    # get input from the user
    value = int(input("Enter a value between 10 and 20: "))
    
    # process and output response
    if value >= 10 and value <= 20:
        valid = True
        
    if valid:
        print("Within range.")
    else:
        print("Outside range.")
        
        
def hit_the_target():
    # hit the target recieves no arguments
    # hit the target asks people for the power and angle
    # shows whether it hit the target or didn't hit the target
    
    
    # initializes variables
    screenWidth = 600
    screenHeight = 600
    targetLLeftX = 100
    targetLLeftY = 250
    targetWidth = 25
    forceFactor = 30
    projectileSpeed = 1
    north = 90
    south = 270
    east = 0
    west = 180
    
    import turtle as t
    
    t.setup(screenHeight,screenWidth)
    
    t.penup()
    t.goto(targetLLeftX, targetLLeftY)
    t.pendown()
    t.setheading(east)
    t.forward(targetWidth)
    t.setheading(north)
    t.forward(targetWidth)
    t.setheading(west)
    t.forward(targetWidth)
    t.setheading(south)
    t.forward(targetWidth)
    
    t.penup()
    t.goto(0,0)
    
    targetAngle = float(input("Enter the projectile's angle: "))
    launchForce = float(input("Enter the launch force: "))
    if launchForce >= 1 and launchForce <= 10:
        t.setheading(targetAngle)
        t.setforce(launchForce)
        