'''
Created on 23 nov. 2020

@author: Lidia Parral
'''
from random import randrange

#Modifica el programa anterior para que se haga un seguimiento de cuántas veces ha introducido
#un número erróneo el usuario hasta dar con el número correcto. Una vez descubierto, si el
#número de veces es mayor que 3 se mostrará el mensaje: 'Ha debido ser muy complicado para
#ti'. En otros casos, se mostrará el mensaje: 'Buen Trabajo!'
numAlea = randrange(10);
num = int(input("Introduzca un numero del 1 al 10:"))
contador = 0;

while(numAlea != num):

    if num > numAlea:
        print("El número a averiguar es menor que", num)
        contador =+ 1;
    elif num < numAlea:
        print("El número a averiguar es mayor que", num)
        contador =+ 1;
    print()
    num = int(input("Introduzca un numero del 1 al 10:")) 
        
print("Has acertado el número a averiguar.")
if contador <= 3:
    print('¡¡Buen Trabajo!!')
else:
    print('Ha debido ser muy complicado para ti')
        
              
        