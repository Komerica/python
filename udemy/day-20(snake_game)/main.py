from turtle import Screen
import time
from snake import Snake
from food import Food
from random import randint

# TODO-1: Create a snake body
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

# TODO-2: Move the snake
snake = Snake()
food = Food()
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

    # TODO-4: Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()

screen.exitonclick()
