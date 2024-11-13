from multiprocessing import Process, Queue 

class ProcesoProductor(Process):
    def __init__(self, cola):
        super().__init__()
        self.cola = cola #se ocupa un parametro tipo cola

    def run(self):
        for item in range(1, 6):
            self.cola.put(f'Dato {item}') #agrega elementos a la cola

class ProcesoConsumidor(Process):
    def __init__(self, cola): 
        #super(ProcesoConsumidor,self).__init__()
        #Process.__init__(self)
        super().__init__()
        self.cola = cola #se ocupa un parametro tipo cola

    def run(self):
        while not self.cola.empty():
            dato = self.cola.get() # saca el elemnto de la cola para imprimirlo
            print(f'Proceso Consumidor recibe: {dato}') 

if __name__ == '__main__':
    cola_compartida = Queue() #se crea la cola compartida 

    proceso_productor = ProcesoProductor(cola_compartida) #se usa la cola compartida para que los 2 procesos tengan acceso a ella
    proceso_consumidor = ProcesoConsumidor(cola_compartida)

    proceso_productor.start()
    proceso_consumidor.start()

    proceso_productor.join()
    proceso_consumidor.join()

    print("fin de los procesos")