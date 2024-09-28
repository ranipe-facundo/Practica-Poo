#Genere 10 lavarropas, 10 cocinas y 10 heladeras. Los modelos deben ser únicos y el
#precio debe ser random. El resto de los datos no tiene exigencias particulares.
#Imprima un listado de recomendados
#
#    -En Cocinas 
#    ■   3 de ellas de forma aleatoria, no repetidas. 
#        Debe mostrar precio, marca y si es eléctrica o no.
#    -En heladeras 
#    ■   3 de ellas en forma aleatoria, no repetidas. 
#        Debe mostrar precio, marca y capacidad total en litros.
#    En lavarropas 
#    ■   3 de ellos en forma aleatoria, no repetidos. 
#    Debe mostrar precio, marca y capacidad en kilogramos.
#        
#    General - Primeros recomendados 
#    ■    3 productos aleatorios no repetidos que pueden ser de cualquier tipo 
#    ● Debe mostrar su información

import random
from Cocina import Cocina
from Heladera import Heladera
from Lavarropas import Lavarropas

def generar_lista_10_lavarropas():
    lista_lavarropas = []
    contador = 0
    for i in range(10):
        contador += 1
        modelo = f"lav_{contador}"
        lavarropas = Lavarropas(modelo,"Electrolux","Blanco")
        lista_lavarropas.append(lavarropas)
    return lista_lavarropas

def generar_lista_10_cocinas():
    lista_cocinas = []
    contador = 0
    for i in range(10):
        contador += 1
        modelo = f"coc_{contador}"
        cocina = Cocina(modelo,"Gafa","Negro")
        lista_cocinas.append(cocina)
    return lista_cocinas

def generar_lista_10_heladeras():
    lista_heladeras = []
    contador = 0
    for i in range(10):
        contador += 1
        modelo = f"hela_{contador}"
        heladera = Heladera(modelo,"Samsung","Gris")
        lista_heladeras.append(heladera)
    return lista_heladeras

lista_lav = generar_lista_10_lavarropas()
lista_coc = generar_lista_10_cocinas()
lista_hel = generar_lista_10_heladeras()


def imprime_recomendados(lista_lav,lista_coc,lista_hel):
    def imprime_3_cocinas(lista_coc):
        print("====================================================")
        print("Recomendaciones cocinas:")
        random.shuffle(lista_coc)
        for i in range(3):
            print(f"== Cocina {i+1} ==")
            print(lista_coc[i])
    
    def imprime_3_heladeras(lista_hel):
        print("====================================================")
        print("Recomendaciones heladeras:")
        random.shuffle(lista_hel)
        for i in range(3):
            print(f"== Heladera {i+1} ==")
            print(lista_hel[i])
    
    def imprime_3_lavarropas(lista_lav):
        print("====================================================")
        print("Recomendaciones lavarropas:")
        random.shuffle(lista_lav)
        for i in range(3):
            print(f"== Heladera {i+1} ==")
            print(lista_lav[i])
            
    print("Recomendaciones de 3 productos por tipo:")
    imprime_3_cocinas(lista_coc)
    imprime_3_heladeras(lista_hel)
    imprime_3_lavarropas(lista_lav)

imprime_recomendados(lista_lav,lista_coc,lista_hel)