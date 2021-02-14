

'''
Created on 12 ene. 2021

@author: Lidia Parral

Escribe una clase llamada Poligono() que genera objetos de polígono de 3 o más lados.
Al crear un objeto __init__() se indica el número de lados que va a tener y se crea una lista
que va a tener ese número de elementos cuyos valores iniciales serán 0.
La clase Poligono() tendrá un método llamado darlados() que le pedirá al usuario que
introduzca uno a uno los valores de todos los lados.
La clase Polígono() tendrá otro método llamado verlados() que mostrará uno a uno los
valores introducidos de todos los lados.
Se va a crear una clase llamada Triangulo() que hereda de la clase Poligono(). Al crear un objeto
triangulo, se invoca al constructor de la clase Poligono() al que se indica el número de lados = 3.
La clase Triangulo() tendrá un método area() que calcule y muestre el área del triángulo
(base*altura/2).
La clase Triangulo() tendrá un método perimetro() que calcule y muestre el perímetro del
triángulo (suma de sus lados).
Crea dos objetos de la clase Triangulo() y muestra el resultado de ejecutar todos los
métodos tanto de la clase Polígono() como de la clase Triangulo().



'''

#HERENCIA
class Poligono():
    '''
    #CONSTRUCTOR
    def __init__(self,l):
        self.l = l
        
    def darlados(self):
        l = input('Introduzca un lado:')
        return l
    
    def verlados(self):
        listLados = []
        return listLados
        
    '''  
#poligono = Poligono()
#print(poligono.darlados())
#print(poligono.verlados())

 
#HERENCIA SIMPLES
class Triangulo(Poligono):
   
    #CONSTRUCTOR
    def __init__(self, b, h, l):
        self.b = b
        self.h = h
        self.l = l
        
    def area(self):
        return (self.b * self.h) / 2
    
    def perimetro(self):
        return (self.b + self.h + self.l)
    
    
triangulo = Triangulo(20,10,5)

print("Área del triángulo: ", triangulo.area())
print("Perímetro del triángulo: ", triangulo.perimetro())

    