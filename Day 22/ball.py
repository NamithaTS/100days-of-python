from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move=10
        self.y_move=10
        self.move_speed=0.1



    def move(self):
        x_n=self.xcor()+self.x_move
        y_n=self.ycor()+self.y_move
        self.goto(x_n,y_n)

    def bounce_y(self):
        self.y_move*= -1
    def bounce_x(self):
        self.x_move*=-1
        self.move_speed*=0.9

    def reset_p(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.bounce_x()
