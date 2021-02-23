'''
Created on 23 feb. 2021

@author: Lidia Parral
'''
from psycopg2._psycopg import cursor

''''

#
import tkinter
from tkinter import *
ventana = tkinter.Tk()

#Abrir la ventana
ventana.mainloop()


#

import tkinter
import time
from tkinter import messagebox

ventana = tkinter.Tk()
ventana.config(bg ='green')

#messagebox --> showinfo(), showwarning(), askquestion(), askyesno()
#skokcancel(), showerror(), askokcancel(), askyesnocancel(), askretrycancel()

messagebox.showinfo(message=time.localtime, title="Fecha y hora")
var = messagebox.askyesno("Pregunta", "¿Vas a venir a la fiesta?")
if var:
    print('Voy a la fiesta')
else:
    print('No voy a la fiesta')



#

import tkinter
from tkinter import *
#TOPLEVEL Es la ventana hija(BLUE) de la ventana padre(CORAL)

ventana = tkinter.Tk()
ventana.title("Primera ventana")
ventana.config(bg = 'coral')
ventana1 = tkinter.Toplevel(ventana)
ventana1.config(bg='blue')
ventana.mainloop()

#

import tkinter
from tkinter import *

ventana = tkinter.Tk()
ventana.title("Primera ventana")

#Tamaño X Y Posición X Y
#Ancho = 300, Alto = 300, (0,0)
ventana.geometry("300x300+0+0")

ventana1 = tkinter.Toplevel(ventana)
ventana1.title("Segunda Ventana")
#Ancho = 400, Alto = 500, (300,300)
ventana1.geometry("400x500+300+300")
#Transient no permite tener minimizar ni maximar en la ventana hija, solo se puede desde la ventana padre
ventana1.transient(ventana)
ventana.mainloop()




#CREACIÓN DE VENTANAS - LIMITAR TAMAÑO MÁXIMO

import tkinter
from tkinter import *

ventana = tkinter.Tk()
ventana.title("Primera ventana")
ventana.geometry("300x300+0+0")

#Ambas formas sirven
ventana.maxsize(400, 500)
#Colocar diferente los atributos height y width
ventana.maxsize(height=500, width=400)
ventana.mainloop()




#CREACIÓN DE VENTANAS - LIMITAR TAMAÑO MÍNIMO

import tkinter
from tkinter import *

ventana = tkinter.Tk()
ventana.title("Primera ventana")
ventana.geometry("200x200+0+0")

#Ambas formas sirve
#atributos ancho y alto
ventana.minsize(500,500)
#Colocar diferente los atributos alto y ancho
ventana.minsize(height=500, width=500)
ventana.mainloop()



#INDICAR REDIMENSIONAMIENTO

import tkinter
from tkinter import *

ventana = tkinter.Tk()
ventana.title("Primera ventana")
ventana.geometry("200x200+0+0")
#Se puede redimensionar el ancho y pero no el alto
ventana.resizable(True, False)
ventana.mainloop()

#


import tkinter
import time

ventana = tkinter.Tk()
ventana.title("Primera ventana")
ventana.geometry("200x200+0+0")

#Oculta la ventana
ventana.withdraw()
#Oculta la ventana durante 10 segundos
time.sleep(10)
#Muestra la ventana
ventana.deiconify()

ventana.mainloop()




#INTRODUCIÓN DE ETIQUETAS
import tkinter
from tkinter import *

ventana = tkinter.Tk()
ventana.title("Prueba de etiquetas")
ventana.geometry("400x200")

etiqueta=tkinter.Label(ventana,text='Primera Etiqueta').pack()
#Se empaquetan los objetos unos debajos de otros, etiqueta centrada en el eje vertical
#etiqueta.pack(), con colocar este método al final se empaquetarían todos.
etiqueta=tkinter.Label(ventana,text='Segunda Etiqueta')
etiqueta.pack()

ventana.mainloop()


'''

#

import tkinter
from tkinter import *

ventana = tkinter.Tk()
ventana.title("Prueba de etiquetas")
ventana.geometry("400x200")

etiqueta=tkinter.Label(ventana,text='Hola Mundo Python',borderwidth=15, bg='cyan').pack()
etiqueta2=tkinter.Label(ventana,text='DAM',borderwidth=15, bg='coral')
#etiqueta2=tkinter.Label(ventana,text='DAM',bd=15, bg='coral').pack()
etiqueta2.pack()

etiqueta2 = tkinter.Label(ventana,text='¿Qué tal?', cursor="hand1").pack() 
#Mano negra
etiqueta3 = tkinter.Label(ventana,text='¿Qué tal?', cursor="hand2").pack()
#Mano blanca
etiqueta4 = tkinter.Label(ventana,text='¿Qué tal?', cursor="dot").pack()
#Punto

ventana.mainloop()










