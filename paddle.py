from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=5)
        self.setheading(90)
        self.goto(position)

    def go_up(self):
        self.fd(20)

    def go_down(self):
        self.bk(20)
