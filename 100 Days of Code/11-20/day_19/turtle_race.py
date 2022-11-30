from turtle import Turtle, Screen
import random

def create_turtle(id_color):
    """returns a turtle with the parameter color and turtle_id_name"""
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.color(id_color)
    turtle.penup()
    return turtle

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles_list = []
for color in color_list:
    turtles_list.append(create_turtle(color))
y_value = -100
for i in turtles_list:
    i.goto(x=-230, y=y_value)
    y_value += 40
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles_list:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"The {winning_color} turtle won! Congratulation!")
            else:
                print(f"You Lost :(, the {winning_color} turtle won...")




screen.exitonclick()
