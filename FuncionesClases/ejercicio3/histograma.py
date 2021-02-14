'''
Created on 12 ene. 2021

@author: Lidia Parral


Crea una función llamada histograma(lista_números) a la que se le pasa una lista de números
enteros. Se mostrará un histograma cuyas columnas midan el valor de los números.
Por ejemplo: histograma([4, 9, 7]) debería imprimir lo siguiente:
'''
def histograma(datos):
    listado = list(datos)
    for i in listado:
        print("*" *int(i))

histograma([4,9,7])