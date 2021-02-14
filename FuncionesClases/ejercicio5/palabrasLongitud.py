'''
Created on 12 ene. 2021

@author: Lidia Parral

Escribe una función palabrasLongitud(frase) que reciba una frase y devuelva un diccionario
con las palabras que contiene y su longitud. Por ejemplo, la función recibe la frase ‘Hola y adiós’
y devuelve un diccionario de la forma {‘Hola’:4, ‘y’:1, ‘adiós’:5}
'''

#MODIFICAR FUNCIÓN

def palabrasLongitud(frase):
    return{
        palabra:len(palabra) for palabra in frase.split()}

print(palabrasLongitud("Hola y adiós"))