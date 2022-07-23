from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# TODO-1: Create a snake body
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

# TODO-2: Move the snake
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.11)
    snake.move()

    # TODO-4: Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # TODO-6: Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.update_high_score()
        snake.reset_snake()

    # TODO-7: Detect collision with tail
    # A bit too wordy(장황한)
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.update_high_score()
            snake.reset_snake()

screen.exitonclick()
