from turtle import *


# moving pen for rectangle
penup()
goto(-60, 0)
pendown()

# loop for rectangle
for i in range(2):
    forward(300)
    right(90)
    forward(250)
    right(90)

# moving pen for triangle
penup()
goto(-75, 0)
pendown()

# loop for triangle
for i in range(3):
    forward(350)
    left(120)

exitonclick()
