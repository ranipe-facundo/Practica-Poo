import threading
import time

# Se definen los metodos a los que se les asignara un thread

def imprimir_numeros():
    for i in range (1,27):
        #time.sleep(0.5) #Con esta espera puedo lograr que se imprima un bucle y despues el otro, uno a uno
        print (f'Número {i}')
    print ("Termina la ejecucion de imprimir_numeros")

def imprimir_letras():
    letras = 'ABCDEFGHIJKLMONPQRSTUVWXYZ'
    for letra in letras:
        #time.sleep(0.5)
        print(f'Letra {letra}')
    print ("termina ejecucion de imprimir_letras")

# Se crean e inician los hilos correctamente
thread1 = threading.Thread(target=imprimir_numeros)  # Instancia el hilo con su método
thread2 = threading.Thread(target=imprimir_letras)   # Instancia el hilo con su método

# Iniciar los hilos
thread1.start()
thread2.start()

# Opcionalmente, esperar a que ambos hilos terminen
thread1.join() # Los join asegurar que el hilo termine antes de que el programa continúe
thread2.join()
#El join no me asegura que el hilo 1 hace una iteracion de bucle y luego empieza la primera iteracion del otro bucle, 
#para lograr eso, se puede dejar un tiempo despues de cada iteracion --> time.sleep(0.5)

print("Termina la ejecucion del programa")