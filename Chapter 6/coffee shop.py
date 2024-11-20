import os

#---------- coffee shop menu ----------
def coffee_shop_menu():
    # coffeee shop menu accepts no arguments
    # it displays and returns a menu chouice
    
    # display menu
    print("\nWelcome to Caffeine Overload Inventory Control System. Please choose an inventory option.")
    print("1) Add a record")
    print("2) Modify a record")
    print("3) Delete a record")
    print("4) Display all saved records")
    print("5) Search for a record")
    print("6) Exit")
    
    choice = input("Inventory option: ")
    
    return choice

#---------- coffee shop main ----------
def main(): # program 2-16 - 6-19
    # coffee shop main accepts no arguments
    # it calls coffee_shop_menu to display a menu to the user
    # and calls each function according to the user input
    
    # prime the loop
    choice = int(coffee_shop_menu())
    
    # validate the menu choice
    while choice <1 or choice > 5:
        print("Invalid choice.")
        choice = int(coffee_shop_menu())
        
    # loop to call the desired function
    while choice != 6:
        if choice == 1:
            write_coffee()
        elif choice == 2:
            modify_coffee()
        elif choice == 3:
            delete_coffee()
        elif choice == 4:
            read_coffee()
        elif choice == 5:
            search_coffee()
        choice = int(coffee_shop_menu())
    print("Thank you for using the Caffeine Overload Inventory Control System. Have a great day.")
    
#--------- write a record ----------
def write_coffee():
    # write_coffee accepts no arguments
    # it opens the file coffee.txt
    # it loops while the user wants to continue entering records
    # it prompts the user for coffee description and the amount of pounds
    # the user should be prompted if they want to continue
    
    # prime the loop, open the file to append, display the header
    another = 'y'
    coffee_file = open("coffee.txt", 'a')
    print("verify - writing")
    
    # loop to get the records from the user
    while another.lower() == 'y':
        print("Enter the following coffee data: \n")
        desc = input("Description: ")
        pounds = input("Quantity (in pounds): ")
        
        # append the information to the file
        coffee_file.write(desc + '\n')
        coffee_file.write(pounds + '\n')
        
        # prompt the user for another entry
        another = input("\nDo you want to enter another (y to continue) : ")
    
    # close the file and print closing message
    coffee_file.close()
    print("All data saved to coffee.txt")

#--------- read a record ---------
def read_coffee(): #program 6-16
    # read_coffee accepts no arguments
    # it loops to readf the records in coffee.txt
    # and ouputs the description and pounds of coffee
    
    # open coffee.txt and read the first description
    coffee_file = open("coffee.txt", 'r')
    desc = coffee_file.readline()
    
    while desc != "":
        desc = desc.rstrip("\n")
        pounds = coffee_file.readline().rstrip()
        
        # output
        print(f"Description: {desc}")
        print(f"Pounds: {pounds}")
        
        # read the next description
        desc = coffee_file.readline()
        
    # close the file
    coffee_file.close()
    print("All records read.")
       
#-------- search for records ---------
def search_coffee(): # program 6-17
    # search coffee accepts no arguments
    # it searches coffee.txt for a string the user enters
    # if no record matches, it outputs a message to the user
    
    # initialize a boolean flag variable
    found = False
    
    # get input from the user
    search = input("Enter a coffee name to search for: ")
    
    # open coffee.txt to read
    coffee_file = open("coffee.txt", "r")
    
    # get the first description to prime the loop
    desc = coffee_file.readline()
    
    while desc != "":
        # read the next line, pounds
        pounds = coffee_file.readline()
        
        # strip new line from description
        desc = desc.rstrip("\n")
        
        # check if desc == search string
        if desc.lower() == search.lower():
            print("\n---Record Found---")
            print(f"Description: {desc}")
            print(f"Pounds: {pounds}")
            found = True
            break
        
        # get the next description
        desc = coffee_file.readline()
    
    # close the file
    coffee_file.close()
    
    if not found: # if found == false
        print("\nThe record was not found.")
    
#---------- change a record ---------
def modify_coffee(): # program 6-18
    # modify coffee accepts no arguments
    # it imports the os module - this is needed to perform OS related file commands
    # it searches through the records and allows the user to modify the quantity
    
    # boolean flag variable
    found = False
    
    # get inputs from the user
    search = input("Enter the coffee description to modify: ")
    newQty = input("Enter the new quantity (in pounds): ")
    
    # open coffee.txt to read and a new temporary file to write
    coffee_file = open("coffee.txt", "r")
    temp_file = open("temp.txt.", "w")
    
    # read the first description to prime the loop
    desc = coffee_file.readline()
    
    # loop to read and process each record
    while desc != "":
        qty = coffee_file.readline()
        
        # strip newline
        desc = desc.rstrip("\n")
        qty = qty.rstrip("\n")
        
        if search.lower() == desc.lower(): # coffee found, add it and new qty to the temp file
            # write the description to temp.txt
            temp_file.write(desc + "\n")
            temp_file.write(qty + "\n")
            found = True
            break
        else: # not the coffee you are looking, write original description and original qty to temp file
            temp_file.write(desc + "\n")
            temp_file.write(qty + "\n")
            
        # read the next description
        desc = coffee_file.readline()
        
    # close both files
    coffee_file.close()
    temp_file.close()
    
    # delete the original coffee.txt
    os.remove("coffee.txt")
    
    #rename the temp file to coffee.txt
    os.rename("temp.txt", "coffee.txt")
    
    # description not found
    if found == False:
        print("\nRecord not found.")
    else:
        print(f"The quantity for {search} has been updated to {newQty} pounds.")

#--------- delete a record --------
def delete_coffee(): # program 6-19
    # delete coffee accepts no arguments
    # it opens the file coffee.txt and searches for a string to delete
    # it writes every other record to a temp file
    # then deletes the old file and renames temp.txt to coffee.txxt
    
    # set a boolean flag
    found = False
    
    # get the search description
    search = input("Enter the coffee description to delete: ")
    
    # open coffee.txt and temp.txt
    coffee_file = open("coffee.txt", "r")
    temp_file = open("temp.txt", "w")
    
    # read the first description to prime the loop
    desc = coffee_file.readline()
    
    # loop while there is input
    while desc != "":
        qty = coffee_file.readline()
        

main()