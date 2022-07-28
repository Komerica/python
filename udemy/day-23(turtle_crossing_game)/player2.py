from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.__init__()
        self.color("white")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.go_to_start()

    # Move the player up
    def go_up(self):
        self.forward(MOVE_DISTANCE)

    # Detect if the player is at finish line
    def is_at_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)
