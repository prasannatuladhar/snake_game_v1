from turtle import Turtle,Screen
from scoredisplay import ScoreDisplay
from snake import Snake
from food import Food
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("Welcome to Classical Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoredisplay = ScoreDisplay()

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
    scoredisplay.display_score()
    
    #collison with food
    if snake.head.distance(food) <15:
        scoredisplay.add_score()
        food.change_location()
        snake.extend_snake()

    #collison with wall
    if snake.head.xcor() >290 or snake.head.xcor() <-290 or snake.head.ycor() >290 or snake.head.ycor() <-290:
        is_game_on=False
        scoredisplay.game_over()


    #collison with body
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) <10:
            is_game_on=False
            scoredisplay.game_over()




screen.exitonclick()

