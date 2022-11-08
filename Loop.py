from display import dis as dis
from tecladop import x as Tl
import time
def loop():
    while True:
        if Tl()=="1":
            dis.clear()
            dis.text("UNA CANICA",1)
            time.sleep(1)
            dis.clear()
        if Tl()=="2":
            dis.clear()
            dis.text("DOS CANICAS",1)
            time.sleep(1)
            dis.clear()
        if Tl()=="3":
            dis.clear()
            dis.text("TRES CANICAS",1)
            time.sleep(1)
            dis.clear()
        if Tl()=="4":
            dis.clear()
            dis.text("SALIR",1)
            time.sleep(1)
            dis.clear()
            break
def loop_2():
    while True:
        if Tl()=="1":
            dis.clear()
            dis.text("UNA CAJA",1)
            time.sleep(1)
            dis.clear()
        if Tl()=="2":
            dis.clear()
            dis.text("DOS CAJAS",1)
            time.sleep(1)
            dis.clear()
        if Tl()=="3":
            dis.clear()
            dis.text("TRES CAJAS",1)
            time.sleep(1)
            dis.clear()
        if Tl()=="4":
            dis.clear()
            dis.text("SALIR",1)
            time.sleep(1)
            dis.clear()
            break
def loop_3():
    while True:
        if Tl()=="1":
            dis.clear()
            dis.text("UN COLOR",1)
            time.sleep(1)
            dis.clear()
        if Tl()=="2":
            dis.clear()
            dis.text("DOS COLORES",1)
            time.sleep(1)
            dis.clear()
        if Tl()=="3":
            dis.clear()
            dis.text("TRES COLORES",1)
            time.sleep(1)
            dis.clear()
        if Tl()=="4":
            dis.clear()
            dis.text("SALIR",1)
            time.sleep(1)
            dis.clear()
            break
def loop_4():
    while True:
        if Tl()=="1":
            dis.clear()
            dis.text("AZUL",1)
            time.sleep(1)
            dis.clear()
        if Tl()=="2":
            dis.clear()
            dis.text("AMARILLO",1)
            time.sleep(1)
            dis.clear()
        if Tl()=="3":
            dis.clear()
            dis.text("ROJO",1)
            time.sleep(1)
            dis.clear()
        if Tl()=="4":
            dis.clear()
            dis.text("SALIR",1)
            time.sleep(1)
            dis.clear()
            break