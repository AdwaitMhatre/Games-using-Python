import random
import winsound
import turtle
import time
import tkinter
from tkinter import messagebox

win = turtle.Screen()
win.title("Space War by Adwait")
win.setup(800,700)
win.bgcolor("black")
win.bgpic("gaa.gif")
win.tracer(0)

class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx,starty)
        self.speed = 2
    def move(self):
        self.fd(self.speed)
        if self.xcor() > 345:
            self.setx(345)
            self.rt(90)
        if self.xcor() < -345:
            self.setx(-345)
            self.rt(90)
        if self.ycor() > 295:
            self.sety(295)
            self.rt(90)
        if self.ycor() < -295:
            self.sety(-295)
            self.rt(90)
    def collision(self,other):
        if self.xcor() <= (other.xcor() + 20) and self.xcor() >= (other.xcor() - 20) and self.ycor() <= (other.ycor() + 20) and self.ycor() >= (other.ycor() - 20):
            return True
        else:
            return False


class Game():
    def __init__(self):
        self.score = 0
        self.level = 1
        self.state = "initiate"
        self.lives = 5
        self.pen = turtle.Turtle()
        self.text = turtle.Turtle()
        self.t2 = turtle.Turtle()
    def border(self):
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.pensize(3)
        self.pen.goto(-350,300)
        self.pen.pendown()
        for i in range(2):
            self.pen.fd(700)
            self.pen.rt(90)
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()
        self.pen.pendown()
    def game_status(self):
        self.pen.undo()
        self.pen.color("white")
        self.pen.speed(0)
        self.pen.penup()
        self.pen.ht()
        if self.lives != 0:
            text = "Score: %d  Live: %d"%(self.score,self.lives)
        elif self.lives == 0:
            text = "Game Over"
        self.pen.goto(-345,320)
        self.pen.write(text,font=("Arial",16,"normal"))
    def game_info(self):
        self.text.speed(0)
        self.text.ht()
        self.text.color("white")
        self.text.penup()
        self.text.goto(180,330)
        self.text.write("w,a,s,d: movement ; space: shoot ")
    def game_text(self):
        self.t2.speed(0)
        self.t2.ht()
        self.t2.color("white")
        self.t2.penup()
        self.t2.goto(180,310)
        self.t2.write("Blue: Allies  ;  Red: Enemies")

