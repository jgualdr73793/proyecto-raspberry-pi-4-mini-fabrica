from display import dis as dis
import time
from tecladop import x as Tl
def setup():
    dis.clear()
    dis.text("seleccione",1)
    dis.text("una opcion",2)
    time.sleep(1)
    dis.text("1 -ROJO",1)
    dis.text("2 -AZUL",2)
    time.sleep(1)
    dis.text("3 -AMARILLO",1)
    dis.text("4 -SALIR",2)
    time.sleep(1)
    dis.clear()

def loop():
    while True:
        if Tl()=="1":
            dis.clear()
            dis.text("ROJO",1)
            time.sleep(1)
            dis.clear()
        if Tl()=="2":
            dis.clear()
            dis.text("AZUL",1)
            time.sleep(1)
            dis.clear()
        if Tl()=="3":
            dis.clear()
            dis.text("AMARILLO",1)
            time.sleep(1)
            dis.clear()
        if Tl()=="4":
            dis.clear()
            dis.text("SALIR",1)
            time.sleep(1)
            dis.clear()
            break

if __name__=='__main__':
    setup()
    loop()
