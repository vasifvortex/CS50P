import turtle
import time
import random
from sys import argv
import sys

#global variable
head = turtle.Turtle()


def choose_apple_colour():
    list=['red','yellow']
    print(f"Available colours: {str(list).replace('[','').replace(']','')}")
    while True:
        i=input("Enter your apple's colour from the list: ")
        if i not in list:
            print("Try available colours")
            pass
        else:
            break
    return i


def choose_snake_colour():
    list=['gray','blue','green','turquoise','cyan','goldenrod','orange','red','magenta','orchid']

    print(f"Available colours: {str(list).replace('[','').replace(']','')}")
    while True:
        i=input("Enter your snake's colour from the list: ")
        if i not in list:
            print("Try available colours")
            pass
        else:
            break
    return i


def choose_height_and_weight(width=600, height=600):
    return int(width),int(height)


def go_up():
    global head
    if head.direction != "down":
        head.direction = "up"


def go_down():
    global head
    if head.direction != "up":
        head.direction = "down"



def go_left():
    global head
    if head.direction != "right":
        head.direction = "left"


def go_right():
    global head
    if head.direction != "left":
        head.direction = "right"


def move():
    global head
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

        
def main():
    delay = 0.1
    score = 0
    highest_score = 0

    #window screen
    screen = turtle.Screen()
    screen.title("Snake Game")
    screen.bgcolor("light green")
    try:
        w,h=choose_height_and_weight(argv[1],argv[2])
    except IndexError:
        sys.exit("Try as example: python project.py 300 300")  
    screen.setup(width=w, height=h)
    screen.tracer(0)
    c=choose_snake_colour()
    a=choose_apple_colour()

    #head
    head.shape("square")
    head.color(f"dark {c}")
    head.penup()
    head.goto(0, 0)
    head.direction = "Stop"

    #apple
    apple = turtle.Turtle()
    apple.speed(0)
    apple.shape('circle')
    apple.color(a)
    apple.penup()
    apple.goto(0, 100)

    #text on top
    text = turtle.Turtle()
    text.speed(0)
    text.shape("circle")
    text.color("white")
    text.penup()
    text.hideturtle()
    text.goto(0, 250)
    text.write("Score : 0  Highest Score : 0", align="center",
            font=("Comic Sans", 24, "bold"))

    # keys
    screen.listen()
    screen.onkeypress(go_up, "w")
    screen.onkeypress(go_down, "s")
    screen.onkeypress(go_left, "a")
    screen.onkeypress(go_right, "d")
    segments = []

    while True:
        screen.update()
        if head.xcor() > (w-20)/2 or head.xcor() < -(w-20)/2  or head.ycor() > (w-20)/2 or head.ycor() < -(w-20)/2:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            text.clear()
            text.write("Score : {} Highest Score : {} ".format(
                score, highest_score), align="center", font=("Comic Sans", 24, "bold"))
        if head.distance(apple) < 20:
            x = random.randint(-((w-20)/2-20), ((w-20)/2-20))
            y = random.randint(-((h-20)/2-20), ((h-20)/2-20))
            apple.goto(x, y)
            #Incrising length
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color(c)#tail colour
            new_segment.penup()
            segments.append(new_segment)
            delay -= 0.001
            score += 10
            if score > highest_score:
                highest_score = score
            text.clear()
            text.write("Score : {} Highest Score : {} ".format(
                score, highest_score), align="center", font=("Comic Sans", 24, "bold"))
            

        #biting itself
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)
        move()
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"
                for segment in segments:
                    segment.goto(1000, 1000)
                segments.clear()

                score = 0
                delay = 0.1
                text.clear()
                text.write("Score : {} Highest Score : {} ".format(
                    score, highest_score), align="center", font=("Comic Sans", 24, "bold"))
        time.sleep(delay)



if __name__=="__main__":
    main()
