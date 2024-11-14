# imports
import menu
import math
import random
import my_graphics
import turtle

#==========================

def title():
    # title accepts no arguments
    # it handles the menu
    
    # calls menu
    choice = menu.main(9)
    # calls exercise
    if choice == 1:
        exercise1()
    elif choice == 2:
        exercise2()
    elif choice == 3:
        exercise3()
    elif choice == 4:
        exercise4()
    elif choice == 5:
        exercise5()
    elif choice == 6:
        exercise6()
    elif choice == 7:
        exercise7()
    elif choice == 8:
        exercise8()
    elif choice == 9:
        exercise9()

#==========================
    
def exercise1(): #sales tax
    # exercise_1 accepts no arguments
    # it asks for the sale amount and finds the tax
    # it is made using multiple functions that way it is modular.
    # it outputs the purchase price, state tax, county tax, total tax, and total sale.
    
    def sale():
        # sale amount accepts no arguments
        # it asks for the sale amount
        # returns the amount the sale was
        
        purchasePrice = float(input("Enter the sale amount : "))
        
        if purchasePrice <= 0:
            print("Please input a number greater than 0.")
            purchasePrice = float(input("Enter the sale amount : "))
        
        return purchasePrice
    
    def state(purchasePrice):
        # state_tax accepts an argument for the purchase price
        # it finds the state tax and returns it
        
        stateTax = purchasePrice * .05
        
        return stateTax
    
    def county(purchasePrice):
        # county tax accepts an argument for purchase price
        # it finds the county tax and returns it
        
        countyTax = purchasePrice * .025
        
        return countyTax
    
    def tax(stateTax, countyTax):
        # tax accepts an argument for stateTax and countyTax
        # calculates taxes and total sales and returns it
        
        totalTax = countyTax + stateTax
        
        return totalTax
    
    def total(totalTax, purchasePrice):
        # total accepts an argument for the tax and purchase price
        # it finds the total sale price and returns it
        
        totalSale = totalTax + purchasePrice
        return totalSale
        
    # calls functions
    purchasePrice = sale()
    stateTax = state(purchasePrice)
    countyTax = county(purchasePrice)
    totalTax = tax(stateTax, countyTax)
    totalSale = total(totalTax, purchasePrice)
    
    # outputs the sale amount, state tax, county tax, total tax, and total sale
    print("Your purchase price was:\t $", format(purchasePrice, '10.2f'), sep = '')
    print("Your state tax amount is:\t $", format(stateTax, '10.2f'), sep = '')
    print("Your county tax amount is:\t $", format(countyTax, '10.2f'), sep = '')
    print("Your total tax is:\t\t $", format(totalTax, '10.2f'), sep = '')
    print("Your total sale is:\t\t $", format(totalSale, '10.2f'), sep = '')
    
#==========================
    
def exercise2(): # calories
    # exercise 2 accepts no arguments
    # it asks you for the grams of carbs and grams of fat you consume
    # outputs your calorie intake for the day.
    
    def carbs():
        # carbs accepts no arguments
        # it asks for the amount of carbs you consumed and finds out how many calories that is
        # it returns the amount of calories they intook today(carbs)
        
        # asks for their intake
        carbIntake = float(input("How many grams of carbs did you consume? : "))
        
        # validates
        while carbIntake <0:
            carbIntake = float(input("Enter a valid amount of grams you consumed. :"))
            
        # finds the amount of calories
        carbCalories = carbIntake * 4
        
        return carbCalories
    
    def fat():
        # fat accepts no arguments
        # it asks for the amount of fat you consumed and finds how many calories that was
        # it returns the amount of calories they intook today(fat)
        
        # asks for their intake
        fatIntake = float(input("How many grams of fat did you consume? : "))
        
        # validates
        while fatIntake <0:
            fatIntake = float(input("Enter a valid grams of fat you consumed. : "))
            
        # finds the amount of fat calories
        fatCalories = fatIntake * 9
        
        return fatCalories
    
    def totalIntake(carbCalories, fatCalories):
        # total intake accepts arguments for carbCalories and fatCalories
        # it prints the total carb intake and fat intake with a message.
        # prints the amount of calories they consumed today
        
        print("Here is your calorie intake for the day.")
        print(f"You consumed {carbCalories} calories worth of carbs today. Nice work...")
        print(f"You consumed {fatCalories} calories worth of fats today. Nice work...")
    
    # finds carbs and fat
    carbCalories = carbs()
    fatCalories = fat()
    
    # passes the amount of carbs and fats to the printing
    totalIntake(carbCalories, fatCalories)
    
#==========================
    
