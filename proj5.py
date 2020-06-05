import turtle as t
import time
import random
import winsound

score = 0
lives = 5

win = t.Screen()
win.setup(width=800,height=500)
win.title("Sky falls by Adwait")
win.bgcolor("yellow")
win.bgpic("needed.gif")
win.tracer(0)
text = t.Turtle()
text.penup()
text.goto(0,200)
text.write("Score: %d  Lives: %d"%(score,lives),align="center",font=("Arial",20,"normal"))
text.hideturtle()

win.register_shape("ll1.gif")
win.register_shape("ll2.gif")
win.register_shape("apple.gif")
win.register_shape("spider.gif")


catcher = t.Turtle()
catcher.speed(0)
catcher.shape("ll1.gif")
catcher.color("black")
catcher.penup()
catcher.goto(0,-210)
catcher.dir = "stop"

goodslist = []

for i in range(15):
    x = random.randint(-380,380)
    y = random.randint(300,400)
    good = t.Turtle()
    good.speed(0)
    good.shape("apple.gif")
    good.color("blue")
    good.penup()
    good.speed = random.uniform(0.7,2)
    good.goto(x,y)
    goodslist.append(good)

badslist = []

for i in range(15):
    x = random.randint(-380,380)
    y = random.randint(300,400)
    bad = t.Turtle()
    bad.speed(0)
    bad.shape("spider.gif")
    bad.color("red")
    bad.penup()
    bad.speed = random.uniform(0.7,2)
    bad.goto(x,y)
    badslist.append(bad)

def right():
    catcher.dir = "right"
    catcher.shape("ll2.gif")
def left():
    catcher.dir = "left"
    catcher.shape("ll1.gif")


win.listen()
win.onkeypress(right,"Right")
win.onkeypress(left,"Left")

while True:

    win.update()

    if lives == 0:
        time.sleep(1)
        for good in goodslist:
            p= random.randint(-380,380)
            q = random.randint(300,400)
            good.goto(p,q)
        for bad in badslist:
            p= random.randint(-380,380)
            q = random.randint(300,400)
            bad.goto(p,q)
        lives=5
        score=0
        text.clear()
        text.write("Score: %d  Lives: %d"%(score,lives),align="center",font=("Arial",20,"normal"))
        catcher.goto(0,-220)


    if catcher.dir == "right":
        catcher.setx(catcher.xcor() + 1)
    if catcher.dir == "left":
        catcher.setx(catcher.xcor() - 1)
    if catcher.xcor() == -380:
        catcher.dir = "right"
        catcher.shape("ll2.gif")
    if catcher.xcor() == 380:
        catcher.dir = "left"
        catcher.shape("ll1.gif")

    for good in goodslist:

        y = good.ycor()
        y -= good.speed
        good.sety(y)

        if y < -230:
            x = random.randint(-380,380)
            y = random.randint(300,400)
            good.goto(x,y)
        if good.distance(catcher) < 26:
            winsound.PlaySound("robot.wav", winsound.SND_ASYNC)
            x = random.randint(-380,380)
            y = random.randint(300,400)
            good.goto(x,y)
            score = score + 1
            text.clear()
            text.write("Score: %d  Lives: %d"%(score,lives),align="center",font=("Arial",20,"normal"))


    for bad in badslist:

        y = bad.ycor()
        y -= bad.speed
        bad.sety(y)

        if y < -230:
            x = random.randint(-380,380)
            y = random.randint(300,400)
            bad.goto(x,y)
        if bad.distance(catcher) < 26:
            winsound.PlaySound("gong.wav", winsound.SND_ASYNC)
            x = random.randint(-380,380)
            y = random.randint(300,400)
            bad.goto(x,y)
            lives = lives - 1
            text.clear()
            text.write("Score: %d  Lives: %d"%(score,lives),align="center",font=("Arial",20,"normal"))



win.mainloop()
