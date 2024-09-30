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
    
    def imprimir(self):
        def comparacion (elemento):
            if elemento == True:
                return "Si"
            else:
                return "No"
        print("Empleado/a:")
        print(f"Edad: {self.__edad}")
        print(f"Sexo: {self.__sexo}")
        print(f"Estudia: {comparacion (self.__estudia)}")
        print(f"Trabaja: {comparacion (self.__trabaja)}")