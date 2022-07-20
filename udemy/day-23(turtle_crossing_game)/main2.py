from turtle import Screen
from scoreboard2 import ScoreBoard
from player2 import Player
from car_manager2 import CarManager
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = ScoreBoard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    # Detect if the player collide with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect if the player is at finish line
    if player.is_at_finish_line():
        car_manager.increase_car_speed()
        player.go_to_start()
        scoreboard.increase_level()
        car_manager.create_more_cars()

screen.exitonclick()
