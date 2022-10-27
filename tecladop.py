import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

fila=13
GPIO.setup(13,GPIO.OUT)

columnas=[8,10,11,12]
GPIO.setup (8,GPIO.IN, GPIO,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup (10,GPIO.IN, GPIO,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup (11,GPIO.IN, GPIO,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup (12,GPIO.IN, GPIO,pull_up_down=GPIO.PUD_DOWN)

def lectura(Filas,caracteres):
    GPIO.output(Filas,GPIO.HIGH)
    if (GPIO.input(columnas[0])==1):
        print (caracteres[0])
    elif (GPIO.input(columnas[1])==1):
        print (caracteres[1])
    elif (GPIO.input(columnas[2])==1):
        print (caracteres[2])
    elif (GPIO.input(columnas[3])==1):
        print (caracteres[3])
    GPIO.output(Filas,GPIO.LOW)

try:
    while True:
        lectura(fila,["1","2","3","4"])
        time.sleep(0,1)
except KeyboardInterrupt:
    print("\nEl programa termino")