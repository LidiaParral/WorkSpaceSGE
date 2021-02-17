'''
Created on 8 feb. 2021

@author: Lidia Parral
'''

import psycopg2
from psycopg2 import sql

#Comienzo del Código
# -*- coding: utf-8 -*-
# Adaptador Python - Postgres
# Se realiza la conexión con la base de datos postgres
conn = psycopg2.connect(host = "localhost", database = "bd1", user = "postgres", password = "10061995")

print("conexión existosa")

#El vehículo que se usa para interactuar con la BBDD
cursor = conn.cursor()

#Comprueba si existe la tabla alumno y si es así la borra
cursor.execute("DROP TABLE IF EXISTS ALUMNO")

sql = """CREATE TABLE ALUMNO(
        NOMBRE CHAR(100) NOT NULL,
        APELLIDO_PATERNO CHAR(100) NOT NULL,
        APELLIDO_MATERNO CHAR(100),
        EDAD INT,
        SEXO CHAR(1),
        CALIFICACION FLOAT
    )
    """

#Crear una tabla en la base de datos previamente definida con el método EXECUTE   
cursor.execute(sql)

#Siempre que se crea, borra o actualiza una tabla o los datos de una tabla para subir ese cambio hay que hacer el método COMMIT()
conn.commit()

print("Tabla creada con éxito")

#Cerrar la conexión de la base de datos con el método CLOSE()
conn.close()
