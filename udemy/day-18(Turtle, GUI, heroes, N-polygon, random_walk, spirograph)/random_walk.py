import turtle
from turtle import Turtle, Screen
from random import randint, choice

tim = Turtle()
turtle.colormode(255)

####################
### Coded myself ###
# Without any help #
####################

# def random_walk():
#     tim.width(10)
#     tim.speed(50)
#     tim.color(randint(0, 255), randint(0, 255), randint(0, 255))
#     degree = 90 * randint(0, 3)
#     tim.right(degree)
#     tim.forward(30)
#
#
# while True:
#     random_walk()


##############
# Udemy code #
##############

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(choice(directions))  # 원하는 방향으로 바로 돌아서 right/left로 도는거보다 빠르다!


screen = Screen()
screen.exitonclick()