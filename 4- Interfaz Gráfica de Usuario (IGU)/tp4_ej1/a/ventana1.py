import sys
from PyQt6.QtCore import QSize
from PyQt6 import QtCore, QtGui, QtWidgets

class Ventana1(object):
    def setupUi(self, Tp3Ejercicio1):
        Tp3Ejercicio1.setObjectName("Tp3Ejercicio1")
        Tp3Ejercicio1.setFixedSize(QSize(500, 250))
        self.centralwidget = QtWidgets.QWidget(parent=Tp3Ejercicio1)
        self.centralwidget.setObjectName("centralwidget")
        self.boton1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.boton1.setGeometry(QtCore.QRect(180, 190, 131, 31))
        self.boton1.setAutoDefault(False)
        self.boton1.setObjectName("boton1")
        self.Etiqueta1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.Etiqueta1.setGeometry(QtCore.QRect(170, 70, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Etiqueta1.setFont(font)
        self.Etiqueta1.setObjectName("Etiqueta1")
        Tp3Ejercicio1.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=Tp3Ejercicio1)
        self.statusbar.setObjectName("statusbar")
        Tp3Ejercicio1.setStatusBar(self.statusbar)

        self.retranslateUi(Tp3Ejercicio1)
        QtCore.QMetaObject.connectSlotsByName(Tp3Ejercicio1)

    def retranslateUi(self, Tp3Ejercicio1):
        _translate = QtCore.QCoreApplication.translate
        Tp3Ejercicio1.setWindowTitle(_translate("Ventana 1", "Ventana 1"))
        self.boton1.setText(_translate("Tp3Ejercicio1", "Presione"))
        self.Etiqueta1.setText(_translate("Tp3Ejercicio1", "Haga click"))

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tp3Ejercicio1 = QtWidgets.QMainWindow()
    ui = Ventana1()
    ui.setupUi(Tp3Ejercicio1)
    Tp3Ejercicio1.show()
    sys.exit(app.exec())
"""