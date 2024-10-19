from Electrodomestico import Electrodemstico
import random

class Heladera (Electrodemstico):
    def __init__(self, modelo, marca, color):
        super().__init__(modelo, marca, color)
        self.__capacidad_total_litro = random.randint(5,20)
        self.__capacidad_freezer_litro = 0
    
    def __str__(self):
        return (f"Precio: {self._precio}\nMarca: {self._marca}\nCapacidad total: {self.__capacidad_total_litro} litros")