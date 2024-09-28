from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import sys

class dialog_simple:
    
    def __init__(self,nombre) -> None:
        self.__nombre = nombre
    
    
    def crea_y_muestra_dialog ():
        app = QApplication(sys.argv)
        window = QMainWindow()
        window.show()
        app.exec()
        

#app = QApplication(sys.argv)
#window = QMainWindow()
#window.show()  # las ventanas por defecto no se muestran, hay que mostrarlas
# Comienza el loop de eventos.
#app.exec()

dialogo = dialog_simple
dialogo.crea_y_muestra_dialog()
