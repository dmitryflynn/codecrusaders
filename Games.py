## ----------------------------------------------------- ##
##            /Importing Graphics and random/              
## ----------------------------------------------------- ##
from cmu_graphics import *
from random import *


## ----------------------------------------------------- ##
##                 /Draw Snake Function/                         
## ----------------------------------------------------- ##
def drawSnake():

    # Delcaring Vars
    colorTurn = 0
    blockSize = 15
    x = 100  

    # For loop to go through each part of the Snake
    for segment in snakeSegments:
        
        # Swaps between 1 and 2 each time 
        colorTurn = (colorTurn % 2) + 1

        #Draws the snake based on which color it is
        if colorTurn == 1:
            snake = Rect(x, segment[1], blockSize, blockSize, fill='green')
        elif colorTurn == 2:
            snake = Rect(x, segment[1], blockSize, blockSize, fill='lightgreen')

        # Increase x for the next loop
        x += blockSize  


## ----------------------------------------------------- ##
##             /Making background and title/                
## ----------------------------------------------------- ##
background = Rect (0,0,400,400,   fill='darkgreen'                  )
screen     = Rect (20,10,360,40,  fill='white',    border='darkgrey')
title      = Label('Snake Game', 200,30,size=25)


## ----------------------------------------------------- ##
##             /Making Walls to mark boders/                
## ----------------------------------------------------- ##
TopWall    = Line(10,100,380,100, lineWidth=10, fill='black')
LeftWall   = Line(10,95,10,390,   lineWidth=10, fill='black')
RightWall  = Line(380,95,380,390, lineWidth=10, fill='black')
BottomWall = Line(10,385,380,385, lineWidth=10, fill='black')


## ----------------------------------------------------- ##
##                 /Coords List / Vars/                         
## ----------------------------------------------------- ##
possible_x_coords = [115, 135, 155, 175, 195, 215, 235, 255, 275, 295, 315, 335, 355, 375]
possible_y_coords = [105, 125, 145, 165, 185, 205, 225, 245, 265, 285, 305, 325, 345, 365]
alive = True
snakeSegments = [[115, 105], [135, 105], [155, 365]] 


## ----------------------------------------------------- ##
##                   /Main While Loop/                     
## ----------------------------------------------------- ##
while alive:

    drawSnake()

    apple_x = choice(possible_x_coords)
    apple_y = choice(possible_y_coords)

    apple = Circle(apple_x, apple_y, 10, fill='Red', borderWidth=5)
    alive = False


    ## IF snake hitshape apple apple_x += snakeSeg

















cmu_graphics.run()


