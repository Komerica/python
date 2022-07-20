from turtle import Turtle
from random import choice, randrange, randint

COLORS = ["red", "orange", "yellow", "green", "lightblue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.chance = 50
        self.car_speed = STARTING_MOVE_DISTANCE

    # Create cars
    def create_car(self):
        random_chance = randint(1, self.chance)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(choice(COLORS))
            random_y = randrange(-200, 280, 80)
            new_car.goto(300, random_y)
            new_car.setheading(180)
            self.all_cars.append(new_car)

    # Move cars
    def move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    # create more cars each stage
    def create_more_cars(self):
        if self.chance <= 10:
            self.chance -= 1
        else:
            self.chance -= 10

    # Increase cars speed each stage
    def increase_car_speed(self):
        self.car_speed += MOVE_INCREMENT
