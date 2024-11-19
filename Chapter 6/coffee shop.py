import io

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
        choice == int(coffee_shop_menu())
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
        
main()