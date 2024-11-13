class Profesor:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__materias = []

    def agregar_materia(self, materia):
        self.__materias.append(materia)

    #### Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_apellido(self, apellido):
        self.__apellido = apellido

    #### Getters
    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_materias(self):
        return self.__materias
    
    def imprimir_materias(self):
        for materia in self.__materias:
            print(materia.get_nombre())
