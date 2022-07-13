from turtle import Turtle
from random import randrange
from scoreboard import ScoreBoard


class Food(Turtle):
    # TODO-3: Create snake food
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("lightblue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = randrange(-280, 280, 20)
        random_y = randrange(-280, 280, 20)
        self.goto(random_x, random_y)

