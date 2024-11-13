from Alumno import Alumno
from Aula import Aula

alumno1 = Alumno("facu", 32, "APU")
alumno2 = Alumno("Pepe", 20, "ING")

print( alumno1._edad)

aula= Aula(alumno1,alumno2)

aula.mostrar_edad_1()