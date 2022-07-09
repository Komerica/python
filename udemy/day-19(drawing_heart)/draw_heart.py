from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")
t = Turtle()
t.pencolor("white")
t.speed("fastest")
t.hideturtle()


def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)


def to_sasa():
    t.fillcolor("red")
    t.begin_fill()
    t.lt(140)
    t.fd(113)
    curve()
    t.lt(120)
    curve()
    t.fd(112)
    t.end_fill()


def write(message, pos):
    x, y = pos
    t.penup()
    t.goto(x, y)
    t.color('white')
    style = ("stencil std", 18, "italic")
    t.write(message, font=style)


to_sasa()
write("I", (-68, 95))
write("L", (-55, 95))
write("O", (-42, 95))
write("V", (-28, 95))
write("E", (-14, 95))
write("Y", (10, 95))
write("O", (26, 95))
write("U", (45, 95))

screen.exitonclick()
