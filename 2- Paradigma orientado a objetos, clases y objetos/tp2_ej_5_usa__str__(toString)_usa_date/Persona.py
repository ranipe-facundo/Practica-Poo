from datetime import date
import math

class Persona:
    # Constructor
    def __init__(self, nombre, apellido, fecha_nacimiento):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_nacimiento = fecha_nacimiento # Año, Mes, Día
    
    #getters
    def get_nombre (self):
        return self.__nombre
    def get_apellido (self):
        return self.__apellido
    def get_fecha_nacimiento (self):
        return self.__fecha_nacimiento
    
    #setters
    def set_nombre (self, nombre):
        self.__nombre = nombre
    def set_apellido (self, apellido):
        self.__apellido = apellido
    
    #Devuelve mensaje de error si está mal ingresada la fecha, no tendria que usarlo porque yo soy el que define la fecha
    def set_fecha_nacimiento(self, fecha_nacimiento):
        if isinstance(fecha_nacimiento, date):
            self.__fecha_nacimiento = fecha_nacimiento
        else:
            raise ValueError("La fecha de nacimiento debe ser de tipo date")
    
    #Devuelve la edad calculada segun la fecha de nacimiento
    def calcula_edad (self):
        fecha_actual = date.today()
        nacimiento = self.get_fecha_nacimiento()
        años = (fecha_actual - nacimiento)
        años = años.days/365
        años = math.floor(años)
        return años
    
    #Es lo que pide como toString. Con esto puedo usar el print con el objeto y que imprima lo que quiero
    def __str__(self):
        # Representación en cadena de la persona
        return (f'====================================================\n'
                f'Nombre: {self.__nombre} {self.__apellido}\n'
                f'Fecha de Nacimiento: {self.__fecha_nacimiento.strftime("%d/%m/%Y")}\n'
                f'Edad: {self.calcula_edad()}')
    
