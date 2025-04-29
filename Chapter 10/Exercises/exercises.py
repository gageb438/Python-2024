import pet
import pickle

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
        
        return choice
    
    def add_pet():
        # add a pet recieves no arguments
        # it adds a pet to the pet list
        name = input("Enter the pets name: ")
        typee = input("Enter the pets type: ")
        age = input("Enter the pets age: ")
        
        file = open("inventory.dat", "rb")
        data = pickle.load(file)
        file.close()
        
        pet_obj = pet.Pet(name, typee, age)
        data.append(pet_obj)
        
        file = open("inventory.dat", "wb")
        pickle.dump(data, file)
        file.close()
        
        return
    
    def modify_pet():
        # modify pet modifies a pet
        # and re-writes the file
        
        file = open("inventory.dat", "rb")
        data = pickle.load(file)
        
        # get the pets name to find
        name = input("Enter the name of the pet you want to find: ")
        name = name.lower()
        