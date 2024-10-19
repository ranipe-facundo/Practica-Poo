class Empresa:
    def __init__(self, nombre, direccion):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__empleados = []

    def get_nombre(self):
        return self.__nombre
    def get_direccion(self):
        return self.__direccion
    def get_empleados(self):
        return self.__empleados

    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_direccion(self, direccion):
        self.__direccion = direccion
    def set_empleados(self, empleados):
        self.__empleados = empleados
        
    def aniadir_empleado(self, empleado):
        self.__empleados.append(empleado)
    
    def total_empleados(self):
        cant_empleados = 0
        for i in self.__empleados:
            cant_empleados += 1
        return cant_empleados
    
    def imprimir(self):
        print(f"Empresa: {self.__nombre}")
        print(f"Dirección: {self.__direccion}")
        print ("Empleados:")
        for i in self.__empleados:
            i.imprimir()
            print("--------------------------------")