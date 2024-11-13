# Ejemplo de uso

from hija_telefono import Telefono

telefono = Telefono("Samsung", "Galaxy S21", "+5491122334455")
print(telefono.mostrar_info())  # Muestra el estado actual y la información del teléfono (apagado)
telefono.encender()  # Enciende el teléfono
telefono.hacer_llamada("+5491188776655")  # Hace una llamada a otro número
print(telefono.mostrar_info())  # Muestra la información del teléfono cuando está encendido