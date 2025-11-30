from turtle import *


# Define function to draw an octagon

penup()
goto(-50, -100)
pendown()


def draw_octagon(side_length):
    for _ in range(8):
        forward(side_length)
        left(45)  # 360 degrees / 8 sides = 45 degrees


# Set drawing speed (optional)
speed(2)

# Draw the octagon with a side length of 100
draw_octagon(100)

# Keep the window open until it is closed manually
done()
