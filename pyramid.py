from turtle import *

speed(3)


# function to draw the triangles
def draw_triangle(points):
    penup()
    goto(points[0])
    pendown()
    goto(points[1])
    goto(points[2])
    goto(points[0])


# points for the pyramid
baseL = (-100, -50)
baseR = (100, -50)
top = (0, 100)
front = (0, -100)

# drawing the left face
draw_triangle([baseL, top, front])

# drawing the right face
draw_triangle([baseR, top, front])

hideturtle()
exitonclick()
