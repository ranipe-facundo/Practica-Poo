from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class BuilderTorta(ABC):
    
    @property
    @abstractmethod
    def torta(self) -> None:
        pass
    
    @abstractmethod
    def torta(self) -> None:
        pass
    
    @abstractmethod
    def set_masa_vainilla(self)-> None:
        pass
    
    @abstractmethod
    def set_relleno_crema(self)-> None:
        pass
    
    @abstractmethod
    def set_masa_coco(self)-> None:
        pass
    
    @abstractmethod
    def set_relleno_fruta(self)-> None:
        pass
    
    @abstractmethod
    def set_masa_nueva(self, masa_nueva):
        pass
    
    @abstractmethod
    def set_relleno_nuevo(self, masa_nueva):
        pass

class ConcreteBuilderTorta(BuilderTorta):
    
    def __init__(self) -> None:
        self.reset()
        
    def reset(self) -> None:
        self._torta = Torta()

    @property
    def torta(self) -> Torta:
        torta = self._torta
        self.reset()
        return torta
    
    def set_masa_vainilla(self)-> None:
        self._torta.masa = "Vainilla"
    
    def set_relleno_crema(self)-> None:
        self._torta.relleno = "Crema"
        
    def set_masa_coco(self)-> None:
        self._torta.masa = "Coco"
    
    def set_relleno_fruta(self)-> None:
        self._torta.relleno = "Fruta"
    
    def set_masa_nueva(self, masa_nueva):
        self._torta.masa = masa_nueva
    
    def set_relleno_nuevo(self, relleno_nuevo):
        self._torta.relleno = relleno_nuevo



class Torta():
    def __init__(self) -> None:
        self.masa = ""
        self.relleno = ""

    def imprimir(self):
        print("Caracteristicas de la torta:")
        print (f'Masa: {self.masa}')
        print (f'Relleno: {self.relleno}')


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> BuilderTorta:
        return self._builder

    @builder.setter
    def builder(self, builder: BuilderTorta) -> None:
        self._builder = builder
    
    def build_torta_de_vainilla(self) -> None:
        self.builder.set_masa_vainilla()
        self.builder.set_relleno_crema()
    
    def build_torta_de_coco(self) -> None:
        self.builder.set_masa_coco()
        self.builder.set_relleno_fruta()
    
    def build_torta_nueva(self) -> None:
        self.builder.set_masa_nueva("Chocolate")
        self.builder.set_masa_nueva("Dulce de leche")

director = Director()
builder = ConcreteBuilderTorta()
director.builder = builder

director.build_torta_de_vainilla()
trota_de_vainilla = builder.torta
trota_de_vainilla.imprimir()
print("---------------------------------")
director.build_torta_de_coco()
trota_de_coco = builder.torta
trota_de_coco.imprimir()
print("---------------------------------")
director.build_torta_nueva()
trota_de_chocolate = builder.torta
trota_de_chocolate.imprimir()