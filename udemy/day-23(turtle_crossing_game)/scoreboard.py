from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-220, 240)
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.current_level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.current_level += 1
        self.update_scoreboard()


