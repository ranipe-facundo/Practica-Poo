class Impuesto:
    def __init__(self, nombre, monto, periodo, estado):
        self.__nombre = nombre
        self.__monto = monto
        self.__periodo = periodo
        self.__cobrado = False
        self.__comprobante = 0
        
        
    def validar_pago (self):
        self.__cobrado = True