def exercise3(): # stadium seating
    # exercise 3 accepts no arguments
    # it asks for the amount of class a, b, and c tickets sold
    # outputs the amount of sales from tickets as a float with 2 decimals
    
    def classA():
        # classA accepts no arguments
        # it asks for the number of class A tickets sold
        # it returns the variable for the amount of classA tickets sold
        
        # asks for the amount of class A tickets
        aTickets = int(input("Enter the number of Class A tickets sold: "))
        
        # validates
        while aTickets < 0:
            aTickets = int(input("Enter a valid number of Class A tickets sold: "))
            
        # returns the amount of tickets sold
        return aTickets
    
    def classB():
        # classB accepts no arguments
        # it asks for the number of class B tickets sold
        # it returns the variable for the amount of classB tickets sold.
        
        # asks for the amount of classB tickets
        bTickets = int(input("Enter the number of Class B tickets sold: "))
        
        # validates
        while bTickets < 0:
            bTickets = int(input("Enter a valid number of ClassB tickets sold: "))
            
        # returns the amount of tickets sold
        return bTickets
        
    def classC():
        # classC accepts no arguments
        # it asks for the number of classC tickets sold
        # it returns the variable for the amount of classC tickets sold.
        
        # ask for the amount of classC tickets sold
        cTickets = int(input("Enter the number of Class C tickets sold: "))
        
        # validates
        while cTickets < 0:
            cTickets = int(input("Enter a valid number of Class C tickets sold: "))
        
        # returns
        return cTickets
    
    def sales(aTickets, bTickets, cTickets):
        # sales accepts an argument for aTickets, bTickets, and cTickets
        # it calculates the total income sales from tickets
        # outputs the amount of income from the sales tickets.
        
        totalSales = ((aTickets * 20) + (bTickets * 15) + (cTickets * 10))
        
        print("The total income sales from tickets is: $", format(totalSales, '.2f'), sep = '')

    aTickets = classA()
    bTickets = classB()
    cTickets = classC()
    
    # calls sales passing aTickets, bTickets, and cTickets
    sales(aTickets, bTickets, cTickets)

#==========================

def exercise4(): # paint job estimator
    # exercise 4 recieves no arguments
    # it asks for the square feet of paint and how much each gallon of paint is
    # outputs the total number of paint gallons required, the cost of paint, the labor charges, and
    # the total cost of the paint job
    
    # initialize constants
    LABORHOURS = 8
    LABORCOST = 35
    WALLSPACE = 112
    
    def paintRequired():
        # paintRequired recieves no arguments
        # asks for the amount of the wall to be paitned
        # returns the total feet required to be painted
        
        squareFeet = float(input("Please enter the total square feet to be painted: "))
        
        # returns it
        return squareFeet
    
    def gallonCost():
        # gallonCost recieves no arguments
        # it asks for the cost of each gallon of paint
        # returns the cost
        
        cost = float(input("How much is each gallon of paint? : "))
        
        # returns
        return cost
    
    def totals(squareFeet, cost):
        # totals recieves an argument for the squareFeet, and cost of the gallons
        # it finds the total costs of everything
        # returns it all

        # finds the gallons
        gallons = WALLSPACE // squareFeet
        
        # finds if there is extra wallspace
        extraWallSpace = squareFeet % WALLSPACE

        if extraWallSpace != 0:
            gallons +=1
        
        # finds paint cost, and hour cost and total
        paintCost = gallons * cost
        hours = gallons * 8
        hourCost = hours * 35
        total = hourCost + paintCost
        
        # prints cost
        print()
        print(f"The cost breakdown of {squareFeet} square feet is:")
        print("-------------------------------------------")
        print(f"Total cost of paint: ${paintCost:,.2f}")
        print(f"Total labor cost: ${hourCost:,.2f}")
        print(f"Total cost of the job is: ${total:,.2f}")
        
    
    squareFeet = paintRequired()
    cost = gallonCost()
    totals(squareFeet, cost)

#==========================

def exercise5(): # math quiz
    # math quiz recieves no arguments
    # math quiz calls get_numbers to get two random numbers, loops while continue = y
    # outputs the problem to the user and prompts to answer the question.
    # prompts the user to continue (y/n)
    
    def get_numbers():
        # recieves no arguments
        # generates and returns two random integers from 1-200
        # outputs nothing
        number1 = random.randint(1,200)
        number2 = random.randint(1,200)
        
        return number1, number2
    
    # starts the continue loop
    go = "y"

    while go == "y":
        number1, number2 = get_numbers()
        answer = number1 + number2
        
        print("Solve:")
        print()
        print(f"\t\t{number1}")
        print(f"+\t\t{number2}")
        print()
        question = float(input("Answer: "))
        
        # finds if the answer is correct or not
        if question == answer:
            print("Correct!")
        else:
            print(f"Incorrect, the answer was {answer}")
        
        print()
        go = input("Do you want another problem (y/n) : ")
        
