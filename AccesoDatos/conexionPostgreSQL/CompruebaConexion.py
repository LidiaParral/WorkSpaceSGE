'''
Created on 17 feb. 2021

@author: Lidia Parral
'''
import psycopg2
import psycopg2.extras

conn = psycopg2.connect(host = "localhost", database = "postgres1", user = "postgres", password = "10061995")

print("conexión existosa")


#El vehículo que se usa para interactuar con la BBDD
cursor = conn.cursor()

cursor.execute('select version()')
version = cursor.fetchone()
print ("versión de PostgreSQL\n", version)

#Cerrar la conexión de la base de datos con el método CLOSE()
conn.close()