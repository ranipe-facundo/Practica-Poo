from multiprocessing import Process
import time

class Numeros(Process): 
    def run(self):
        for i in range(1, 27):
            time.sleep(0.01)  # Retraso para visualizar mejor el paralelismo
            print(f'Número {i}')
        print("Termina la ejecución de imprimir_numeros")

class Letras(Process):
    def run(self):
        letras = 'ABCDEFGHIJKLMONPQRSTUVWXYZ'
        for letra in letras:
            time.sleep(0.01)  # Retraso para visualizar mejor el paralelismo
            print(f'Letra {letra}')
        print("termina ejecución de imprimir_letras")

if __name__ == '__main__':
    procesoNumeros = Numeros()
    procesoLetras = Letras()

    procesoNumeros.start()
    procesoLetras.start()

    # Esperar a que ambos procesos terminen antes de continuar
    procesoNumeros.join()
    procesoLetras.join()

    print("Termina la ejecución del programa.")
