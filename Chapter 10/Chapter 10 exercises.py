# imports
import random
import pickle

# pet class exercises
class pet():
    # pet recieves no arguments
    def __init__(self):
        # init recieves no arguments
        # create starting values
        self.__name = "no_name"
        self.__animal_type = "no_type"
        self.__age = "no_age"

    def get_name(self):
        # get name recieves no arguments
        # it gets the pets name and returns it
        return self.__name

    def get_animal_type(self):
        # get animal type recieves no arguments
        # it returns the pets name
        return self.__animal_type

    def get_age(self):
        # get age recieves no arguments
        # it gets and returns the pets age
        return self.__get_age

def pet_main():
    # pet_main recieves no arguments
    # it handles all pet functions
    def pet_menu():
        # pet_menu recieves no arguments
        # it prints all inputs and returns a choice

        # initialize variables
        valid_choices = [1,2,3,4,5]
        choice = 0
        
        while choice not in valid_choices:
            try:
                choice = int(input("1) Add a pet\n2) Modify a pet\n3) Display a pet\n4) Display all pets\n5) Quit\n:>"))
            except:
                print("Invalid choice, use numbers only.")

        return choice
    
