from Tkinter import *
import pygame
from pygame.locals import *
import time
pygame.init()



#Es en esta funcion en la que definimos la ventana de Inicio 
def ocultar(ventana):ventana.withdraw()

def inicia():
    raiz.withdraw()
    pygame.mixer.music.load("sonido/iniciohistoria.mp3")
    pygame.mixer.music.play(1)
    Inicia = Toplevel()
    Inicia.geometry("700x570")
    Inicia.title("Historias")   
    imagen2=PhotoImage(file="imagen/episodio1.gif")
    bientext = Label(Inicia, image=imagen2)
    bientext.grid(row=1, column=2)
    opcion1 = Button(Inicia,text="Piensas Exigir tu regreso a la Tierra", fg='yellow', font='Arial', bg='BLUE',command=opcionA, width=70, height=5)
    opcion1.grid(row=0, column=2)
    opcion2 = Button(Inicia,text="Si quieres saber algo mas sobre los U-TY", fg='yellow', font='Arial', bg='BLUE',command=opcionB,width=70, height=5)
    opcion2.grid(row=2, column=2)
    
    Inicia.mainloop()
    

def dormir():
   # pygame.mixer.music.load("sonido/baby.mp3")
    #pygame.mixer.music.play(4)
    dor = Toplevel()
    dor.geometry("640x470")
    dor.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcion5.gif")
    bientext = Label(dor, image=imagen2)
    bientext.grid(row=1, column=2)
    opcion1 = Button(dor,text="A pesar de todo decides quitarte la banda", fg='yellow', font='Arial', bg='BLUE',command=dormir, width=70, height=5)
    opcion1.grid(row=0, column=2)
    opcion2 = Button(dor,text="Si prefieres dejartela puesta para ver que ocurre", fg='yellow', font='Arial', bg='BLUE',command=explorar,width=70, height=5)
    opcion2.grid(row=2, column=2)
    dor.mainloop()
    
def explorar():
    #pygame.mixer.music.load("sonido/baby.mp3")
    #pygame.mixer.music.play(4)
    explo = Toplevel()
    explo.geometry("550x350")
    explo.title("Historias")   
    imagen2=PhotoImage(file="imagen/OPCION8.gif")
    bientext = Label(explo, image=imagen2)
    bientext.grid(row=1, column=2)
    explo.mainloop()
    
def caePa():
    #pygame.mixer.music.load("sonido/baby.mp3")
    #pygame.mixer.music.play(4)
    cae = Toplevel()
    cae.geometry("610x360")
    cae.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcion50.gif")
    bientext = Label(cae, image=imagen2)
    bientext.grid(row=1, column=2)
    cae.mainloop()

def noCaePa():
    #pygame.mixer.music.load("sonido/baby.mp3")
    #pygame.mixer.music.play(4)
    nocae = Toplevel()
    nocae.geometry("610x360")
    nocae.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcion41.gif")
    bientext = Label(nocae, image=imagen2)
    bientext.grid(row=1, column=2)
    nocae.mainloop()
    
def ayudarUTY():
    #pygame.mixer.music.load("sonido/baby.mp3")
    #pygame.mixer.music.play(4)
    ayuda = Toplevel()
    ayuda.geometry("690x570")
    ayuda.title("Historias")   
    imagen2=PhotoImage(file="imagen/episodio3op(22).gif")
    bientext = Label(ayuda, image=imagen2)
    bientext.grid(row=1, column=2)
    opcion1 = Button(ayuda,text="Hablas con el Anciano", fg='yellow', font='Arial', bg='BLUE',command=dormir, width=70, height=5)
    opcion1.grid(row=0, column=2)
    opcion2 = Button(ayuda,text="Hablas con Kim Lee", fg='yellow', font='Arial', bg='BLUE',command=explorar,width=70, height=5)
    opcion2.grid(row=2, column=2)
    ayuda.mainloop()
    
def preguntarUTY():
    #pygame.mixer.music.load("sonido/baby.mp3")
    #pygame.mixer.music.play(4)
    pregunta = Toplevel()
    pregunta.geometry("640x570")
    pregunta.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcion25.gif")
    bientext = Label(pregunta, image=imagen2)
    bientext.grid(row=1, column=2)
    opcion1 = Button(pregunta,text="Cae dentro de la papelera", fg='yellow', font='Arial', bg='BLUE',command=caePa, width=70, height=5)
    opcion1.grid(row=0, column=2)
    opcion2 = Button(pregunta,text="Cae fuera de la papelera", fg='yellow', font='Arial', bg='BLUE',command=noCaePa,width=70, height=5)
    opcion2.grid(row=2, column=2)
    pregunta.mainloop()

def opcionA():  
    
    pygame.mixer.music.load("sonido/opcionA.mp3")
    pygame.mixer.music.play(1)
    opcia = Toplevel()
    opcia.geometry("640x570")
    opcia.title("Historias")   
    terminarAplicacion()
    imagen2=PhotoImage(file="imagen/opcio3.gif")
    bientext = Label(opcia, image=imagen2)
    bientext.grid(row=1, column=2)
    opcion1 = Button(opcia,text="Si quieres irte a dormir", fg='yellow', font='Arial', bg='BLUE',command=dormir, width=70, height=5)
    opcion1.grid(row=0, column=2)
    opcion2 = Button(opcia,text="Ir a explorar el lugar", fg='yellow', font='Arial', bg='BLUE',command=explorar,width=70, height=5)
    opcion2.grid(row=2, column=2)
    opcia.mainloop()
    
def terminarAplicacion():
    inicia.quit()
#En esta parte definimos la ventana de la siguiente parte de la historia
def opcionB():
    raiz.withdraw()
    #pygame.mixer.music.load("sonido/baby.mp3")
    #pygame.mixer.music.play(4)
    opcib = Toplevel()
    opcib.geometry("640x570")
    opcib.title("Historias")   
    imagen2=PhotoImage(file="imagen/2episodioop(4).gif")
    bientext = Label(opcib, image=imagen2)
    bientext.grid(row=1, column=2)
    opcion1 = Button(opcib,text="Si estas dispuesto a ayudar a los U-TY a encontrar Ultima", fg='yellow', font='Arial', bg='BLUE',command=ayudarUTY, width=70, height=5)
    opcion1.grid(row=0, column=2)
    opcion2 = Button(opcib,text="Si quieres preguntar a los U-TY como piensan llegar a Ultima pasando por la Tierra", fg='yellow', font='Arial', bg='BLUE',command=preguntarUTY,width=70, height=5)
    opcion2.grid(row=2, column=2)
    opcib.mainloop()
    
    
    
#Se crean y nombra la ventana prinsipal"raiz" (en algunos casos llamada root)"
raiz=Tk()
raiz.geometry("380x490")
raiz.title("Historias")

#creamos la variable del texto dentro de la ventana
imagen1=PhotoImage(file="imagen/PORTADA.gif")
bientext = Label(raiz, image=imagen1)

#lo colocamos dentro de "la grilla"
bientext.grid(row=1, column=2)

#Creamos el boton que invocara a la siguiente ventana 
inicio = Button(raiz, text="Inicia",height=2 ,command=inicia, width=30)
inicio.grid(row=1, column=2)

raiz.mainloop()

