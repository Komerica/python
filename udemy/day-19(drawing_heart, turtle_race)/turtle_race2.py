from turtle import Turtle, Screen
from random import randint

##############
# Udemy code #
##############

is_race_on = False
screen = Screen()
screen.bgcolor("black")
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a color:\n"
                                   "\n1.red\n2.orange\n3.yellow\n4.green\n5.lightblue\n6.purple\n")

colors = ["red", "orange", "yellow", "green", "lightblue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)  # 새로운 turtle에게 변수이름을 각자 다르게 주기 보다는, 전부 list에 넣어서

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You've won!😁")
            else:
                print(f"You've lost! 😱")
            print(f"The {winning_color} turtle is the winner!")
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
