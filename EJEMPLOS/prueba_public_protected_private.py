class Demo:

    def public(self):
        print("Esto es publico!")

    def _protected(self):
        print('Solo los hijos e instancias del padre pueden usarlo!')

    def __privado(self):
        print('Esto es privado!')

class Child(Demo):
    def pase(self):
        pass
#    def __secret(self):
#        print('No puedo contarte!')

demo = Demo() #pruebas con una istancia del padre
#demo.public()
#demo._protected()
#demo.__privado() # tira error

hijo = Child()
#hijo.public()
#hijo._protected()
#hijo.__privado() # tira error