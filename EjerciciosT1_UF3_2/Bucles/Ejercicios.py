'''
Created on 25 nov. 2020

@author: Lidia Parral
'''


#Ejercicio1
#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
palabra = str(input('Introduzca una palabra:\n'))
for i in range(10):
    print(palabra)
    
print()


#Ejercicio 2
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
edad = int(input('Introduzca su edad:\n'))
for i in range(edad):
    print('Has cumplido', i + 1,' años.')
    
print()


#Ejercicio 3
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
num = int(input('Introduzca un número:\n'))
if num > 0:
    for i in range(1,num+1,2):
        print(i, end=',')
else:
    print('ERROR')

print()



#Ejercicio 4
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
num = int(input('Introduzca un número:\n'))
if num > 0:
    for i in range(num,-1,-1):
        print(i, end=',')
else:
    print('ERROR')
    
print()



#Ejercicio 5
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
cantidad = float(input('¿Cantidad a invertir?'))
interes = float(input('¿Interés anual?'))
años = int(input('Introduzca los años:'))

for i in range(años):
    cantidad *= (1 + interes)/ 100
    print("Capital tras",str(i+1)," años: ",cantidad)


print()



#Ejercicio 6
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
num = int(input('Introduce la altura del triángulo:'))
if num > 0:
    for i in range(num):
        for j in range(i+1):
            print('*', end='')
        print()

print()



#Ejercicio 7
#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
for i in range(1,11):
    for j in range(1,11):
        print(i*j, end ='\t')
    print()


print()



#Ejercicio 8
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
num = int(input('Introduce la altura del triángulo:'))

for i in range(1,num+1,2):
    for j in range(i,0,-2):
        print(j, end='')
    print()

print()




#Ejercicio 9
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
cont = '1234'
contraseña = str(input('Introduzca la contraseña:\n'))
while(contraseña != cont):
    print('Contraseña incorrecta')
    contraseña = str(input('Introduzca la contraseña:\n'))
    
print('Contraseña correcta')


print()


#Ejercicio 10
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
num = int(input('Introduzca un número mayor que 2:'))
i = 2
while(num%i != 0):
    i+=1
if i == num:
    print(num,'es primo')  
else:
    print(num,'no es primo') 


print()




#Ejercicio 11
#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
palabra = input('Introduzca una palabra:\n')
for caracter in palabra[::-1]:
    print(caracter)


print()




#Ejercicio 12
#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
frase = str(input('Introduzca una frase:'))
letra = str(input('Introduzca una letra que aparezca en la frase:'))
count = 0
for i in frase:
    if i == letra:
        count +=1
print("la letra",letra,"se repite",count,"veces.")

print()



#Ejercicio 13
#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
palabras = str(input('Introduzca una palabra:'))
print(palabras)
while(palabras != 'salir'):
    palabras = str(input('Introduzca una palabra:'))
    print(palabras)
  
print()







