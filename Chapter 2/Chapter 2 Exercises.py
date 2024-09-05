import turtle as t

def personal_info():
    # personal_info accepts no arguments
    # This program asks user for and displays personal information
    # Outputs personal information
    
    # Asks user for their name, address, phone number, and major
    Name = input("What is your name? ")
    Address = input("What is your address? ")
    Phone_Number = input("What is your phone number? ")
    Major = input("What is your projected college major? ")
    
    
    # Prints their answers to the questions
    print("Here is what you have input: ")
    print("Your name is: ", Name, sep = '')
    print("Your phone number is: ", Phone_Number, sep = '')
    print("Your address is: ", Address, sep = '')
    print("Your major is: ", Major, sep = '')
    

def total_purchase():
    # total_purchase accepts no arguments
    # This program asks people for the cost of items and then adds it up with tax
    # Outputs the subtotal, tax, and total.
    
    # Asks the user for the price of their five items
    firstItem = float(input("Please enter a price for your first item: "))
    secondItem = float(input("Please enter a price for your second item: "))
    thirdItem = float(input("Please enter a price for your third item: "))
    fourthItem = float(input("Please enter a price for your fourth item: "))
    fifthItem = float(input("Please enter a price for your fifth item: "))
    
    # calculates subtotal, tax, and total
    subTotal = firstItem + secondItem + thirdItem + fourthItem + fifthItem
    salesTax = subTotal * .07
    finalTotal = subTotal + salesTax

    # prints the sub total, sales tax, and final total formatted
    print("Subtotal:\t$", format(subTotal, '8.2f'), sep = '')
    print("Tax:\t\t$", format(salesTax, '8.2f'), sep = '')
    print("Total:\t\t$", format(finalTotal, '8.2f'), sep = '')

def distance_traveled():
    # distance_traveled accepts no arguments
    # this program asks for how fast someone is driving
    # outputs how far they will go in 6,10, and 15 hours
    
    # asks for how fast they are driving
    drivingSpeed = int(input("How fast are you driving? "))
    
    # calculates the time
    sixHours = (6 * drivingSpeed)
    tenHours = (10 * drivingSpeed)
    fifteenHours = (15 * drivingSpeed)
    
    # outputs the distance they will go
    print("At 60 miles per hour you will travel ", sixHours," miles in 6 hours.", sep = '')
    print("At 60 miles per hour you will travel ", tenHours," miles in 10 hours.", sep = '')
    print("At 60 miles per hour you will travel ", fifteenHours," miles in 15 hours.", sep = '')
    
    
def sales_tax():
    # sales_tax accepts no arguments
    # this program asks for the sale price and outputs the tax and total cost
    # outputs tax and total cost
    
    # asks for the scale amount
    saleAmount = float(input("Enter the sale amount: "))
    
    # calculates taxes and total sales
    stateTax = saleAmount * .05
    countyTax = saleAmount * .025
    totalTax = countyTax + stateTax
    totalSale = saleAmount + totalTax
    
    # prints taxes, total sales, and sale amount,
    print("Your purchase price was:\t $", format(saleAmount, '10.2f'), sep = '')
    print("Your state tax amount is:\t $", format(stateTax, '10.2f'), sep = '')
    print("Your county tax amount is:\t $", format(countyTax, '10.2f'), sep = '')
    print("Your total tax is:\t\t $", format(totalTax, '10.2f'), sep = '')
    print("Your total sale is:\t\t $", format(totalSale, '10.2f'), sep = '')
    
    
def tip_tax_total():
    # tip_tax_total accepts no arguments
    # asks user for their sale amount and calculates the tip and tax then total
    # outputs the sale amount, tip amount, and tax amount
    
    # asks for sale amount
    gross_total = float(input("Please enter the sale amount: $"))
    tip = gross_total * .18
    tax = gross_total * .07
    net_total = tip + tax + gross_total
    
    print("The sale was: \t\t\t$",format(gross_total, '7.2f'), sep = '')
    print("The tip amount is: \t\t$",format(tip, '7.2f'), sep = '')
    print("The sales tax amount is: \t$",format(tax, '7.2f'), sep = '')
    print("The total bill is: \t\t$",format(net_total, '7.2f'), sep = '')
    
    
def temp_converter():
    # temp_converter recieves no arguments
    # asks the user for the degrees in celsius then converts it to farenheit
    # outputs the amount in farenheit
    degreesCelsius = float(input("Please enter the degrees Celsius: "))
    
    # converts it to farenheit
    fahrenheit = float(((9/5) * degreesCelsius) + 32)
    
    # outputs the degrees celsius
    print(int(degreesCelsius)," degrees celsius is ", format(fahrenheit, '.1f'), " degrees fahrenheit", sep = '')
    
    
