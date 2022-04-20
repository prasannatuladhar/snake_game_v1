from turtle import Turtle

class ScoreDisplay(Turtle):
    def __init__(self):
        self.score = 0

        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.display_score()
        self.hideturtle()

    def display_score(self):
        self.clear()
        self.color("purple")
        self.write(f"Score:{self.score}", font=("Verdana",15, "normal"),align="center")


    def add_score(self):
        self.score += 1
        

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", font=("Verdana",25, "normal"),align="center")

