from turtle import *

penup()
goto(-150, 0)
bgcolor("black")
color("yellow")
begin_fill()
pendown()

points = 1
while points < 5:
    forward(250)
    left(145)
    points = points+1

end_fill()
exitonclick()
