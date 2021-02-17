'''
Created on 17 feb. 2021

@author: Lidia Parral
'''
import psycopg2
import psycopg2.extras
import sys
import pprint


conn = psycopg2.connect(host = "localhost", database = "postgres1", user = "postgres", password = "10061995")
print("conexión existosa")

#El vehículo que se usa para interactuar con la BBDD
cursor = conn.cursor()

print ("Conectado!\n")
#Se ejecutan una serie de consultas o queries
#Si existe la tabla prueba se borrará para evitar excepciones al ejecutar el código de nuevo


conn.commit()
conn.close()







