from cmu_graphics import *
import cmu_graphics

background = Rect(0,0,400,400,fill='lightgrey')
title = Label('Calulator App', 200,20,size=25)
screen = Rect(20,40,360,60,fill='white',border='darkgrey')

button1Group = Group(
    button1 = Rect(20,120,40,40,fill='gray'),
    button1Label = Label('1',40,140,fill='white',size=26),
    )

button2Group = Group(
    button2 = Rect(80,120,40,40,fill='gray'),
    button2Label = Label('2',100,140,fill='white',size=26),
)

button3Group = Group(
    button3 = Rect(140,120,40,40,fill='gray'),
    button3Label = Label('3',160,140,fill='white',size=26),
    )


button4Group = Group(
    button4 = Rect(20,180,40,40,fill='gray'),
    button4Label = Label('4',40,200,fill='white',size=26),
    )

button5Group = Group(
    button5 = Rect(80,180,40,40,fill='gray'),
    button5Label = Label('5',100,200,fill='white',size=26),
    )

button6Group = Group(
    button6 = Rect(140,180,40,40,fill='gray'),
    button6Label = Label('6',160,200,fill='white',size=26),
    )

button7Group = Group(
    button7 = Rect(20,240,40,40,fill='gray'),
    button7Label = Label('7',40,260,fill='white',size=26),
    )

button8Group = Group(
    button8 = Rect(80,240,40,40,fill='gray'),
    button8Label = Label('8',100,260,fill='white',size=26),
    )

button9Group = Group(
    button9 = Rect(140,240,40,40,fill='gray'),
    button9Label = Label('9',160,260,fill='white',size=26),
    )

button1Group.value = 1
button2Group.value = 2
button3Group.value = 3
button4Group.value = 4
button5Group.value = 5
button6Group.value = 6
button7Group.value = 7
button8Group.value = 8
button9Group.value = 9

def keyChecker(mouseX,mouseY):
    pass
    

cmu_graphics.run()
