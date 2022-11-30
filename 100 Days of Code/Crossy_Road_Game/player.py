from turtle import Turtle
STARTING_POSITION = (0, -280)
TURTLE_HEADING = 90
TURTLE_COLOR = ["brown", "green"]
TURTLE_SPEED = "fastest"
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color(TURTLE_COLOR[0], TURTLE_COLOR[1])
        self.goto(STARTING_POSITION)
        self.reached_goal = False
        self.setheading(TURTLE_HEADING)
        self.speed(TURTLE_SPEED)

    def up(self):
        self.forward(10)


    def is_goal_reached(self):
        """Returns True if goal is reached"""
        if self.ycor() >= FINISH_LINE_Y:
            self.reached_goal = True
