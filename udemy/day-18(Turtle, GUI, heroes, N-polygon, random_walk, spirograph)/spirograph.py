from turtle import Turtle, Screen, colormode
from random import randint

tim = Turtle()
colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")
tim.pensize(2)

# My code (Not working as needed it to be)
# for _ in range(18):
#     tim.circle(100)
#     tim.right(20)


# Udemy code
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(36)

screen = Screen()
screen.exitonclick()
