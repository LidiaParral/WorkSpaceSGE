#!/usr/bin/env ptython
# 




'''
Created on 03-nov-2020

@author: Lidia Parral
'''

'''
#No es necesario ; al final de la sentencia
print("HOLA MUNDO PYTHON")
print('NUEVA PRUEBA')

#Se puede realizar una operacion dentro del print
print(5+9)
print(10-4)
print(11*3)
print(49/7)
print(5**3) 

#Comentario: se realiza con #
#Se puede concatenar varios tipos de variables en una misma sentencia
#separados por una coma(,).
print('LOS ALUMNOS DE CLASE SON:',8)
print('HOLA','ALUMNOS DE 2ªDAM')

#Multiplicar un número por una cadena
print(4*"HOY")

#En esta operacion el + no realiza la operación de sumar sino de concatenar
print(4*"HOY" + 2*'ES')
#Diferencia entre + y , . El + no deja separación entre la concatenacion y la , deja espacio entre uno y otro.
print(4*"HOY", 2*'ES')
#\n se utiliza para el salto de línea
print("primera Linea \n Segunda Linea")
#Si se colocan unas comillas dobles dentro de unas simples, a la hora de mostrarse
#aparecen las comillas dobles en la consola.
print('"Sí," dijo él')
#Se pueden colocar las comillas dobles dentro de otras comillas dobles que queremos que se muestren por pantalla
#En esta caso hay que colocar la contrabarra para que se puedan mostrar
print("\"Sí,\"dijo él")
'''
'''
#Utilizacion de variables
ancho = 20
altura = 10
print(ancho*altura)

tasa = 125/100
precio = 148.50
print(precio*tasa)

#Se puede concatenar una variable de tipo String con una de tipo Int
# y mostrarlas por pantalla, colocando previamente su separación mediante comas.
print("El valor de 2+2 es:",2+2)
print("El valor de 2*3:",2*3, "es mayor que el valor de 3*1:",3*1)

#Se colocan juntas las cadenas
print('AA' + 'BB' + 'CC')
#Se colocan separadas las cadenas
print('AA','BB','CC')

#Comparación de valores
#Indica que 1.8 no es igual a 5
print(1.8 == 5)
#Si 3,8 es igual a 8 y si 4 es igual a 2
#La coma separa la cadena. Si 8 es igual a 8 pero como 4 no es igual a 2
#se muestra un false
#Se tiene que cumplir las dos condiciones
print(3,8==8 and 4==2)
#Como no tiene que cumplirse ambas operaciones se puede mostrar y aparece true concatenado con el número 3
print(3,8==8 or 4==2)
print(7,'a' == ('a' or 'b'))


#Variables
num1 = 5
num2 = 4.3
num3 = 20.8
num4 =("HOLA")
num5 = '2DAM'
num6 = "de Alcobendas"
#Leer los valores por separado, ya que en la sentencia hay indicada una coma
print(num1,num2,num3,num4,num5, num6)

#Type: indica el tipo de dato que existe en la variable
print((type(num1))) #Int
print((type(num2))) #Float
print((type(num4))) #String
print((type(num5))) #String

#Método que convierte un tipo int en tipo String, el número se convierte en carácter
print(repr(num1))
#Otro forma de ver el mismo método
num7 = repr(num1)
print(type(num7))

#Método convertir un tipo String a tipo Int
var1 = '15'
print(type(var1)) #String
var2 = int(var1)
print(type(var2)) #Int

#Método convertir un tipo String a tipo Float
var3 = "25.9"
print(type(var3))
var4 = float(var3)
print(type(var4))

#ERROR: Si contiene caracteres raros no imprime el valor
var5 = '*tv66'
var6 = int(var5)
print(var6)


#Método que extrae un número de una cadena.También indica el tipo de dato que se extrae
v = eval('123')
print(v,type(v)) #Int

v = eval('84.72')
print(v,type(v)) #Float

#ERROR: 
v = eval('dam')
print(v,type(v))


#Listas:
v3 = eval("[2, 7, 5, 8]")
print(v3, type(v3))

#Lista protegida o tupla: significa que esta lista no se puede ni crear ni modificar una vez creada.
#Lista protegida se usan los paréntesis ()
mitupla = ("aa", 6, 'BB', 7.2, "aa", 3.89, 6, 'adios')
print(mitupla)
print(type(mitupla))


#Lista NO protegida: en la lista no protegida se usan los corchetes []
milista = ["aa", 6, 'BB', 7.2, "aa", 3.89, 6, 'adios']
print(milista)
print(type(milista))

#Método len = contador del número de elementos que hay en esta caso en la lista.
#milista = 8 elementos
print(len(milista)) #Función externa
print(milista.__len__()) #Método propio del objetos, en este caso de la lista


#Elegir los elementos de una lista desde una posición en concreto hasta otra
#No se muestra la posición 3, en esta caso, se muestra la posición anterior 2.
print(milista[1:3])
print(milista[0:5])
#Muestra toda la cadena
print(milista[:])
print(milista)

#Desde la posición 4 hasta el final
print(milista[4:])

#Desde el principio hasta la posición anterior a 4, que es 3
print(milista[:4])

#Mostrar un elemento de la lista en una posición en concreto, 1.
print(milista[1])


#Mostrar la posición en la que se encuentra el elemento en la lista
#INDEX: Indice la posición del elemento
print(milista.index('BB'))
print(mitupla.index('BB'))

#Mostrar el número de veces que se repite el elemento indicado dentro de la función COUNT.
#COUNT: contar el número de veces que se repite un elemento
print(milista.count(6))
print(mitupla.count(6))

#Crear una lista que muestra 10 elementos numéricos(lista protegida)
#RANGE = función que genera en esta caso 10 números.
listnum = list(range(10)) #Se muestra 9 números(0,1,2,3,4,5,6,7,8,9)
print(listnum)

#Crear una lista de 12 elementos números , con unas posiciones en concreto.
#Desde la posición 2 a la posición 11, anterior a la 12.
listnum1 = list(range(2,12)) #Se muestra 10 números(2,3,4,5,6,7,8,9,10,11)
print(listnum1)
listnum2 = list(range(3,7)) #Se muestra 4 números(3,4,5,6)
print(listnum2)


#Añadir un elemento al final de la lista con la función APPEND
#APPEND: añadir elementos al final de una lista
milista.append('trece')
print(milista)
#ERROR: con las tuplas no funciona el método APPEND
#mitupla.append('trece')
#print(mitupla)
#Insertar el elemento CORAZÓN en la posición 1
#INSERT: Añadir en la lista un elemento nuevo, en una posición indicada. Desplaza todos los demás valores a la derecha
#*Esta función no sirve para utilizar en las tuplas.
milista.insert(1, 'CORAZÓN')
print(milista)

#POP: Permite sacar un elemento de la lista y almacenarlo en una variable
#Extraer el último elemento de la lista, cuando entre paréntesis no se indica la posición. Luego poder guardarlo en una variable 
mivar = milista.pop()
print(milista) #Se muestra la lista sin el último elemento, que se acaba de extraer en una variable externa.
print(mivar) #Se muestra trece
mivar1 = milista.pop(1)
print(milista) #Se muestra la lista sin el elemento de la posición 1
print(mivar1) #Se muestra corazón

#DEL: Eliminar el elemento para siempre
#Eliminar el elemento de la posición 4, 'aa'
del milista[4]
print(milista)

#Elimina todos los elementos de la lista = lista vacía
print(milista.clear())
milista.clear()
#LISTA VACÍA
print(milista)

milista = ["aa", 6, 'BB', 7.2, "aa", 3.89, 6, 'adios']
print(milista)
#Cambiar los valores de la posición 1 y 2, posición anterior a la final que es 3
milista[1:3] = [66, 'CC']
print(milista)

#Ordenador los elementos desde el menor al mayor, con la función SORT
milista1 = [1,5,8,7,3,2,0,4]
milista1.sort() #Se muestra [0,1,2,3,4,5,7,8] 
print(milista1)
#Ordenador los elementos de mayor a menor, con la función REVERSE
milista1.reverse() #Se muestra [8,7,5,4,3,2,1,0]
print(milista1)

lista = [1,3,5,7]
lista1 = [20,40,60,80]

#Copia de una lista
lista2 = lista.copy()
print(lista2)

#Extensión de una lista
lista.extend(lista1)
print(lista)


#PILA O COLA LIFO
stack = [1,2,3,4]
print(stack)
#Añadir elementos a la lista, elementos: 5,6,7
stack.append(5)
print(stack)
stack.append(6)
print(stack)
stack.append(7)
print(stack)
#Eliminar los elementos: 5,6,7
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)


#BUCLES
a = 0

#WHILE
#Siempre en los bucles hay que poner tabulación después de los :
while a < 10 : #Los dos puntos, tienen el mismo significado que las llaves {}
    a = a + 1
    print(a)  
print('WHILE') 
#Se muestra una serie de números desde el 1 hasta el 10

año = 2001
while año <= 2012 :
    print("Informes del año",str(año))
    año += 1
#Se muestra una lista concatenada con el STRING más el AÑO, que va desde el 2001 al 2012


#Pedir dos números al usuario
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
#Sumar los dos números
suma = num1 + num2
#Comprobar si la suma es menor que 10 (n<10)
if suma < 10 :
    print(suma)
    print("La suma de los números es menor a 10")
    

while True: 
    nombre = str(input("Introduce tu nombre: "))
    print(nombre)
    if nombre :
        break
print() #Linea en blanco

#Dos maneras distintas
fin_prog = ""
while fin_prog != "s"  and fin_prog != "S":
    print("Estás dentro del WHILE")
    fin_prog=input("Pulsa la letra s para salir: ")

fin_prog = ""
while fin_prog != ("s"  and "S"):
    print("Estás dentro del WHILE")
    fin_prog=input("Pulsa la letra s para salir: ")

print()

#IF
#Si le pongo cualquier valor a semaforo diferente a verde, se mostrará el mensaje de espera
#mientras que si se le coloca el valor = verde, se mostrará el mensaje de cruza.
semaforo = "rojo" 
if semaforo == "verde" :
    print("cruza")
else:
    print("espera")
print()

#VALOR ABSOLUTO
#Calcular el valor absoluto de un número
n=-10
if n < 0 :
    print("El valor absoluto de",n, " es ",-n)
else:
    print("El valor absoluto de" ,n, " es ",n)

print()

#COMPARACION DE NUMEROS INTRODUCIDOS POR TECLADO
num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce un número: "))

if num1 < num2 :
    print("El número ", num1, " es menor que el número ", num2)
elif num1 > num2 :
    print("El número ", num1, " es mayor que el número ", num2)
else:
    print("Los números ", num1, " y " , num2, " son iguales")

print()    

print(10==10) #TRUE
print(10==5) #FALSE

print()


if 'clavel' in lista:
    print('clavel está en la lista')
else:
    print('clavel no está en la lista')

#Si el elemento no está se puede incluir en la lista, con el método APPEND
if 'gardenia' not in lista:
    lista.append('gardenia')

print(lista)
print()

#Extraer los elementos y mostrarlos en diferentes lineas.
lista = ['geranio','clavel','tupilán','rosa','margarita']
#i = es el indice que indica la posición de cada elemento.
for i in lista:
    print(i)
#k = es el indice de la posición de cada elemento
#x = es el valor de cada elemento de la lista
for k, x, in enumerate(lista):
    print("lista[", k, "] = ", x)
print()
#Muestra las posiciones de los elementos de la lista
for e in range(1,3):
    print(e)
#Muestra el valor de las posiciones indicadas de la lista
#clavel y tulipán
for i in range(1,3):
    print(lista[i])
print()
#Mostrar todos los elementos de la lista
for i in range(len(lista)):
    print(lista[i])
print()
#Mostrar los elementos desde la posición 2(incluida) hasta el final
for i in range(2,len(lista)):
    print(lista[i])
print()
#Mostrar las posiciones desde el principio hasta dos posiciones antes del final,
# es decir, 0,1,2
for i in range(len(lista)-2):
    print(lista[i])
    
print()



#Sumar todos los números que hay dentro de la lista
listnum = [2,5,8,10,3,7,20,1]
print(sum(listnum))

#Otra manera
suma = 0
for num in listnum :
    suma = suma + num
#*PRINT : sin tabular, ya que si se tabula se incluye dentro del FOR
print("La suma total de los números es ",suma)

#Ampliar los valores de una lista ya obtenida anteriormente, con los elementos de una lista nueva
listnum1 = [8,20,5,8]
listnum.extend(listnum1)
print(listnum)

print()
#Contar el número de veces que se repiten los números que son iguales de la cadena
#Ordenar la lista
listnum.sort()

num = None #NONE es igual NULL
print(listnum)



#*TERMINAR
for i in listnum:
    if num == i :
        print("Hay un duplicado del número", num)
    num = i 
    
    
print()
#Otra manera de contar los elementos repetidos de una lista
cuenta1 = collections.Counter(listnum)
print(cuenta1)
print()

#Otra manera
for i,v in cuenta1.items():
    if v == 1 :
        print("Número",i, " se repite ", v, "vez")
    else :
        print("Número",i, " se repite ", v, "veces")
print()
#MATRICES
#Crear una lista vacía. Después añadir los elementos con un bucle FOR.
#En este caso, se añade una serie de elementos(10) con el valor(1)
miarray = []
for i in range(10):
    miarray.append(1)
    print(miarray[i])
print(miarray)

#Lista que se generan los valores en ejecucción
#Generar una lista, incluyendo los valores en un bucle FOR.
#En este caso generando 12 elementos con el valor 0, y se cambia en la posición 1 por el valor 25
miarray2 = [0 for i in range(12)]
miarray2[1] = 25
print(miarray2)
print(miarray2[1:3])
print(miarray2[:3])

#Crear una lista, en la que se va a aumentando en 1 el valor. En la que el valor es igual al indice
miarray2 = [i for i in range(12)]
print(miarray2)

miarray2 = [i*i for i in range(12)]
print(miarray2)

#Array bidimensional
arraydim2 = [[1,3],[4,6]]
print(arraydim2)

#Extraer los elementos que compone una matriz
for i in range(len(arraydim2)):
    for j in range(len(arraydim2[i])):
        print("El valor de la posición es", arraydim2[i])
        
        
for fila in arraydim2:
    for elemento in fila:
        print("El valor de la posición es", elemento)
        

print()
#Crear una matriz 3x3 en la cual, los valores de x no pueden ser iguales a los valores de y
matriz = [ (x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
print(matriz)
print()

#Crear una matrices 3x3, con elementos dentro con un valor = 0
matriz1 = [[0 for j in range(3)] for i in range(3)]
print(matriz1)

matriz2 =[[i*j for j in range(3)] for i in range(3)]
print(matriz2)
print()

#Mostrar las columnas de una matriz(VERTICAL)
columna0 = [row[0] for row in matriz2]
print(columna0)
columna1 = [row[1] for row in matriz2]
print(columna1)
columna2 = [row[2] for row in matriz2]
print(columna2)

#Mostrar las columnas de manera HORIZONTAL
for i in matriz2:
    print(i,end = '')

print()
print()
#Generar lista de números del 0 al 9 de manera VERTICAL
for i in range(10):
    print(i)
#Generar lista de números del 0 al 9 de manera HORIZONTAL    
for i in range(10):
    print(i,end='')



matriz = [(x,y,x*y) for x in [1,2,3] for y in [3,1,4]]
print(matriz)
print(len(matriz))

print()

#Matriz de 3x3 = 9 Valores
matriz = [[i+j for i in range(3)] for j in range(3)]
print(matriz)
print(len(matriz))

#Columna 0 de la matriz (HORIZONTAL)
columna = [row[0] for row in matriz]
#Devuelve los valores de la columna en la posición 0 de la matriz
print(columna)

'''      