import turtle
import time
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []
score = 0
high_score = 0
delay = 0.1
paused = False
running = True

pen = turtle.Turtle()
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


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
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)


def toggle_pause():
    global paused
    paused = not paused
    pen.clear()
    if paused:
        pen.write("Paused", align="center", font=("Courier", 24, "normal"))
    else:
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))


def stop_game():
    global running
    running = False


screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_right, "Right")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_up, "w")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_right, "d")
screen.onkeyrelease(toggle_pause, "space")
screen.onkeyrelease(stop_game, "Escape")

while running:
    screen.update()

    if paused:
        time.sleep(0.1)
        continue

    if head.distance(food) < 20:
        x = random.randrange(-280, 281, 20)
        y = random.randrange(-280, 281, 20)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))
        delay -= 0.001

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        pen.clear()
        pen.write("Game Over", align="center", font=("Courier", 24, "normal"))
        screen.update()
        time.sleep(1)

        head.goto(0, 0)
        head.direction = "stop"

        for seg in segments:
            seg.goto(1000, 1000)
        segments.clear()

        score = 0
        delay = 0.1
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    for segment in segments:
        if segment.distance(head) < 20:
            pen.clear()
            pen.write("Game Over", align="center", font=("Courier", 24, "normal"))
            screen.update()
            time.sleep(1)

            head.goto(0, 0)
            head.direction = "stop"

            for seg in segments:
                seg.goto(1000, 1000)
            segments.clear()

            score = 0
            delay = 0.1
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

screen.bye()