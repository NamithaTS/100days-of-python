import random
from turtle import Turtle, Screen

t=Turtle()
t.shape("turtle")
directions=[0,90,180,270]
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
'''task 1:draw a square
for i in range(4):

    t.forward(200)
    t.right(90)'''


'''task 2: draw a dashed line
for _ in range(50):

    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()'''

'''#task 3: draw different shape
def draw(n):
    angle=360/n
    for i in range(n):
        t.forward(100)
        t.right(angle)
for s in range(3,11):
    t.color(random.choice(colours))
    draw(s)
'''
'''#task 4: draw random walk
t.pensize(15)
for i in range(50):
    t.color(col())
    t.forward(40)
    t.setheading(random.choice(directions))'''

#task 5:draw a spirograph
t.speed("fastest")
def draw(s):

    for _ in range(int(360/s)):
        t.color(random.choice(colours))
        t.circle(50)
        t.setheading(t.heading()+s)
draw(10)
'''import heroes
print(heroes.gen())'''
screen=Screen()
screen.exitonclick()