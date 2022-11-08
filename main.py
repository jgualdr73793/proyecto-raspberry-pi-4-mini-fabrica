<<<<<<< HEAD
from display import dis as dis
import time
import Menu as m
import teclado as Tl

n_canicas=0
n_colors=0
color=0
n_cajas=0


m.setup()
if Tl.readLine(29)=="1":
    dis.clear()
    dis.text("UNA CANICA",1)
    n_canicas=1
    time.sleep(1.5)
    dis.clear()
elif Tl.readLine(29)=="2":
    dis.clear()
    dis.text("DOS CANICAS",1)
    n_canicas=2
    time.sleep(1.5)
    dis.clear()
elif Tl.readLine(29)=="3":
    dis.clear()
    n_canicas=3
    dis.text("TRES CANICAS",1)
    time.sleep(1.5)
    dis.clear()
elif Tl.readLine(29)=="4":
    dis.clear()
    dis.text("SALIR",1)
    time.sleep(1.5)
    dis.clear()

if n_canicas!=1:
   
    m.setup_2()
    if Tl.readLine(29)=="1":
        dis.clear()
        dis.text("UN COLOR",1)
        n_colors=1
        time.sleep(1.5)
        dis.clear()
    elif Tl.readLine(29)=="2":
        dis.clear()
        dis.text("DOS COLORES",1)
        n_colors=2
        time.sleep(1.5)
        dis.clear()
    elif Tl.readLine(29)=="3":
        dis.clear()
        dis.text("TRES COLORES",1)
        n_colors=3
        time.sleep(1.5)
        dis.clear()
    elif Tl.readLine(29)=="4":
        dis.clear()
        dis.text("SALIR",1)
        time.sleep(1.5)
        dis.clear()
            
m.setup_3()
c=0
while (c<n_colors):
    
    if Tl.readLine(29)=="1":
        dis.clear()
        dis.text("AZUL",1)
        time.sleep(1.5)
        c=c+1
        color=1
        dis.clear()
    elif Tl.readLine(29)=="2":
        dis.clear()
        dis.text("AMARILLO",1)
        time.sleep(1.5)
        c=c+1
        color=2
        dis.clear()
    elif Tl.readLine(29)=="3":
        dis.clear()
        dis.text("ROJO",1)
        time.sleep(1.5)
        c=c+1
        color=3
        dis.clear()
    elif Tl.readLine(29)=="4":
        dis.clear()
        dis.text("SALIR",1)
        time.sleep(1.5)
        dis.clear()

if n_canicas!=1:
    
    m.setup_4()
    if Tl.readLine(29)=="1":
        dis.clear()
        n_cajas=1
        dis.text("UNA CAJA",1)
        time.sleep(1.5)
        dis.clear()
    elif Tl.readLine(29)=="2":
        dis.clear()
        n_cajas=2
        dis.text("DOS CAJAS",1)
        time.sleep(1.5)
        dis.clear()
    elif Tl.readLine(29)=="3":
        dis.clear()
        n_cajas=3
        dis.text("TRES CAJAS",1)
        time.sleep(1.5)
        dis.clear()
    elif Tl.readLine(29)=="4":
        dis.clear()
        dis.text("SALIR",1)
        time.sleep(1.5)
        dis.clear()
=======
import Menu
import Loop

>>>>>>> 62f7665495b664ade1e26a34cdc515c830d44f67
