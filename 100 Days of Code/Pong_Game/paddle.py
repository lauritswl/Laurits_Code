from turtle import Turtle
import random
movement_distance = 1

UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=4, stretch_wid=0.5)  # make circle into a 10 by 10 circle by halving size
        self.color("white")
        self.speed("fastest")
        self.setheading(90)



class PlayerPaddle(Paddle):
    def __init__(self):
        super().__init__()
        self.goto(x=-570, y=0)

    def right(self):
        self.goto(x=570, y=0)

    def up(self):
        self.forward(10)

    def down(self):
        self.forward(-10)

# class CpuPaddle(Paddle):
#
#     def __init__(self):
#         super().__init__()
#         self.goto(570, 0)
#         self.towards_up = True
#         self.cpu_movement()
#
#     def cpu_movement(self):
#         while True:
#             while self.ycor() < 260:
#                 self.forward(random.random())
#             self.setheading(DOWN)
#             while self.ycor() > -260:
#                 self.forward(random.random())
#             self.setheading(UP)





