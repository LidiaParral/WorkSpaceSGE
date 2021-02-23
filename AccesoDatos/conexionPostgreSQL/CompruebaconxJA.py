'''
Created on 8 feb. 2021

@author: Lidia Parral
'''

#Comienzo del Código
# -*- coding: utf-8 -*-
import psycopg2 # Adaptador Python - Postgres
import psycopg2.extras
import pprint #Para mostrar los valores de las tuplas recibidas
from conexionPostgreSQL.CreacionTablasJA import conx
#Conexión a la base de datos en Postgresql
print()
print("PRUEBA DE CONEXIÓN A POSTGRES Y VERSIÓN DE LA BASE DE DATOS")
print()
#conn = None #Para destruir cualquier conexión conx existente
print("Conexión a la Base de Datos Postgres")
#Se usa try para poder capturar las excepciones producidas durante la conexión
try:
# Se realiza la conexión con la base de datos postgres
    conx = psycopg2.connect("database = ejercicio1, user = postgres, password = 10061995")
    print("Estableciendo conexión a la base de datos ...")
    #conx.cursor devuelve un objeto cursor necesario para realizar las consultas SQL
    cur = conx.cursor()
    print ("Conectado!\n")
    #Se muestra la versión de Postgresql
    cur.execute('select version()')
    version = cur.fetchone()
    print ("versión de PostgreSQL\n", version)
except:
    print ("No se puede conectar con la Base de Datos")
#Fin del código
