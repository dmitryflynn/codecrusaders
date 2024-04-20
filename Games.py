##Importing 
from cmu_graphics import *


background = Rect(0,0,400,400,fill='darkgreen')
screen = Rect(20,10,360,40,fill='white',border='darkgrey')
title = Label('Snake Game', 200,30,size=25)

apple = Circle(200, 200, 10, fill='Red', borderWidth=5)

cmu_graphics.run()

def onKeyPress(key):
    if(key == 'w'):
        #move up
        print('w')
    elif(key == 'a'):
        #move left
        print('a')
    elif(key == 's'):
        #move down
        print('s')
    elif(key == 'd'):
        #move right
        print('d')
