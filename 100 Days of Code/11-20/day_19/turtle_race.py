from turtle import Turtle, Screen


def create_turtle(id_color):
    """returns a turtle with the parameter color and turtle_id_name"""
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.color = id_color
    return turtle


turtle_001 = create_turtle("green")
turtle_002 = create_turtle("red")



screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

for turtle in screen.turtles():
    print(turtle.color())

turtle_001.

screen.exitonclick()