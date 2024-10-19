from Paquete import Paquete
from Cartero import Cartero
from Furgoneta import Furgoneta
from GestorEnvios import GestorEnvios

cartero = Cartero()
furgoneta = Furgoneta()

transportesDisponibles = [cartero, furgoneta]

paqueteLiviano = Paquete(3,23,30,15)
paquetePesado = Paquete(50,60,40,50)

gestor=GestorEnvios()

gestor.gestionarEnvio(transportesDisponibles, paqueteLiviano, 15)
gestor.gestionarEnvio(transportesDisponibles, paquetePesado, 25)


# Lo utilizado para "Trasnporte" fue una interfaz, 
# esto es debido a que Cartero y Furgoneta comparten la capacidad de llevar a cavo la accion de transportar y no las caracteristicas
#propias de un trasporte, un cartero no es un trasporte y la furgoneta si

#La abstraccion de paquete podria hacerse teniendo en cuenta los pesos de los paquetes.
#La clase abstracta tendria las subclases PaqueteLiviano y PaquetePesado.
#esto seria util porque podra evaluarse de antemano quien realizaria el envio, dejando para el cartero los livianos
#y para la furgoneta los pesados. Permitiria la reutilizacion de los paramametros y algun metodo en comun como get_dimensiones
# o algun otro tipo de informacion que podria ser necesaria en un futuro. En un futuro tambien podria implementarse una 
#subclase PaqueteIntermedio o PaqueteMuyPesado que se podria amoldar al sistema sin necesidad de modificar la clase padre