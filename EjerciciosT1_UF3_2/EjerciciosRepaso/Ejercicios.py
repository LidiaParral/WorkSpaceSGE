'''
Created on 30 nov. 2020

@author: Lidia Parral

'''

#Ejercicio 1
#Crea una variable numérica y si está entre 0 y 10, muestra un mensaje indicándolo.
num = 2;
if(num > 0 and num < 10):
    print("El número está comprendido entre 0 y 10")
else:
    print("El número no está comprendido entre 0 y 10")
 

   
#Ejercicio 2
#Añade al ejercicio anterior el caso de que si la variable numérica está entre 11 y 20, muestre
#otro mensaje diferente y, además, que si está entre 21 y 30 muestre otro mensaje.
num = 45;
if(num > 0 and num < 10):
    print("El número está comprendido entre 0 y 10")
elif (num > 11 and num < 20):
    print("El número está comprendido entre 11 y 20")
elif (num > 21 and num < 30):
    print("El número está comprendido entre 21 y 30")
else:
    print("El número está fuera del rango")
    



#Ejercicio 3
#Muestra con un while los números del 1 al 100.
num = 0
while num < 100:
    num += 1
    print(num)
    


#Ejercicio 4
# Muestra con un for los números del 1 al 100
for i in range(1,101):
    print(i)
    


#Ejercicio 5
#Muestra los caracteres de la cadena “Hola Mundo Python”.
frase = 'Hola Mundo Python'
indice = 0
while indice < len(frase):
    letra = frase[indice]
    print(letra)
    indice += 1




#Ejercicio 6
#Muestra los números pares entre 1 al 100
for i in range(1,101):
    if(i%2 == 0):
        print(i)




#Ejercicio 7
#Muestra tanto el elemento como el índice sobre el que estás iterando. Hazlo sobre el texto
#“Hola” y utiliza enumerate
frase = 'Hola'
for i in enumerate(frase):
    print(i)
    


#Ejercicio 8
#Muestra los caracteres de “hola” en horizontal

frase = 'Hola'
indice = 0
while indice < len(frase):
    letra = frase[indice]
    print(letra, end = " ")
    indice += 1



#Ejercicio 9
#Se da la siguiente lista a=[7, 14, 21, 0, 6, 8]. Muestra los valores de la lista y si un elemento
#vale 0, que no imprima el resto de valores.
a = [7,14,21,0,6,8]
if (a.__contains__(0)):
    print(a[:3])
else:
    print(a)
    


#Ejercicio 10
#Se da la siguiente lista a=[7, 14, 21, 0, 6, 8]. Muestra los valores de la lista y si un elemento
#vale 0, éste no se imprime pero sí el resto de valores
a = [7,14,21,0,6,8]
if (a.__contains__(0)):
    a.pop(3)
    print(a)
else:
    print(a)
    


#Ejercicip 11
#Construye una lista que contenga valores dentro del rango de 3 a 9.
lista = list(range(3,10))
print(lista)



#Ejercicio 12
#Construye una lista que contenga valores dentro del rango de 1 a 21 dando saltos de 5 en 5.
lista = list(range(1,22,5))
#El último valor del RANGE indica de cuanto en cuanto se quiere imprimir el valor
print(lista)



#Ejercicio 13
#Construye una lista que tenga 10 elementos usando range
lista = list(range(11))
print(lista)



#Ejercicio 14
#Calcula e imprime la suma de todos los números desde el 1 hasta el 100 ambos incluidos.
suma = 0
num = 1
while num <= 100:
    suma += num
    num += 1
    print(suma)
    

#Ejercicio 15
#Introduce un número por teclado y muestra si es par o impar.
num = int(input('Introduzca un número:'))
if(num%2 == 0):
    print("El número es par")
else:
    print("El número es impar")
    


#Ejercicio 16
#Muestra los números del 1 al 100 y calcula la suma de todos los números pares por un lado,
#y la suma de los números impares por otro.
sumaPares = 0
sumaImpares = 0
num = 1
for num in range(100):
    if(num%2 == 0):
        sumaPares += num
        num += 1
    else :
        sumaImpares += num
        num += 1
        
print("La suma de los pares es",sumaPares)
print("La suma de los impares es", sumaImpares)




#Ejercicio 17
#Introduce dos números por teclado. Muestra los números que hay entre ellos comenzando
#por el más pequeño. Cuenta cuántos números hay y cuántos de ellos son pares. Calcula la
#suma de los números pares

num1 = int(input('Introduzca un número:'))
num2 = int(input('Introduzca un número:'))
suma = 0
count = 0
for i in range(num1,num2+1):
    print(i)
    if(i%2 == 0):
        suma += i
        count += 1
        
print("La suma de los pares es", suma)
print("Números pares hay", count)
lista = list(range(num1,num2+1))  
print("Cuantos números hay", len(lista))



#Ejercicio 18
#Muestra, suma y cuenta los números que hay entre 1 y un determinado número introducido
#por el teclado y que sean a la vez múltiplos de 2 y de 3.
num = int(input('Introduzca un número:'))
suma = 0
count = 0
for i in range(1,num+1):
    if(i%2 == 0 and i%3 == 0):
        suma += i
        count += 1
print("La suma es", suma)
print("Números hay", count)



#Ejercicio 19
#Introduce dos valores A y B. Si A>=B, calcula y muestra la suma 10+14+18+22+…+46+50.
#Si A/B<=30, calcula e imprime el valor de (A^2+B^2)
A = int(input("Introduce un número:"))
B = int(input("Introduce un número:"))
if(A>=B):
    lista = list(range(10,51))
    print(lista)
    print(sum(lista))
elif (A/B<=30):
    print((A**2+B**2))