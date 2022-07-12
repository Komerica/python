from turtle import Turtle, Screen
import time
from snake import Snake
from random import randint

# TODO-1: Create a snake body
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

# TODO-2: Move the snake
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()