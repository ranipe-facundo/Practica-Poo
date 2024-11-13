class Calculadora:
    def sumar(self, *args):
        return sum(args)  # Suma todos los argumentos que se pasen

# Uso
calc = Calculadora()
print(calc.sumar(1, 2))         # Suma de dos números
print(calc.sumar(1, 2, 3, 4))   # Suma de cuatro números

class lista_numeors:
    def __init__(self, lista = []):
        self.__lista = lista

    def agregar_nemros_lista(self,*args):
        self.__lista.append(args)
    
    def get_lista(self):
        return self.__lista
    
lista = lista_numeors()

lista.agregar_nemros_lista(65,88,96,95,4,4,5,948,84,4,4,4,54,4,654,)

for i in lista.get_lista():
    print(i)