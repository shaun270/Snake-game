from turtle import Turtle
positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

class Snake:
    def __init__(self):
        for i in range(3):
            tim = Turtle("square")
            tim.penup()
            tim.color("green")
            tim.goto(positions[i])
            segments.append(tim)
        self.head = segments[0]


    def move(self):
        for i in range(len(segments) - 1, 0, -1):
            segments[i].goto(segments[i - 1].xcor(), segments[i - 1].ycor())
            if i == 1:
                segments[0].forward(20)
                break

    def extend(self):
        new_turtle=Turtle("square")
        new_turtle.penup()
        new_turtle.color("green")
        new_turtle.goto(segments[len(segments)-1].xcor(),segments[len(segments)-1].ycor())
        segments.append(new_turtle)


    def up(self):
        if segments[0].heading()!=270:
            segments[0].setheading(90)

    def right(self):
        if segments[0].heading()!=180:
            segments[0].setheading(0)

    def left(self):
        if segments[0].heading()!=0:
            segments[0].setheading(180)

    def down(self):
        if segments[0].heading()!=90:
            segments[0].setheading(270)

    def check(self):
        for i in segments:
            if i==self.head or i==segments[1] or i==segments[2]:
                pass
            elif self.head.distance(i)<10:
                return False
        return True