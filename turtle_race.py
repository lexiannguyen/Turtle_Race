import turtle
import time
import random
#start/finish lines
start = turtle.Turtle()
start.speed(0)
start.color("black")
turtle.bgcolor("light blue")
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

#title 
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
writer.goto(-220, 300)
writer.write("Start", font=("Arial", 25))
writer.goto(160, 300)
writer.write("Finish", font=("Arial", 25))
#players
thor = turtle.Turtle()
thor.speed(2)
thor.penup()
thor.goto(-300, 200)
thor.shape("turtle")
thor.color("red")

loki = turtle.Turtle()
loki.speed(2)
loki.penup()
loki.goto(-300, -100)
loki.shape("turtle")
loki.color("dark green")

#distances
distances = [25, 18, 34, 47, 98, 67, 53, 72, 81, 27, 100, 136]
totaldist = 500
thordist = 0
lokidist = 0

while(thordist < totaldist and lokidist < totaldist):
    x = random.choice(distances)
    y = random.choice(distances)
    thor.forward(x)
    loki.forward(y)
    thordist += x
    lokidist += y

ref = turtle.Turtle()
ref.penup()
ref.hideturtle()
ref.goto(-220, -170)


#score
if thordist >= totaldist:
    ref.write("The winner is Thor!", font=("Arial", 25))
    ref.goto(-220, -200)
    ref.write(f"Thor: {thordist} miles", font=("Arial", 25))
    ref.goto(-220, -230)
    ref.write(f"Loki: {lokidist} miles", font=("Arial", 25))
elif lokidist >= totaldist:
    ref.write("The winner is Loki!", font=("Arial", 25))
    ref.goto(-220, -200)
    ref.write(f"Thor: {thordist} miles", font=("Arial", 25))
    ref.goto(-220, -230)
    ref.write(f"Loki: {lokidist} miles", font=("Arial", 25))


turtle.mainloop()
