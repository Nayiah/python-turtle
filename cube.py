from turtle import *

speed(3)


# function to draw the squares
def draw_square(points):
    penup()
    goto(points[0])
    pendown()
    goto(points[1])
    goto(points[2])
    goto(points[3])
    goto(points[0])


# points for the cube
baseL = (-100, -50)
topL = (-100, 100)
baseR = (100, -50)
topR = (100, 100)
top = (0, 50)
front = (0, -100)
topB = (0, 150)

# drawing the left face
draw_square([baseL, topL, top, front])

# drawing the right face
draw_square([baseR, topR, top, front])


# drawing the top face
draw_square([topR, topB, topL, top])

hideturtle()
exitonclick()
