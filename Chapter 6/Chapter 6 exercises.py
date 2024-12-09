# imports
import menu

def main():
    # menu recieves no arguments
    # it calls the module menu and processes the choice
    # it then calls the exercise based of the choice
    
    # initialize variable
    choice = -1
    
    # checks if it is below 0 or above 8
    while 1:
        try:
            while choice < 0 or choice > 8:
                choice = menu.menu()
        except:
            print("Please choose a number between 0 and 8.")
            main()

    if choice == 1:
        line_numbers()
    elif choice == 2:
        line_counter()
    elif choice == 3:
        average_numbers()
    elif choice == 4:
        random_number_write()
    elif choice == 5:
        random_number_read()
    elif choice == 6:
        golf_scores()
    elif choice == 7:
        personal_page_generator()
    elif choice == 8:
        average_steps()
    elif choice == 0:
        print("Goodbye.")

def line_numbers(): #exercise 3
    pass

def line_counter(): #exercise 4
    pass

def average_numbers(): #exercise 6
    pass

def random_number_write(): # exercise 7
    pass

def random_number_read(): #exercise 8
    pass

def golf_scores(): #exercise 10
    pass

def personal_page_generator(): #exercise 11
    pass

def average_steps(): #exercise 12
    pass

