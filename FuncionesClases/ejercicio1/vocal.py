'''
Created on 25 ene. 2021

@author: Lidia Parral
'''

'''
Escribe una función vocal(carácter) a la que se le pasa un carácter. La función devolverá True
si es una vocal; de lo contrario devolverá False.
'''

def vocal(letra):
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        return True
    else: 
        return False

letra = str(input("Introduzca un carácter: "))
caracter = vocal(letra)
if caracter == True:
    print("es vocal")
else: 
    print("no es vocal")

