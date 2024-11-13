#   personas es importante conocer su edad, sexo, si estudia y si trabaja.
class Persona:
    def __init__(self, nombre , edad, sexo, estudia, trabaja):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__estudia = estudia
        self.__trabaja = trabaja
        self.__permitido_trabajar = self.permitido_trabajar()
        self.__permitido_manejar_vehiculo_particular = self.permitido_manejar_vehiculo_particular()

    def get_nombre (self): 
        return self.__nombre
    def get_edad (self): 
        return self.__edad
    def get_sexo (self): # no se usa en el main, no seria necesario agregarlo
        return self.__sexo
    def get_estudia (self): # no se usa en el main, no seria necesario agregarlo
        return self.__estudia
    def get_trabaja (self):
        return self.__trabaja
    def get_permitido_trabajar (self):
        return self.__permitido_trabajar
    def get_manejar_vehiculo_particular (self):
        return self.__permitido_manejar_vehiculo_particular

    def permitido_trabajar (self):
        if self.get_edad() > 15:
            return True
        else:
            return False
    def permitido_manejar_vehiculo_particular (self):
        if self.get_edad() > 16:
            return True
        else:
            return False
    
    def __str__(self):
        permitido_trabajar_str = f"Tiene permitido tabajar?: {'sí' if self.get_permitido_trabajar() else 'no'}"
        permitido_manejar_vehiculo_particular_str = f"Tiene permitido manejar un vehículo particular?: {'sí' if self.get_manejar_vehiculo_particular() else 'no'}"
        estudia_str = f"Estudia?: {'sí' if self.get_estudia() else 'no'}"
        trabaja_str = f"Trabaja?: {'sí' if self.get_trabaja() else 'no'}"
        return f"Nombre: {self.get_nombre()}, Edad: {self.get_edad()}, Sexo: {self.get_sexo()}, {trabaja_str}, {estudia_str}, {permitido_trabajar_str}, {permitido_manejar_vehiculo_particular_str} "

#empleado_1 = Persona("Facundo Rañipe", 50, 'M', False, True)
#print(empleado_1)

#persona_R1 = Persona(38, 'M', False, True)

#print (f"Permitido trabajar: {persona_R1.get_permitido_trabajar()}, Permitido manejar: {persona_R1.get_manejar_vehiculo_particular()}")

## Los setters de Persona son solo necesarios si se utiliza el @clasmethod que cree una instancia de Persona con atributos vacios
## Con el constructor __init__ ya son establecidos los valores a la hora de instanciar
    #def set_edad (self,edad):
    #    self.__edad = edad
    #def set_sexo (self,sexo):
    #    self.__sexo = sexo
    #def set_estudia (self,estudia):
    #    self.__estudia = estudia
    #def set_trabaja (self,trabaja):
    #    self.__trabaja = trabaja

#    @classmethod
#    def Persona(cls):
#        Persona = cls.__new__(cls)
#        Persona.__edad = ''
#        Persona.__sexo = ''
#        Persona.__estudia = False
#        Persona.__trabaja = False
#        return Persona