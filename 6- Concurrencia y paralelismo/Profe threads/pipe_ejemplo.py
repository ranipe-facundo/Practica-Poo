from  multiprocessing import Process, Pipe

class ProcesoEnvio(Process):
    def __init__(self, canal):
        super(ProcesoEnvio, self).__init__()
        self.canal = canal #parametro que recibe el pipe creado en el 

    def run(self):
        mensajes = ["Hola", "Alumnos","de", "POO"]
        for mensaje in mensajes:
            print(f"Enviando: {mensaje}")
            self.canal.send(mensaje) #.send() envia datos mediante el pipe asignado 
        self.canal.send(None)

class ProcesoRecepcion(Process):
    def __init__(self, canal):
        super(ProcesoRecepcion, self).__init__()
        self.canal = canal

    def run(self):
        mensaje = ""
        while mensaje is not None:
            mensaje = self.canal.recv()#.recv() recibe datos mediante el pipe asignado
            if mensaje is not None: 
                print(f"Recibido: {mensaje}")

if __name__ == '__main__':
    #inicializo 2 variables par aser usadas de parametros en la isntanciacin de los procesos que usan ppe, devuelve dos pipes conectadas siempre
    pipe_conn1, pipe_conn2 = Pipe() 

    # los pipes conectados se envian como parametro al creador de los Process para la transmision de datos
    proceso_envio = ProcesoEnvio(pipe_conn1)
    proceso_recepcion = ProcesoRecepcion(pipe_conn2)

    proceso_envio.start()
    proceso_recepcion.start()

    proceso_envio.join()
    proceso_recepcion.join()
    print("fin de la ejecución")
