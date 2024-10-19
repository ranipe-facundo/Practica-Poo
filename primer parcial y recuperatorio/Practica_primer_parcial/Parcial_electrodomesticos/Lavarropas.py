from Electrodomestico import Electrodemstico
import random

class Lavarropas(Electrodemstico):
    def __init__(self, modelo, marca, color):
        super().__init__(modelo, marca, color)
        self.__capacidad_kilos = random.randint(5,50)
        self.__carga_frontal = False

    def __str__(self):
        return (f"Precio: {self._precio}\nMarca: {self._marca}\nCapacidad: {self.__capacidad_kilos} kilos")