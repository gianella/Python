from Tkinter import *
import pygame
from pygame.locals import *
import time
pygame.init()



#Es en esta funcion en la que definimos la ventana de Inicio 
def inicia():
    raiz.withdraw()
    pygame.mixer.music.load("sonido/iniciotodo.mp3")
    pygame.mixer.music.play()
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

def opcionA():  
    pygame.mixer.music.load("sonido/opciona.mp3")
    pygame.mixer.music.play()
    opcia = Toplevel()
    opcia.geometry("640x570")
    opcia.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcio3.gif")
    bientext = Label(opcia, image=imagen2)
    bientext.grid(row=1, column=2)
    opcion1 = Button(opcia,text="Si quieres irte a dormir", fg='yellow', font='Arial', bg='BLUE',command=dormir, width=70, height=5)
    opcion1.grid(row=0, column=2)
    opcion2 = Button(opcia,text="Ir a explorar el lugar", fg='yellow', font='Arial', bg='BLUE',command=explorar,width=70, height=5)
    opcion2.grid(row=2, column=2)
    opcia.mainloop()

def explorar():
    pygame.mixer.music.load("sonido/explora.mp3")
    pygame.mixer.music.play()
    explo = Toplevel()
    explo.geometry("650x570")
    explo.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcion10.gif")
    bientext = Label(explo, image=imagen2)
    bientext.grid(row=1, column=2)
    opcion1 = Button(explo,text="Si tomas el idolo", fg='yellow', font='Arial', bg='BLUE',command=idolo, width=70, height=5)
    opcion1.grid(row=0, column=2)
    opcion2 = Button(explo,text="Si lo dejas", fg='yellow', font='Arial', bg='BLUE',command=dejasIdolo,width=70, height=5)
    opcion2.grid(row=2, column=2)
    explo.mainloop()
    
def dejasIdolo():
    pygame.mixer.music.load("sonido/dejasidolo.mp3")
    pygame.mixer.music.play()
    explo = Toplevel()
    explo.geometry("650x570")
    explo.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcion18.gif")
    bientext = Label(explo, image=imagen2)
    bientext.grid(row=1, column=2)
    opcion1 = Button(explo,text="Si decides ir a la camara prohibida", fg='yellow', font='Arial', bg='BLUE',command=camarap, width=70, height=5)
    opcion1.grid(row=0, column=2)
    opcion2 = Button(explo,text="Si quieres buscar otro sistema para escapar", fg='yellow', font='Arial', bg='BLUE',command=otro,width=70, height=5)
    opcion2.grid(row=2, column=2)
    explo.mainloop()

def camarap():
    pygame.mixer.music.load("sonido/camaraprohibida.mp3")
    pygame.mixer.music.play()
    explo = Toplevel()
    explo.geometry("650x370")
    explo.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcion34.gif")
    bientext = Label(explo, image=imagen2)
    bientext.grid(row=1, column=2)
    explo.mainloop()

def otro():
    pygame.mixer.music.load("sonido/otrosistemaescapar.mp3")
    pygame.mixer.music.play()
    explo = Toplevel()
    explo.geometry("670x570")
    explo.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcion10.gif")
    bientext = Label(explo, image=imagen2)
    bientext.grid(row=1, column=2)
    explo.mainloop()  
     
def idolo():
    pygame.mixer.music.load("sonido/sitomaselidol.mp3")
    pygame.mixer.music.play()
    explo = Toplevel()
    explo.geometry("650x570")
    explo.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcion15.gif")
    bientext = Label(explo, image=imagen2)
    bientext.grid(row=1, column=2)
    opcion1 = Button(explo,text="Si Cumples lo prometido a INCU", fg='yellow', font='Arial', bg='BLUE',command=cumples, width=70, height=5)
    opcion1.grid(row=0, column=2)
    opcion2 = Button(explo,text="Si Decides despreocuparte de INCU ", fg='yellow', font='Arial', bg='BLUE',command=descopi,width=70, height=5)
    opcion2.grid(row=2, column=2)
    explo.mainloop()

