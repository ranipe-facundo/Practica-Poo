import sys
from PyQt6 import QtWidgets
from controlador import Controlador  # Asegúrate de que "Controlador" esté en el archivo controlador.py

if __name__ == "__main__":
    # Crear la aplicación de PyQt
    app = QtWidgets.QApplication(sys.argv)

    # Crear una instancia del controlador
    controlador = Controlador()

    # Mostrar la primera ventana del controlador
    controlador.ventana1_mainwindow.show()

    # Ejecutar el bucle de eventos de la aplicación
    sys.exit(app.exec())
