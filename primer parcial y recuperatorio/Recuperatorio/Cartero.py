from Transporte import Transporte

class Cartero (Transporte):
    def __init__(self):
        self.__pesoMaximo = 5
        self.__velocidadPromedio = 5
        self.__costoPorKm = 270
    
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
            costoTrasnporte = 0.2 * tiempo + 0.8 * costo
            return costoTrasnporte


