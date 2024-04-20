from cmu_graphics import *


background = Rect(0,0,400,400,fill='lightgrey')
title = Label('Calulator App', 200,20,size=25)
screen = Rect(20,40,360,60,fill='white',border='darkgrey')

button1 = Rect(20,120,40,40,fill='gray')
button1.value = 1
button1Label = Label('1',40,140,fill='white',size=26)

button2 = Rect(80,120,40,40,fill='gray')
button2.value = 2
button2Label = Label('2',100,140,fill='white',size=26)

button3 = Rect(140,120,40,40,fill='gray')
button3.value = 3
button3Label = Label('3',160,140,fill='white',size=26)

button4 = Rect(20,180,40,40,fill='gray')
button4.value = 4
button4Label = Label('4',40,200,fill='white',size=26)

button5 = Rect(80,180,40,40,fill='gray')
button5.value = 5
button5Label = Label('5',100,200,fill='white',size=26)

button6 = Rect(140,180,40,40,fill='gray')
button6.value = 6
button6Label = Label('6',160,200,fill='white',size=26)

button7 = Rect(20,240,40,40,fill='gray')
button7.value = 7
button7Label = Label('7',40,260,fill='white',size=26)

button8 = Rect(80,240,40,40,fill='gray')
button8.value = 8
button8Label = Label('8',100,260,fill='white',size=26)

button9 = Rect(140,240,40,40,fill='gray')
button9.value = 9
button9Label = Label('9',160,260,fill='white',size=26)

button0 = Rect(80,300,40,40,fill='gray')
button0.value = 0
button0Label = Label('0',100,320,fill='white',size=26)

addition = Rect(340,120,40,40,fill='gray')
additonLabel = Label('+',360,140,fill='white',size=26)

minus = Rect(340,180,40,40,fill='gray')
minusLabel = Label('-',360,200,fill='white',size=26)

multiply = Rect(340,240,40,40,fill='gray')
multiplyLabel = Label('X',360,260,fill='white',size=26)

division = Rect(340,300,40,40,fill='gray')
divisionLabel = Label('÷',360,320,fill='white',size=28)

negative = Rect(140,300,40,40,fill='gray')
negativeLabel = Label('(-)',160,320,fill='white',size=26)

equals = Rect(340,360,40,40,fill='gray')
equalsLabel = Label('=',360,380,fill='white',size=26)

operator = 'plus'
numbers = [button1,button2,button3,button4,button5,button6,button7,button8,button9,button0]
app.current_numbers = []
app.currentnumber = ''
app.newnumber = 0
result = Label(app.currentnumber,200,200,fill='white',size=30)

def keyChecker(X, Y):
    global operator
    for i in range(len(numbers)):
        if numbers[i].contains(X, Y):

            app.current_numbers.append(numbers[i].value)
            app.currentnumber = ''
            for k in range(len(app.current_numbers)):
                app.currentnumber += str(app.current_numbers[k])
                print(app.currentnumber)
            result.value = app.currentnumber
    
def onMousePress(mouseX,mouseY):
    global operator

    if addition.contains(mouseX, mouseY):
        operator = 'plus'
        app.newnumber = int(app.currentnumber)
        app.currentnumber = ''
        app.current_numbers = []
        result.value = ''

    elif minus.contains(mouseX, mouseY):
        operator = 'subtract'
        app.newnumber = int(app.currentnumber)
        app.currentnumber = ''
        app.current_numbers = []
        result.value = ''

    elif multiply.contains(mouseX, mouseY):
        operator = 'multiply'
        app.newnumber = int(app.currentnumber)
        app.currentnumber = ''
        app.current_numbers = []
        result.value = ''

    elif division.contains(mouseX, mouseY):
        operator = 'divide'
        app.newnumber = int(app.currentnumber)
        app.currentnumber = ''
        app.current_numbers = []
        result.value = ''
    
    elif negative.contains(mouseX, mouseY):
        operator = 'negative'
        app.currentnumber = int(app.currentnumber)*-1
        app.currentnumber = str(app.currentnumber)
        result.value = app.currentnumber

    elif equals.contains(mouseX,mouseY):
        if operator == 'plus':
            total = app.newnumber + int(app.currentnumber)
            result.value = str(total)
            app.currentnumber = 0

        elif operator == 'subtract':
            total = app.newnumber - int(app.currentnumber)
            result.value = str(total)
            app.currentnumber = total

        elif operator == 'multiply':
            total = app.newnumber * int(app.currentnumber)
            result.value = str(total)
            app.currentnumber = total

        elif operator == 'divide':
            total = app.newnumber / int(app.currentnumber)
            result.value = str(total)
            app.currentnumber = total
    else:
        keyChecker(mouseX, mouseY)

cmu_graphics.run()
