from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self, x):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score = 0
        self.goto(x=x, y=260)

    def increase_score(self):
        self.clear()
        score_string = f"{self.score}"
        self.write(arg=score_string, align="center", font=("Times New Roman", 24, "normal"))
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        score_string = f"Game Over"
        self.write(arg=score_string, align="center", font=("Times New Roman", 24, "normal"))

    def middle_line(self, height):
        int_height = int(height/40)
        self.goto(x=0, y=(height/2))
        self.setheading(270)
        for _ in range(0,int_height):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)




