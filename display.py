import lcddriver
import time
import tecladop as Tl

dis= lcddriver.lcd()

def display(Tl):
  if Tl.lectura=="1":
    dis.lcd_display_string("se pulso numero 1",1)
    time.sleep(4)
  if Tl.lectura=="2":
    dis.lcd_display_string("se pulso numero 2",1)
    time.sleep(4)
  if Tl.lectura=="3":
    dis.lcd_display_string("se pulso numero 3",1)
    time.sleep(4)
  if Tl.lectura=="4":
    dis.lcd_display_string("se pulso numero 4",1)
    time.sleep(4)
