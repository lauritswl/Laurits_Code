from turtle import Turtle

down_towards_player = 225
up_towards_player = down_towards_player - 90

down_towards_cpu = 315
up_towards_cpu = down_towards_cpu + 90


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # make circle into a 10 by 10 circle by halving size
        self.color("white")
        self.speed("fastest")
        self.start_up()

    def start_up(self):
        self.towards_player = True
        self.towards_up = True
        self.set_ball_heading()
        self.goto(0, 0)
        self.movement_distance = 1

    def increase_speed(self):
        self.movement_distance *= 1.01

    def move(self):
        self.forward(self.movement_distance)

    def set_ball_heading(self):
        # Player = True and Up = True
        if self.towards_player and self.towards_up:
            self.setheading(up_towards_player)

        # Player True amd Up = False
        if self.towards_player and not self.towards_up:
            self.setheading(down_towards_player)

        # Player = False and Up = True
        if not self.towards_player and self.towards_up:
            self.setheading(up_towards_cpu)

        # Player = False and Up = False
        if not self.towards_player and not self.towards_up:
            self.setheading(down_towards_cpu)
