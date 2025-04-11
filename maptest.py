import turtle

turtle.setup(500, 500, 0, 0)

def starting_room():
    # starting room draws starting room in turtle
    turtle.hideturtle()
    turtle.penup()
    
    # get variables
    ROOM_HEIGHT = 50
    ROOM_HALF = ROOM_HEIGHT / 2
    
    # moving to the top middle
    turtle.forward(ROOM_HALF)
    turtle.right(90)
    
    # move to upper right
    turtle.forward(ROOM_HALF)
    
    # start the fill
    turtle.begin_fill() # top right
    turtle.right(90)
    turtle.forward(ROOM_HEIGHT) # bottom right
    turtle.right(90)
    turtle.forward(ROOM_HEIGHT) # bottom left
    turtle.right(90)
    turtle.forward(ROOM_HEIGHT) # top left
    turtle.right(90)
    turtle.f