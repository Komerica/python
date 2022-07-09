# colorgram: https://pypi.org/project/colorgram.py/
import colorgram
from turtle import Turtle, Screen, colormode
from random import choice

####################
### Coded myself ###
# Without any help #
####################

colormode(255)
# Extract 10 colors from an image.
colors = colorgram.extract('image.jpg', 30)
print(colors)

rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

print(rgb_colors)

color_list = [(238, 236, 234), (230, 226, 228), (34, 108, 167), (223, 229, 235), (227, 233, 230), (245, 77, 36),
              (112, 163, 211), (153, 57, 85), (219, 156, 94), (201, 60, 27), (24, 133, 55), (246, 204, 84),
              (190, 151, 47), (225, 119, 152), (46, 53, 121), (221, 68, 97), (113, 199, 156), (147, 37, 30),
              (253, 202, 0), (91, 113, 192), (74, 40, 32), (248, 153, 143), (111, 41, 49), (155, 212, 203),
              (53, 174, 163), (38, 31, 67), (154, 210, 219), (43, 33, 45), (35, 55, 46), (99, 93, 2)]

tim = Turtle()
tim.speed("fast")


def random_color():
    return choice(color_list)


def paint_dots(paint_size):
    for i in range(paint_size):
        tim.home()
        tim.penup()
        tim.sety(50 * i)
        for _ in range(paint_size):
            tim.dot(20, random_color())
            tim.penup()
            tim.forward(50)


paint_dots(3)

screen = Screen()
screen.exitonclick()
