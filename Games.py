##Importing 
from cmu_graphics import *


background = Rect(0,0,400,400,fill='darkgreen')
screen = Rect(20,10,360,40,fill='white',border='darkgrey')
title = Label('Snake Game', 200,30,size=25)


keyLabel = Label('', 200, 200, size=50)


cmu_graphics.run()

def onKeyPress(key):
    keyLabel.value = key
    print(keyLabel)


def onKeyPress(key):
    # Move the sword and brighten the sky and gem in Excalibur's handle.
    print('hhhhhh')
    pass