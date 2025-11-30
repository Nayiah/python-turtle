from turtle import *


# function for drawing the pentagram
def draw_pentagram(size):
    for i in range(5):
        forward(size)
        right(72)
        forward(size)
        right(144)


penup()
goto(-150, 0)
pendown()


# drawing the shape
draw_pentagram(200)


exitonclick()
