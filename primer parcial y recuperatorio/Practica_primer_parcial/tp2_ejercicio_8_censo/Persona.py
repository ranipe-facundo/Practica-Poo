class Persona:
    def __init__(self, edad, sexo, estudia, trabaja):
        self.__edad = edad
        self.__sexo = sexo
        self.__estudia = estudia
        self.__trabaja = trabaja
    
    def get_edad(self):
        return self.__edad
    def get_trabaja(self):
        return self.__trabaja