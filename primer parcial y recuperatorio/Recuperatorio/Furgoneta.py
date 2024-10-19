from Transporte import Transporte

class Furgoneta (Transporte):
    def __init__(self):
        self.__pesoMaximo = 100
        self.__velocidadPromedio = 60
        self.__costoPorKm = 1000
    
    def calcularTiempo(self,distancia):
        return self.__velocidadPromedio * distancia
    
    def costo(self,distancia):
        return self.__costoPorKm *  distancia
    
    def tansportarPaquete(self, distancia,pesoPaquete):
        if pesoPaquete > self.__pesoMaximo:
            return -1
        else:
            tiempo = self.calcularTiempo(distancia)
            costo = self.costo(distancia)
            costoTrasnporte = 0.7 * tiempo + 0.3 * costo
            return costoTrasnporte



