class Senso:

    def __init__(self):
        self.__lista_familias = []

    def get_familias (self):
        return self.__lista_familias

    def agregar_familia (self, familia):
        self.__lista_familias.append(familia)

    def cantidad_failias_censadas (self):
        num = 0
        for i in self.__lista_familias:
            num += 1
        return num

    def cantidad_personas_censadas(self):
        num = 0
        for familia in self.get_familias():
            for integrante in familia.get_integrantes():
                num += 1
        return num

    def promedio_edad (self):
        cantidad_integrantes = self.cantidad_personas_censadas()
        edades_sumadas = 0
        for familia in self.get_familias():
            for integrante in familia.get_integrantes():
                edades_sumadas += integrante.get_edad()
        return (edades_sumadas / cantidad_integrantes)

    def cantidad_trabajan (self):
        num = 0
        for familia in self.get_familias():
            for integrante in familia.get_integrantes():
                if integrante.get_trabaja() == True:
                    num += 1
        return num