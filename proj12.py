import turtle as t
import random
import time

# game window
win = t.Screen()
win.title("Flappy Butterfly by Adwait")
win.setup(width=450,height=600)
win.bgcolor("blue")
win.bgpic("bb.gif")

win.register_shape("bf.gif")
win.register_shape("pd.gif")
win.register_shape("pu.gif")


# bug specifications
bug = t.Turtle()
bug.speed(0)
bug.shape("bf.gif")
bug.color("yellow")
bug.penup()
bug.goto(-115,0)
# speed changers
bug.dx = 0
bug.dy = 3

# Pipes
p1t = t.Turtle()
p1t.speed(0)
p1t.shape("pu.gif")
p1t.color("green")
p1t.shapesize(30,3,0)
p1t.penup()
p1t.goto(0,360)
p1t.dx = 5

p1b = t.Turtle()
p1b.speed(0)
p1b.shape("pd.gif")
p1b.color("green")
p1b.shapesize(30,3,0)
p1b.penup()
p1b.goto(0,-360)
p1b.dx = 5

# score variables
score = 0
scaler = 1

# score display
text = t.Turtle()
text.ht()
text.speed(0)
text.penup()
text.goto(0,250)
text.write("Score: %d" %score, align = "center", font = ("Arial",20,"normal"))

# gravity
gravity = -1

# up func
def up():
    bug.dy = 11
    # upper limit
    if bug.dy > 11:
        bug.dy = 11

# user binding
win.listen()
win.onkeypress(up,"space")

# main game loop
while True:

    # move bug up
    bug.sety(bug.ycor() + bug.dy)
    # move bug down
    bug.dy = bug.dy + gravity

    # lower limit
    if bug.ycor()  < -280:
        bug.dy = 0
        bug.sety(-280)

    # look for collision
    if (bug.xcor() + 12.5) > (p1t.xcor() - 28) and (bug.xcor() - 12.5) < (p1t.xcor() + 28):
        if (bug.ycor() + 12.5) > (p1t.ycor() - 297) or (bug.ycor() - 12.5) < (p1b.ycor() + 297):
            time.sleep(2)
            p1t.setx(270)
            p1b.setx(270)
            score = 0
            text.clear()
            text.write("Score: %d" %score, align = "center", font = ("Arial",20,"normal"))
    if (p1t.xcor() + 30) < (bug.xcor() + 20):
        p1b.dx = 7
        p1t.dx = 7
        p1t.setx(p1t.xcor() - p1t.dx)
        p1b.setx(p1b.xcor() - p1b.dx)
        score = score + scaler
        scaler = 0
        text.clear()
        text.write("Score: %d" %score, align = "center", font = ("Arial",20,"normal"))
        p1b.dx = 5
        p1t.dx = 5

    # move the Pipes
    p1t.setx(p1t.xcor() - p1t.dx)
    p1b.setx(p1b.xcor() - p1b.dx)
    if p1t.xcor() < -285:
        a = random.choice([460,260,360,120,600,560,160])
        if a == 460:
            b = -260
        elif a == 360:
            b = -360
        elif a == 260:
            b = -460
        elif a == 560:
            b = -160
        elif a == 160:
            b = -560
        elif a == 600:
            b = -120
        elif a == 120:
            b = -600
        p1t.sety(a)
        p1t.setx(250)
        p1b.sety(b)
        p1b.setx(250)
        scaler = 1


win.mainloop()
