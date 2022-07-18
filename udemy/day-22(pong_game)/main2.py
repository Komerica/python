from turtle import Screen
from paddle2 import Paddle
from ball2 import Ball
from scoreboard2 import ScoreBoard
import time

####################
### Coded myself ###
# Without any help #
####################


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
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

    # Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 335 and ball.distance(r_paddle) < 55 or ball.xcor() < -335 and ball.distance(l_paddle) < 55:
        ball.bounce_x()

    # l_paddle win
    if ball.xcor() > 400:
        ball.restart_game()
        scoreboard.l_point()

    # r_paddle win
    if ball.xcor() < -400:
        ball.restart_game()
        scoreboard.r_point()

screen.exitonclick()
