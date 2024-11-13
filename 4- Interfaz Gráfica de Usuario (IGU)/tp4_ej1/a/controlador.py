from PyQt6 import QtWidgets
from ventana1 import Ventana1
from ventana2 import Ventana2

class Controlador(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Crea las instancias de las ventanas
        self.ventana1_ui = Ventana1()
        self.ventana2_ui = Ventana2()

        # Crear una instancia del QMainWindow para la primera ventana
        self.ventana1_mainwindow = QtWidgets.QMainWindow()
        
        # Configura la ventana 1 como la primera a mostrar
        self.ventana1_setup()
        
    def ventana1_setup(self):
        # Llama al método que configura la UI de la primera ventana
        self.ventana1_ui.setupUi(self.ventana1_mainwindow)
        
        # Muestra la ventana 1
        self.ventana1_mainwindow.show()
        
        # Conecta el botón de la primera ventana con la función para cambiar a la segunda ventana
        self.ventana1_ui.boton1.clicked.connect(self.mostrar_ventana2)

    def mostrar_ventana2(self):
        # Oculta la ventana 1
        #self.ventana1_mainwindow.close()

        # Crear una instancia del QMainWindow para la segunda ventana
        self.ventana2_mainwindow = QtWidgets.QMainWindow()

        # Llama al método que configura la UI de la segunda ventana
        self.ventana2_ui.setupUi(self.ventana2_mainwindow)

        # Muestra la ventana 2
        self.ventana2_mainwindow.show()

        # Conecta los botones de la ventana 2 a otras funciones
        self.ventana2_ui.BotonCancelar.clicked.connect(self.cancelar)
        self.ventana2_ui.BotonAceptar.clicked.connect(self.aceptar)

    def cancelar(self):
        # Acción para el botón "Cancelar"
        print("Acción de cancelar")  # Aquí puedes poner la acción que prefieras
        # No se cierra la ventana ni la aplicación

    def aceptar(self):
        # Acción para el botón "Aceptar"
        print("Acción de aceptar")  # Aquí puedes poner la acción que prefieras
        # No se cierra la ventana ni la aplicación

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     controlador = Controlador()
#     sys.exit(app.exec())
