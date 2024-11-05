# imports
import menu
import math
import random
import my_graphics

#==========================

def title():
    # title accepts no arguments
    # it handles the menu
    
    # calls menu
    choice = menu.main()
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
    
    def totals():
        # totals recieves an argument for the squareFeet, and cost of the gallons
        # it finds the total costs of everything
        # returns it all

        # finds the gallons
        gallons = wallSpace % squareFeet
        
        # finds if there is extra wallspace
        extraWallSpace = squareFeet % wallSpace

        if extraWallSpace != 0:
            gallons += 1

        
        
title()