def cookie_monster():
    # cookie monster recieves no arguments
    # asks user for how many cookies they want to make
    # outputs the amoutn of sugar, butter, and flour needed to make the
    
    # asks for the amount they want to make
    amountOfCookies = float(input("How many cookies do you want to make? "))

    # calculates the recipe
    sugarCups = float((.5 * amountOfCookies) // 8)
    sugarOunces = float((.5 * amountOfCookies) % 8)
    flourCups = float((.9166 * amountOfCookies) // 8)
    flourOunces = float((.9166* amountOfCookies) % 8 )
    butterCups = float((.3333 * amountOfCookies) // 8)
    butterOunces = float((.3333 * amountOfCookies) % 8)

    # outputs the recipe
    print("For ", amountOfCookies," cookies you will need:", sep = '')
    print(format(sugarCups, '.0f'), " cup(s) ", format(sugarOunces, '.0f'), " ounce(s) of sugar.", sep = '')
    print(format(butterCups, '.0f'), " cup(s) ", format(butterOunces, '.0f'), " ounce(s) of sugar.", sep = '')
    print(format(flourCups,'.0f')," cup(s) ", format(flourOunces, '.0f'), " ounce(s) of sugar.", sep = '')


def class_demographics():
    # class demographics recieves no arguments
    # asks the user for the amount of males and females in a class
    # outputs the percent of males and females

    females = float(input("Enter the number of females: "))
    males = float(input("Enter the number of males: "))

    # adds to find the total of males and females.
    total = females + males

    # calculates the percent of males and females
    femalePercent = float((females / total) * 100)

    malePercent = float((males / total) * 100)

    # outputs the amount of males and females
    print("The class consists of ", format(femalePercent, '.0f'),"% females and ", format(malePercent, '.0f'), "% males.", sep = '')
    
    
def tortuga_1():
    # tortuga_1 recieves no arguments
    # draws and labels the compass rose
    # draws a compass rose and labels it
    
    # assigns all the variables
    north_x = (0)
    north_y = (200)
    south_x = (0)
    south_y = (-200)
    east_x = (200)
    east_y = (0)
    west_x = (-200)
    west_y = (0)
    northeast_x = (100)
    northeast_y = (100)
    northwest_x = (-100)
    northwest_y = (100)
    southeast_x = (100)
    southeast_y = (-100)
    southwest_x = (-100)
    southwest_y = (-100)
   
    # set the turtle up
    t.goto(0,0)
    t.pensize(5)
    
    # draws the north-south line and labels
    t.goto(north_x, north_y)
    t.write("N", font = ("Arial", 16))
    t.goto(south_x, south_y)
    t.penup()
    t.goto(south_x - 20, south_y - 20)
    t.write("S", font = ("Arial", 16))
    t.pendown()
    
    # returns to 0,0
    t.penup()
    t.goto(0,0)
    
    # draws east-west line and labels
    t.pendown()
    t.goto(west_x, west_y)
    t.write("W", font = ("Arial", 16))
    t.goto(east_x, east_y)
    t.write("E", font = ("Arial", 16))
    
    # returns to 0,0 and changes pensize
    t.penup()
    t.goto(0,0)
    t.pensize(2.5)
    
    # draws northeast-southwest line
    t.pendown()
    t.goto(northeast_x, northeast_y)
    t.goto(southwest_x, southwest_y)
    
    # returns to 0,0
    t.goto(0,0)
    
    # draws northwest-southeast line
    t.goto(northwest_x, northwest_y)
    t.goto(southeast_x, southeast_y)
    
    t.hideturtle()
    t.done()


def tortuga_2():
    # tortuga_2 recieves no arguments
    # it draws the olympic rings
    # outputs the olympic rings
    
    # assigns variables and there locations
    bluering_x = -200
    bluering_y = 0
    yellowring_x = -100
    yellowring_y = -100
    blackring_x = 0
    blackring_y = 0
    greenring_x = 100
    greenring_y = -100
    redring_x = 200
    redring_y = 0
    
    t.penup()
    t.goto(bluering_x, bluering_y)
    t.pensize(15)
    t.pencolor("blue")
    t.pendown()
    t.circle(90)
    
    t.penup()
    t.goto(yellowring_x, yellowring_y)
    t.pencolor("yellow")
    t.pendown()
    t.circle(90)
    
    t.penup()
    t.goto(blackring_x, blackring_y)
    t.pencolor("black")
    t.pendown()
    t.circle(90)
    
    t.penup()
    t.goto(greenring_x, greenring_y)
    t.pencolor("green")
    t.pendown()
    t.circle(90)
    
    t.penup()
    t.goto(redring_x, redring_y)
    t.pencolor("red")
    t.pendown()
    t.circle(90)
    