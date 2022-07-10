from turtle import Turtle, Screen
from random import randint

####################
### Coded myself ###
# Without any help #
####################

screen = Screen()
screen.setup(500, 400)
screen.bgcolor("black")

colors = ["red", "orange", "yellow", "green", "lightblue", "purple"]
y_positions = [70, 45, 20, -5, -30, -55]
turtles = []

user_guess = screen.textinput("Turtle Race", "Which turtle will win the race? Enter a color:\n\n"
                                             "1. red\n"
                                             "2. orange\n"
                                             "3. yellow\n"
                                             "4. green\n"
                                             "5. lightblue\n"
                                             "6. purple\n")

for i in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[i])
    new_turtle.pendown()
    turtles.append(new_turtle)

is_race_on = True
while is_race_on:
    if user_guess:
        for turtle in turtles:
            turtle.forward(randint(0, 10))
            if turtle.xcor() > 230:
                is_race_on = False
                if user_guess == turtle.fillcolor():
                    print(f"You win! The {turtle.fillcolor()} turtle is the winner!")
                else:
                    print(f"You lose! The {turtle.fillcolor()} turtle is the winner!")

screen.exitonclick()
