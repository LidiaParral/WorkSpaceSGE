'''
Created on 23 feb. 2021

@author: Lidia Parral
'''

''''

#
import tkinter
from tkinter import *
ventana = tkinter.Tk()

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


'''

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








