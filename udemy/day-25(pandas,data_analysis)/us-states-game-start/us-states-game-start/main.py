import turtle
import pandas
from answer import Answer

####################
### Coded myself ###
# Without any help #
####################

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.bgcolor("black")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
correct_guess = []

answer_state = screen.textinput(title="Guess the States", prompt="What's another state's name?").title()

while len(correct_guess) < 50:
    if answer_state == "Exit":
        missing_state = []
        for state in data.state:
            if state not in correct_guess:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state, columns=["state"])
        new_data.to_csv("states_to_learn.csv")
        break
    for state in data.state:
        if answer_state == state:
            row = data[data.state == answer_state]
            answer = Answer(int(row.x), int(row.y), state)
            correct_guess.append(state)
    answer_state = screen.textinput(title=f"{len(correct_guess)}/50 States Correct",
                                    prompt="What's another state's name?").title()



# turtle.mainloop()  # Alternative for
