class DispositivoElectronico:
    def __init__(self, marca, modelo):
        self.marca = marca  # Público: La marca es accesible desde fuera.
        self._modelo = modelo  # Protegido: El modelo es accesible solo en clases derivadas o internas.
        self.__encendido = False  # Privado: Estado del dispositivo solo accesible dentro de la clase.
    
    # Método para encender el dispositivo (accede al atributo privado)
    def encender(self):
        self.__encendido = True
        print(f"El {self._modelo} está ahora encendido.")
    
    # Método para apagar el dispositivo (accede al atributo privado)
    def apagar(self):
        self.__encendido = False
        print(f"El {self._modelo} está ahora apagado.")
    
    # Método para mostrar la información del dispositivo (incluye acceso a atributos privados y protegidos)
    def mostrar_info(self):
        estado = "encendido" if self.__encendido else "apagado"
        return f"Dispositivo {self.marca} {self._modelo}, actualmente {estado}."