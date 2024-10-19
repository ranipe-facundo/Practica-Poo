class Plantilla:
    def __init__(self, usuario, pais_favorito, equipo_favorito):
        self.__usuario = usuario
        self.__pais_favorito = pais_favorito
        self.__equipo_favorito  = equipo_favorito
        self.__plantel = []

    def set_plantel(self, plantel):
        self.__plantel = plantel
            
    def __calcular_quimica(self):
        quimica = 0
        for i in self.__plantel:
            if str(i) == "especial":
                quimica += 100
                continue
            if self.__pais_favorito == i.get_pais() and self.__equipo_favorito == i.get_club():
                quimica += 100
                continue
            if self.__pais_favorito == i.get_pais() or self.__equipo_favorito == i.get_club():
                quimica += 80
        return int(quimica/11)
    
    def imprimir(self):
        print(f"{self.__usuario}\n")
        print(f"Quimica {self.__calcular_quimica()}")
        for i in self.__plantel:
            i.imprimir()
            print("------------------------------------")