# this program allows the user to choose various
# geometry calculations from a menu. This program
# imports the circle and rectangle modules.
import circlemath
import rectanglemath

# constants for menu choices
AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5

# the main function
def main():
    # The choice variable controls the loop and holds the user's menu choice
    choice = 0
    
    while choice != QUIT_CHOICE:
        # display the menu
        display_menu()
        
        # get the user's choice
        choice = int(input("Enter your choice: "))
        
        # perform the selected action
        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input("Enter the circle's radius: "))
            print("The area is", circlemath.area(radius))
        elif choice == CIRCUMFERENCE_CHOICE:
            radius = float(input("Enter the circle's radius: "))
            print("The circumference is", circlemath.circumference(radius))
        elif choice == AREA_RECTANGLE_CHOICE:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print("The area is", rectanglemath.area(width, length))
        elif choice == PERIMETER_RECTANGLE_CHOICE:
            width = float(input("Enter your ractangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print("The perimeter is", rectanglemath.perimeter(width,length))
        elif choice == QUIT_CHOICE:
            print("Exiting program...")
        else:
            print("Error: Invalid selection.")
        
        print()

def display_menu():
    print("        MENU")
    print("1) Area of a circle")
    print("2) Circumference of a circle")
    print("3) Area of a rectangle")
    print("4) Perimeter of a rectangle")
    print("5) Quit")
    
    
# call the main function
main()
