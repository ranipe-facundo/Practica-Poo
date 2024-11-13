from Materia import Materia
from Profesor import Profesor

poo = Materia ("POO", "PrOO_001")
algebra = Materia ("Algebra", "Alge_001")
introduccion_computacion = Materia ("Introduccion a la Computacion", "InaC_001")
algoritmica = Materia ("Algoritmica", "Algo_201")

profesor_1 = Profesor("Pedro","Hernandez")
profesor_1.agregar_materia(poo)
profesor_1.agregar_materia(algebra)

profesor_2 = Profesor("Romina","Alvarez")
profesor_2.agregar_materia(introduccion_computacion)
profesor_2.agregar_materia(algoritmica)

profesor_3 = Profesor("Laura","Perez")

print (f"Profesor: {profesor_1.get_apellido(),profesor_1.get_nombre()}")
print("Materias:")
profesor_1.imprimir_materias()

print (f"Profesor: {profesor_2.get_apellido()} {profesor_2.get_nombre()}")
print("Materias:")
profesor_2.imprimir_materias()

print (f"Profesor: {profesor_3.get_apellido()},{profesor_3.get_nombre()}")
print("Materias:")
profesor_3.imprimir_materias()