# Annamarie McIntosh
# Drawing With Turtles Part 2

def square(size):
    ''' makes a square in turtle based on the inputed size '''
    # draw a square with forward() command
    import turtle # import turtle module

    turtle.shape("turtle")
    turtle.reset() # resets turtle position
    turtle.clear() # clears the screen

    for side in range(4): # makes a square
        turtle.forward(size)
        turtle.left(90)
   # turtle.hideturtle()


def polygon(num_sides, size):
    ''' makes a polygon with the inputed number of sides and size '''
    import turtle # imports turtle module

    turtle.shape("turtle")
    turtle.reset() # resets turtle position
    turtle.clear() # clears the screen
    
    for side in range(num_sides): # makes a square
        turtle.forward(size)
        turtle.left(360/num_sides)
    

    
