from Censo import Censo
from Familia import Familia
from Persona import Persona

persona1 = Persona(42, "m", True, False)
persona2 = Persona(42, "f", False, True)
persona3 = Persona(6, "m", True, False)
persona4 = Persona(15, "f", True, False)

persona5 = Persona(28, "m", False, True)
persona6 = Persona(28, "f", False, True)

persona7 = Persona(32, "f", False, True)
persona8 = Persona(32, "m", True, False)
persona9 = Persona(5, "m", True, False)


familia_1 = Familia()
familia_2 = Familia()
familia_3 = Familia()

familia_1.agregar_integrante(persona1)
familia_1.agregar_integrante(persona2)
familia_1.agregar_integrante(persona3)
familia_1.agregar_integrante(persona4)

familia_2.agregar_integrante(persona5)
familia_2.agregar_integrante(persona6)

familia_3.agregar_integrante(persona7)
familia_3.agregar_integrante(persona8)
familia_3.agregar_integrante(persona9)

censo1= Censo()

censo1.agregar_familia(familia_1)
censo1.agregar_familia(familia_2)
censo1.agregar_familia(familia_3)

print(f"Cantidad de familias censadas: {censo1.cantidad_familias_censadas()}")
print(f"Cantidad de personas censadas: {censo1.cantidad_personas_censadas()}")
print(f"Promedio de dedades de personas censadas: {censo1.promedio_edades_personas_censadas()}")
print(f"Cantidad de personas que trabajan: {censo1.cantidad_personas_trabajan()}")

# Utilizando lo implementado en el ejercicio anterior, desarrolle una simulación que cense
#  entre tres y cinco familias y finalmente imprima en pantalla los siguientes datos
#  a. Cantidad de familias censadas
#  b. Cantidad de personas
#  c. Promedio de edad
#  d. Cantidad de personas que trabajan