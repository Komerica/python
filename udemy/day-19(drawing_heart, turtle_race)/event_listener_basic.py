from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.bgcolor("black")
tim.pencolor("white")


def move_forwards():
    tim.forward(10)


screen.listen()
screen.onkey(move_forwards, "space")
# screen.onkey(key="space", fun=move_forwards) # 이렇게도 가능함!
screen.exitonclick()
