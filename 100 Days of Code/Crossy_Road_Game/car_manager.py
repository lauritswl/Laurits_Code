from turtle import Turtle
import time
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.speed("fastest")
        self.setheading(180)
        self.random_initiation()
        self.current_speed = 5

    def set_speed(self, ROUND):
        self.current_speed = STARTING_MOVE_DISTANCE + MOVE_INCREMENT*ROUND



    def random_initiation(self):
        self.color(random.choice(COLORS))
        self.goto(300, random.randint(-250, 250))




