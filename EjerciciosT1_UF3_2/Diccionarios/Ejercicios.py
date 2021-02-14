'''
Created on 26 nov. 2020

@author: Lidia Parral


'''


#Ejercicio 1
#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
currencies = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
currency = input("Introduce una divisa: ")
print(currencies.get(currency.title(), "La divisa no está."))


print()



#Ejercicio 2
#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
persona = {}
nombre = 'Lidia'
edad = 25
direccion = 'Antonio del Campo 7'
telefono = 601444641

persona[nombre] = edad,direccion,telefono
print(nombre,'tiene',edad,'años, vive en',direccion,'y su número de teléfono es',telefono)

print()



#Ejercicio 3
#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
fruits = {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
fruit = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruit in fruits:
    print(kg, 'kilos de', fruit, 'valen', fruits[fruit]*kg )
else: 
    print("Lo siento, la fruta",fruit,"no está disponible.")
    

print()




#Ejercicio 4
#Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
months = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
date = input('Introduce una fecha en formato dd/mm/aaaa: ')
date = date.split('/')
print(date[0], 'de', months[int(date[1])], 'de', date[2])

print()



#Ejercicio 5
#Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total_credits = 0
for subject, credits in curso.items():
    print(subject, 'tiene', credits, 'créditos')
    total_credits += credits
print('Número total de créditos del curso: ', total_credits)

print()



#Ejercicio 6
#Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

persona = {}
more = 'Si'
while more=='Si':
    key = input('¿Qué dato quieres introducir? ')
    value = input(key + ': ')
    persona[key] = value
    print(persona)
    more = input('¿Quieres añadir más información (Si/No)? ')


print()



#Ejercicio 7
#Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

basket = {}
more = 'Si'
while more == 'Si':
    item = input('Introduce un artículo: ')
    price = float(input('Introduce el precio de ' + item + ': '))
    basket[item] = price
    more = input('¿Quieres añadir artículos a la lista (Si/No)? ')
cost = 0
print('Lista de la compra')
for item, price in basket.items():
    print(item, '\t', price)
    cost += price
print('Coste total: ', cost)



print()




#Ejercicio 8
#Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.

dictionary = {}
words = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")
for i in words.split(','):
    key, value = i.split(':')
    dictionary[key] = value
phrase = input('Introduce una frase en español: ')
for i in phrase.split():
    if i in dictionary:
        print(dictionary[i], end=' ')
    else:
        print(i, end=' ')


print()



#Ejercicio 9
#Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.

invoices = {}
collected = 0
remains = 0
more = ''
while more != 'T':
    if more == 'A':
        key = input('Introduce el número de la factura: ')
        cost = float(input('Introduce el coste de la factura: '))
        invoices[key] = cost
        remains += cost
    if more == 'P':
        key = input('Introduce el número de la factura a pagar: ')
        cost = invoices.pop(key, 0)
        collected += cost
        remains -= cost
    print('Recaudado:', collected)
    print('Pendiente de cobro: ', remains)
    more = input('¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)? ')
    
print()




#Ejercicio 10
#Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

#Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
#Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
#Preguntar por el NIF del cliente y mostrar sus datos.
#Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
#Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
#Terminar el programa


clients = {}
option = ''
while option != '6':
    if option == '1':
        nif = input('Introduce NIF del cliente: ')
        name = input('Introduce el nombre del cliente: ')
        address = input('Introduce la dirección del cliente: ')
        phone = input('Introduce el teléfono del cliente: ')
        email = input('Introduce el correo electrónico del cliente: ')
        vip = input('¿Es un cliente preferente (S/N)? ')
        client = {'nombre':name, 'dirección':address, 'teléfono':phone, 'email':email, 'preferente':vip=='S'}
        clients[nif] = client
    if option == '2':
        nif = input('Introduce NIF del cliente: ')
        if nif in clients:
            del clients[nif]
        else:
            print('No existe el cliente con el nif', nif)
    if option == '3':
        nif = input('Introduce NIF del cliente: ')
        if nif in clients:
            print('NIF:', nif)
            for key, value in clients[nif].items():
                print(key.title() + ':', value)
        else:
            print('No existe el cliente con el nif', nif)
    if option == '4':
        print('Lista de clientes')
        for key, value in clients.items():
            print(key, value['nombre'])
    if option == '5':
        print('Lista de clientes preferentes')
        for key, value in clients.items():
            if value['preferente']:
                print(key, value['nombre'])
    option = input('Menú de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar clientes\n(5) Listar clientes preferentes\n(6) Terminar\nElige una opción:')
    
print()















    



















