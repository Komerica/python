from turtle import Turtle

####################
### Coded myself ###
# Without any help #
####################

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.l_score} vs {self.r_score}", align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
