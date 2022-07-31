from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.bgcolor("black")
image = "blank_states_img.gif"
screen.addshape(image)
states = Turtle()
states.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
print(states_list)

guessed_states = []
while len(guessed_states) < 50:
    user_guess = screen.textinput(title=f"{len(guessed_states)}/50 States correct",
                                  prompt="What's another state name?").title()
    if user_guess == "Exit":
        missed_states = []
        for state in states_list:
            if state not in guessed_states:
                missed_states.append(state)
        df = pandas.DataFrame(missed_states, columns=["state"])
        df.to_csv("states_to_learn3.csv")
        break

    if user_guess in states_list:
        guessed_states.append(user_guess)
        state_row = data[data.state == user_guess]
        state_text = Turtle()
        state_text.penup()
        state_text.hideturtle()
        state_text.goto(int(state_row.x), int(state_row.y))
        state_text.write(user_guess)

    print(guessed_states)

screen.mainloop()
