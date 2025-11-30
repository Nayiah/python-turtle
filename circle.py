from turtle import * #calls everything from the turtle library


penup() #lifting the pen
goto(0,-100) #move to that speific spot
bgcolor("blue")
color("red","cyan") #color of both the line and the inside of the circle
pensize(5) #change how thick the pen is

pendown() #placing the pen back down
begin_fill()
circle(120) #radius of the circle
end_fill()

      
done() 
