'''
Created on 24 nov. 2020

@author: Lidia Parral


Escribe una función calificaPalabras(diccionario) que reciba un diccionario con las
asignaturas y las notas numéricas de un alumno y devuelva otro diccionario con las asignaturas en
mayúsculas y las calificaciones correspondientes a las notas con palabras.
El criterio será el siguiente: nota <5 → Suspenso; 5 <= nota < 7 → Aprobado;
7 <= nota < 9 → Notable; 9 <= nota <=10 → Sobresaliente. La nota no puede sobrepasar 10.
Por ejemplo, la función recibe el diccionario {'Android':8.2, 'Hilos':5, 'Python':9.3, 'Interfaces':4.4}
y devuelve el diccionario {'ANDROID’:’Notable’, ‘HILOS’:’Aprobado’, ‘PYTHON’:’Sobresaliente’,
‘INTERFACES’:’Suspenso’ }

'''
def grado(nota):
    if nota < 5:
        return 'Suspenso'
    elif 5 <= nota < 7:
        return 'Aprobado'
    elif 7 <= nota < 9:
        return 'Notable'
    elif 9 <= nota < 10:
        return 'Sobresaliente'
    else:
        return 'No está disponible'

def calificaPalabras(notas):
    return {
        asignatura.upper():grado(nota) for asignatura, nota in notas.items()}

print(calificaPalabras({'Android':8.2, 'Hilos':5, 'Python':9.3, 'Interfaces':4.4}))