from random import randint
from turtle import Turtle, Screen, colormode

####################
### Coded myself ###
# Without any help #
####################

tim = Turtle()
colormode(255)

tim.width(5)
tim.speed("fastest")


def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    rd_color = (r, g, b)
    return rd_color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        current_direction = tim.heading()
        tim.setheading(current_direction + size_of_gap)


draw_spirograph(12)

screen = Screen()
screen.exitonclick()
