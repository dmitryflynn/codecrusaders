from cmu_graphics import *
import cmu_graphics

background = Rect(0,0,400,400,fill='lightgrey')
title = Label('Calulator App', 200,20,size=25)
screen = Rect(20,40,360,60,fill='white',border='darkgrey')

button1 = Rect(20,120,40,40,fill='gray')
button1.value = 1
button1Label = Label('1',40,140,fill='white',size=26)
button2 = Rect(80,120,40,40,fill='gray')
button2.value = 2
button3 = Rect(140,120,40,40,fill='gray')
button3.value = 3

button4 = Rect(20,180,40,40,fill='gray')
button4.value = 4
button5 = Rect(80,180,40,40,fill='gray')
button5.value = 5
button6 = Rect(140,180,40,40,fill='gray')
button6.value = 6

button7 = Rect(20,240,40,40,fill='gray')
button7.value = 7
button8 = Rect(80,240,40,40,fill='gray')
button8.value = 8
button9 = Rect(140,240,40,40,fill='gray')
button9.value = 9

cmu_graphics.run()
