'''
Created on 8 feb. 2021

@author: Lidia Parral
'''

#Comienzo del Código
# -*- coding: utf-8 -*-
import psycopg2 # Adaptador Python - Postgres

import pprint #Para mostrar los valores de las tuplas recibidas
#Conexión a la base de datos en Postgresql
pprint()
print("PRUEBA DE CONEXIÓN A POSTGRES Y VERSIÓN DE LA BASE DE DATOS")
print()
#conn = None #Para destruir cualquier conexión conx existente
print("Conexión a la Base de Datos Postgres")
#Se usa try para poder capturar las excepciones producidas durante la conexión
try:
# Se realiza la conexión con la base de datos postgres
conn = psycopg2.connect( database = "postgres1", user = "postgres", password = "10061995")
print("Estableciendo conexión a la base de datos ...")
#conx.cursor devuelve un objeto cursor necesario para realizar las consultas SQL
cur = conn.cursor()
print ("Conectado!\n")
#Se muestra la versión de Postgresql
cur.execute('select version()')
version = cur.fetchone()
print ("versión de PostgreSQL\n", version)
except:
print ("No se puede conectar con la Base de Datos")
#Fin del código

