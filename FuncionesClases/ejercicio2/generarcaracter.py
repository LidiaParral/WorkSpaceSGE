'''
Created on 25 ene. 2021

@author: Lidia Parral
'''
'''
Escribe una función generar_n_caracteres(n, carácter) a la que se le pasa un número
entero n y un carácter. Devolverá el carácter multiplicado por n. Por ejemplo:
generar_n_caracteres(5, "x") debería devolver "xxxxx". Tantas x como indique el número.
'''


def generar_n_caracteres(a,b):
    c = b
    for i in range(a):
        b = b + c
    return b


print(generar_n_caracteres(5, "*"))