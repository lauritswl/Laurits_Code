import math
import turtle
from turtle import Turtle, Screen

# TODO: Defining Timmy The Turtle
tim = Turtle()
#tim.shape("turtle")
#tim.color("#7FFF00", "#A0522D")

# TODO: Draw a square
# for _ in range(0,4):
#     tim.forward(100)
#     tim.left(90)

# TODO: Create a good dashed line
# test_range = 10
# for _ in range(0,4):
#     tim.forward(test_range)
#     tim.penup()
#     tim.forward(test_range)
#     tim.pendown()
# TODO: Create a dashed function


def forward_dashed(self, distance):
    loop_range = int(distance/20)
    modulo_distance = distance % 20
    for _ in range(0,loop_range):
        self.forward(10)
        self.penup()
        self.forward(10)
        self.pendown()
    if modulo_distance > 10:  # check if modulo distance ends penup or pendown
        self.forward(10)  # move first 10 pendown
        self.penup()
        self.forward(modulo_distance-10)
    else:  # ends pendown
        self.forward(modulo_distance)  # move rest after for loop


# TODO: Draw a dashed square
# for _ in range(0,4):
#     forward_dashed(tim, 100)
#     tim.left(90)


# TODO: Create a function that can draw shapes depending on sides
def shape(self, sides, side_length):
    sides = int(sides)
    if sides < 2:
        return
    turning_angle = 360 / sides
    print(f"sides = {sides}")
    for _ in range(0, sides):
        self.forward(side_length)
        self.left(turning_angle)

# TODO: draw shapes with sides 1-10

#
# colors = ['#d0384e', '#ee6445', '#fa9b58', '#fece7c', '#fff1a8',
# '#f4faad', '#d1ed9c', '#97d5a4', '#5cb7aa', '#3682ba']

# for _ in range(0, 10):
#     tim.pencolor(colors[_])
#     shape(tim, _, 100)


# TODO: Draw a Random Walk
import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

# turtle.colormode(255)
# tim.pensize(10)
# tim.speed(0)
# direction = [0, 90, 180, 270]
#
#
# for _ in range(200):
#     # x_pos = tim.xcor()
#     # y_pos = tim.ycor()
#     # my_screen.setworldcoordinates(x_pos - 2000, y_pos - 2000, x_pos + 2000, y_pos + 2000)
#     tim.pencolor(random_color())
#     tim.forward(30)
#     tim.left(random.choice(direction))


### Spirograph
turtle.colormode(255)

tim.speed(0)



def spirograph(circles, cir_size, ):

    tim.pensize(math.sqrt(circles * cir_size)/100)
    for _ in range(circles+1):
        tim.pencolor(random_color())
        tim.circle(cir_size)
        tim.left(360/circles)

spirograph(150, 100)

my_screen = Screen()
my_screen.exitonclick()
