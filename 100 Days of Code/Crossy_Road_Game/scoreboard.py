from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("Black")
        self.penup()
        self.score = 0
        self.goto(-270, y=260)

    def increase_score(self):
        self.clear()
        score_string = f"Round: {self.score}"
        self.write(arg=score_string, align="left", font=FONT)
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        score_string = f"Game Over"
        self.write(arg=score_string, align="center", font=FONT)







