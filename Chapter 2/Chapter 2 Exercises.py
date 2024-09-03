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
    amountOfCookies = float(input("How many cookies do you want to make? "))
    sugarCups = int((.5 * amountOfCookies) // 8)
    sugarOunces = int((.5 * amountOfCookies) % 8)
    flourCups = int((.9166 * amountOfCookies) // 8)
    flourOunces = int((.9166* amountOfCookies) % 8 )
    butterCups = int((.3333 * amountOfCookies) // 8)
    butterOunces = int((.3333 * amountOfCookies) % 8)
    print("For ", amountOfCookies," cookies you will need:", sep = '')
    print(sugarCups," cup(s) ", sugarOunces, " Ounce(s) of sugar.", sep = '')
    print(butterCups," cup(s) ", butterOunces, "ounce(s) of sugar.", sep = '')
    
    
