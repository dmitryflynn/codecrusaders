from cmu_graphics import *


sky = Rect(0, 0, 400, 400, fill='midnightBlue')

ground = Rect(0, 350, 400, 85,
            fill=gradient(rgb(0, 60, 0), rgb(0, 80, 0), start='bottom'))

excalibur = Group(
    Polygon(185, 150, 215, 150, 215, 325, 200, 365, 185, 325,
            fill=rgb(230, 240, 250)),
    Line(200, 155, 200, 335, fill=rgb(220, 220, 220)),
    Rect(150, 140, 100, 10, fill='silver'),
    Line(200, 140, 200, 60, fill=rgb(100, 100, 100), lineWidth=15),
    Line(200, 140, 200, 60, fill='silver', lineWidth=15, dashes=(9, 0.1))
    )

gem = Circle(200, 60, 15, fill='grey', border='silver', borderWidth=6)

excalibur.add(gem)

# rock
Polygon(60, 395, 340, 395, 300, 345, 100, 345,
        fill=gradient('dimGrey', 'grey', start='bottom'))
Rect(100, 315, 200, 30, fill=gradient('grey', 'silver', start='bottom'))

def onMousePress(mouseX, mouseY):
    # Move the sword and brighten the sky and gem in Excalibur's handle.
    gem.fill = rgb(225,255,220)
    sky.fill = gradient('midnightBlue',rgb(15,245,200),'midnightBlue',start='left')
    excalibur.centerY -= 45
    pass

def onMouseRelease(mouseX, mouseY):
    # Return Excalibur to the stone and darken the sky and gem.
    gem.fill = 'grey'
    sky.fill = 'midnightBlue'
    excalibur.centerY += 45
    pass


cmu_graphics.run()