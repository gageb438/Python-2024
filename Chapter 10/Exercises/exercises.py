import pet
import pickle
import os

def pet_driver():
    # pet driver recieves noa rguments
    # it drives the pet class
    # it outputs a menu
    # and does what the option was
    
    def menu():
        # menu recieves no arguments
        # it prints the menu, returns the choice
        
        # initialize choices
        choices = [1,2,3,4,5]
        choice = -1
        
        print("1) Add a pet\n2) Modify a pet\n3) Display a pet\n4) Display all pets\n5) Quit")
        while choice not in choices:
            try:
                choice = int(input("Enter a choice: "))
            except:
                pass
        
        if choice == 1:
            add_pet()
        elif choice == 2:
            modify_pet()
        elif choice == 3:
            display_pet()
        elif choice == 4:
            display_all()
        else:
            print("Goodbye.")
        
        return choice
    
    def add_pet():
        # add a pet recieves no arguments
        # it adds a pet to the pet list
        
        # initialize data
        data = []
        
        # get info
        print()
        name = input("Enter the pets name: ")
        typee = input("Enter the pets type: ")
        age = input("Enter the pets age: ")
        print()
        
        if os.path.exists("pets_data.dat"):
            file = open("pets_data.dat", "rb")
            
            # account for empty file
            try:
                data = pickle.load(file)
            except:
                data = []
            
            # close
            file.close()
        else:
            # create and close
            file = open("pets_data.dat", "wb")
            file.close()
            
        pet_obj = pet.Pets(name, typee, age)
        data.append(pet_obj)
        
        file = open("pets_data.dat", "wb")
        pickle.dump(data, file)
        file.close()
        
        return
    
    def modify_pet():
        # modify pet modifies a pet
        # and re-writes the file
        
        if not os.path.exists("pets_data.dat"):
            print("No pets stored, returning to menu! Add some before trying to find.")
            return
        
        file = open("pets_data.dat", "rb")
        data = pickle.load(file)
        
        # get the pets name to find
        name = input("Enter the name of the pet you want to modify(CASE SENSITIVE): ")
        
        for item in data:
            if item.get_name() == name:
                typee = input("Enter the pets type: ")
                age = input("Enter the pets age: ")
                
                item.set_animal_type(typee)
                item.set_age(typee)
            else:
                print("Pet not found.")
                
        file.close()
        
    def display_pet():
        # display pet recieves no arguments
        # it displays the requested pet
        # and outputs it
        
        if os.path.exists("pets_data.dat"):
            file = open("pets_data.dat", "rb")
            
            pet_name = input("What is the name of the pet? (CASE SENSITIVE): ")
            data = pickle.load(file)
            for item in data:
                if item.get_name() == pet_name:
                    print()
                    print(item)
                    print()
                    printed = True
            if printed != True:
                print("Pet not found.")
        else:
            print("\nNo pets stored, returning to menu! Add some before trying to find.\n")
            return
        file.close()
    
    def display_all():
        # display all receieves no argument
        # it reads the whole fiel
        # and displays everything
        if os.path.exists("pets_data.dat"):
            file = open("pets_data.dat", "rb")
        else:
            print("\nNo pets stored, returning to menu! Add some before trying to find.\n")
            return
        
        data = pickle.load(file)
        for item in data:
            print()
            
        file.close()
    
    choice = 1
    
    while choice != 5:
        choice = menu()
pet_driver()