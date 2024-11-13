class Empresa:
    def __init__(self, nombre_empresa, direccion):
        self.__nombre_empresa = nombre_empresa
        self.__direccion = direccion
        self.__empleados = []
    
    def set_nombre (self, nombre):
        self.__nombre = nombre
    def set_nombre_empresa (self, nombre_empresa):
        self.__direccion = nombre_empresa
    def agregar_empleado (self, empleado):
        self.__empleados.append(empleado)
    
    def get_nombre_empresa(self):
        return self.__nombre_empresa
    def get_direccion(self):
        return self.__direccion
    def get_empleados(self):
        return self.__empleados

    def cantidad_empleados (self):
        cant_empleados = 0
        for i in self.get_empleados():
            cant_empleados += 1
        return cant_empleados

    def __str__(self):
        print(f"Empresa {self.get_nombre_empresa()}")
        for empleado in self.get_empleados():
            print(empleado)
        return f""