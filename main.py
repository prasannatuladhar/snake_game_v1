from turtle import Turtle,Screen
from snake import Snake
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("Welcome to Classical Snake Game")
screen.tracer(0)


snake = Snake()

screen.listen()
screen.onkey(snake.move_up,"Up")
screen.onkey(snake.move_right,"Right")
screen.onkey(snake.move_left,"Left")
screen.onkey(snake.move_down,"Down")


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    






screen.exitonclick()

