'''
Created on 12 ene. 2021

@author: Lidia Parral


Escribe una clase llamada Punto() que cree un punto con sus coordenadas x e y.
Al crear un objeto __init__() se indicarán dichos valores. Si no se indicaran dichos valores, el
punto se creará con x = 0 e y = 0. De tal forma que se podrían crear objetos de la forma
p1=Punto(2,5) o p2=Punto().
La clase Punto() tendrá un método llamado __str__() que permita imprimir o mostrar los
valores de los objetos creados (coordenadas de los puntos) como si se tratara de una cadena de
caracteres. Este método devolverá el valor x y el valor y del punto creado de la forma (x,y):
 return "({0},{1})".format(self.x,self.y)
Para probarlo, se haría: print(p1.__str__())
Este método hará lo mismo que harían las funciones ya creadas str(p1) o format(p1)
La clase Punto() tendrá un método llamado __suma__() que permita sumar los valores de dos
puntos, sumando los valores de x y los valores de y devolviendo un punto con valor (x1+x2, y1+y2)
Para probarlo, se haría: print(p1.__suma__(p2))
Este método hará lo mismo que print(p1 + p2) pero así no funciona. Para que print()
funcione, la función debería llamarse __add__() porque print la invoca internamente.
Cámbialo. Crea un tercer punto y prueba print (p1+p2+p3)
Crea tres puntos como mínimo para probar toda esta funcionalidad.



'''

class Punto():
    
    #CONSTRUCTOR
    def __init__(self,x,y):
        self.x = x
        self.y = y
     
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __suma__(self,p1,p2):
        x1 = p1.x
        y1 = p1.y
        x2 = p2.x
        y2 = p2.y
        return (x1 + x2) + (y1 +y2)
        

p1 = Punto(2,5)
p2 = Punto(1,3)
#str(p1)
format(p1)
print(p1.__str__())
print(format(p1))
format(p2)
print(p2.__str__())
print(format(p2))


#----------------------
#MÉTODOS
#print(p1.__suma__(p2))
#print(__add__()) 
#print(p1 + p2)
#print(p1+p2+p3)

    