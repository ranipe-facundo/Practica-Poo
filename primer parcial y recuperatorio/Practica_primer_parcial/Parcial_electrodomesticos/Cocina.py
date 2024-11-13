from Electrodomestico import Electrodemstico

class Cocina(Electrodemstico):
    def __init__(self, modelo, marca, color):
        super().__init__(modelo, marca, color)
        self.__es_electrica = False # Este va privado porque no tien ningun hijo que lo utiliza
    
    def __str__(self):
        return (f"Precio: {self._precio}\nMarca: {self._marca}\nElectrica: {self.__es_electrica}")
