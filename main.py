from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score_board import ScoreBoard

my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("Pong")
my_screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score_board = ScoreBoard()

my_screen.listen()
my_screen.onkey(r_paddle.go_up, "Up")
my_screen.onkey(r_paddle.go_down, "Down")
my_screen.onkey(l_paddle.go_up, "w")
my_screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    my_screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() >= 285 or ball.ycor() <= -285:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # Detect r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.l_point()

    # Detect l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()

my_screen.exitonclick()
