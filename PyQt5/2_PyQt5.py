import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

def saludar():
    etiqueta.setText("¡Hola desde PyQt5!")

app = QApplication(sys.argv)

ventana = QWidget()
ventana.setWindowTitle("Botón y señal")
ventana.resize(300, 150)

layout = QVBoxLayout()

etiqueta = QLabel("Pulsa el botón")
boton = QPushButton("Saludar")
boton.clicked.connect(saludar)  # Conectamos la señal con la función

layout.addWidget(etiqueta)
layout.addWidget(boton)

ventana.setLayout(layout)
ventana.show()

sys.exit(app.exec_())

