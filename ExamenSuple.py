from tkinter import*
import pygame
from pygame.locals import*
def crear(nomArch):
    ##crear archivo B##
    archi=open(nomArch,'w')
    archi.close()

def leer():
    archi2=open('a.txt','r')
    linea= archi2.readline()

    print(linea)
    return linea
    archi2.close()
        
def aplicacion1():
    print("VOLUMEN DE UNA ESFERA")
    #root2=Tk()
    #vcl1=Label(root2,text="Ingrese el valor del radio")
    #entrada1= Entry(root2)
    #bc1=Button(root2, text="Calcular", command=calcularVolumenEsfera).pack()
    print("INGRESE EL RADIO DE LA ESFREA")
    radio=int(input())
    
    volumen=(4/3)*3.14*(pow(radio,3))
    print("La respuesta es: ")
    print(volumen)
    

    #entrada1.pack()

def aplicacion2():
    print("COPIAR CONTENIDO DE UN ARCHIVO a A UN ARCHIVO B")

    print("Ingrese el nombre del archivo al que quiere copiar el contenido del archivo a.txt")
    nomArch=input()
    crear(nomArch)
    es=leer()

    ##escribir en B##
    archi1=open(nomArch,'a')
    archi1.write(str(es))
    archi1.close()  

def aplicacion3():
    print("MOSTRAR EL NOMBRE EN PYGAME")
    pygame.init()
    pantalla=pygame.display.set_mode((500,500),0,32)
    pygame.display.set_caption("Aplicacion 3")
    relog=pygame.time.Clock()

    fuente=pygame.font.Font(None, 50)
    texto=fuente.render("Joel Mendoza",0,(255,255,255))

    while True:
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                exit()

        relog.tick(20)
        pantalla.blit(texto,(100,100))
        pygame.display.update()

def salir():
    exit()
    
root=Tk()
root.title("EXAMEN FINAL - JOEL MENDOZA")
root.geometry("300x300+0+0")
frame1= Frame(root)
frame1.pack()
frame1.place(x=100,y=50)


l1=Label(frame1,text="Aplicacion 1 ")
l1.pack(side="left")
b1=Button(frame1, text="1", command=aplicacion1)
b1.pack(side="right")

frame2= Frame(root)
frame2.pack()
frame2.place(x=100,y=100)

l2=Label(frame2,text="Aplicacion 2 ")
l2.pack(side="left")
b2=Button(frame2, text="2", command=aplicacion2)
b2.pack(side="right")

frame3= Frame(root)
frame3.pack()
frame3.place(x=100,y=150)

l3=Label(frame3,text="Aplicacion 3 ")
l3.pack(side="left")
b3=Button(frame3, text="3", command=aplicacion3)
b3.pack(side="right")

frame4= Frame(root)
frame4.pack()
frame4.place(x=100,y=200)

l4=Label(frame4,text="Salir ")
l4.pack(side="left")
b4=Button(frame4, text="X", command=salir)
b4.pack(side="right")


root.mainloop()