#==========================
        
def exercise6(): # falling distance
    # exercises 6 recieves no arguments
    # it finds the distance an object will fall for 10 seconds.
    # outputs the distance an object will fall for 10 seconds
    
    # initialize variable
    SECONDS = 10
    
    def time_loop(seconds):
        # time loop recieves seconds
        # loops 1-10 calls falling_distance passing time, 1-10 in seconds
        # outputs a table with each second and how far the object fell in that second.
        
        for time in range(1, seconds + 1):
            distance = falling_distance(time)
            print(f"{time} sec \t\t {distance:.2f}m")
            
    def falling_distance(time):
        # recieves time
        # calculates the distance fallen and returns distance
        # outputs nothing
        distance = .5 * 9.8 * time ** 2
        
        # returns
        return distance
    
    # prints header
    print(f"Here is the distance an object will fall for {SECONDS} seconds.")
    print("-------------------------------------------------------------------")

    
    time_loop(SECONDS)

#==========================

def exercise7(): # rock, paper, scissors, lizard, spock
    # exercise 7 recieves no arguments
    # it calls game to run the game.
    # outputs the winner and requests to play again
    
    def game():
        # game recieves no arguments
        # calls comp_choice, player_choice, and winner to play the game
        # outputs a greeting, each player's weapon, and prompts to continue.
        
        def comp_choice():
            # comp_choice recieves no arguments
            # chooses a random integer 1-5 and returns the integer
            # outputs nothing
            
            computer_weapon = random.randint(1,5)
            
            return computer_weapon
        
        def player_choice():
            # player choice recieves no arguments
            # it prompts the user for their weapon and returns the weapon
            # outputs choose your weapon. (rock, paper, scissors, lizard, spock)
            
            player_weapon = input("Type your weapon of choice (rock, paper, scissors, lizard, spock) : ")
            
            return player_weapon.lower()
        
        def winner(computer_weapon, player_weapon):
            # winner recieves computer_weapon and player_weapon
            # determines the winner
            # outputs who won
            
            # creates computer weapon
            if computer_weapon == 1:
                computer_weapon = "rock"
            elif computer_weapon == 2:
                computer_weapon = "paper"
            elif computer_weapon == 3:
                computer_weapon = "scissors"
            elif computer_weapon == 4:
                computer_weapon = "lizard"
            elif computer_weapon == 5:
                computer_weapon = "spock"

            # prints what the player chose
            print()
            print("You chose... ", player_weapon, ".", sep = '')
            print()
            print("Computer chose... ", computer_weapon, ".", sep = '')
            print()
            
            # finds who won
            if player_weapon == computer_weapon:
                print("It's a tie!")
            elif player_weapon == 'rock' and computer_weapon == 'scissors':
                print(f"You win! Rock crushes scissors.")
            elif player_weapon == 'rock' and computer_weapon == 'lizard':
                print("You win! Rock crushes lizard.")
            elif player_weapon == 'rock' and computer_weapon == 'paper':
                print("You lose. Paper covers rock.")
            elif player_weapon == 'rock' and computer_weapon == 'spock':
                print("You lose. Spock vaporizes rock.")
            elif player_weapon == 'paper' and computer_weapon == 'rock':
                print("You win! Paper covers rock.")
            elif player_weapon == 'paper' and computer_weapon == 'spock':
                print("You win! Paper disproves spock.")
            elif player_weapon == 'paper' and computer_weapon == 'scissors':
                print("You lose. Scissors cuts paper.")
            elif player_weapon == 'paper' and computer_weapon == 'lizard':
                print("You lose. Lizard eats paper.")
            elif player_weapon == 'scissors' and computer_weapon == 'rock':
                print("You lose. Rock crushes paper.")
            elif player_weapon == 'scissors' and computer_weapon == 'paper':
                print("You win! Scissors cuts paper.")
            elif player_weapon == 'scissors' and computer_weapon == 'lizard':
                print("You win! Scissors decapitates lizard.")
            elif player_weapon == 'scissors' and computer_weapon == 'spock':
                print("You lose. Spock smashes scissors.")
            elif player_weapon == 'lizard' and computer_weapon == 'rock':
                print("You lose. Rock crushes lizard.")
            elif player_weapon == 'lizard' and computer_weapon == 'paper':
                print("You win! Lizard eats paper.")
            elif player_weapon == 'lizard' and computer_weapon == 'scissors':
                print("You lose. Scissors decapitates lizard.")
            elif player_weapon == 'lizard' and computer_weapon ==  'spock':
                print("You win! Lizard poisons spock.")
            elif player_weapon == 'spock' and computer_weapon == 'rock':
                print("You win! Spock vaporizes rock.")
            elif player_weapon == 'spock' and computer_weapon == 'paper':
                print("You lose. Paper disproves spock.")
            elif player_weapon == 'spock' and computer_weapon == 'scissors':
                print("You win! Spock smashes scissors.")
            elif player_weapon == 'spock' and computer_weapon == 'lizard':
                print("You lose. Lizard poisons spock.")
            else:
                print("The computer wins! You entered an invalid weapon. Cheater!")
            
            print()
            play = input("Would you like to play again?(y/n) :> ")
            
            if play == 'y':
              game()
        computer_weapon = comp_choice()
        player_weapon = player_choice()
        winner(computer_weapon, player_weapon)
    game()
    
