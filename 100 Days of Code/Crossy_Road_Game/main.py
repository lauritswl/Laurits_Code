import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
CAR_LIST = []
ROUND_COUNTER = -1
LOOP_COUNTER = 0
game_is_on = True


screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.title("My Crossy Road Game")
screen.tracer(0)


scoreboard = Scoreboard()
game_over = Scoreboard()


player = Player()
screen.onkeypress(player.up, "w")


while game_is_on:
    ROUND_COUNTER += 1
    scoreboard.increase_score()
    round_is_on = True
    while round_is_on:
        time.sleep(0.1)
        screen.update()
        for CAR in CAR_LIST:
            if CAR.xcor() <= -300:
                CAR_LIST.remove(CAR)
                CAR.hideturtle()
            else:
                for i in range(0,1+2*ROUND_COUNTER):
                    if CAR.distance(player) < 15:
                        game_is_on = False
                        round_is_on = False
                    CAR.forward(CAR.current_speed)

        # Print Cars
        if LOOP_COUNTER < 5:
            LOOP_COUNTER += 1
        else:
            car = CarManager()
            CAR_LIST.append(car)
            LOOP_COUNTER = 0

        # Hitting finish line:
        if player.ycor() == 280:
            player.sety(-280)
            round_is_on = False


for CAR in CAR_LIST:
    CAR.hideturtle()

game_over.game_over()
screen.update()

screen.exitonclick()
