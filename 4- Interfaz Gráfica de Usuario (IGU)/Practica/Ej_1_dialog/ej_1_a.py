import sys
from PyQt6.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QLabel

# Clase para el diálogo simple
class SimpleDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Crear y configurar el layout
        layout = QVBoxLayout()

        # Agregar una etiqueta con el texto al layout
        layout.addWidget(QLabel("¿Deseas continuar?"))

        # Crear el botón de OK y agregarlo al layout
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.on_ok_clicked)  # Conectar a una función que no cierra el diálogo
        layout.addWidget(ok_button)

        # Crear el botón de Cancelar y agregarlo al layout
        cancel_button = QPushButton("Cancelar")
        cancel_button.clicked.connect(self.on_cancel_clicked)  # Conectar a una función que no cierra el diálogo
        layout.addWidget(cancel_button)

        # Establecer el layout para el diálogo
        self.setLayout(layout)

    def on_ok_clicked(self):
        # Acción cuando se presiona "OK" (no cierra la ventana)
        pass

    def on_cancel_clicked(self):
        # Acción cuando se presiona "Cancelar" (no cierra la ventana)
        pass

# Función principal
def main():
    app = QApplication(sys.argv)

    # Crear y mostrar el diálogo
    dialog = SimpleDialog()
    dialog.exec()  # Mostrar el diálogo

    sys.exit(app.exec())

# Llamada directa a la función principal
main()
