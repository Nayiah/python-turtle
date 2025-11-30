from turtle import *

penup()
goto(-20, 45)
fillcolor("purple")
begin_fill()
pendown()

for i in range(2):
    forward(300)
    right(90)
    forward(150)
    right(90)

end_fill()
exitonclick()
