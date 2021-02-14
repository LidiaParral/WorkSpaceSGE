'''
Created on 24 nov. 2020

@author: Lidia Parral
'''
from _ctypes_test import func
from _ast import Or



#DICCIONARIOS
contactos = {}
nombre = 'Lidia Parral'
numero = 664789523
#Asociar un número a un nombre
#Incluir ambas parejas de valores NUMERO Y NOMBRE a CONTACTOS
contactos[nombre] = numero

nombre = 'Albert Einstein'
numero = 698523120
contactos[nombre] = numero


print('El teléfono es:', contactos['Lidia Parral'])
#Donde aparece KEYS en esta caso es igual a NOMBRES.
print(contactos.keys())

print()
#Recorrer las claves y valores de CONTACTOS
#X = clave, Contactos[x] = valor
print("Recorrer las claves y valores de CONTACTOS")
for x in contactos:
    print('Nombre:',x,'Numero:',contactos[x])
#\t = TABULACIÓN


print()
#Este bucle deja el diccionario vacío
print("Diccionario vacío")
if nombre in contactos:
    del contactos[nombre]
    

for x in contactos:
    print('Nombre:',x,'Numero:',contactos[x])
    

print()

#Diccionario con unas claves y unos valores
diccionario = {'nombre': 'Carlos', 'edad': 22, 
               'cursos' : ['Python', 'Django', 'Javascript']}

#Imprimir los valores(CARLOS,22,PYTHON,DJANGO) de cada clave(NOMBRE,EDAD,CURSOS) de DICCIONARIO
print("Imprimir los valores(CARLOS,22,PYTHON,DJANGO) de cada clave(NOMBRE,EDAD,CURSOS) de DICCIONARIO")
print(diccionario['nombre'])
print(diccionario['edad'])
print(diccionario['cursos'])

#Imprimir los valores de cada posición de la clave CURSOS
print("Imprimir los valores de cada posición de la clave CURSOS")
print(diccionario['cursos'][0])
print(diccionario['cursos'][1])
print(diccionario['cursos'][2])

print()
#Mostrar los valores del DICCIONARIO, según cada clave relacionada con su valor.
#Las claves y sus valores correspondientes están separador por dos puntos(:)
print("Mostrar los valores del DICCIONARIO, según cada clave relacionada con su valor")
for key in diccionario:
    print(key, ":", diccionario[key])
    
print()

#Crear una clase diccionario = DICT
#Generar unas claves con valores. En esta caso la clave a : 1, b : 2, c : 3, d : 4
print("Crear una clase diccionario = DICT")
dic = dict(zip('abcd', [1,2,3,4]))
print(dict)
print(dic)
print()

print("Imprimir las claves:")
print(dic.keys())
print("Otra manera de imprimir las claves:")
keys = dic.keys()
print(keys)
print()

print("Imprimir las parejas(claves y valores):")
items = dic.items()
print(items)
print()

print("Imprimir los valores:")
print(dic.values())

#Imprimir el valor de la clave especificada.
print("Imprimir el valor de la clave especificada")
valor = dic.get('b')
print(valor)

print()
#Copiar un diccionario en otro diccionario nuevo
print("Copiar diccionarios")
dic1 = dic.copy()
print(dic1)
print()

#Eliminar el valor de la posición correspodiente a la clave pasada
print("Eliminar el valor de la clave pasada")
valor = dic.pop('b')
print(valor)
print(dic)
print()

#MÉTODO: setdefault
#Método que muestra el valor de la clave especificada.
print("Mostrar el valor de la clave 'a':")
valor = dic.setdefault('a')
print(valor)
print()

#Añadir un nuevo elemento con clave y valor al DICCIONARIO
print("Añadir elemento nuevo al DICCIONARIO:")
valor = dic.setdefault('e',5)
print(valor)
print(dic)

print()
#MÉTODO = fromKeys
#método que sirve para asignar el mismo valor, a todos las claves del diccionario.
print("Crear un diccionario que todas las claves tengan el mismo valor(1):")
dic = dict.fromkeys(['a','b','c','d'], 1)
print(dic)

print()
#Crear dos diccionarios
dic1 = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}
dic2 = {'c' : 6, 'b' : 5, 'e' : 9, 'f' : 10}
#Actualiza los valores de un diccionario con los valores de otro diccionario distinto
dic1.update(dic2)
print(dic1)

print()
#Método que cuando se le pasa un valor número lo convierte en el String correspondiente previamente definido.
def uno():
    return "Enero"
def dos():
    return "Febrero"
def tres():
    return "Marzo"
def cuatro():
    return "Abril"
def cinco():
    return "Mayo"
def seis():
    return "Junio"
def siete():
    return "Julio"
def ocho():
    return "Agosto"
def nueve():
    return "Septiembre"
def diez():
    return "Octubre"
def once():
    return "Noviembre"
def doce():
    return "Diciembre"

def numeros_a_meses(argumento):
    switcher = {
        1: uno(),
        2: dos(),
        3: tres(),
        4: cuatro(),
        5: cinco(),
        6: seis(),
        7: siete(),
        8: ocho(),
        9: nueve(),
        10: diez(),
        11: once(),
        12: doce()
    }

    func = switcher.get(argumento, lambda: "mes inválido")
    print(func)
#Imprimir el valor del valor númerico definido anteriormente    
numeros_a_meses(1)
print()
#Si ese valor número no está definido da ERROR
print("ERROR")
numeros_a_meses(13)

