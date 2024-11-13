class Censo:
    def __init__(self):
        self.__familias = []
    
    def agregar_familia(self, familia):
        self.__familias.append(familia)

    def cantidad_familias_censadas(self):
        cantidad_familias = 0
        for i in self.__familias:
            cantidad_familias += 1
        return cantidad_familias
    
    def cantidad_personas_censadas(self):
        cantidad_personas = 0
        for i in self.__familias:
            for j in i.get_integrantes():
                cantidad_personas += 1
        return cantidad_personas
    
    def promedio_edades_personas_censadas(self):
        total_edaddes = 0
        for i in self.__familias:
            for j in i.get_integrantes():
                total_edaddes = total_edaddes + j.get_edad()
        return total_edaddes/self.cantidad_personas_censadas()
    
    def cantidad_personas_trabajan(self):
        cantidad_trabajan = 0
        for i in self.__familias:
            for j in i.get_integrantes():
                if j.get_trabaja() == True:
                    cantidad_trabajan += 1
        return cantidad_trabajan
    
    