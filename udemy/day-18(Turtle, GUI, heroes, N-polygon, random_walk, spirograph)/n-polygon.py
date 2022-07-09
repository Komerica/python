# N-polygon: triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
# n각형 만들기: 3~10각형
# 360 / 3  = 120
# 360 / 4  = 90
# 360 / 5  = 72
# 360 / 6  = 60
# 360 / 7  = 51.42857142857143
# 360 / 8  = 45
# 360 / 9  = 40
# 360 / 10 = 36
import turtle
from turtle import Turtle, Screen
# from random import randint
import random

turtle.colormode(255) # generate random color
tim = Turtle()



####################
### Coded myself ###
# Without any help #
####################

# for i in range(3,11):
#     degree = 360 / i
#     tim.color(randint(0, 255), randint(0, 255), randint(0, 255)) # generate random color
#     for _ in range(i):
#         tim.right(degree)
#         tim.forward(100)


##############
# Udemy code #
##############
colours = ["aquamarine", "dark orange", "tan", "olive drab", "deep sky blue", "dim gray"]


def draw_shape(num_sides):
    degree = 360 / num_sides
    for _ in range(num_sides):
        tim.right(degree)
        tim.forward(100)


for shape_side in range(3,11):
    tim.color(random.choice(colours))
    tim.width(5)
    tim.speed(5000)
    draw_shape(shape_side)

screen = Screen()
screen.exitonclick()