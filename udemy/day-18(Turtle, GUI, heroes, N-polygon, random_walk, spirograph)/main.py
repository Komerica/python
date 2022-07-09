# turtle color: https://trinket.io/docs/colors
# https://www.tcl.tk/man/tcl8.4/TkCmd/colors.html

from turtle import Turtle, Screen

tim = Turtle()

tim.shape("turtle")
tim.color("red")
tim.shapesize(2)

# Make square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# Dashed line
for _ in range(5):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


screen = Screen()
screen.exitonclick()
