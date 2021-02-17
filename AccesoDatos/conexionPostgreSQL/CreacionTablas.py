'''
Created on 17 feb. 2021

@author: Lidia Parral
'''
import psycopg2
import psycopg2.extras
import sys
import pprint

conn = psycopg2.connect(host = "localhost", database = "postgres1", user = "postgres", password = "10061995")

#El vehículo que se usa para interactuar con la BBDD
cursor = conn.cursor()

print ("Conectado!\n")
#Se ejecutan una serie de consultas o queries
#Si existe la tabla prueba se borrará para evitar excepciones al ejecutar el código de nuevo
cursor.execute("DROP TABLE IF EXISTS prueba")
print("La tabla prueba se ha eliminado")
#Se crea una tabla nueva llamada prueba con un campo que será clave primaria
cursor.execute("CREATE TABLE prueba (id serial PRIMARY KEY, nombre varchar, sueldo integer)")
#Se insertan algunas tuplas en la tabla. La última se inserta de otra forma
cursor.execute("INSERT INTO prueba (nombre, sueldo) VALUES (%s, %s)",("Miguel Sánchez", 1500))
cursor.execute("INSERT INTO prueba (nombre, sueldo) VALUES (%s, %s)",("Clara Muñoz", 1600))
cursor.execute("INSERT INTO prueba (nombre, sueldo) VALUES (%s, %s)",("Paco López", 1580))
cursor.execute("INSERT INTO prueba (nombre, sueldo) VALUES (%s, %s)",("Nerea Montalbán", 1570))
cursor.execute("INSERT INTO prueba (nombre, sueldo) VALUES (%s, %s)",("Luis Bermúdez", 1650))
cursor.execute("INSERT INTO prueba (nombre, sueldo) VALUES (%s, %s)",("Ana Palomo", 1590))
#Se inserta una tupla más de otra manera
cursor.execute(
"""INSERT INTO prueba (nombre, sueldo)
VALUES (%s, %s);""",
("Lola Otero", 1700))




print("conexión existosa")


