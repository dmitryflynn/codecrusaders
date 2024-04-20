##This is code
from cmu_graphics import *

Rect(0,0,400,400,fill='skyblue')
Circle(0,200,4,fill='green')

for i in range(400):
    Circle.centerX += 1

cmu_graphics.run()  