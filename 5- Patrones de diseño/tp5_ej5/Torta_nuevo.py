# Tener en cuenta que no es correcto hacer todo en el mismo codigo, sino que es necesario separar las 
# partes Builder, Class, Director y Main en archivos distintos
# 
# Builder + ConcreteBuilder:
#       Builder: Interface con los metodos necesarios
#               @property     //la property no esta pensada para uso interno, sino para uso externo a la clase
#               @abstractmethod                     <--- Todo esto no estoy seguro si va
#               def smartphone(self) -> None:
#                   pass   
#                Debe incluir el reset tambien
#       ConcreteBuilder: se desarrollan los metodos del builder
#                        se desarrolla el reset en privado si no hay otras clases que hereden de él
#                        se desarrolla el @property     <--- preguntar si esto se mantienetambien
#                        
# Class: Clase base de los que va a producir con el director y el builder
#        Los atributos nunca son publicos
#        Se pueden agregar metodos haciendo referencia siempre a los metodos privados
#        
# Director: Establece el contenido, tanto de metodos y atributos que la clase va a tener
#           el builder va en privado --> self.__builder = None
#           se establece la property que devuelve un , es un getter, siempre es publica y es para que otros objetos usen mi builder solo se declara si es necesaria
#           se hace llamado al builder de forma privada --> self.__builder.nombreDelMetedo()

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class BuilderTorta(ABC):
    
    @property
    @abstractmethod
    def torta(self) -> None:
        pass
    
    @abstractmethod
    def reset(self) -> None:
        pass
    
    @abstractmethod 
    def set_masa(self, masa) -> None:
        pass
    
    @abstractmethod 
    def set_relleno(self, relleno) -> None:
        pass
    
class ConcreteBuilderTorta(BuilderTorta):
    def __init__(self) -> None:
        self.reset()
    
    def reset(self):
        self.__torta = Torta()
    
    @property
    def torta(self) -> Torta:
        torta = self.__torta
        self.reset()
        return torta
    
    def set_masa(self, masa) -> None:
        self.__torta.set_masa(masa)
    
    def set_relleno(self, relleno) -> None:
        self.__torta.set_relleno(relleno)

class Torta():
    def __init__(self):
        self.__masa = ""
        self.__relleno = ""
    
    def set_masa(self, masa):
        self.__masa = masa
    
    def set_relleno(self, relleno):
        self.__relleno = relleno
    
    def imprimir(self):
        print("Caracteristicas de la torta:")
        print(f"Masa: {self.__masa}")
        print(f"Relleno: {self.__relleno}")

class DirectorTorta():
    def __init__(self) -> None:
        self.__builder = None
    
    @property 
    def builder(self) -> BuilderTorta:
        return self.__builder
    
    @builder.setter
    def builder(self, builder: BuilderTorta) -> None:
        self.__builder = builder
    
    def buildTortaVainilla (self):
        self.__builder.set_masa("Vainilla")
        self.__builder.set_relleno("Crema")
    
    def buildTortaCoco (self):
        self.__builder.set_masa("Coco")
        self.__builder.set_relleno("Fruta")
    
    def buildTorata(self, masa, relleno):
        self.__builder.set_masa(masa)
        self.__builder.set_relleno(relleno)

director = DirectorTorta()
builder = ConcreteBuilderTorta()
director.builder = builder

director.buildTortaVainilla()
builder.torta.imprimir()

director.buildTortaCoco()
builder.torta.imprimir()

director.buildTorata("Chocolate","Dulce de leche")
builder.torta.imprimir()

# preguntar como sería para que una variable tome el valor de "director.buildTorata"