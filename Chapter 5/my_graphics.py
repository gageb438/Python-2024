# imports
import turtle


def circle(x, y, radius, color):
    # circle accepts an argument for x, y, the radius, and the color
    # it draws a circle using those aguments
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    
    
def square(x, y, width, color):
    # square accepts an argument for x, y, the width, and the color
    # it draws a square using those aguments
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()

def rectangle(x,y, topWidth, sideWidth, color):
    # rectangle accepts an argument for the x,y, topWidth, sideWidth, and color
    # it draws a rectangle using these arguments
    turtle.penup()
    turtle.goto(x,y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(topWidth)
    turtle.left(90)
    turtle.forward(sideWidth)
    turtle.left(90)
    turtle.forward(topWidth)
    turtle.left(90)
    turtle.forward(sideWidth)
        
    turtle.end_fill()

def line(startX, startY, endX, endY, color):
    # line accepts arguments for startx, starty, endx, endy, and color
    # it draws a line using these arguments
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.goto(endX, endY)
