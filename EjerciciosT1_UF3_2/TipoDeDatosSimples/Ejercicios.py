'''
Created on 25 nov. 2020

@author: Lidia Parral
'''

#Ejercicio1
#Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
print('Hola Mundo!')

print()
#Ejercicio2
#Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
saludo = 'Hola Mundo!'
print(saludo)

print()
#Ejercicio3
#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
nombre = str(input('Introduzca un nombre:'))
print('Hola', nombre)

print()

#Ejercicio4
#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
nombre = str(input('Introduzca un nombre:'))
numero = int(input('Números de veces para repetir el nombre:'))
print((nombre + '\n') * numero)

print()
#Ejercicio5
#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
nombre = str(input('Introduzca un nombre:'))
print(len(nombre))
print(nombre,'tiene', len(nombre), 'letras')

print()


#Ejercicio 6
#Escribir un programa que realice la siguiente operación aritmética (((3+2)/(2*5))^2)
print(((3+2)/(2*5))**2)

print()


#Ejercicio7
#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
horas = int(input('Introduzca el número de horas trabajadas:'))
coste = float(input('Introduzca el coste por hora:'))
print('La paga es', horas*coste, ' euros.')


print()

#Ejercicio 8
#Escribir un programa que lea un entero positivo, , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta . La suma de los  primeros enteros positivos puede ser calculada de la siguiente forma:
num = int(input('Introduzca un número:'))
suma = (num*(num+1))/2
print('La suma de los primeros números enteros desde 1 hasta',num,'es',suma)


print()

#Ejercicio 9
#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
kg = float(input('Introduzca su peso(kg):'))
m = float(input('Introduzca su estatura(m):'))
imc = kg/m**2
print('Tu índice de masa corporal es', imc)

print()


#Ejercicio 10
#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
n = int(input('Introduzca un número(dividendo):'))
m = int(input('Introduzca otro número(divisor):'))
print(n,'entre',m,'da un cociente',(n//m),'y un resto',(n%m))

print()

#Ejercicio 11
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
cantidad = float(input('¿Cantidad a invertir?'))
interes = float(input('¿Interés anual?'))
años = int(input('¿Años?'))
print('Capital final:', (round(cantidad * (interes / 100 + 1) ** años, 2)))


print()

#Ejercicio 12
#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
payaso = int(input('Introduzca la cantidad de payasos:'))
pesoPayaso = payaso*112
muñeca = int(input('Introduzca la cantidad de muñecas:'))
pesoMuñeca = muñeca*75
pesoTotal = pesoPayaso + pesoMuñeca
print("El peso total del paquete a enviar es de",pesoTotal,'g')


print()

#Ejercicio 13
#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
cantidad = int(input('Introduzca la cantidad de dinero depositada:'))
primerAño = cantidad * 1.04
print('Balance tras el primer año',primerAño)
segundoAño = primerAño * 1.04
print('Balance tras el segundo año',segundoAño)
tercerAño = segundoAño * 1.04
print('Balance tras el tercer año',tercerAño)


print()

#Ejercicio 14
#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
pan = int(input('Introduzca el número de barras de pan que son del día:'))
panDia = 3.49
descuento = 0.6
print("El coste de la barra fresca",panDia)
print("Descuento por ser una barra no fresca",descuento)
print("Coste total", ((pan*panDia)*(1-descuento)))