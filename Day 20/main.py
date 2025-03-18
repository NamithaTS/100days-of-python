import time
from turtle import Turtle,Screen
'''t=Turtle()
t.shape("square")
t.color("white")
t1=Turtle()
t1.shape("square")
t1.color("white")
t1.goto(-20,0)
t2=Turtle()
t2.shape("square")
t2.color("white")
t2.goto(-40,0)'''
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)
s=[(0,0),(-20,0),(-40,0)]
segments=[]
for i in s:
    t = Turtle()
    t.shape("square")
    t.color("white")
    t.penup()
    t.goto(i)
    segments.append(t)

is_on=True
while is_on:
    screen.update()
    time.sleep(0.1)
    for segment in segments:
        segment.forward(20)


screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("my snake game")
screen.exitonclick()