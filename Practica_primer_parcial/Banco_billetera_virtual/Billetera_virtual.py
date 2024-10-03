from Cuenta import Cuenta
import random

class Billetera_virtual(Cuenta):
    def __init__(self, duenio):
        super().__init__(duenio)
        self.__cvu = random.randint(0,999)