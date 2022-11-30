import turtle
from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.direction = self.head.heading()

    def create_snake(self):
        for displacement_value in range(0, 3):
            x_value = displacement_value * (-20)
            y_value = 0
            xy_value = (x_value, y_value)
            self.add_segment(xy_value)

    def add_segment(self, position):
        square = Turtle(shape="square")
        square.color("white")
        square.penup()
        square.goto(position)
        self.segments.append(square)

    def reset(self):
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.direction = self.head.heading()

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # Make all segments of the snake follow the head
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)  # Move head of snake
        self.direction = self.head.heading()

    def up(self):
        if self.direction != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.direction != UP:
            self.segments[0].setheading(DOWN)

    def right(self):
        if self.direction != LEFT:
            self.segments[0].setheading(RIGHT)

    def left(self):
        if self.direction != RIGHT:
            self.segments[0].setheading(LEFT)

