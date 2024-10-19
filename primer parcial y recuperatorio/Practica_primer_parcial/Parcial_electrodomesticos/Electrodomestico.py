from abc import ABC
import random

def precio_random():
    return random.randint(0,100000)

class Electrodemstico(ABC):
    def __init__(self, modelo, marca, color):
        self._modelo = modelo
        self._precio = precio_random()
        self._marca = marca
        self._color = color