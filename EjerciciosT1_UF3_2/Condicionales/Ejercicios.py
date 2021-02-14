'''
Created on 25 nov. 2020

@author: Lidia Parral

'''

#Ejercicio 1
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
edad = int(input('Introduzca su edad:'))
if edad >= 18:
    print('Es mayor de edad')
else:
    print('No es mayor de edad')
    
print()


#Ejercicio 2
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
contraseña = ('contraseña')
cont = str(input('Introduzca una contraseña:'))
if cont.lower() == contraseña:
    print('Es correcta')
else:
    print('No es correcta')

print()


#Ejercicio 3
#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

num1 = int(input('Introduzca un número:'))
num2 = int(input('Introduzca un número:'))
if (num1 == 0) or (num2 == 0):
    print('ERROR')
else:
    print('La división es',(num1/num2))

print()



#Ejercicio 4
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
num = int(input('Introduzca un número para averiguar si es par o impar:'))
if (num%2 == 0):
    print('NÚMERO PAR')
else:
    print('NÚMERO IMPAR')
    
    
print()



#Ejercicio 5
#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
edad = int(input('Introduzca su edad:'))
ingresos = float(input('Introduzca sus ingresos:'))
if edad >= 16 and ingresos > 1000:
    print('Puede tributar')
else:
    print('No puede tributar')

print()



#Ejercicio 7
#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
rentaAnual = float(input('Introduzca su renta anual:'))
if rentaAnual <= 10000:
    print('El tipo de impositivo que le corresponde es de un 5%')
elif rentaAnual > 10000 and  rentaAnual <= 20000:
    print('El tipo de impositivo que le corresponde es de un 15%')
elif rentaAnual > 20000 and rentaAnual <= 35000:
    print('El tipo de impositivo que le corresponde es de un 20%')
elif rentaAnual > 35000 and rentaAnual <= 60000:
    print('El tipo de impositivo que le corresponde es de un 30%')
elif rentaAnual > 60000:
    print('El tipo de impositivo que le corresponde es de un 40%')
    
    
print()



#Ejercicio 6
#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
nombre = str(input('Introduzca su nombre:'))
sexo = str(input('Introduzca su sexo(H/M):'))
if sexo == 'M':
    if nombre.lower() < 'm':
        grupo = 'A'
    else:
        grupo = 'B'
else:
    if nombre.lower() > 'n':
        grupo = 'A'
    else:
        grupo = 'B'
print('Tu grupo es', grupo)


print()


#Ejercicio 8
#Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
puntuacion = float(input('Introduzca su puntuación:'))
if puntuacion == 0.0 or puntuacion == 0.4 or puntuacion >= 0.6:
    if puntuacion == 0.0:
        dinero = 2400 * puntuacion
        print('Inaceptable')
        print('La cantidad de dinero que recibes es de', dinero,'euros.')
    elif puntuacion == 0.4:
        dinero = 2400 * puntuacion
        print('Aceptable')
        print('La cantidad de dinero que recibes es de', dinero,'euros.')
    elif puntuacion >= 0.6:
        dinero = 2400 * puntuacion
        print('Meritorio')
        print('La cantidad de dinero que recibes es de', dinero,'euros.')
        
else:
    print('ERROR')
    

print()



#Ejercicio 9
#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
edad = int(input('Introduzca su edad:')) 
if edad < 4:
    print('La entrada es GRATIS')
elif edad > 4 and edad <= 18:
    print('La entrada cuesta 5 euros')
elif edad > 18:
    print('La entrada cuesta 10 euros')
    
print()




#Ejercicio 10
#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
#Ingredientes vegetarianos: Pimiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
pizza = str(input('Eliga entre pizza vegetariana o no:\n'))
if pizza == 'vegetariana':
    vegetariana = {'pimiento','tofu'}
    print(vegetariana)
    ing = str(input('Elige un ingrediente:\n'))
    if ing == 'Tofu':
        print('La pizza elegida es vegetariana y el ingrediente escogido es',ing)
    else:
        print('La pizza elegida es vegetariana y el ingrediente escogido es',ing)
else:
    novegetariana = {'Peperoni','Jamón','Salmón'}
    print(novegetariana)
    ing = str(input('Elige un ingrediente:\n'))
    if ing == 'Peperoni':
        print('La pizza elegida es no vegetariana y el ingrediente escogido es',ing)
    elif ing == 'Jamón':
        print('La pizza elegida es no vegetariana y el ingrediente escogido es',ing)
    else:
        print('La pizza elegida es no vegetariana y el ingrediente escogido es',ing)



print()


