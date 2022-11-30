from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.score = 0
        self.import_high_score()
        self.increase_score()

    def increase_score(self):
        self.clear()
        score_string = f"Score: {self.score}    High Score: {self.high_score}"
        self.write(arg=score_string, align="center", font=("Times New Roman", 24, "normal"))
        self.score += 1
    #
    # def game_over(self):
    #     self.goto(0,0)
    #     score_string = f"Game Over"
    #     self.write(arg=score_string, align="center", font=("Times New Roman", 24, "normal"))

    def reset(self):
        if self.score-1 > self.high_score:
            self.high_score = self.score-1
            self.save_high_score()
        self.score = 0
        self.increase_score()

    def import_high_score(self):
        with open("high_score.txt", mode="r") as file:
            high_score = int(file.read())
            self.high_score = high_score

    def save_high_score(self):
        with open("high_score.txt", mode="w") as file:
            file.write(f"{self.high_score}")
