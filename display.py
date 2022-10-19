import lcddriver
import time
display=lcddriver.lcd()

try:
  while True:
    print("toy funcionando")
    display.lcd_display_string("linea uno",1)
    display.lcd_dislpay_string("linea dos",2)
    time.sleep(2)
    display.lcd_display_string("prueba de inciio al teclado")
    time.sleep(2)
    display.lcd_clear()
    time.sleep(2)
except KeyboardInterrupt:
  print("limpiando uwu")
  display.lcd.clear()