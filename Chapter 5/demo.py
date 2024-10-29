import circlemath
import rectanglemath

def main():
    # main accepts and argument fron the user
    # and uses the circle and rectangle modules
    # to calculate the area, circumference
    # and perimeter
    
    # take input form the user for the radius
    radius = int(input("Enter the radius: "))
    
    # use the circlemath.py module to find the area of the circle
    print(f"The area of the circle is: {circlemath.area(radius)}.")
    print(f"The circumference of the circle is: {circlemath.circumference(radius)}.")
    
    # take input from the user for the length and width of a rectangle
    length = int(input("Enter the length of a side: "))
    width = int(input("Enter the width of a side: "))

    # use the rectanglemath.py module to find the area and perimeter of a rectangle
    print(f"The perimeter of the rectangle is: {rectanglemath.perimeter(width, length)}.")
    print(f"The area of the rectangle is: {rectanglemath.area(width, length)}.")
main()
