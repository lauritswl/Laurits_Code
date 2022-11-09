# # TODO: Import packages
# import colorgram
# # TODO: Create color palette
# colors = colorgram.extract('image.jpg', 109)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
color_list = [(34, 108, 167), (223, 229, 235), (227, 233, 230), (245, 77, 36), (112, 163, 211), (153, 57, 85), (219, 156, 94), (201, 60, 27), (24, 133, 55), (246, 204, 84), (190, 151, 47), (225, 119, 152), (46, 53, 121), (221, 68, 97), (113, 199, 156), (147, 37, 30), (253, 202, 0), (91, 113, 192), (74, 40, 32), (248, 153, 143), (111, 41, 49), (155, 212, 203), (53, 174, 163), (38, 31, 67), (154, 210, 219), (43, 33, 45), (35, 55, 46), (99, 93, 2), (43, 151, 190), (10, 111, 51), (228, 169, 182), (177, 186, 217)]

# TODO: Import turtle and random
import turtle
import random as ran
turtle.colormode(255)


def one_line(self, color):
    for _ in range(10):
        dot_color = ran.choice(color)
        self.dot(20, dot_color)
        self.forward(50)


def turn_up(self):
    direction = int(self.heading())
    if direction == 0:
        for _ in range(2):
            self.left(90)
            self.forward(50)
    if direction == 180:
        for _ in range(2):
            self.right(90)
            self.forward(50)


# Running the turtle
screen = turtle.Screen()
screen.setworldcoordinates(-10, -10, 460, 460)
tur = turtle.Turtle()
tur.hideturtle()
tur.speed("fastest")
tur.penup()


print(screen.canvwidth)
print(screen.canvwidth)
for _ in range(10):
    one_line(tur, color_list)
    turn_up(tur)


screen.exitonclick()