#==========================   

def exercise8():
    # exercise 8 recieves no arguments
    # it handles the snowman drawing functions
    # outputs a snowman
    
    def drawSnowman():
        # recieves no arguments
        # main function to call all other functions
        # outputs nothing
        
        def drawBase():
            # drawBase recieves no arguments
            # draws the base of the snowman
            # outputs the bottom most large circle.
            turtle.pencolor('black')
            my_graphics.circle(0, -150, 150, 'blue')
            
        def drawMidSection():
            # drawMidSection recieves no arguments
            # draws the mid section of the snowman
            # outputs the second largest circle on top of the first
            my_graphics.circle(0, 120, 125, 'blue')
            
        def drawArms():
            # drawArms recieves no arguments
            # draws the arms of the snowman
            # outputs seven total lines depicting arms
            my_graphics.line(-113, 170, -250, 110, 'brown')
            my_graphics.line(-250, 110, -280, 10, 'brown')
            my_graphics.line(-250, 110, -270, 160, 'brown')
            my_graphics.line(113, 170, 250, 60, 'brown')
            my_graphics.line(250, 60, 280, 130, 'brown')
            my_graphics.line(250, 60, 220, 120, 'brown')
            my_graphics.line(250, 60, 270, -40, 'brown')
            turtle.pencolor('black')
            
        def drawHead():
            # draw head recieves no arguments
            # draws the head for the snowman with the eyes
            # outputs a smaller circle on top of the middle circle. Two filled circles for eyes
            my_graphics.circle(0, 330, 100, 'blue')
            
        def drawHat():
            # drawHat recieves no arguments
            # draws the hat for the snowmal
            # two rectangular shapes filled to depict a hat
            my_graphics.rectangle(-75,430, 150, 40, 'red')
            my_graphics.rectangle(27,470, -150, -60, 'red')
        
        def drawFace():
            # draw face recieves no arguments
            # draws a mouth and a corncomb pipe with smoke billowing out
            # outputs a line for the mouth, a filled square attached to a line
            # attached to the mouth for the pipe
            # loop to create gray smoke billowing out of the pipe with a thicker pen size
            my_graphics.circle(-50, 375, 10, 'black')
            my_graphics.circle(50, 375, 10, 'black')
            my_graphics.line(-60, 290, 60, 290, 'black')
            my_graphics.line(40, 290, 150, 155, 'brown')
            my_graphics.square(160,165, 10, 'brown')
            turtle.pensize(10)
            turtle.setheading(90)
            for swirl in range(4):
                turtle.left(20)
                turtle.forward(10)
                               
        turtle.speed(50)
        drawBase()
        drawMidSection()
        drawArms()
        drawHead()
        drawHat()
        drawFace()
        turtle.done()
        
    drawSnowman()
    
#==========================
    
def exercise9():
    # exercise 9 recieves no arguments
    # it draws a checkerboard
    # outputs a checkerboard
    
    # initialize variables
    SQUAREWIDTH = 100
    WIDTH = 5
    HEIGHT = 5
    isBlack = True
    squareX = -500
    squareY = 500
    turtle.speed = 180
    # setup turtle
    turtle.setup(1500,1500)
    for height in range(HEIGHT):
        for width in range(WIDTH):
            if isBlack == True:
                my_graphics.square(squareX,squareY, SQUAREWIDTH, 'black')
                squareX = squareX + SQUAREWIDTH
                isBlack = False
            else:
                my_graphics.square(squareX,squareY, SQUAREWIDTH, 'white')
                squareX = squareX + SQUAREWIDTH
                isBlack = True
        
        squareX = squareX - (SQUAREWIDTH * WIDTH)
        squareY = squareY - SQUAREWIDTH
            
    turtle.done()
    
title()
