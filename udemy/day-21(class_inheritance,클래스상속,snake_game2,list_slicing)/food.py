from turtle import Turtle
from random import randrange


####################
### Coded myself ###
# Without any help #
####################

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(0.5)
        self.color("lightblue")
        self.create_food()

    def create_food(self):
        x, y = (randrange(-280, 280, 20), randrange(-280, 280, 20))
        self.goto(x, y)
