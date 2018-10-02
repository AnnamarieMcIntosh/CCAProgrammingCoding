# Annamarie McIntosh
# Drawing With Turtles Part 1

import turtle
import random

turtle.color("orchid2") # set to purple color
turtle.down # put the the pen down
turtle.begin_fill() # start to fill shape
turtle.circle(50) # make a circle with (radius)
turtle.end_fill() # fully fill circle
turtle.up() # put pen up

turtle.goto(50, 50) # goes to (30, 30) on the coordinate plane
turtle.color(random.random(), random.random(), random.random()) # chooses a random color
turtle.down() # puts the pen down

# MAKES A SQUARE
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.up()

turtle.goto(-100, -100)
turtle.begin_fill()
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.end_fill()


