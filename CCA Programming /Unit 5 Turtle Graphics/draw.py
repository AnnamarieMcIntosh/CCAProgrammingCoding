## Annamarie McIntosh
## Drawing With Turtles Part 1

import turtle

# makes coral spiral
turtle.pencolor("coral1")
turtle.penup()
turtle.goto(200,200)
turtle.pendown()
for i in range(39):
    turtle.forward(200)
    turtle.left(123)
turtle.penup()

# make coral star
turtle.goto(305, 220)
turtle.pendown()
for i in range(5):
    turtle.forward(75)
    turtle.right(144)
turtle.penup()

# makes blue spiral 
turtle.goto(-200, 200)
turtle.pencolor("deepskyblue2")
turtle.pendown()
for i in range(39):
    turtle.forward(200)
    turtle.left(123)
turtle.penup()

# make blue star
turtle.goto(-263,285)
turtle.pendown()
for i in range(5):
    turtle.forward(75)
    turtle.right(144)
turtle.penup()

# makes pink spiral
turtle.goto(-250, -100)
turtle.pencolor("orchid2")
turtle.pendown()
for i in range(39):
    turtle.forward(200)
    turtle.left(123)
turtle.penup()

# make pink star
turtle.goto(-299,-200)
turtle.pendown()
for i in range(5):
    turtle.forward(75)
    turtle.right(144)
turtle.penup()

# makes green spiral
turtle.goto(200, -250)
turtle.pencolor("chartreuse2")
turtle.pendown()
for i in range(39):
    turtle.forward(200)
    turtle.left(123)
turtle.penup()

# make green star
turtle.goto(305,-245)
turtle.pendown()
for i in range(5):
    turtle.forward(75)
    turtle.right(144)
turtle.penup()

# makes words in the center
turtle.home()
turtle.pencolor("black")
turtle.pendown()
turtle.write("hello ;)", move=False, align="center", font=("Comic Sans MS", 100, "normal"))
turtle.penup()



