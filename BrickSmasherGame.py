## ---------------------------------------- ##
##                 Imports                       
## ---------------------------------------- ##
import turtle
import random

# Setting up the screen
screen = turtle.Screen()                           ##Making screen
screen.title("Brick Breaker")                      ##Makign title
screen.bgcolor("black")                            ##Making clolor black
screen.setup(width=600, height=600)                ##Size
screen.tracer(0)                                   ##Turning of animation

# Paddle
paddle = turtle.Turtle()                           ##Making turt
paddle.speed(0)                                    ##Setting speed 0
paddle.shape("square")                             ##Making sqaure
paddle.color("white")                              ##Setting color
paddle.shapesize(stretch_wid=1, stretch_len=5)     ##SEtting size
paddle.penup()                                     ##Stop drawing
paddle.goto(0, -250)                               ##Moving pen

# Ball
ball = turtle.Turtle()                             ##making turt
ball.speed(0)                                      ##Setting speed 0
ball.shape("circle")                               ##making circle
ball.color("white")                                ##SEtting color
ball.penup()                                       ##Stop drawing
ball.goto(0, 0)                                    ##Moving pen
ball.dx = 1                                        ##SEtting x veclocity
ball.dy = -1                                       ##setting y velocity

# Bricks
bricks = []                                        ##Making a list bricks

for i in range(-200, 200, 40):                     ## 2 for loops to make a grid pattern
    for j in range(200, 280, 20):                  
        brick = turtle.Turtle()                    ##Making a turtle for bricks
        brick.speed(0)                             ##Setting speed 0
        brick.shape("square")                      ##making sqaures
        brick.color("blue")                        ##Making color blue
        brick.penup()                              ##stop drawing
        brick.goto(i, j)                           ##Moving to next spot
        bricks.append(brick)                       ##add the brick to the list


## ---------------------------------------- ##
##            Paddle Left move                       
## ---------------------------------------- ##
def paddle_move_left(): 
    x = paddle.xcor()            ##Get currrentlocation
    x -= 20                      ##Move it a bit left
    if x < -280:                 ##Makes sure its not out of bonds
        x = -280                 ##If its dont move it
    paddle.setx(x)               ## sets the new x


## ---------------------------------------- ##
##            Paddle right move                       
## ---------------------------------------- ##
def paddle_move_right():
    x = paddle.xcor()              ##Get current x
    x += 20                        ## move it right
    if x > 280:                    ##Checks bounds
        x = 280                    ##if out of bound dont move
    paddle.setx(x)                 ##set new x


# Keyboard bindings
screen.listen()                                #Listeing
screen.onkeypress(paddle_move_left, "Left")    #If u hits left move left
screen.onkeypress(paddle_move_right, "Right")  #If move right then hit it
screen.onkeypress(screen.bye, "Escape")        ##IF esc leave

## ---------------------------------------- ##
##               Main Loop                       
## ---------------------------------------- ##
while True:

    screen.update()                        ##Update screen



    # Move the ball
    ball.setx(ball.xcor() + ball.dx)      ##Move ball x
    ball.sety(ball.ycor() + ball.dy)      ##Move ball y

    # Border checking
    if ball.xcor() > 290:                 ##Checks +x bound
        ball.setx(290)                    ##If out of x bound move
        ball.dx *= -1                     ##Set new veloicty

    if ball.xcor() < -290:                ##Checks -X bound
        ball.setx(-290)                   ##Set new x
        ball.dx *= -1                     ##Set new velocity

    if ball.ycor() > 290:                 ##Checks +Y bound
        ball.sety(290)                    ##Set new y 
        ball.dy *= -1                     ##Set new velocity

    if ball.ycor() < -290:                ##Check -Y bound            
        ball.goto(0, 0)                   ##Move ball
        ball.dy *= -1                     ##set new velocity


    # Paddle and ball collisions
    if (ball.ycor() < -240) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):   ##If paddle collides
        ball.sety(-240)                                                                    ##set new y
        ball.dy *= -1                                                                      ##set new veloicty

    # Ball and brick collisions
    for brick in bricks:                                                                                     ##For every brick
        if (ball.ycor() + 10 > brick.ycor() - 10) and (brick.xcor() - 20 < ball.xcor() < brick.xcor() + 20): ##If it collides
            ball.dy *= -1                                                                                    ##set new veolicty 
            bricks.remove(brick)                                                                             ##remove brick
            brick.hideturtle()                                                                               ##Hide turtle


