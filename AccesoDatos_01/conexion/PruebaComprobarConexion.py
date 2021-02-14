'''
Created on 8 feb. 2021

@author: Lidia Parral
'''
from pip._vendor.distlib import database
import psycopg2

#Comienzo del Código
# -*- coding: utf-8 -*-
# Adaptador Python - Postgres
conn = psycopg2.connect(database = "postgres", user = "postgres", password = "10061995", host= "localhost", port="5433")
print("Se ha conectado con" + database)

conectar = conn.cursor()
conectar.execute("INSERT INTO ALUMNOS(ID,NOMBRE) VALUES (%d,%s)", (2,"Miguel"))

conn.commit()
conn.close()
conectar.close()