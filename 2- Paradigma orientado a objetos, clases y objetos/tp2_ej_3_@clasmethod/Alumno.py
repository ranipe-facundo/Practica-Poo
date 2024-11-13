#class Alumno ():

#    __nombre = ''
#    __apellido = ''
#    dni = 0

#    def __init__(self):
#        pass

#    @classmethod
#    def iniciar_con_nom_ape(cls, nombre, apellido):
#        alumno = cls. __new__(cls)
#        alumno.__nombre = nombre
#        alumno.__apellido = apellido
#        return alumno

################ Corregido ###################

class Alumno: 
    #Constructor normal como lo venimos usando
    def __init__(self, nombre, apellido, dni):
        self.__nombre = nombre
        self.__apellido= apellido
        self.__dni = dni
        
    @classmethod #constructor alternativo que permite instanciar un Alumno sin darle atributos ya que estan predefinidos
    def Alumno(cls):
        return cls('', '', 0)

    
    @classmethod #constructor alternativo que permite instanciar un Alumno solo dandole los campos de nombre y apellido, dni está predefinido en 0
    def iniciar_con_nom_ape(cls, nombre, apellido):
        return cls(nombre, apellido, 0)

    @classmethod #constructor alternativo que permite instanciar un Alumno sin darle atributos ya que estan predefinidos
    def iniciar(cls):
        return cls('', '', 0)

## Setters
    def setNombre(self, nombre):
        self.__nombre = nombre
    def setApellido(self, apellido):
        self.__apellido = apellido
    def setDni(self, dni):
        self.__dni = dni
## Getters
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getDni(self):
        return self.__dni
    
    def getNombreYapellido (self):
        return self.__nombre, self.__apellido
        