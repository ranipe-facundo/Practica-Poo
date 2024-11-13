from abc import ABC, abstractmethod

# Interfaz que define los métodos abstractos para vehículos
class Vehiculo(ABC):
    @abstractmethod
    def obtener_detalles(self):
        pass

    @abstractmethod
    def calcular_consumo(self):
        pass

class Coche(Vehiculo):
    def __init__(self, modelo, consumo):
        self.__modelo = modelo  # Atributo privado para el modelo
        self.__consumo = consumo  # Atributo privado para el consumo

    def obtener_detalles(self):
        return f"Modelo: {self.__modelo}, Consumo: {self.__consumo} L/100km"

    def calcular_consumo(self, distancia):
        """Calcula el consumo de combustible para una distancia dada."""
        return (self.__consumo / 100) * distancia

if __name__ == "__main__":
    coche = Coche("Toyota Corolla", 6.5)  # Crear un coche con modelo y consumo
    print(coche.obtener_detalles())  # Imprimir detalles del coche
    distancia = 150  # Distancia en kilómetros
    consumo_real = coche.calcular_consumo(distancia)  # Calcular el consumo para una distancia
    print(f"Consumo para {distancia} km: {consumo_real:.2f} L")

