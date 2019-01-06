import turtle
import time
import random

delay = 0.1
score = 0

#player's name
player_name = ''
print('Welcome to Snake Game made by Vo Dong Cac.\n')
player_name = input('Your name: ')
while len(player_name)>6:
    print('I only allow names with 6 characters or less, sorry!')
    player_name = input('Your name: ')

#set up the screen
screen = turtle.Screen()
screen.title("Snake Game by Vo Dong Cac")
screen.bgcolor("azure")
screen.setup(width=600, height=600)
screen.tracer(0) # Turns off the screen updates

#snake's head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

#list containing parts of snake's body
parts = []

#border in case player expand the window
border = turtle.Turtle()
border.color("red")
border.penup()
border.hideturtle()
border.goto(-300, 300)
border.pendown()
border.goto(-300, 300)
border.goto(300, 300)
border.goto(300, -300)
border.goto(-300, -300)
border.goto(-300, 300)

#pen used to write player's name and score
pen = turtle.Turtle()
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 270)
pen.write("Player: {}  Score: 0".format(player_name), align="center", font=("Courier", 18, "normal"))

#set up snake's direction, not allowing the snake to move directly opposite to its current direction
def goUp():
    if head.direction != "down":
        head.direction = "up"

def goDown():
    if head.direction != "up":
        head.direction = "down"

def goLeft():
    if head.direction != "right":
        head.direction = "left"

def goRight():
    if head.direction != "left":
        head.direction = "right"

#move
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

#control
screen.listen()
screen.onkeypress(goUp, "Up")
screen.onkeypress(goDown, "Down")
screen.onkeypress(goLeft, "Left")
screen.onkeypress(goRight, "Right")

#main game
while True:
    screen.update()
    
    #change screen color when player got to 100 points or more
    if score > 99: screen.bgcolor("grey")
    else: screen.bgcolor("azure")

    #check if touched border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #hide the body parts (throw them out of the screen =)))
        for part in parts:
            part.goto(1000, 1000)
        
        #clear list of body parts since it's already ded
        parts.clear()

        #reset the score
        score = 0

        #reset the delay
        delay = 0.1

        #reset the info written on screen
        pen.clear()
        pen.write("Player: {}  Score: {}".format(player_name, score), align="center", font=("Courier", 18, "normal")) 


    #check if the snake got the food
    if head.distance(food) < 20:
        #move the food to a random spot
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x,y)

        #add a new part to the snake's body
        new_part = turtle.Turtle()
        new_part.speed(0)
        new_part.shape("circle")
        new_part.color("grey")
        new_part.penup()
        parts.append(new_part)

        #shorten the delay
        if delay > 0.02:
            delay -= 0.002

        #increase the score
        score += 10
        
        #update score (same as reset the info on the screen)
        pen.clear()
        pen.write("Player: {}  Score: {}".format(player_name, score), align="center", font=("Courier", 18, "normal")) 

    #get the body parts of the snake to stick to their previous parts and stick to the head
    for index in range(len(parts)-1, 0, -1):
        x = parts[index-1].xcor()
        y = parts[index-1].ycor()
        parts[index].goto(x, y)
    if len(parts) > 0:
        x = head.xcor()
        y = head.ycor()
        parts[0].goto(x,y)

    move()    

    #check if crashed to own's body
    for part in parts:
        if part.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            #hide the body parts (throw them out of the screen =)))
            for part in parts:
                part.goto(1000, 1000)
        
            #clear list of body parts since it's already ded
            parts.clear()

            #reset the score
            score = 0

            #reset the delay
            delay = 0.1
        
            #reset the info written on screen
            pen.clear()
            pen.write("Player: {}  Score: {}".format(player_name, score), align="center", font=("Courier", 18, "normal")) 

    time.sleep(delay)