def descopi():
    pygame.mixer.music.load("sonido/quetellevenalatierra.mp3")
    pygame.mixer.music.play()
    explo = Toplevel()
    explo.geometry("650x570")
    explo.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcion97.gif")
    bientext = Label(explo, image=imagen2)
    bientext.grid(row=1, column=2)
    opcion1 = Button(explo,text="Ordenas a los U-TY que se dirijan a Alara", fg='yellow', font='Arial', bg='BLUE',command=ordenasUTY, width=70, height=5)
    opcion1.grid(row=0, column=2)
    opcion2 = Button(explo,text="Si vas a dejar que la nave siga el rumbo a la tierra ", fg='yellow', font='Arial', bg='BLUE',command=rumboaTierra,width=70, height=5)
    opcion2.grid(row=2, column=2)
    explo.mainloop()

def ordenasUTY():
    pygame.mixer.music.load("sonido/alara.mp3")
    pygame.mixer.music.play()
    explo = Toplevel()
    explo.geometry("550x370")
    explo.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcion14.gif")
    bientext = Label(explo, image=imagen2)
    bientext.grid(row=1, column=2)
    explo.mainloop()

def rumboaTierra():
    pygame.mixer.music.load("sonido/rumboatierra.mp3")
    pygame.mixer.music.play()
    explo = Toplevel()
    explo.geometry("650x570")
    explo.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcion20.gif")
    bientext = Label(explo, image=imagen2)
    bientext.grid(row=1, column=2)
    opcion1 = Button(explo,text="Si dejas que el ordenador decida el aterrizaje en la isla de los dioses", fg='yellow', font='Arial', bg='BLUE',command=dejasO, width=70, height=5)
    opcion1.grid(row=0, column=2)
    opcion2 = Button(explo,text="Si insistes en aterrizar en los estados unidos ", fg='yellow', font='Arial', bg='BLUE',command=insiste,width=70, height=5)
    opcion2.grid(row=2, column=2)
    explo.mainloop()

def dejasO():
    pygame.mixer.music.load("sonido/isladelosdioses.mp3")
    pygame.mixer.music.play()
    explo = Toplevel()
    explo.geometry("550x370")
    explo.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcion14.gif")
    bientext = Label(explo, image=imagen2)
    bientext.grid(row=1, column=2)
    explo.mainloop()
    
def insiste():
    pygame.mixer.music.load("sonido/aterrizar.mp3")
    pygame.mixer.music.play()
    explo = Toplevel()
    explo.geometry("550x370")
    explo.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcion97.gif")
    bientext = Label(explo, image=imagen2)
    bientext.grid(row=1, column=2)
    explo.mainloop()
def nocumples():
    pygame.mixer.music.load("sonido/rumboatierra.mp3")
    pygame.mixer.music.play()
    dor = Toplevel()
    dor.geometry("670x570")
    dor.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcion10.gif")
    bientext = Label(dor, image=imagen2)
    bientext.grid(row=1, column=2)
    opcion1 = Button(dor,text="Si ordenas a los U-TY que se dirijan a Alara", fg='yellow', font='Arial', bg='BLUE',command=quitbanda, width=70, height=5)
    opcion1.grid(row=0, column=2)
    opcion2 = Button(dor,text="Si vas a dejar que la nave siga su rumbo a la Tierra", fg='yellow', font='Arial', bg='BLUE',command=dejarteBanda,width=70, height=5)
    opcion2.grid(row=2, column=2)
    dor.mainloop()

def cumples():
    pygame.mixer.music.load("sonido/prometidoaincu.mp3")
    pygame.mixer.music.play()
    dor = Toplevel()
    dor.geometry("670x370")
    dor.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcion27.gif")
    bientext = Label(dor, image=imagen2)
    bientext.grid(row=1, column=2)
    dor.mainloop()
    
def dormir():
    pygame.mixer.music.load("sonido/decidesdormirte.mp3")
    pygame.mixer.music.play()
    dor = Toplevel()
    dor.geometry("660x570")
    dor.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcion5.gif")
    bientext = Label(dor, image=imagen2)
    bientext.grid(row=1, column=2)
    opcion1 = Button(dor,text="A pesar de todo decides quitarte la banda", fg='yellow', font='Arial', bg='BLUE',command=quitbanda, width=70, height=5)
    opcion1.grid(row=0, column=2)
    opcion2 = Button(dor,text="Si prefieres dejartela puesta para ver que ocurre", fg='yellow', font='Arial', bg='BLUE',command=dejarteBanda,width=70, height=5)
    opcion2.grid(row=2, column=2)
    dor.mainloop()

