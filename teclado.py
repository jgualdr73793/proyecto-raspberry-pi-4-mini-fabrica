import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

fila=29

columnas=[35,37,31,33]

keypadPressed = -1
secretCode = "123"
input = ""

GPIO.setup(29,GPIO.OUT)

GPIO.setup (31,GPIO.IN,GPIO.PUD_DOWN)
GPIO.setup (33,GPIO.IN,GPIO.PUD_DOWN)
GPIO.setup (35,GPIO.IN,GPIO.PUD_DOWN)
GPIO.setup (37,GPIO.IN,GPIO.PUD_DOWN)

def keypadCallback(channel):
    global keypadPressed
    if keypadPressed == -1:
        keypadPressed = channel
GPIO.add_event_detect(31, GPIO.RISING, callback = keypadCallback)
GPIO.add_event_detect(33, GPIO.RISING, callback = keypadCallback)
GPIO.add_event_detect(35, GPIO.RISING, callback = keypadCallback)
GPIO.add_event_detect(37, GPIO.RISING, callback = keypadCallback)


def setAllLines(state):
    GPIO.output(fila, state)

def checkSpecialKey():
    global input
    pressed = False
    
    GPIO.output(fila, GPIO.HIGH)
    
    
    
    if not pressed and (GPIO.input(33) == 1):
        if input == secretCode:
            print("code correct")
        else:
            print("Incorrect Code")
        pressed = True
    GPIO.output(fila, GPIO.LOW)
    
    if(GPIO.input(33) == 1):
        print("Input Reset")
        pressed = True
    GPIO.output(fila, GPIO.HIGH)
    
    if pressed:
        input = ""
    return pressed

def readLine(line):
    global input
    while True:
        GPIO.output(line,GPIO.HIGH)
        if GPIO.input(columnas[0])==1:
            input = "1"
            print(input)
            break
        if GPIO.input(columnas[1])==1:
            input = "2"
            print(input)
            break
        if GPIO.input(columnas[2])==1:
            input = "3"
            print(input)
            break
        if GPIO.input(columnas[3])==1:
            input ="4"
            print(input)
            break
    return(input)
    GPIO.output(line,GPIO.LOW)