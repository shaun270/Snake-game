import turtle
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Score
import time
TIME=0.1
turtle.listen()
is_on=True
screen = Screen()
screen.title("THE SNAKE GAME")
screen.bgcolor("black")
screen.screensize(600, 600)
positions=[(0,0),(-20,0),(-40,0)]
segments=[]
screen.tracer(0)
snake=Snake()
food=Food()
score=Score()
turtle.listen()
turtle.onkey(snake.up,"Up")
turtle.onkey(snake.down, "Down")
turtle.onkey(snake.left, "Left")
turtle.onkey(snake.right, "Right")

while is_on:
    screen.update()
    time.sleep(TIME)
    snake.move()
    if food.distance(snake.head)<15:
        food.ref()
        score.point()
        snake.extend()
        TIME=TIME-0.005

    if snake.head.xcor()>630 or snake.head.xcor()<-630 or snake.head.ycor()>330 or snake.head.ycor()<-330:
        is_on=False
        break

    is_on=snake.check()

score.game_over()



screen.exitonclick()
