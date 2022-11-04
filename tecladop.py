import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

fila=13
GPIO.setup(13,GPIO.OUT)

columnas=[8,10,11,12]
GPIO.setup (8,GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup (10,GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup (11,GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup (12,GPIO.IN, GPIO.PUD_DOWN)

def lectura():
    GPIO.output(fila,GPIO.HIGH)
    if GPIO.input(columnas[0])==1:
        return 1
    if GPIO.input(columnas[1])==1:
        return 2
    if GPIO.input(columnas[2])==1:
        return 3
    if GPIO.input(columnas[3])==1:
        return 4
    GPIO.output(fila,GPIO.LOW)


# Path: main.py
# Compare this snippet from display.py:
# from rpi_lcd import LCD
# import time
# dis= LCD()
#
