from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from score import Score

import time


screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("pong")
screen.tracer(0)


r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
score=Score()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

is_on=True
while is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision
    if ball.ycor() >280 or ball.ycor()<-280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320 :
        ball.bounce_x()

    #detect when paddle misses
    if ball.xcor()>380:
        ball.reset_p()
        score.l_point()

    if ball.xcor()<-380:
        ball.reset_p()
        score.r_point()


screen.exitonclick()