from turtle import *

penup()
goto(0,0)
fillcolor("blue")
begin_fill()
pendown()

for i in range(3):
    forward(200)
    left(120)

end_fill()
exitonclick()