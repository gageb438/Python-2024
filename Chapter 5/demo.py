import circle
import rectangle

def main():
    # main accepts and argument fron the user
    # and uses the circle and rectangle modules
    # to calculate the area, circumference
    # and perimeter
    
    # take input form the user for the radius
    radius = int(input("Enter the radius: "))
    
    # use the circle.py module to find the area of the circle
    print(f"The area of the circle is: {circle.area(radius)}.")
    print(f"The circumference of the circle is: {circle.circumference(radius)}.")
    
    # take input from the user for the length and width of a rectangle
    length = int(input("Enter the length of a side: "))
    width = int(input("Enter the width of a side: "))
    
    print(f"The perimeter of the rectangle is: {rectangle.perimeter(width, length)}.")
    print(f"The area of the rectangle is: {rectangle.area(width, length)}.")
main()