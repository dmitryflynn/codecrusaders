from cmu_graphics import *

background = Rect(0,0,400,400,fill='lightgrey')
title = Label('Honor Society Tracker', 200,20,size=25)


inputer = Group(
    Rect(20,50,360,40,fill='lightgrey',border='darkgrey'),
    Label('Enter in Your Hours',190,70,size=20),
)

def onMousePress(mouseX,mouseY):
    if inputer.contains(mouseX,mouseY):
        purpose = app.getTextInput('What is the name of the entry?')
        inputer[0].fill='darkgrey'
def onMouseRelease(mouseX,mouseY):
    if inputer.contains(mouseX,mouseY):
            inputer[0].fill='lightgrey'

cmu_graphics.run()