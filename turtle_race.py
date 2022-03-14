import turtle
import time
import random
#multiple races, ask user, clear screen, keep track of wins/losses print win percentage after least race

redscore = 0
greenscore = 0
totalscore = 0
#numrace
numrace = int(input("How nany races would you like to see? "))
for x in range(numrace):
    #beginning score
    score = turtle.Turtle()
    score.speed(0)
    score.penup()
    score.hideturtle()
    score.goto(70, -170)
    score.write(f"Red's Wins: {redscore}", font=("Arial", 25))
    score.goto(70, -200)
    score.write(f"Green's Wins: {greenscore}", font=("Arial", 25))

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
    #start
    writer = turtle.Turtle()
    writer.penup()
    writer.hideturtle()
    writer.goto(-220, 300)
    writer.write("Start", font=("Arial", 25))
    writer.goto(160, 300)
    writer.write("Finish", font=("Arial", 25))
    #players
    red = turtle.Turtle()
    red.speed(0)
    red.penup()
    red.goto(-200, 200)
    red.shape("turtle")
    red.color("red")
    red.speed(2)

    green = turtle.Turtle()
    green.speed(0)
    green.penup()
    green.goto(-200, -100)
    green.shape("turtle")
    green.color("dark green")
    green.speed(2)
    #distances
    distances = [25, 18, 34, 47, 98, 67, 53, 72, 81, 27, 100, 136]
    totaldist = 450
    reddist = 0
    greendist = 0
    #moving
    while(reddist < totaldist and greendist < totaldist):
        x = random.choice(distances)
        y = random.choice(distances)
        red.forward(x)
        green.forward(y)
        reddist += x
        greendist += y
    #ref
    ref = turtle.Turtle()
    ref.penup()
    ref.hideturtle()
    ref.goto(-240, -170)
    #winner
    if reddist >= totaldist:
        ref.clear()
        ref.write("The winner is red!", font=("Arial", 25))
        ref.goto(-240, -200)
        ref.write(f"Thor: {reddist} miles", font=("Arial", 25))
        ref.goto(-240, -230)
        ref.write(f"Loki: {greendist} miles", font=("Arial", 25))
        redscore += 1
        totalscore +=1
    elif greendist >= totaldist:
        ref.clear()
        ref.write("The winner is green!", font=("Arial", 25))
        ref.goto(-240, -200)
        ref.write(f"Red: {reddist} miles", font=("Arial", 25))
        ref.goto(-240, -230)
        ref.write(f"Green: {greendist} miles", font=("Arial", 25))
        greenscore += 1
        totalscore += 1
    

    
    score.clear()
    score.speed(0)
    score.penup()
    score.hideturtle()
    score.goto(70, -170)
    
    score.write(f"Red's Wins: {redscore}", font=("Arial", 25))
    score.goto(70, -200)
    
    score.write(f"Green's Wins: {greenscore}", font=("Arial", 25))
    #wait
    time.sleep(2)
    turtle.clearscreen()

redscore = redscore
greenscore = greenscore
totalscore = totalscore
print(totalscore)
#stats screen
turtle.bgcolor("pink")
stats = turtle.Turtle()
stats.hideturtle()
stats.penup()
stats.speed(0)
stats.goto(-140, 150)
stats.write("STATS:", font=("Arial", 25))
stats.goto(-140,100)
stats.write(f"Red's Wins: {redscore}", font=("Arial", 25))
stats.goto(-140, 70)
stats.write(f"Green's Wins: {greenscore}", font=("Arial", 25))

#winpercentage
redPercent = int(redscore)/int(totalscore)
redPercent2 = (redPercent * 100)
greenPercent = int(greenscore)/int(totalscore)
greenPercent2 = (greenPercent * 100)
stats.goto(-140, 40)
stats.write(f"Red's Win Percentage: {redPercent2:.2f} %", font=("Arial", 25))
stats.goto(-140, 10)
stats.write(f"Green's Win Percentage: {greenPercent2:.2f} %", font=("Arial", 25))
stats.goto(-140, -20)
stats.write(f"Total Races: {totalscore}", font=("Arial", 25))






#turtle.clearscreen()

turtle.mainloop()
