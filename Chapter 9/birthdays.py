def birthday_main():
    # birthday main recieves no arguments
    # it presets a variable for the dictionary, then gets user choice
    
    # preset birthdays
    birthdays = dict()
    
    # get choice and find option
    choice = get_menu_choice()
    while choice != 5:
        if choice == 1:
            look_up(birthdays)
        elif choice == 2:
            add_bday(birthdays)
        elif choice == 3:
            change_bday(birthdays)
        elif choice == 4:
            delete_bday(birthdays)
        # recall the choice
        choice = get_menu_choice()
    
    print("Goodbye.")
    
def get_menu_choice():
    # get menu choice recieves no arguments
    # it gets the users menu choice
    # and returns it
    
    # preset variables
    go = True
    
    # print headers
    print("\nFriends and their birthdays\n---------------------------\n1. Lookup\n2. Add a new birthday\n3. Change a birthday\n4. Delete a birthday\n5. Quit")
    
    # while they mess up, ask for another choice
    while go == True:
        try:
            choice = int(input("\nEnter a menu choice: "))
            
            if choice < 1 or choice > 5:
                print("Use only numbers on the list.")
            else:
                go = False
        except:
            print("Numbers only")
    
    return choice
def look_up(birthdays):
    # look up recieves an argument for birthdays
    # it looks to see if the birthday is in the dictionary
    
    person = input("\nWho would you like to search for: ")
    if birthdays == {}:
        print("\nThere are no birthdays to search!")
    else:
        date = birthdays.get(person, "Not found.")
        print(date)
        
def add_bday(birthdays):
    # add birthday recieves an argument for the dictionary of birthdays
    # it adds the users birthday and name into the dictionary
    # if there is already one, it outputs an errotr message.
    
    name = input("\nEnter a name: ")
    birthday = input("Enter a birthday: ")
    
    if name in birthdays:
        print("\nName already being used.")
    else:
        birthdays[name] = birthday
    

def change_bday(birthdays):
    # change bday recieves an argument for the dictionary if birthdays
    # it checks to see if the name is in the dictionary
    # then changes it to what the user wants.
    
    person = input("\nEnter a name to change the birthday for: ")
    birthday = input("Enter a new birthday: ")
    
    if person in birthdays:
        birthdays[person] = birthday
        print(f"\nBirthday changed for {person}.")
    else:
        print(f"\n{person} not found.")

def delete_bday(birthdays):
    # delete birthday recieves an argument for the dictionary of bithdays
    # it deletes the person from the dictionary
    
    person = input("\nEnter a name to delete: ")
    if person in birthdays:
        del birthdays[person]
        print(f"\n{person} deleted.")
    else:
        print(f"\n{person} not found.")

birthday_main()