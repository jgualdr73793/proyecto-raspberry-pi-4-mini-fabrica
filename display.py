import RPi.GPIO as GPIO
import time

# Declaracion de pines

LCD_RS = 21#26 
LCD_E  = 20#24
LCD_D4 = 16#22
LCD_D5 = 12#18
LCD_D6 = 1#16
LCD_D7 = 7#12

bits_datos=[LCD_RS,LCD_E,LCD_D4,LCD_D5,LCD_D6,LCD_D7]

# Constantes del dispositivo

LCD_CHR = True    # Modo caracteres (Salida de caracteres)

LCD_CMD = False   # Modo comandos (Dar instrucciones)

LCD_CHARS = 16    # Caracteres por linea (16 max)

LINE_1 = 0x80 # Localizacion en memoria de 1ra linea en LCD 

LINE_2 = 0xC0 # Localizacion en memoria de 2da linea en LCD 



#Definicion de GPIO

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)  

for i in range (6): 

   GPIO.setup(bits_datos[i],GPIO.OUT)    

#GPIO.setup(LCD_RS, GPIO.OUT)  

#GPIO.setup(LCD_E, GPIO.OUT)

#GPIO.setup(LCD_D4, GPIO.OUT)

#GPIO.setup(LCD_D5, GPIO.OUT)

#GPIO.setup(LCD_D6, GPIO.OUT)

#GPIO.setup(LCD_D7, GPIO.OUT)



# Definicion del programa principal

def main():

 lcd_init()

 lcd_texto("DIGITE COLOR DE DSITRIBUCION ",LINE_1)


 time.sleep(3) # 3 segundos de delay

# Inicializa y limpia el display

def lcd_init():

 lcd_write(0x33,LCD_CMD) # Inicializar

 lcd_write(0x32,LCD_CMD) # Establecer en modo 4 bits

 lcd_write(0x06,LCD_CMD) # Direccion de movimiento del cursor

 lcd_write(0x0C,LCD_CMD) # Apagar el cursor

 lcd_write(0x28,LCD_CMD) # Pantalla de 2 lineas

 lcd_write(0x01,LCD_CMD) # Limpiar display

 time.sleep(0.0005)      # Delay entre comandos



def lcd_write(bits, mode):

 # Send byte to data pins

 # bits = data

 # mode = True for character

 # False for command



 GPIO.output(LCD_RS, mode) # RS



#High bits

 GPIO.output(LCD_D4, False)

 GPIO.output(LCD_D5, False)

 GPIO.output(LCD_D6, False)

 GPIO.output(LCD_D7, False)

 if bits&0x10==0x10:

   GPIO.output(LCD_D4, True)

 if bits&0x20==0x20:

   GPIO.output(LCD_D5, True)

 if bits&0x40==0x40:

   GPIO.output(LCD_D6, True)

 if bits&0x80==0x80:

   GPIO.output(LCD_D7, True)



# Alternar pin 'Habilitar'

 lcd_toggle_enable()



# Low bits

 GPIO.output(LCD_D4, False)

 GPIO.output(LCD_D5, False)

 GPIO.output(LCD_D6, False)

 GPIO.output(LCD_D7, False)

 if bits&0x01==0x01:

   GPIO.output(LCD_D4, True)

 if bits&0x02==0x02:

   GPIO.output(LCD_D5, True)

 if bits&0x04==0x04:

   GPIO.output(LCD_D6, True)

 if bits&0x08==0x08:

   GPIO.output(LCD_D7, True)



# Alternar pin 'Habilitar'

 lcd_toggle_enable()



def lcd_toggle_enable():

 time.sleep(0.0005)

 GPIO.output(LCD_E, True)

 time.sleep(0.0005)

 GPIO.output(LCD_E, False)

 time.sleep(0.0005)



def lcd_texto(message,line):

  #Enviar texto al dsplay

 message = message.ljust(LCD_CHARS," ")



 lcd_write(line, LCD_CMD)


 for i in range(LCD_CHARS):

   lcd_write(ord(message[i]),LCD_CHR)



if __name__ == '__main__':

  #Inicio del programa

 try:

   main()

 except KeyboardInterrupt:

   pass

 finally:

   lcd_write(0x01, LCD_CMD)

   lcd_texto("LAS UNIDADES HAN SIDO DISTRIBUJIDAS",LINE_1)

   lcd_texto("   :)   :D",LINE_2)

   GPIO.cleanup()