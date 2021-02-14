'''
Created on 23 nov. 2020

@author: Lidia Parral
'''

#Ejercicio6
#Escribe un programa en Python que convierta la temperatura dada en grados Fahrenheit, en grados Celsius y viceversa
print("Escribe un programa en Python que convierta la temperatura dada en grados Fahrenheit, en grados Celsius y viceversa")
fahrenheit = int(input('Introduzca una temperatura en grados Fahrenheit: '))

celsius = (fahrenheit - 32) * 5.0/9.0
print('{} grados Fahrenheit son {} grados Celsius '.format(fahrenheit, celsius))
print()

celsius = int(input('Introduzca la temperatura en grados Celsius: '))
fahrenheit = 9.0/5.0 * celsius + 32
print('{} grados Celsius son {} grados Fahrenheit'.format(fahrenheit, celsius))