def dejarteBanda():
    pygame.mixer.music.load("sonido/dejarsband.mp3")
    pygame.mixer.music.play()
    dor = Toplevel()
    dor.geometry("670x370")
    dor.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcion14.gif")
    bientext = Label(dor, image=imagen2)
    bientext.grid(row=1, column=2)
    dor.mainloop()
    
def quitbanda():
    pygame.mixer.music.load("sonido/quitartelabanda.mp3")
    pygame.mixer.music.play()
    dor = Toplevel()
    dor.geometry("670x570")
    dor.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcion11.gif")
    bientext = Label(dor, image=imagen2)
    bientext.grid(row=1, column=2)
    opcion1 = Button(dor,text="Si le dices a Mopo que puede fiarse de los Terricolas", fg='yellow', font='Arial', bg='BLUE',command=fiarseTerricolas, width=70, height=5)
    opcion1.grid(row=0, column=2)
    opcion2 = Button(dor,text="Si le dices a Mopo que no puedes garantizarle un trato digno", fg='yellow', font='Arial', bg='BLUE',command=noGarantizar,width=70, height=5)
    opcion2.grid(row=2, column=2)
    dor.mainloop()
    
def noGarantizar():
    pygame.mixer.music.load("sonido/nomopo.mp3")
    pygame.mixer.music.play()
    dor = Toplevel()
    dor.geometry("570x370")
    dor.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcion21.gif")
    bientext = Label(dor, image=imagen2)
    bientext.grid(row=1, column=2)
    dor.mainloop()

def fiarseTerricolas():
    pygame.mixer.music.load("sonido/fiarsedelosterricolas.mp3")
    pygame.mixer.music.play()
    dor = Toplevel()
    dor.geometry("640x570")
    dor.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcion20.gif")
    bientext = Label(dor, image=imagen2)
    bientext.grid(row=1, column=2)
    opcion1 = Button(dor,text="Si dices al capitan que informe al Guardia Costera", fg='yellow', font='Arial', bg='BLUE',command=informeGuardia, width=70, height=5)
    opcion1.grid(row=0, column=2)
    opcion2 = Button(dor,text="Si le propones que no diga nada hasta llegar a Seattle", fg='yellow', font='Arial', bg='BLUE',command=NoinformeGuardia,width=70, height=5)
    opcion2.grid(row=2, column=2)
    dor.mainloop()
    
def informeGuardia():
    pygame.mixer.music.load("sonido/fin.mp3")
    pygame.mixer.music.play()
    dor = Toplevel()
    dor.geometry("550x370")
    dor.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcion57.gif")
    bientext = Label(dor, image=imagen2)
    bientext.grid(row=1, column=2)
    dor.mainloop()
    
def NoinformeGuardia():
    pygame.mixer.music.load("sonido/nofin.mp3")
    pygame.mixer.music.play()
    dor = Toplevel()
    dor.geometry("550x370")
    dor.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcion58.gif")
    bientext = Label(dor, image=imagen2)
    bientext.grid(row=1, column=2)
    dor.mainloop()
    
#En esta parte definimos la ventana de la siguiente parte de la historia
def opcionB():
    raiz.withdraw()
    pygame.mixer.music.load("sonido/opcionb.mp3")
    pygame.mixer.music.play()
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
    
def ayudarUTY():
    pygame.mixer.music.load("sonido/dispuestoayudaruty.mp3")
    pygame.mixer.music.play()
    ayuda = Toplevel()
    ayuda.geometry("690x570")
    ayuda.title("Historias")   
    imagen2=PhotoImage(file="imagen/episodio3op(22).gif")
    bientext = Label(ayuda, image=imagen2)
    bientext.grid(row=1, column=2)
    opcion1 = Button(ayuda,text="Hablas con el Anciano", fg='yellow', font='Arial', bg='BLUE',command=anciano, width=70, height=5)
    opcion1.grid(row=0, column=2)
    opcion2 = Button(ayuda,text="Hablas con Kim Lee", fg='yellow', font='Arial', bg='BLUE',command=kim,width=70, height=5)
    opcion2.grid(row=2, column=2)
    ayuda.mainloop()
    
def kim():
    pygame.mixer.music.load("sonido/kim.mp3")
    pygame.mixer.music.play()
    ayuda = Toplevel()
    ayuda.geometry("640x370")
    ayuda.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcion41.gif")
    bientext = Label(ayuda, image=imagen2)
    bientext.grid(row=1, column=2)
    ayuda.mainloop()
    
