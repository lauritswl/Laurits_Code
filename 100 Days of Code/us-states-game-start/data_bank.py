import turtle
import pandas as pd

screen = turtle.Screen()

class GuessChecker(turtle.Turtle):
    def __init__(self):
        self.data = pd.read_csv("50_states.csv")
        self.answer = "Empty"
        self.guess_is_wrong = True
        self.writing_turtle = turtle.Turtle()
        self.writing_turtle.penup()
        self.writing_turtle.hideturtle()
        self.current_state = "placeholder for df"
        self.current_state_list = ["state", "x", "y"]


    def ask_for_a_guess(self):
        self.answer = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

    def check_if_guess_is_wrong(self):
        self.guess_is_wrong = True
        for STATE in self.data.state:
            if STATE == self.answer:
                self.guess_is_wrong = False

    def print_state(self):
        self.current_state = self.data[self.data.state == self.answer]
        self.writing_turtle.goto(int(self.current_state.x), int(self.current_state.x))
        self.writing_turtle.write(self.current_state.state.item())


