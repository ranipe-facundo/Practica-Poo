from threading import Thread

class Numeros (Thread): 
# con el (Thread) estoy indicando que Letras es un thread y puedo usar las 
# acciones de los hilo directamente desde esta clase

    def run(self): #run define lo que hará el hilo cuando se ejecute
        for i in range (1,27):
        #time.sleep(0.5) #Con esta espera puedo lograr que se imprima un bucle y despues el otro, uno a uno
            print (f'Número {i}')
        print ("Termina la ejecucion de imprimir_numeros")

class Letras(Thread):

    def run(self):
        letras = 'ABCDEFGHIJKLMONPQRSTUVWXYZ'
        for letra in letras:
            #time.sleep(0.5)
            print(f'Letra {letra}')
        print ("termina ejecucion de imprimir_letras")

hiloNumeros = Numeros()
hiloLetras = Letras()

#for i in range (0,5):
#    Letras().start()
#    Numeros().start()

hiloNumeros.start() #Si acá uso .run, va a interpretar que es una llamada al metodo .run y se va a ejecutar completo antes de continuar (Como un metodo normal) 
hiloLetras.start()

#Estos join aseguran que se terminen de ejecutar los thread para poder continuar con el programa
hiloNumeros.join() 
hiloLetras.join()

print ("Termina la ejecucion del programa.")