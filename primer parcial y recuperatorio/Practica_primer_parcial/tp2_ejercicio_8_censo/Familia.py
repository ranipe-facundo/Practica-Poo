class Familia:
    def __init__(self):
        self.__integrantes = []
    
    def get_integrantes(self):
        return self.__integrantes
        
    def agregar_integrante(self, integrante):
        self.__integrantes.append(integrante)
