'''
Created on 12 ene. 2021

@author: Lidia Parral


Escribe una función funcionLista(función, lista) que reciba otra función y una lista, y
devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos de la
lista. Por ejemplo, la función que se le pasa calcula el cubo de un número. La lista que se pasa es
una lista de números enteros. A cada número de la lista se le aplica la función y se calculará el
cubo de todos ellos, mostrándolos en otra lista nueva. Si la lista que se pasara fuera [1,2,3,4,5] la
función devolvería [1,8,27,64,125]


'''

def funcionLista(funcion, lista):
    listaNum = []
    for i in lista:
        listaNum.append(funcion(i))
    return listaNum

def cubo(n):
    return n * n * n

print(funcionLista(cubo, [1,2,3,4,5]))