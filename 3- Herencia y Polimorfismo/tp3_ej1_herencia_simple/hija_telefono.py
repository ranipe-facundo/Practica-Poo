# Clase hija: Telefono
# Rol: Esta clase hereda de DispositivoElectronico, especializándose en teléfonos.
# Motivo: El teléfono es un tipo específico de dispositivo electrónico, y es correcto que 
# la herencia gestione los niveles de acceso, protegiendo información sensible como el número de teléfono.

from padre_DispositivoElectronico import DispositivoElectronico

class Telefono(DispositivoElectronico):
    def __init__(self, marca, modelo, numero_telefono):
        # Llamada al constructor de la clase base para inicializar marca y modelo
        super().__init__(marca, modelo)
        self.__numero_telefono = numero_telefono  # Privado: El número de teléfono es sensible y no debe ser modificado externamente.
    
    # Método para hacer una llamada (accede a atributo privado de la clase base y propio)
    def hacer_llamada(self, numero_destino):
        if self._DispositivoElectronico__encendido:  # Acceso a atributo privado de la clase base usando name mangling.
            print(f"Llamando al {numero_destino} desde {self.__numero_telefono}...")
        else:
            print("El teléfono está apagado. No se puede hacer una llamada.")
    
    # Método para mostrar la información extendida del teléfono (incluye número privado)
    def mostrar_info(self):
        info_base = super().mostrar_info()  # Obtener la información de la clase base
        return f"{info_base} Número de teléfono: {self.__numero_telefono}."