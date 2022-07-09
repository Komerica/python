# colorgram: https://pypi.org/project/colorgram.py/
import colorgram
from turtle import Turtle, Screen, colormode
from random import choice

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
screen = Screen()

screen.bgcolor("black")

tim.speed("fast")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen.exitonclick()
