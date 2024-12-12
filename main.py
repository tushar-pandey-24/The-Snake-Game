from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food
import time

screen = Screen()
screen.screensize(canvwidth=600, canvheight=600, bg="black")
screen.tracer(0)

snake = Snake()
score = Scoreboard()
food = Food()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with the food.
    if snake.snake_head.distance(food) < 15:
        score.increase_score()
        food.refresh()
        snake.extend_tail()

    # Detect collision with the wall.
    if (snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or
            snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280):
        score.reset()
        snake.reset()

    # Detect collision with the tail.
    for segments in snake.snake_list[1:]:
        if snake.snake_head.distance(segments) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()