class Enemy(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 5
        self.setheading(random.randint(0,360))

class Ally(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 3
        self.setheading(random.randint(0,360))
    def move(self):
        self.fd(self.speed)
        if self.xcor() > 345:
            self.setx(345)
            self.lt(90)
        if self.xcor() < -345:
            self.setx(-345)
            self.lt(90)
        if self.ycor() > 295:
            self.sety(295)
            self.lt(90)
        if self.ycor() < -295:
            self.sety(-295)
            self.lt(90)
    def avoid(self,other):
        if (self.xcor() >= (other.xcor() -40)) and (self.xcor() <= (other.xcor() + 40)) and (self.ycor() >= (other.ycor() -40)) and (self.ycor() <= (other.ycor() + 40)):
            self.lt(20)



class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.lives = 3
        self.shapesize(0.7,1.1)
    def turn_left(self):
        self.lt(20)
    def turn_right(self):
        self.rt(20)
    def accelerate(self):
        self.speed += 1
        if self.speed > 6:
            self.speed = 6
    def decelerate(self):
        self.speed -= 1
        if self.speed < -2:
            self.speed = -2

class Bullet(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(0.3,0.4)
        self.speed = 20
        self.status = "ready"
        self.goto(1000,1000)

    def fire(self):
        if self.status == "ready":
            winsound.PlaySound("enemyshot.wav", winsound.SND_ASYNC)
            self.goto(player.xcor(),player.ycor())
            self.setheading(player.heading())
            self.status = "firing"
    def move(self):
        if self.status == "firing":
            self.fd(self.speed)
            if self.xcor() > 345 or self.xcor() < -345 or self.ycor() > 295 or self.ycor() < -295:
                self.goto(1000,1000)
                self.status = "ready"

class Debris(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(0.1,0.1)
        self.goto(1000,1000)
        self.speed = 0
    def explosion(self,x,y):
        self.goto(x,y)
        self.setheading(random.randint(0,360))
        self.speed = 1
    def move(self):
        if self.speed != 0:
            self.fd(16 - self.speed)
            self.speed += 1
            if self.speed < 5:
                self.shapesize(0.3,0.3)
            elif self.speed < 10:
                self.shapesize(0.2,0.2)
            else:
                self.shapesize(0.1,0.1)
            if self.speed > 16:
                self.speed = 0
                self.goto(1000,1000)

game = Game()
game.border()
game.game_status()
game.game_info()
game.game_text()

player = Player("triangle", "white", 0, 0)
#enemy = Enemy("circle","red",300,-250)
bullet = Bullet("circle","orange",0,0)
#ally = Ally("triangle","blue",-250,200)

win.listen()
win.onkeypress(player.turn_left,"a")
win.onkeypress(player.turn_right,"d")
win.onkeypress(player.accelerate,"w")
win.onkeypress(player.decelerate,"s")
win.onkeypress(bullet.fire,"space")

if game.state == "initiate":
    enemies = []
    for i in range(5):
        enemies.append(Enemy("circle","red",300,-250))
    allies = []
    for i in range(5):
        allies.append(Ally("triangle","blue",-250,200))
    debris = []
    for i in range(3):
        debris.append(Debris("circle","orange",1000,1000))
    for i in range(3):
        debris.append(Debris("circle","yellow",1000,1000))
    for i in range(3):
        debris.append(Debris("circle","red",1000,1000))

    game.state = "play"

#Main game loop
while True:
    win.update()
    time.sleep(0.025)

    if game.state == "restart":
        game.lives = 5
        game.score = 0
        game.game_status()
        player.goto(0,0)
        player.setheading(random.randint(0,360))
        game.state = "play"

    if game.state == "play":

        player.move()
        #enemy.move()
        bullet.move()
        #ally.move()
        for enemy in enemies:
            enemy.move()

            if player.collision(enemy):
                winsound.PlaySound("reserve.wav", winsound.SND_ASYNC)
                player.color("red")
                for deb in debris:
                    deb.explosion(enemy.xcor(),enemy.ycor())
                game.lives -= 1
                if game.lives < 1:
                    for deb in debris:
                        deb.explosion(enemy.xcor(),enemy.ycor())
                    game.state = "gameover"
                game.score -= 10
                game.game_status()
                player.speed = 0
                player.goto(0,0)
                a = random.randint(-310,310)
                b = random.randint(-260,260)
                enemy.setheading(random.randint(0,360))
                enemy.goto(a,b)
                player.color("white")
            if bullet.collision(enemy):
                winsound.PlaySound("enemyblast.wav", winsound.SND_ASYNC)
                for deb in debris:
                    deb.explosion(enemy.xcor(),enemy.ycor())
                game.score += 10
                game.game_status()
                a = random.randint(-310,310)
                b = random.randint(-260,260)
                enemy.setheading(random.randint(0,360))
                enemy.goto(a,b)
                bullet.goto(1000,1000)
                bullet.status = "ready"

        for ally in allies:
            ally.move()
            ally.avoid(player)
            for enemy in enemies:
                ally.avoid(enemy)
            if bullet.collision(ally):
                winsound.PlaySound("allyblast.wav", winsound.SND_ASYNC)
                for deb in debris:
                    deb.explosion(ally.xcor(),ally.ycor())
                game.score -= 10
                game.game_status()
                a = random.randint(-310,310)
                b = random.randint(-260,260)
                ally.setheading(random.randint(0,360))
                ally.goto(a,b)
                bullet.goto(1000,1000)
                bullet.status = "ready"

        for deb in debris:
            deb.move()

        if game.state == "gameover":
            if messagebox.askyesno("Game Over", "Play again?") == True:
                game.state = "restart"
            else:
                exit()



win.mainloop()
