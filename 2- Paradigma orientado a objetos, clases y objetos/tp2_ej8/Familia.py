class Familia:
    def __init__(self,apellido_familia, direccion_familia):
        self.__integrantes = []
        self.__apellido_familia = apellido_familia
        self.__direccion_familia = direccion_familia
        
    def get_integrantes (self):
        return self.__integrantes
    
    def agregar_integrante_familia (self, persona):
        self.__integrantes.append(persona)
    
    def cantidad_integrantes_familia(self):
        num=0
        for i in self.__integrantes:
            num += 1
        return num