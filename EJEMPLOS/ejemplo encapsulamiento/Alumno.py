from Persona import Persona

class Alumno(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.__carrera = carrera