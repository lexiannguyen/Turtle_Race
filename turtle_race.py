import turtle
import time
import random
#multiple races, ask user, clear screen, keep track of wins/losses print win percentage after least race



thorscore = 0
lokiscore = 0
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
    score.write(f"Thor's Wins: {thorscore}", font=("Arial", 25))
    score.goto(70, -200)
    score.write(f"Loki's Wins: {lokiscore}", font=("Arial", 25))

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
    thor = turtle.Turtle()
    thor.speed(0)
    thor.penup()
    thor.goto(-200, 200)
    thor.shape("turtle")
    thor.color("red")
    thor.speed(2)

    loki = turtle.Turtle()
    loki.speed(0)
    loki.penup()
    loki.goto(-200, -100)
    loki.shape("turtle")
    loki.color("dark green")
    loki.speed(2)
    #distances
    distances = [25, 18, 34, 47, 98, 67, 53, 72, 81, 27, 100, 136]
    totaldist = 400
    thordist = 0
    lokidist = 0
    #moving
    while(thordist < totaldist and lokidist < totaldist):
        x = random.choice(distances)
        y = random.choice(distances)
        thor.forward(x)
        loki.forward(y)
        thordist += x
        lokidist += y
    #ref
    ref = turtle.Turtle()
    ref.penup()
    ref.hideturtle()
    ref.goto(-220, -170)
    #winner
    if thordist >= totaldist:
        ref.clear()
        ref.write("The winner is Thor!", font=("Arial", 25))
        ref.goto(-220, -200)
        ref.write(f"Thor: {thordist} miles", font=("Arial", 25))
        ref.goto(-220, -230)
        ref.write(f"Loki: {lokidist} miles", font=("Arial", 25))
        thorscore += 1
        totalscore +=1
    elif lokidist >= totaldist:
        ref.clear()
        ref.write("The winner is Loki!", font=("Arial", 25))
        ref.goto(-220, -200)
        ref.write(f"Thor: {thordist} miles", font=("Arial", 25))
        ref.goto(-220, -230)
        ref.write(f"Loki: {lokidist} miles", font=("Arial", 25))
        lokiscore += 1
        totalscore += 1
    

    
    score.clear()
    score.speed(0)
    score.penup()
    score.hideturtle()
    score.goto(70, -170)
    
    score.write(f"Thor's Wins: {thorscore}", font=("Arial", 25))
    score.goto(70, -200)
    
    score.write(f"Loki's Wins: {lokiscore}", font=("Arial", 25))
    #wait
    time.sleep(2)
    turtle.clearscreen()

thorscore = thorscore
lokiscore = lokiscore
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
stats.write(f"Thor's Wins: {thorscore}", font=("Arial", 25))
stats.goto(-140, 70)
stats.write(f"Loki's Wins: {lokiscore}", font=("Arial", 25))

#winpercentage
thorp = int(thorscore)/int(totalscore)
thorp2 = (thorp * 100)
lokip = int(lokiscore)/int(totalscore)
lokip2 = (lokip * 100)
stats.goto(-140, 40)
stats.write(f"Thor's Win Percentage: {thorp2:.2f} %", font=("Arial", 25))
stats.goto(-140, 10)
stats.write(f"Loki's Win Percentage: {lokip2:.2f} %", font=("Arial", 25))
stats.goto(-140, -20)
stats.write(f"Total Races: {totalscore}", font=("Arial", 25))






#turtle.clearscreen()

turtle.mainloop()
