class GestorEnvios():
        
    def gestionarEnvio(self,transportesDisponibles, paquete, distancia):
        if paquete.getPeso() > paquete.pesoVolumetrico():
            pesoPaquete = paquete.getPeso()
        else:
            pesoPaquete = paquete.pesoVolumetrico()
        masEfectivo = 0
        for i in transportesDisponibles:
            if i.tansportarPaquete(distancia,pesoPaquete) == -1:
                print(f"Paquete demasiado pesado para el {str(i)} ")
            else:
                print(f"Este transporte tarda {i.calcularTiempo(distancia)}hs con un costo de ${i.costo(distancia)}, indicador de costo de transporte {i.tansportarPaquete(distancia, pesoPaquete)}.")
# faltaria comparar y mostrar cual es la mejor opcion
