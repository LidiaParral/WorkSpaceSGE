'''
Created on 23 nov. 2020

@author: Lidia Parral
'''

#Escribe un programa en Python que cree una lista con los cuadrados de todos los numeros
#enteros del 0 al 10.
print("Escribe un programa en Python que cree una lista con los cuadrados de todos los numeros enteros del 0 al 10")
miarray = []
i = 0
for i in range(11):
    miarray.append(i*i)
    print(miarray[i])
print(miarray)