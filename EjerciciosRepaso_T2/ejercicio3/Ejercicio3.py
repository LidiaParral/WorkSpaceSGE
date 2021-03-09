'''
Created on 8 mar. 2021

@author: Lidia Parral

Escribir una función que reciba un número entero positivo y devuelva su factorial.

'''

def factorial(num):
    n = 1
    for i in range(num):
        n *= i +1
    return n
print(factorial(24))
print(factorial(5))
print(factorial(9))
