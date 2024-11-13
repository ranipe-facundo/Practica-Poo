#import sys
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import QSize

class Ventana2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(QSize(373, 111))
        #MainWindow.resize(373, 111)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BotonCancelar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BotonCancelar.setGeometry(QtCore.QRect(280, 60, 80, 24))
        self.BotonCancelar.setObjectName("BotonCancelar")
        self.BotonAceptar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BotonAceptar.setGeometry(QtCore.QRect(190, 60, 80, 24))
        self.BotonAceptar.setObjectName("BotonAceptar")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 311, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Ventana 2", "Ventana 2"))
        self.BotonCancelar.setText(_translate("MainWindow", "Cancelar"))
        self.BotonAceptar.setText(_translate("MainWindow", "Aceptar"))
        self.label.setText(_translate("MainWindow", "Está seguro que quiere dar de baja al usuario?"))

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ventana2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
"""