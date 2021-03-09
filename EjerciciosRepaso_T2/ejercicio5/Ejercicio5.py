'''
Created on 8 mar. 2021

@author: Lidia Parral

Escribir una función que calcule el área de un círculo y
otra que calcule el volumen de un cilindro usando la primera función

'''

def areaCirculo(radio):
    pi = 3.1416
    return  pi*radio**2;

areaCirculo(10)
areaCirculo(5.2)

def volumenCilindro(radio, altura):
    return areaCirculo(radio)*altura

print(volumenCilindro(10, 20))
print(volumenCilindro(3, 5))