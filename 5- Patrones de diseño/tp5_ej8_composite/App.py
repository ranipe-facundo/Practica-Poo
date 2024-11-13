from Archivo import Archivo
from Carpeta import Carpeta

#creo los archivos
archivo1 = Archivo("Archivo 1")
archivo2 = Archivo("Archivo 2")
archivo3 = Archivo("Archivo 3")
archivo4 = Archivo("Archivo 4")

#creo las carpetas
carpeta1 = Carpeta("Carpeta 1")
carpeta2 = Carpeta("Carpeta 2")
carpeta3 = Carpeta("Carpeta 3")

#agrego los elementos a las carpetas

carpeta1.agregar_elemnto(carpeta2)
carpeta1.agregar_elemnto(archivo3)


carpeta2.agregar_elemnto(archivo1)
carpeta2.agregar_elemnto(archivo2)

carpeta3.agregar_elemnto(archivo4)

carpeta1.imprimir()
