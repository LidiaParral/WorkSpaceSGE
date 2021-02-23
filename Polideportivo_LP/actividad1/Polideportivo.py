'''
Created on 21 feb. 2021

@author: Lidia Parral
'''
import psycopg2, psycopg2.extras, sys, pprint
from psycopg2 import sql

conx = None

try:
    conx = psycopg2.connect(host="localhost", database="bd2", user="postgres", password="10061995")
    print("Estableciendo conexión con la base de datos...")
    cur = conx.cursor()
    print("Conectado!\n")
    
    class Clientes:

        def __init__(self, dni, nombre, fecha, telefono):
            self.dni = dni
            self.nombre = nombre
            self.fecha = fecha
            self.telefono = tlf
            cur = conx.cursor()
            sql = """INSERT INTO CLIENTES (dni,nombre,fecha,telefono) 
            VALUES (%s, %s, %s, %s)"""
            cur.execute(sql, (dni, nombre, fecha, telefono,))
            conx.commit()
            
        def __datos__(self):
            query = "SELECT * FROM CLIENTES"
            cur.execute(query)
            
        def __deportes__(self):
            vdni = input("DNI:")
            vcliente = cur.execute("SELECT IDC FROM CLIENTES WHERE dni=vdni")
            cur.execute("SELECT NOMBRE FROM SE_MATRICULAN, DEPORTES WHERE")
            tuplas = cur.fetchall()
            for row in tuplas:
                print(row)
   
    cur.execute("DROP TABLE IF EXISTS SE_MATRICULAN CASCADE")
    cur.execute("DROP TABLE IF EXISTS CLIENTES CASCADE")
    cur.execute("DROP TABLE IF EXISTS DEPORTES CASCADE")
    
    cur.execute("CREATE TABLE CLIENTES (IDC SERIAL PRIMARY KEY, NOMBRE VARCHAR(150), DNI VARCHAR(9), FECHA INT, TELEFONO VARCHAR(12));")
    cur.execute("CREATE TABLE DEPORTES (IDDEPO SERIAL PRIMARY KEY, NOMBRE VARCHAR(20), PRECIO INT);")
    
    cur.execute("INSERT INTO DEPORTES (NOMBRE, PRECIO) VALUES (%s, %s)", ("Tenis", 30))
    cur.execute("INSERT INTO DEPORTES (NOMBRE, PRECIO) VALUES (%s, %s)", ("Natacion", 15))
    cur.execute("INSERT INTO DEPORTES (NOMBRE, PRECIO) VALUES (%s, %s)", ("Atletismo", 22))
    cur.execute("INSERT INTO DEPORTES (NOMBRE, PRECIO) VALUES (%s, %s)", ("Baloncesto", 10))
    cur.execute("INSERT INTO DEPORTES (NOMBRE, PRECIO) VALUES (%s, %s)", ("Futbol", 12))
    
    cur.execute("CREATE TABLE se_matriculan(IDS SERIAL PRIMARY KEY, CLIENTE INT, DEPORTE INT, HORARIO VARCHAR, FOREIGN KEY (CLIENTE) REFERENCES CLIENTES (IDC), FOREIGN KEY (DEPORTE) REFERENCES DEPORTES (IDDEPO));")
    
    conx.commit()
 
    num = 0

    while num != 7:
        print("1.Dar de alta un cliente con sus datos personales")
        print("2.Dar de baja un cliente")
        print("3.Mostrar los datos personales de un cliente o de todos")
        print("4.Matricular a un cliente en un deporte")
        print("5.Desmatricular a un cliente en un deporte")
        print("6.Mostrar los deportes de un cliente")
        print("7.Salir")
        num = int(input("Introduce una opción.."))
        
        if num == 1:
            dni = input("DNI:")
            nombre = input("Nombre:")
            fecha = input("Fecha de nacimiento:")
            tlf = input("Teléfono:")
            c = Clientes(dni, nombre, fecha, tlf)
            
        if num == 2:    
            vdni = input("DNI:")
            if vdni is not None:
                query = "DELETE FROM CLIENTES WHERE DNI= %s"
                cur.execute(query, (vdni,))
                print("El cliente con dni ", vdni, " ha sido dado de baja")
                conx.commit()
            else:
                print("El cliente con dni ", vdni, " no ha sido dado de baja")
            
        if num == 3:
            opcion = input("¿Quieres ver un cliente o todos?, uno/todos")
            if opcion == "uno":
                query = "SELECT * FROM CLIENTES WHERE DNI = %s"
                vdni = input("DNI:")
                cur.execute(query, (vdni,))
                tupla = cur.fetchone()
                pprint.pprint(tupla)
            else:
                cur.execute("SELECT * FROM CLIENTES")
                tuplas = cur.fetchall()
                pprint.pprint(tuplas)
                 
        if num == 4:
            vdni = input("DNI:")
            vdpt = input("Deporte a matricular:")
            vhor = input("Horario(hora):")
            query = "SELECT * FROM CLIENTES WHERE DNI = %s"
            cur.execute(query, (vdni,))
            fila = cur.fetchone()
            vcli = fila[0]
            vdept = fila[0]
            cur = conx.cursor()
            sql = """INSERT INTO SE_MATRICULAN(CLIENTE, DEPORTE, HORARIO) VALUES (%s, %s, %s)"""
            cur.execute(sql, (vcli, vdept, vhor,))
            conx.commit()
        
        #NO FUNCIONA  
        if num == 5:
            vdni = input("DNI:")
            vdpt = input("Deporte a desmatricular:")
            vhor = input("Horario(hora):")
            query = "SELECT * FROM CLIENTES WHERE DNI = %s"
            cur.execute(query, (vdni,))
            fila = cur.fetchone()
            vcli = fila[0]
            vdepto = fila[0]
            cur = conx.cursor()
            sql = """DELETE FROM SE_MATRICULAN WHERE CLIENTE = %s AND DEPORTE = %s"""
            cur.execute(sql,(vcli, vdept))
            conx.commit()            
            print("Se ha dado de baja la  matricula del deporte")
            
        if num == 6:
            vdni = input("DNI:")
            query = "SELECT IDC FROM CLIENTES WHERE DNI = %s"
            cur.execute(query, (vdni,))
            fila = cur.fetchone()
            vcliente = fila[0]
            query = (''' SELECT NOMBRE, HORARIO FROM SE_MATRICULAN INNER JOIN DEPORTES 
            ON SE_MATRICULAN.DEPORTE = DEPORTES.IDDEPO 
            AND SE_MATRICULAN.CLIENTE = %s ''')
            cur.execute(query, (vcliente,))
            tuplas = cur.fetchall()
            pprint.pprint(tuplas)
            conx.commit()

except(Exception, psycopg2.DatabaseError) as error:
    print(error)

finally:
    cur.close()
    if conx is not None:
        conx.close()

# Fin del código
    