def anciano():
    pygame.mixer.music.load("sonido/hablasconelanciano.mp3")
    pygame.mixer.music.play()
    ayuda = Toplevel()
    ayuda.geometry("670x570")
    ayuda.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcion37.gif")
    bientext = Label(ayuda, image=imagen2)
    bientext.grid(row=1, column=2)
    opcion1 = Button(ayuda,text="Si decides fingir locura", fg='yellow', font='Arial', bg='BLUE',command=locura, width=70, height=5)
    opcion1.grid(row=0, column=2)
    opcion2 = Button(ayuda,text="Si decides no hacer eso", fg='yellow', font='Arial', bg='BLUE',command=nohacereso,width=70, height=5)
    opcion2.grid(row=2, column=2)
    ayuda.mainloop()

def locura():
    pygame.mixer.music.load("sonido/fingirlocura.mp3")
    pygame.mixer.music.play()
    ayuda = Toplevel()
    ayuda.geometry("640x370")
    ayuda.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcion63.gif")
    bientext = Label(ayuda, image=imagen2)
    bientext.grid(row=1, column=2)
    ayuda.mainloop()

def nohacereso():
    pygame.mixer.music.load("sonido/nodebeshaceresto.mp3")
    pygame.mixer.music.play()
    ayuda = Toplevel()
    ayuda.geometry("670x570")
    ayuda.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcion16.gif")
    bientext = Label(ayuda, image=imagen2)
    bientext.grid(row=1, column=2)
    opcion1 = Button(ayuda,text="Si tratas de escapar con angus", fg='yellow', font='Arial', bg='BLUE',command=escaparangus, width=70, height=5)
    opcion1.grid(row=0, column=2)
    opcion2 = Button(ayuda,text="Si tratas de hallar otra solucion", fg='yellow', font='Arial', bg='BLUE',command=otrasolucion,width=70, height=5)
    opcion2.grid(row=2, column=2)
    ayuda.mainloop()

def escaparangus():
    pygame.mixer.music.load("sonido/tratasdeescaparte.mp3")
    pygame.mixer.music.play()
    ayuda = Toplevel()
    ayuda.geometry("570x370")
    ayuda.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcion41.gif")
    bientext = Label(ayuda, image=imagen2)
    bientext.grid(row=1, column=2)
    ayuda.mainloop()
    
    
def otrasolucion():
    pygame.mixer.music.load("sonido/oton.mp3")
    pygame.mixer.music.play()
    ayuda = Toplevel()
    ayuda.geometry("570x370")
    ayuda.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcion14.gif")
    bientext = Label(ayuda, image=imagen2)
    bientext.grid(row=1, column=2)
    ayuda.mainloop()
    


    


def preguntarUTY():
    pygame.mixer.music.load("sonido/preguntaralosuty.mp3")
    pygame.mixer.music.play(4)
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
    
    
def caePa():
    pygame.mixer.music.load("sonido/cayodentrodelcesto.mp3")
    pygame.mixer.music.play(4)
    cae = Toplevel()
    cae.geometry("610x360")
    cae.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcion50.gif")
    bientext = Label(cae, image=imagen2)
    bientext.grid(row=1, column=2)
    cae.mainloop()

def noCaePa():
    pygame.mixer.music.load("sonido/sinocayoenelcesto.mp3")
    pygame.mixer.music.play(4)
    nocae = Toplevel()
    nocae.geometry("610x360")
    nocae.title("Historias")   
    imagen2=PhotoImage(file="imagen/opcion41.gif")
    bientext = Label(nocae, image=imagen2)
    bientext.grid(row=1, column=2)
    nocae.mainloop()
    



    
    
    
#Se crean y nombra la ventana prinsipal"raiz" (en algunos casos llamada root)"
raiz=Tk()
raiz.geometry("380x490")
raiz.title("Historias")

#creamos la variable del texto dentro de la ventana
imagen1=PhotoImage(file="imagen/PORTADA.gif")
bientext = Label(raiz, image=imagen1)

pygame.mixer.music.load("sonido/suspenso.mp3")
pygame.mixer.music.play()
#lo colocamos dentro de "la grilla"
bientext.grid(row=1, column=2)

#Creamos el boton que invocara a la siguiente ventana 
inicio = Button(raiz, text="Inicia",height=2 ,command=inicia, width=30)
inicio.grid(row=1, column=2)

raiz.mainloop()

