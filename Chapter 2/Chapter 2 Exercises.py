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
    
    firstItem = input("Please enter a price for your first item: ")
    secondItem = input("Please enter a price for your second item: ")
    thirdItem = input("Please enter a price for your third item: ")
    fourthItem = input("Please enter a price for your fourth item: ")
    fifthItem = input("Please enter a price for your fifth item: ")
    
    subTotal = firstItem + secondItem + thirdItem + fourthItem + fifthItem
    
    salesTax = subTotal * .07
    
    