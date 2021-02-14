'''
Created on 22 nov. 2020

@author: Lidia Parral
'''


#Ejercicio2
print("Escribe un programa en Python que cree una lista NO protegida llamada mares1")
mares1 = ['mediterraneo','cantabrico','baltico','adriatico','tirreno','egeo']
print(mares1)
print(type(mares1))

print("Crea otra lista llamada mares2 con 6 posiciones")
mares2 = ['rojo','muerto','caspio','negro','arabigo','sulu']
print(mares2)
print(type(mares2))

print("Se creara tambien una lista nueva llamada mares")
mares = mares1 + mares2
print(mares)
print(type(mares))

#Cambia a la vez los valores de los elementos undecimo y duodecimo de la lista mares por los
#valores 'del norte' y 'alboran'
print("Cambia a la vez los valores de los elementos undecimo y duodecimo de la lista mares por los valores del norte y alboran")
print(mares[11])
mares[11] = "del norte"
print(mares)

mares.append("alboran")
print(mares[12])

#Comprueba el cambio del valor de dichos elementos
print("Comprueba el cambio del valor de dichos elementos")
print(mares)

print()
#Inserta en la lista mares una posicion mas con el valor 'baltico'
print("Inserta en la lista mares una posicion mas con el valor 'baltico'")
mares.append("baltico")
print(mares)

print()
#Borra el quinto elemento de la lista mares
print("Borra el quinto elemento de la lista mares")
print(mares[5])
del mares[5]

#Comprueba el cambio realizado
print("Comprueba el cambio realizado")
print(mares)

print()
#Muestra la longitud de la lista mares
print("Muestra la longitud de la lista mares")
print(len(mares))


print()
#*Cuenta los valores repetidos en la lista mares
print("Cuenta los valores repetidos en la lista mares")
mares.sort()
print(mares)

for i in mares:
    if mares.count(i)>1:
        print(i,"está duplicado")
'''
print(mares[:])
mares = []
for i in mares:
    if mares.count(i)>1 and i not in mares:
        print(i, " está duplicado", mares.count(i), " veces")*/

'''

print()
#Elimina el elemento de la tercera posicion de la lista mares y guardalo en la variable mar1
print("Elimina el elemento de la tercera posicion de la lista mares y guardalo en la variable mar1")
mar1 = mares.pop(3)
print(mares)
print(mar1)

print()
#Elimina el ultimo elemento de la lista mares y guardalo en la variable mar2
print("Elimina el ultimo elemento de la lista mares y guardalo en la variable mar2")
mar2 = mares.pop()
print(mares)
print(mar2)

print()
#Guarda el valor de la novena posicion en la variable mar3
print("Guarda el valor de la novena posicion en la variable mar3")
print(mares[9])
mar3 = mares.pop(9)
print(mares)
print(mar3)

print()
#Muestra los valores de las variables mar1, mar2 y mar3
print("Muestra los valores de las variables mar1, mar2 y mar3")
print(mar1)
print(mar2)
print(mar3)

print()
#Elimina el primer elemento de la lista mares con valor 'baltico'
print("Elimina el primer elemento de la lista mares con valor 'baltico'")
#posicion de baltico
print(mares.index('baltico'))
del mares[3]
print(mares)

print()
#Elimina todos los elementos de la lista mares
print("Elimina todos los elementos de la lista mares")
print(mares.clear())
print(mares)

print()
#Ordena por orden alfabetico de 'a' a 'z' los elementos de la lista mares1
print("Ordena por orden alfabetico de 'a' a 'z' los elementos de la lista mares1")
mares1 = ['mediterraneo','cantabrico','baltico','adriatico','tirreno','egeo']
print(mares1)
mares1.sort()
print(mares1)

print()
#Ordena por orden alfabetico de 'z' a 'a' los elementos de la lista mares2
print("Ordena por orden alfabetico de 'z' a 'a' los elementos de la lista mares2")
mares2 = ['rojo','muerto','caspio','negro','arabigo','sulu']
print(mares2)
mares2.reverse()
print(mares2)



