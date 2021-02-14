'''
Created on 23 nov. 2020

@author: Lidia Parral
'''
from random import randrange
from _ast import If



#Ejercicio7
#Escribe un programa en Python que permita calcular el numero que esconde. El usuario debe averiguar que numero esconde el programa. 
#Se pide numeros al usuario y se le informara de si el numero es mas grande o mas pequenio que el numero a averiguar. Si lo acierta se le informara
#con el mensaje correspondiente.
numAlea = randrange(100);
num = int(input("Introduzca un numero del 1 al 100:"))

while(numAlea != num):

    if num > numAlea:
        print("El número a averiguar es menor que", num)
    elif num < numAlea:
        print("El número a averiguar es mayor que", num)
    print()
    num = int(input("Introduzca un numero del 1 al 100:")) 
        
print("Has acertado el número a averiguar.")        
        
        
        
        
        
        
        