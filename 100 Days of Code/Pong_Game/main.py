from turtle import Screen
from ball import Ball
from paddle import PlayerPaddle
from scoreboard import ScoreBoard
import time

speed_of_ball = 0.003
screen_width = 1200
screen_height = 600
game_is_on = True

screen = Screen()
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

middle_line = ScoreBoard(0)
middle_line.middle_line(screen_height)

player_1 = ScoreBoard(-50)
player_1.increase_score()
player_2 = ScoreBoard(50)
player_2.increase_score()

paddle_1 = PlayerPaddle()
paddle_2 = PlayerPaddle()
paddle_2.right()

ball = Ball()

screen.listen()
screen.onkeypress(paddle_1.up, "w")
screen.onkeypress(paddle_1.down, "s")
screen.onkeypress(paddle_2.up, "Up")
screen.onkeypress(paddle_2.down, "Down")

while game_is_on:
    round_is_on = True
    ball.start_up()
    while round_is_on:
        ball.set_ball_heading()
        ball.move()
        screen.update()
        time.sleep(0.001)

        # Detect collision with wall and flip direction horizontally
        if ball.ycor() ** 2 > 290 ** 2:
            if ball.towards_up:
                ball.towards_up = False
            else:
                ball.towards_up = True

        # Detect collision with paddle and flip direction vertically
        test_paddle_distance = 555 ** 2 < ball.xcor() ** 2 < 570 ** 2
        touches_paddle = ball.distance(paddle_1) < 50 or ball.distance(paddle_2) < 50
        if test_paddle_distance and touches_paddle:
            if ball.towards_player:
                ball.towards_player = False
                ball.increase_speed()
            else:
                ball.towards_player = True
                ball.increase_speed()

        # Detect collision missed ball
        if ball.xcor() > 600:
            player_1.increase_score()
            round_is_on = False
        if ball.xcor() < -600:
            player_2.increase_score()
            round_is_on = False
