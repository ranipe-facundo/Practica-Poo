from ConstructorDeTortaCoco import ConstructorDeTortaCoco
from ConstructorDeTortaVainilla import ConstructorDeTortaVainilla
from DirectorTorta import DirectorDeTorta

constructor_de_torta = ConstructorDeTortaVainilla()
director = DirectorDeTorta(constructor_de_torta)

director.construir_torta_vainilla()
torta_vainilla = director.get_torta()

constructor_de_torta = ConstructorDeTortaCoco()
director = DirectorDeTorta(constructor_de_torta)

director.construir_torta_coco()
torta_coco = director.get_torta()

torta_vainilla.imprimir()
torta_coco.imprimir()