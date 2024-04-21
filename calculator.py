from cmu_graphics import *
import math

background = Rect(0,0,400,400,fill='skyblue')
title = Label('Calculator App', 200,20,size=25)
screen = Rect(20,40,360,60,fill='white',border='blue')

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

buttonpi = Rect(20,300,40,40,fill='gray')
buttonpi.value = math.pi
buttonpiLabel = Label('π',40,320,fill='white',size=26)

sin = Rect(20,360,40,40,fill='gray')
sinLabel = Label('sin',40,380,fill='white',size=22)

cos = Rect(80,360,40,40,fill='gray')
cosLabel = Label('cos',100,380,fill='white',size=22)

tan = Rect(140,360,40,40,fill='gray')
tanLabel = Label('tan',160,380,fill='white',size=22)

addition = Rect(340,120,40,40,fill='gray')
additonLabel = Label('+',360,140,fill='white',size=26)

exponent = Rect(280,120,40,40,fill='gray')
exponentLabel = Label('^',300,140,fill='white',size=26)

minus = Rect(340,180,40,40,fill='gray')
minusLabel = Label('-',360,200,fill='white',size=26)

root = Rect(280,180,40,40,fill='gray')
rootLabel = Label('√',300,200,fill='white',size=26)

multiply = Rect(340,240,40,40,fill='gray')
multiplyLabel = Label('X',360,260,fill='white',size=26)

modulo = Rect(280,240,40,40,fill='gray')
moduloLabel = Label('%',300,260,fill='white',size=26)

division = Rect(340,300,40,40,fill='gray')
divisionLabel = Label('÷',360,320,fill='white',size=28)

negative = Rect(140,300,40,40,fill='gray')
negativeLabel = Label('(-)',160,320,fill='white',size=26)

equals = Rect(340,360,40,40,fill='gray')
equalsLabel = Label('=',360,380,fill='white',size=26)

clear = Rect(280,360,40,40,fill='gray')
clearLabel = Label('AC',300,380,fill='white',size=26)

operator = 'plus'
numbers = [button1,button2,button3,button4,button5,button6,button7,button8,button9,button0,buttonpi]
app.current_numbers = []
app.currentnumber = ''
app.newnumber = 0
result = Label(app.currentnumber,200,70,fill='dimgrey',size=35)

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

    ##Checks whether add has been pressed and clears the numbers, stores new number
    if addition.contains(mouseX, mouseY):
        operator = 'plus'
        app.newnumber = float(app.currentnumber)
        app.currentnumber = ''
        app.current_numbers = []
        result.value = ''

    ##Checks whether exponent has been pressed and clears the numbers, stores new number
    elif exponent.contains(mouseX, mouseY):
        if app.currentnumber != '': 
            operator = 'exponent'
            app.newnumber = float(app.currentnumber)
            app.currentnumber = ''
            app.current_numbers = []
            result.value = ''

    ##Checks whether minus has been pressed and clears the numbers, stores new number
    elif minus.contains(mouseX, mouseY):
        operator = 'subtract'
        app.newnumber = float(app.currentnumber)
        app.currentnumber = ''
        app.current_numbers = []
        result.value = ''

    elif root.contains(mouseX, mouseY):
        if app.currentnumber != '': 
            app.currentnumber = math.sqrt(float(app.currentnumber))
            total = app.currentnumber
            result.value = str(total)
            app.currentnumber = total
            app.current_numbers = []

    elif modulo.contains(mouseX, mouseY):
        if app.currentnumber != '': 
            operator = 'modulus'
            app.newnumber = float(app.currentnumber)
            app.currentnumber = ''
            app.current_numbers = []
            result.value = ''

    ##Checks whether multiply has been pressed and clears the numbers, stores new number
    elif multiply.contains(mouseX, mouseY):
        operator = 'multiply'
        app.newnumber = float(app.currentnumber)
        app.currentnumber = ''
        app.current_numbers = []
        result.value = ''

    ##Checks whether divide has been pressed and clears the numbers, stores new number
    elif division.contains(mouseX, mouseY):
        operator = 'divide'
        app.newnumber = float(app.currentnumber)
        app.currentnumber = ''
        app.current_numbers = []
        result.value = ''
    
    elif sin.contains(mouseX, mouseY):
        if app.currentnumber != '': 
            app.currentnumber = math.sin(float(app.currentnumber))
            total = app.currentnumber
            result.value = str(total)
            app.currentnumber = total
            app.current_numbers = []

    elif cos.contains(mouseX, mouseY):
        if app.currentnumber != '': 
            app.currentnumber = math.cos(float(app.currentnumber))
            total = app.currentnumber
            result.value = str(total)
            app.currentnumber = total
            app.current_numbers = []

    elif tan.contains(mouseX, mouseY):
        if app.currentnumber != '': 
            app.currentnumber = math.tan(float(app.currentnumber))
            total = app.currentnumber
            result.value = str(total)
            app.currentnumber = total
            app.current_numbers = []

    ##Handles negative operator
    elif negative.contains(mouseX, mouseY):
        if app.currentnumber != '':  # Check if current number is not empty
            app.currentnumber = float(app.currentnumber) * -1
            app.currentnumber = str(app.currentnumber)
            result.value = str(app.currentnumber)

    elif clear.contains(mouseX,mouseY):
        operator = 'clear'
        result.value = ''
        app.currentnumber = ''
        app.newnumber = None
        app.current_numbers = []




    elif equals.contains(mouseX,mouseY):

        ##Handles the addition operator
        if operator == 'plus':
            if app.currentnumber != '':
                total = app.newnumber + float(app.currentnumber)
                result.value = str(total)
                app.currentnumber = total
                app.current_numbers = []

        ## Handles the subtraction operator
        elif operator == 'subtract':
            if app.currentnumber != '':
                total = app.newnumber - float(app.currentnumber)
                result.value = str(total)
                app.currentnumber = total
                app.current_numbers = []

        ## Handles the multiplication operator
        elif operator == 'multiply':
            if app.currentnumber != '':
                total = app.newnumber * float(app.currentnumber)
                result.value = str(total)
                app.currentnumber = total
                app.current_numbers = []

        ## Handles the division operator 
        elif operator == 'divide':
            if app.currentnumber != '':
                total = app.newnumber / float(app.currentnumber)
                result.value = str(total)
                app.currentnumber = total
                app.current_numbers = []

        elif operator == 'exponent':
            if app.currentnumber != '':
                app.currentnumber = float(app.currentnumber)
                total = app.newnumber ** app.currentnumber
                result.value = str(total)
                app.currentnumber = total
                app.current_numbers = []

        elif operator == 'modulus':
            if app.currentnumber != '':
                app.currentnumber = float(app.currentnumber)
                total = app.newnumber % app.currentnumber
                result.value = str(total)
                app.currentnumber = total
                app.current_numbers = []

        
    else:
        keyChecker(mouseX, mouseY)

cmu_graphics.run()
