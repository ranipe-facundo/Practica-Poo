class Empresa:
    def __init__(self, nombre, direccion):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__empleados = []
    
    def set_nombre (self, nombre):
        self.__nombre = nombre
    def set_nombre (self, direccion):
        self.__direccion = direccion
    def agregar_empleado (self, empleado):
        self.__empleados.append(empleado)
    
    def get_nombre(self):
        return self.__nombre
    def get_direccion(self):
        return self.__direccion
    def get_empleados(self):
        return self.__empleados

    def cantidad_empleados (self):
        cant_empleados = 0
        for i in self.get_empleados():
            cant_empleados += 1
        return cant_empleados
    
    def imprime_empleados(self):
        for i in self.get_empleados():
            print("==================================================")
            i.imprime_empleado()