from turtle import Turtle


######################################
#### Coded myself without any help ###
## After reading a bit of Udemy code #
######################################

class Snake:
    POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in self.POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move_snake(self):
        for segment_index in range(len(self.segments) - 1, 0, -1):
            new_x_pos = self.segments[segment_index - 1].xcor()
            new_y_pos = self.segments[segment_index - 1].ycor()
            self.segments[segment_index].goto(new_x_pos, new_y_pos)
        self.segments[0].forward(20)

    def up(self):
        if not self.segments[0].heading() == self.DOWN:
            self.segments[0].setheading(self.UP)

    def down(self):
        if not self.segments[0].heading() == self.UP:
            self.segments[0].setheading(self.DOWN)

    def left(self):
        if not self.segments[0].heading() == self.RIGHT:
            self.segments[0].setheading(self.LEFT)

    def right(self):
        if not self.segments[0].heading() == self.LEFT:
            self.segments[0].setheading(self.RIGHT)
