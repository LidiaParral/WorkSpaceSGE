#Ejercicio1
print("Escribe un programa en Python que cree una lista NO protegida llamada mares1")
mares1 = ['mediterraneo','cantabrico','baltico','adriatico','tirreno','egeo']
print(mares1)
print(type(mares1))

print()
print("Crea otra lista llamada mares2 con 6 posiciones")
mares2 = ['rojo','muerto','caspio','negro','arabigo','sulu']
print(mares2)
print(type(mares2))

print()
print("Se creara tambien una lista nueva llamada mares")
mares = mares1 + mares2
print(mares)
print(type(mares))

print()
#Longitud de la lista mares1
print("Longitud de la lista mares1")
print(len(mares1))

print()
#Valores de todas las posiciones de la lista mares1
print("Valores de todas las posiciones de la lista mares1")
print(mares1[:])

print()
#Longitud de la lista mares2
print("Longitud de la lista mares2")
print(len(mares2))

print()
#Valores de todas las posiciones de la lista mares2
print("Valores de todas las posiciones de la lista mares2")
print(mares2[:])

print()
#Longitud de la lista mares
print("Longitud de la lista mares")
print(len(mares))

print()
#Los valores de las posiciones 1, 2 y 3 de mares 1
print("Los valores de las posiciones 1, 2 y 3 de mares 1")
print(mares1[1:4])

print()
#El indice o posicion del mar egeo en mares1
print("El indice o posicion del mar egeo en mares1")
print(mares1.index('egeo'))

print()
#Los valores de las posiciones 4, 5 y 6 de mares2
print("Los valores de las posiciones 4, 5 y 6 de mares2")
print(mares2[4:7])

print()
#El indice o posicion del mar caspio en mares2
print("El indice o posicion del mar caspio en mares2")
print(mares2.index('caspio'))

print()
#El indice o posicion del mar caspio en mares
print("El indice o posicion del mar caspio en mares")
print(mares.index('caspio'))




