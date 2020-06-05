import turtle
import time
import random
import winsound

delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by Adwait")
wn.bgcolor("yellow")
wn.bgpic("backg2.gif")
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates
turtle.write("Press SPACE to start",align="center",font=("Arial",24,"bold"))
turtle.hideturtle()

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
a = random.randint(0,290)
b = random.randint(0,290)
food.goto(a,b)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)


# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

def start():
    turtle.clear()
    global delay
    global score
    global high_score
    pen.write("Score: {} High Score: {}".format(score,high_score), align="center", font=("Arial", 24, "normal"))

# Main game loop
    while True:
        wn.update()
        a = random.randint(0,280)
        b = random.randint(0,280)

    # Check for a collision with the border
        if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
            winsound.PlaySound("gong.wav", winsound.SND_ASYNC)
            time.sleep(1)
            head.goto(0,0)
            head.home()
            food.goto(a,b)
            head.direction = "stop"

        # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

        # Clear the segments list
            segments.clear()

        # Reset the score
            score = 0

        # Reset the delay
            delay = 0.1

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Arial", 24, "normal"))


    # Check for a collision with the food
        if head.distance(food) < 20:
            winsound.PlaySound("robot.wav", winsound.SND_ASYNC)
        # Move the food to a random spot
            x = random.randrange(-280, 281, 20)
            y = random.randrange(-280, 281, 20)
            food.goto(x,y)

        # Add a segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("grey")
            new_segment.penup()
            segments.append(new_segment)

        # Shorten the delay
            delay -= 0.001

        # Increase the score
            score += 10

            if score > high_score:
                high_score = score

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Arial", 24, "normal"))

    # Move the end segments first in reverse order
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)

    # Move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x,y)

        move()

    # Check for head collision with the body segments
        for segment in segments:
            if segment.distance(head) < 20:
                winsound.PlaySound("gong.wav", winsound.SND_ASYNC)
                time.sleep(1)
                head.goto(0,0)
                head.home()
                food.goto(a,b)
                head.direction = "stop"

            # Hide the segments
                for segment in segments:
                    segment.goto(1000, 1000)

            # Clear the segments list
                segments.clear()

            # Reset the score
                score = 0

            # Reset the delay
                delay = 0.1

            # Update the score display
                pen.clear()
                pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Arial", 24, "normal"))

        time.sleep(delay)

wn.onkeypress(start,"space")
wn.mainloop()
