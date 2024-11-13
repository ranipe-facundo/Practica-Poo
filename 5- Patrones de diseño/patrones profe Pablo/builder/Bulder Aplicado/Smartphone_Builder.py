#   BUILDERS

from Smartphone_Base import Smartphone
from abc import ABC, abstractmethod

class BuilderSmartphone(ABC):

    @property #El uso de @property en Python convierte un método en una propiedad, lo que permite acceder a él como si fuera un atributo en lugar de invocarlo como un método.
    @abstractmethod
    def smartphone(self) -> None:
        pass

    @abstractmethod
    def smartphone(self) -> None:
        pass

    @abstractmethod
    def produce_screen(self) -> None:
        pass

    @abstractmethod
    def produce_network(self) -> None:
        pass
    
    @abstractmethod
    def produce_bluetooth(self) -> None:
        pass

class ConcreteBuilderSmartphone(BuilderSmartphone):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._smartphone = Smartphone()

    @property
    def smartphone(self) -> Smartphone:
        smartphone = self._smartphone
        self.reset()
        return smartphone

    def produce_screen(self) -> None:
        self._smartphone.add("PANTALLA GORILLA GLASS etc..")

    def produce_network(self) -> None:
        self._smartphone.add("BANDA 5G")

    def produce_bluetooth(self) -> None:
        self._smartphone.add("BLUETOOTH")