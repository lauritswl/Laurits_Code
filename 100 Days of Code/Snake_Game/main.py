from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


food = Food()
snake = Snake()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()     # refreshing screen
    time.sleep(0.1)     # Speed of snake
    snake.move()        # Snake movement method

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()  # create a new piece of food
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor()**2 > 290**2 or snake.head.ycor()**2 > 290**2:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
