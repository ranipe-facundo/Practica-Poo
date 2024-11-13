class Materia:
    
    def __init__(self, nombre, codigo_materia):
        self.__nombre = nombre
        self.__codigo_materia = codigo_materia
    
    def get_nombre (self):
        return self.__nombre
    def get_codigo (self):
        return self.__codigo_materia
    
    def set_nombre (self, nombre):
        self.__nombre = nombre
    def set_codigo (self, codigo_materia):
        self.__codigo_materia = codigo_materia