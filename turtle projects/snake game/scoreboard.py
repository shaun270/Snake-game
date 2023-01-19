from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0, 220)
        self.write("Score: "+str(self.score),align="center",font=("Arial",24,"normal"))
        self.hideturtle()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))

    def point(self):
        self.score+=1
        self.clear()
        self.write("Score: " + str(self.score), align="center", font=("Arial", 24, "normal"))