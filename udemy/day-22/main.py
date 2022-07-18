from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 60 and ball.xcor() > 330 \
            or ball.distance(l_paddle) < 60 and ball.xcor() < -330:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 400:
        scoreboard.l_point()
        ball.reset_position()

    # Detect L paddle misses
    if ball.xcor() < -400:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()
