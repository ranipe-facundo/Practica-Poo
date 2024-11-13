#   Como parte de un pequeño censo, para relevar la cantidad de personas de una comuna
#   se solicita un sistema que permita cargar familias, donde cada una está compuesta por varias personas. 
#   De estas personas es importante conocer su edad, sexo, si estudia y si trabaja.
#   Desarrolle y diseñe las clases que compondrían el sistema y su respectivo diagrama de clases.

#   Utilizando lo implementado en el ejercicio anterior, desarrolle una simulación que cense entre tres y cinco familias y finalmente imprima en pantalla 
#   los siguientes datos
#    a. Cantidad de familias censadas -
#    b. Cantidad de personas - 
#    c. Promedio de edad - 
#    d. Cantidad de personas que trabajan - 

from Persona import Persona
from Familia import Familia
from Senso import Senso

persona_G1 = Persona(50, 'M', False, True)
persona_G2 = Persona(48, 'F', False, True)
persona_G3 = Persona(20, 'M', True, False)
persona_G4 = Persona(18, 'F', True, False)
famila_gonsalez = Familia("Gonzales", "San Martin 123")
famila_gonsalez.agregar_integrante_familia(persona_G1)
famila_gonsalez.agregar_integrante_familia(persona_G2)
famila_gonsalez.agregar_integrante_familia(persona_G3)
famila_gonsalez.agregar_integrante_familia(persona_G4)

persona_R1 = Persona(38, 'M', False, True)
persona_R2 = Persona(36, 'F', False, True)
persona_R3 = Persona(12, 'F', True, False)
persona_R4 = Persona(8, 'F', True, False)
famila_ramirez = Familia("Ramirez", "Rivadavia 123")
famila_ramirez.agregar_integrante_familia(persona_R1)
famila_ramirez.agregar_integrante_familia(persona_R2)
famila_ramirez.agregar_integrante_familia(persona_R3)
famila_ramirez.agregar_integrante_familia(persona_R4)

persona_F1 = Persona(45, 'M', False, True)
persona_F2 = Persona(42, 'M', False, True)
persona_F3 = Persona(16, 'M', True, False)
persona_F4 = Persona(10, 'F', True, False)
famila_fernandez = Familia("Fernandez", "Sarmiento 123")
famila_fernandez.agregar_integrante_familia(persona_F1)
famila_fernandez.agregar_integrante_familia(persona_F2)
famila_fernandez.agregar_integrante_familia(persona_F3)
famila_fernandez.agregar_integrante_familia(persona_F4)

persona_L1 = Persona(40, 'M', False, True)
persona_L2 = Persona(38, 'F', False, True)
persona_L3 = Persona(17, 'F', True, False)
persona_L4 = Persona(21, 'F', True, True)
famila_lopez = Familia("Gonzales", "Belgrano 123")
famila_lopez.agregar_integrante_familia(persona_L1)
famila_lopez.agregar_integrante_familia(persona_L2)
famila_lopez.agregar_integrante_familia(persona_L3)
famila_lopez.agregar_integrante_familia(persona_L4)

senso_2024 = Senso()
senso_2024.agregar_familia (famila_gonsalez)
senso_2024.agregar_familia (famila_ramirez)
senso_2024.agregar_familia (famila_fernandez)
senso_2024.agregar_familia (famila_lopez)

print (f"Cantidad de familias sensadas: {senso_2024.cantidad_failias_censadas()}")
print (f"Cantidad de personas sensadas: {senso_2024.cantidad_personas_censadas()}")
print (f"Promedio edades: {senso_2024.promedio_edad()}")
print (f"Cantidad de personas que trabajan : {senso_2024.cantidad_trabajan()}")