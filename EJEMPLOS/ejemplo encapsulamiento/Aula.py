class Aula:
    def __init__(self,alumno1,alumno2):
        self.__alumno1 = alumno1
        self.__alumno3 = alumno2
    
    def mostrar_edad_1(self):
        print (self.__alumno1._edad)