## LOG:
## Noah Wichman
## 4/20 7:33 am PCT  - 9:48 am PCT
## 4/20 10:02 am PCT - 2:47 pm PCT
## TOTAL HOURS: 7 hours and 2 mins



## ---------------------------------------- ##
##                 Imports                       
## ---------------------------------------- ##
import turtle
import random

## ---------------------------------------- ##
##                 Varibles                       
## ---------------------------------------- ##
CELL_SIZE = 20
GRID_WIDTH = 20
GRID_HEIGHT = 15
UP = 0         # direction var
DOWN = 1       # direction var
LEFT = 2       # direction var
RIGHT = 3      # direction var


## ---------------------------------------- ##
##                 SnakeGame                       
## ---------------------------------------- ##
class SnakeGame:


    ## ---------------------------------------- ##
    ##             initial function                       
    ## ---------------------------------------- ##
    def __init__(self):

        
        self.window = turtle.Screen()                                         ## makes a new window
        self.window.title("Snake Game")                                       ## defines the title
        self.window.setup(GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE)    ## sets size of window
        self.window.tracer(0)                                                 ## turn off turtle
        
        self.snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]                    ##Sets snakes start postion
        self.direction = RIGHT                                                ##Sets intial direcvtion
        self.apple = self.generateApple()                                     ##generates first apple
        self.score = 0                                                        ##sets score to 0 (apples eatten)

        self.pen = turtle.Turtle()                                                                      ##makes the turtle
        self.pen.penup()                                                                                ##makes sure turtle not drawing yet
        self.pen.hideturtle()                                                                           ##Hides turtle
        self.pen.goto(0, GRID_HEIGHT * CELL_SIZE // 2 - 20)                                             ##Move turtle to start postion
        self.pen.write("Score: {}".format(self.score), align="center", font=("Courier", 24, "normal"))  ##Wirte intail score

        self.window.listen()                                ##Listens for keypress
        self.window.onkeypress(self.goUp, "w")             ##if key was w do GoUp   Method
        self.window.onkeypress(self.goDown, "s")           ##if key was s do GoDown method
        self.window.onkeypress(self.goLeft, "a")           ##if key was A do goLeft Method
        self.window.onkeypress(self.goRight, "d")          ##if key was D do goRight method

        self.update()                                       ##Start loop


    ## ---------------------------------------- ##
    ##         Generate Apple function                       
    ## ---------------------------------------- ##
    def generateApple(self):
        while True:                                     ##Loops until it gets a spot
            x = random.randint(0, GRID_WIDTH - 1)       ##random X
            y = random.randint(0, GRID_HEIGHT - 1)      ##random Y
            if (x, y) not in self.snake:                ##Make sure snake isnt at that spot
                return (x, y)                           ##If spot is good returns it


    ## ---------------------------------------- ##
    ##           Draw a cell function                       
    ## ---------------------------------------- ##
    def drawCell(self, x, y):
        self.pen.goto(x * CELL_SIZE - GRID_WIDTH * CELL_SIZE // 2, y * CELL_SIZE - GRID_HEIGHT * CELL_SIZE // 2)  ##Moves pen to spot
        self.pen.pendown()                                                                                        ##Gets ready to drwa
        self.pen.begin_fill()                                                                                     ##Starts making shape
        for _ in range(4):                                                                                        ##For each side of sqaure
            self.pen.forward(CELL_SIZE)                                                                           ##Move pen forward
            self.pen.right(90)                                                                                    ##Then roate to get ready for next side
        self.pen.end_fill()                                                                                       ##stops making shape
        self.pen.penup()                                                                                          ##ends drawing


    ## ---------------------------------------- ##
    ##           Draw snake function                       
    ## ---------------------------------------- ##
    def draw_snake(self):
        for x, y in self.snake:       ##For every peice of the snake
            self.drawCell(x, y)       ##Draw it lol


    ## ---------------------------------------- ##
    ##           Draw apple function                       
    ## ---------------------------------------- ##
    def drawApple(self):
        self.drawCell(*self.apple)    ##Draw the apple Idk what to say lol


    ## ---------------------------------------- ##
    ##         Draw the grid function                       
    ## ---------------------------------------- ##
    def draw_grid(self): 

        for x in range(-GRID_WIDTH // 2, GRID_WIDTH // 2 + 1):                             ##For every vertical line AKA x
            self.pen.goto(x * CELL_SIZE - CELL_SIZE // 2, -GRID_HEIGHT * CELL_SIZE // 2)   ##go to the spot
            self.pen.pendown()                                                             ##start drwaing
            self.pen.goto(x * CELL_SIZE - CELL_SIZE // 2, GRID_HEIGHT * CELL_SIZE // 2)    ##draw the line
            self.pen.penup()                                                               ##stop drawing

        for y in range(-GRID_HEIGHT // 2, GRID_HEIGHT // 2 + 1):                           ##For every hortzianl line AKA y
            self.pen.goto(-GRID_WIDTH * CELL_SIZE // 2, y * CELL_SIZE - CELL_SIZE // 2)    ##go to the begain
            self.pen.pendown()                                                             ##start drawing
            self.pen.goto(GRID_WIDTH * CELL_SIZE // 2, y * CELL_SIZE - CELL_SIZE // 2)     ##draw the line
            self.pen.penup()                                                               ##stop drawing


    ## ---------------------------------------- ##
    ##              GoUp function                       
    ## ---------------------------------------- ##
    def goUp(self):
        if self.direction != DOWN: ##Check to make sure ur not doing a 180
            self.direction = UP    ##Swaps the direction


    ## ---------------------------------------- ##
    ##             GoDown function                       
    ## ---------------------------------------- ##
    def goDown(self):
        if self.direction != UP:         ##Make sure u not 180
            self.direction = DOWN        ##change direction


    ## ---------------------------------------- ##
    ##             GoLeft function                       
    ## ---------------------------------------- ##
    def goLeft(self):
        if self.direction != RIGHT:            ##Makes sure ur not 180ing
            self.direction = LEFT              ##change direction


    ## ---------------------------------------- ##
    ##             GoRight function                       
    ## ---------------------------------------- ##
    def goRight(self):
        if self.direction != LEFT:          ##Check to make sure ur not 180
            self.direction = RIGHT          ##change direction


    ## ---------------------------------------- ##
    ##             Update function                       
    ## ---------------------------------------- ##
    def update(self):
        # Move the snake
        head = self.snake[0]                     ##Get postion of the head
        if self.direction == UP:                 ##If direction is up
            new_head = (head[0], head[1] + 1)    ##Move up

        elif self.direction == DOWN:             ##if direction is down
            new_head = (head[0], head[1] - 1)    ##move down
            
        elif self.direction == LEFT:             ## if direction is left
            new_head = (head[0] - 1, head[1])    ## move left

        elif self.direction == RIGHT:            ##If direction is right
            new_head = (head[0] + 1, head[1])    ##mobe right


        # Check for collision
        if (                                    ##Checks to make sure the player hasnt ran into anything
            new_head[0] < 0                     ## check to make sure it not out of bound
            or new_head[0] >= GRID_WIDTH        ## check to make sure it not out of bound
            or new_head[1] < 0                  ## check to make sure it not out of bound
            or new_head[1] >= GRID_HEIGHT       ## check to make sure it not out of bound
            or new_head in self.snake           ## check it didnt hit it self
        ):
            self.gameOver()                     ##If the player has ran into something end the game 

        # Check if the snake eats the Apple
        if new_head == self.apple:                                                                          ##If snake eat apple
            self.score += 1                                                                                 ##Increase score
            self.pen.clear()                                                                                ##prep to redraw shuf
            self.pen.write("Score: {}".format(self.score), align="center", font=("Courier", 24, "normal"))  ##Wirte new score
            self.snake.insert(0, new_head)                                                                  ##make new head
            self.apple = self.generateApple()                                                               ##make new apple

        else:                                                                                               ##If snake not eat apple
            self.snake.insert(0, new_head)                                                                  ##Add new head anyways
            self.snake.pop()                                                                                ##destory old head

        self.pen.clear()            ## clear old drwaings
        self.draw_grid()            ## draw grid
        self.draw_snake()           ## draw snake
        self.drawApple()            ## draw apple
        self.window.update()        ## update (RECURISSION AP CSA TOPIC LOL) keeps loop going

        # Update again in 200 milliseconds
        self.window.ontimer(self.update, 200)


    ## ---------------------------------------- ##
    ##            GameOver function                       
    ## ---------------------------------------- ##
    def gameOver(self):
        self.pen.goto(0, 0)                                                             ##move pen to 0
        self.pen.write("Game Over", align="center", font=("Courier", 24, "normal"))     ##wirte end message
        self.window.update()                                                            ##shows what turtle worte 
        self.window.mainloop()                                                          ##Makes sure game doesnt die instant


# Runs the acutal game lol
game = SnakeGame()
game.window.mainloop()