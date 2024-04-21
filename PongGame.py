## LOG:
## Noah Wichman
## 4/20 4:29 pm PCT  - 6:53 pm PCT
## TOTAL HOURS: 2 hours and 24 mins



## ---------------------------------------- ##
##                 Imports                       
## ---------------------------------------- ##
import turtle

# Setting up the screen
screen = turtle.Screen()                     ##Makeing screen
screen.title("Pong")                         ##Setting title
screen.bgcolor("black")                      ##Bg black
screen.setup(width=600, height=400)          ##Size
screen.tracer(0)                             ##Turn off animation       

# Paddle A (controlled by mouse)
paddleA = turtle.Turtle()                           ##Making tutrtle
paddleA.speed(0)                                    ##Setting speed 0
paddleA.shape("square")                             ##Making the sqaure
paddleA.color("white")                              ##setting color
paddleA.shapesize(stretch_wid=5, stretch_len=1)     ##setting size
paddleA.penup()                                     ##Stop drawing
paddleA.goto(-250, 0)                               ##moving pen

# Paddle B (controlled by AI)
paddleB = turtle.Turtle()                           ##Making tutrtle
paddleB.speed(0)                                    ##Setting speed 0
paddleB.shape("square")                             ##Making the sqaure
paddleB.color("white")                              ##setting color
paddleB.shapesize(stretch_wid=5, stretch_len=1)     ##setting size
paddleB.penup()                                     ##Stop drawing
paddleB.goto(250, 0)                                ##moving pen

# Ball
ball = turtle.Turtle()                              ## Making a turtle 
ball.speed(0)                                       ## Setting speed 0
ball.shape("square")                                ## Making the sqaure
ball.color("white")                                 ##setting color
ball.penup()                                        ##Stop drawing
ball.goto(0, 0)                                     ##moving pen
ball.dx = 0.1                                       ##Setting the ball velocity x
ball.dy = 0.1                                       ##Setting the ball velocity Y


## ---------------------------------------- ##
##            Set paddleA location                       
## ---------------------------------------- ##
def paddleAMove(y):
    paddleA.sety(y) ##Sets the paddles new Y location

## ---------------------------------------- ##
##            Ai location paddle                       
## ---------------------------------------- ##
def paddleBAi():
    if ball.ycor() < paddleB.ycor() and abs(ball.ycor() - paddleB.ycor()) > 20:       ## Returns current y of the ball and checks to see if need to move
        paddleB.sety(paddleB.ycor() - 0.1)                                            ## If need to move do it 
    elif ball.ycor() > paddleB.ycor() and abs(ball.ycor() - paddleB.ycor()) > 20:     ## checks current x of ball and see if need to move
        paddleB.sety(paddleB.ycor() + 0.1)                                            ##if need to move then do it


## ---------------------------------------- ##
##              Update paddle                        
## ---------------------------------------- ##
def updatePaddleA(x, y):
    paddleAMove(y)           ##Moves paddle


# Keyboard bindings (for exiting the game) 
screen.listen()                                      ##Listeing
screen.onkeypress(screen.bye, "Escape")              ##if Esc leave 

# Bind updatePaddleA to mouse clicks within the window
screen.onscreenclick(updatePaddleA)


## ---------------------------------------- ##
##             Main game loop                       
## ---------------------------------------- ##
while True:

    screen.update()                        ##Updates screen

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)       ##Moves x of ball
    ball.sety(ball.ycor() + ball.dy)       ##Moves y of ball

    # Border checking
    if ball.ycor() > 190:                  ##If off screen
        ball.sety(190)                     ##reast ball
        ball.dy *= -1                      ##reast velocity

    if ball.ycor() < -190:                 ##If off screen
        ball.sety(-190)                    ##reast ball
        ball.dy *= -1                      ##reast velocity

    if ball.xcor() > 290:                  ##If off screen
        ball.goto(0, 0)                    ##reast ball
        ball.dx *= -1                      ##reast velocity

    if ball.xcor() < -290:                 ##If off screen
        ball.goto(0, 0)                    ##reast ball
        ball.dx *= -1                      ##reast velocity

    # Paddle B (AI control)
    paddleBAi()

    # Paddle and ball collisions
    if (ball.xcor() > 240 and ball.xcor() < 250) and (ball.ycor() < paddleB.ycor() + 50 and ball.ycor() > paddleB.ycor() - 50):           ###If balla hits Paddle b
        ball.setx(240)                                                                                                                    ## set new x
        ball.dx *= -1                                                                                                                     ##set new velocity

    if (ball.xcor() < -240 and ball.xcor() > -250) and (ball.ycor() < paddleA.ycor() + 50 and ball.ycor() > paddleA.ycor() - 50):         ##If balla hits Paddle a
        ball.setx(-240)                                                                                                                   ## set new x
        ball.dx *= -1                                                                                                                     ##set new velocity
