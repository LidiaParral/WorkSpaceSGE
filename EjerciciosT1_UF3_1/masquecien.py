'''
Created on 23 nov. 2020

@author: Lidia Parral
'''

#Ejercicio5
#Escribe un programa en Python que pida al usuario dos numeros. Si la suma de ambos numeros es mayor que 100 se mostrara el mensaje: La suma supera la centena y es, suma.
#De lo contrario se mostrara el mensaje el resultado de la suma no supera la centena.
print("Escribe un programa en Python que pida al usuario dos numeros. Si la suma de ambos numeros es mayor que 100 se mostrara el mensaje:La suma supera la centena y es + suma.")
print("De lo contrario se mostrara el mensaje el resultado de la suma no supera la centena.")
num1 = int(input("Introduzca un numero:"))
num2 = int(input("Introduzca otro numero:"))

suma = num1 + num2
if suma > 100: 
    print("La suma supera la centena y es:", suma)
else:
    print("El resultado de la suma no supera la centena")