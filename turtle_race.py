import turtle
import time
import random

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

turtle1 = turtle.Turtle()
turtle1.speed(0)
turtle1.penup()
turtle1.goto(-300, 200)
turtle1.shape("turtle")
turtle1.color("pink")

turtle2 = turtle.Turtle()
turtle2.speed(0)
turtle2.penup()
turtle2.goto(-300, -200)
turtle2.shape("turtle")
turtle2.color("blue")

distances = []
turtle.mainloop()
