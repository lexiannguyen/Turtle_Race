import turtle
import time
import random
#start/finish lines
start = turtle.Turtle()
start.speed(0)
start.color("black")
turtle.bgcolor("light green")
start.pensize(6)
start.penup()
start.goto(-250, 400)
start.pendown()
start.goto(-250, -400)
start.penup()
start.goto(250, 400)
start.pendown()
start.goto(250, -400)
start.penup()
start.hideturtle()

#score/title 

#players
thor = turtle.Turtle()
thor.speed(2)
thor.penup()
thor.goto(-300, 200)
thor.shape("turtle")
thor.color("pink")

loki = turtle.Turtle()
loki.speed(2)
loki.penup()
loki.goto(-300, -100)
loki.shape("turtle")
loki.color("blue")

#distances
distances = [25, 18, 34, 47, 98, 67, 53, 72, 81, 27, 100, 136]
totaldist = 500
thordist = 0
lokidist = 0

while(thordist <= totaldist or lokidist <= totaldist):
    x = random.choice(distances)
    y = random.choice(distances)
    thor.forward(x)
    loki.forward(y)
    thordist += x
    lokidist += y

turtle.mainloop()
