from threading import Thread

class Letras(Thread):

    def run(self):
        letras = 'ABCDEEFGHIJKLMNÑOPQRSTUVWXYZ'
        for letra in letras:
            print(self.name+" Letra: "+letra)
        print(self.name+" termina ejecución de imprimir_letras")

class Numeros(Thread):
    
    def run(self):
        for i in range(1, 10):
            print(self.name+" Número: "+str(i))
        print(self.name+" termina ejecución de imprimir_numeros")

#for i in range(0,5):
#    Letras().start()
#    Numeros().start()

# que sucede si saco los join?
#print("termina ejecución de programa") 


varLetras = Letras()
varNumeros = Numeros()

#varLetras.start()
#varNumeros.start()

varLetras.run()
varNumeros.start()
varNumeros.join()

