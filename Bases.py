
import random
from datetime import datetime, date,timedelta
nombres = ["Javier Pérez", "Manuel López", "Manuel Ortega", "Ana Díaz", "Elena Castillo", "Patricia Ramos", "Raúl Ortega", "Ana García", "Sergio Pérez", "Patricia Vargas", "Luis Sánchez", "Luis Díaz", "Patricia García", "María Gómez", "Paula García", "Sergio Cruz", "Luis Castillo", "Raúl Morales", "Francisco Sánchez", "Carlos Sánchez", "Pedro Gómez", "Patricia Rodríguez", "Juan Martínez", "Elena Vega", "Francisco Gómez", "Lucía Molina", "Sergio López", "Laura Vargas", "María Gutiérrez", "Raúl Martínez", "Isabel Fernández", "Raúl Castillo", "Pedro Cruz", "Pedro Vargas", "José Martínez", "Sara Díaz", "Juan Torres", "María Cruz", "Sergio Rodríguez", "Juan Sánchez", "Carlos Díaz", "Carmen Cruz", "Carmen Vargas", "Juan Vargas", "Carlos Morales", "María Castillo", "Paula Gómez", "Carmen Morales", "Juan Ortega", "Luis Molina", "Patricia López", "Laura Molina", "Manuel Fernández", "Laura Gómez", "Juan Gómez", "Patricia Cruz", "Javier Molina", "Carlos Torres", "Francisco López", "Manuel Vega", "Carmen García", "Manuel Morales", "Isabel Martínez", "Elena Molina", "Ana López", "Luis Gómez", "Isabel Pérez", "Juan Díaz", "Javier Vargas", "Pedro Pérez", "Elena Pérez", "Isabel Vargas", "Isabel Molina", "Luis Rodríguez", "Sergio Molina", "Carlos Fernández", "Isabel Vega", "Javier Fernández", "Javier López", "Carmen López", "Paula Vargas", "Laura Vega", "Manuel García", "Juan Molina", "Patricia Vega", "Luis García", "Carlos Pérez", "Paula Pérez", "Luis Cruz", "Sara Pérez", "Raúl Vega", "Laura Torres", "Manuel Castillo", "Carlos Ortega", "Paula Fernández", "María García", "Patricia Gutiérrez", "José Vargas", "Raúl Pérez", "Francisco Martínez", "José Gómez", "Sara Cruz", "Paula Ortega", "Sergio Castillo", "Elena Ortega", "Sergio Ramos", "Carmen Castillo", "Sergio Ortega", "Ana Martínez", "Lucía Pérez", "Raúl Cruz", "José Rodríguez", "Carmen Rodríguez", "María Vargas", "Manuel Torres", "Manuel Cruz", "Paula Rodríguez", "Paula Morales", "Lucía López", "Elena Flores", "Francisco Vega", "Manuel Sánchez", "Carlos Vargas", "Sara Flores", "Patricia Sánchez", "Lucía Cruz", "Paula Martínez", "Javier García", "Pedro Molina", "Luis Ortega", "Raúl Ramos", "Javier Ortega", "Javier Gómez", "Raúl López", "Raúl Gómez", "Patricia Flores", "Lucía Castillo", "Raúl Sánchez", "Patricia Martínez", "Isabel Flores", "Paula Torres", "Sara Castillo", "Sara Martínez", "Patricia Pérez", "María Fernández", "Javier Rodríguez", "Carmen Gutiérrez", "Francisco Fernández", "Isabel Díaz", "Francisco Vargas", "Patricia Ortega", "María Ortega", "Raúl Vargas", "María Molina", "Laura Gutiérrez", "María Martínez", "Paula Ramos", "Francisco García", "José Molina", "José Cruz", "Carlos Martínez", "Sara Vega", "Sara Torres", "Francisco Ortega", "Isabel Gutiérrez", "Raúl Díaz", "Ana Rodríguez", "Paula Gutiérrez", "Manuel Flores", "Patricia Torres", "Ana Fernández", "Carmen Fernández", "Sergio Martínez", "Patricia Gómez", "Sergio Díaz", "Paula Sánchez", "Pedro Fernández", "Elena Díaz", "Luis Pérez", "Isabel Castillo", "Javier Flores", "Raúl Rodríguez", "Raúl Torres", "Paula Díaz", "Ana Vega", "Francisco Molina", "Francisco Flores", "Sergio Morales", "Paula Flores", "Elena Rodríguez", "Sara Sánchez", "Raúl García", "Juan Fernández", "Lucía Vargas", "Sergio Gómez", "Sergio Vargas", "Elena Sánchez", "Javier Martínez", "Javier Ramos", "Patricia Díaz"]
domicilios = ["Av. 9 de Julio", "Calle 25 de Mayo", "Av. 3 de Febrero", "Calle 12 de Octubre", "Calle 15 de Noviembre", "Av. 1 de Mayo", "Calle 17 de Agosto", "Calle 20 de Junio", "Calle 11 de Septiembre", "Av. 7 de Marzo", "Calle 5 de Abril", "Calle 14 de Diciembre", "Calle 10 de Enero", "Av. 6 de Julio", "Calle 16 de Octubre", "Calle 18 de Mayo", "Av. 2 de Febrero", "Calle 8 de Agosto", "Calle 13 de Noviembre", "Calle 19 de Marzo"]
titulos = ["Profesor de Educación Secundaria", "Maestro de Educación Primaria", "Docente de Nivel Inicial", "Catedrático en Ciencias Sociales", "Instructor de Tecnologías de la Información", "Tutor Académico de Matemáticas"]

"""
tipo_cliente = ["particular", "farmacia", "construccion", "sector_publico", "mayorista", "minorista", "alimento"]
ciudades = ["Bariloche", "Neuquén", "Trelew", "Puerto Madryn", "Comodoro Rivadavia", "Esquel", "San Martín de los Andes", "El Bolsón", "Viedma", "Sarmiento"]
fecha = datetime(2024, 10, 8)
nueva_fecha = fecha - timedelta(days=random.randint(1,25))
numero_con_decimales = round(random.uniform(1, 500), 2)
"""

"""
#crear cliente
for i in range(300):
    print("INSERT INTO ej1.cliente (nombre_cliente, renta_anual, tipo_cliente)") 
    print(f"VALUES ('{random.choice(nombres)}', {random.randint(9000000,20000000)}, '{random.choice(tipo_cliente)}');")
"""

"""
#crear embarques
for i in range (321):
    nueva_fecha = nueva_fecha - timedelta(days=random.randint(1,25))
    print ("insert into ej1.embarque (id_cliente, peso, id_camion, destino, fecha_embarque)")
    print (f"values ('{random.randint(1,501)}','{round(random.uniform(1, 500), 2)}','{random.randint(5,54)}','{random.choice(ciudades)}','{nueva_fecha.strftime('%Y/%m/%d')}');")
"""
"""
for i in range (3) :
    nueva_fecha = nueva_fecha - timedelta(days=random.randint(1,25))
    print ("insert into ej1.embarque (id_cliente, peso, id_camion, destino, fecha_embarque)")
    print (f"values ('433','{round(random.uniform(1, 500), 2)}','{random.randint(5,54)}','{random.choice(ciudades)}','{nueva_fecha.strftime('%Y/%m/%d')}');")
"""

#ALUMNO (LEGAJO, NOMBRE, DIRECCIÓN, EDAD, CONDICIÓN)



for i in domicilios:
    print ("insert into ej2.docente (dni, apellido, nombre, domicilio, titulo)")
    print (f'values({random.randint(20000000,80000000)}, {random.choice(nombres)}, {i}, {random.choice(titulos)})')