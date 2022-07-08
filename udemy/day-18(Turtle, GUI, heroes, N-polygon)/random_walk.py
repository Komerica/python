import turtle
from turtle import Turtle, Screen
from random import randint, choice

turtle.colormode(255)
tim = Turtle()

####################
### Coded myself ###
# Without any help #
####################

def random_walk():
    tim.width(10)
    tim.speed(50)
    tim.color(randint(0, 255), randint(0, 255), randint(0, 255))
    degree = 90 * randint(0, 3)
    tim.right(degree)
    tim.forward(30)


while True:
    random_walk()



##############
# Udemy code #
##############

# colours = ["aquamarine", "dark orange", "tan", "olive drab", "deep sky blue", "dim gray"]
# directions = [0, 90, 180, 270]
#
# for _ in range(200):
#     tim.speed(3)
#     tim.width(5)
#     tim.forward(30)
#     tim.color(choice(colours))
#     tim.setheading(choice(directions))  # 원하는 방향으로 바로 돌아서 right/left로 도는거보다 빠르다!


screen = Screen()
screen.exitonclick()