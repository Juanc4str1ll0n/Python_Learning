# PyQt5 es un conjunto de bindings de Python para la biblioteca Qt5,
#  una herramienta potente para desarrollar interfaces gráficas (GUI).

#Cada aplicacion con PyQt5 sigue una estructura tipica:

import sys
from PyQt5.QtWidgets import QApplication, QWidget

# Paso 1: Crear la aplicación
app = QApplication(sys.argv)

# Paso 2: Crear una ventana
ventana = QWidget()
ventana.setWindowTitle("Mi primera app con PyQt5")
ventana.resize(300, 200)
ventana.show()

# Paso 3: Ejecutar la app
sys.exit(app.exec_())

# QApplication	Requerido para cualquier app Qt; gestiona el loop de eventos.
# QWidget	Clase base para todos los elementos visuales (botones, ventanas, etc.).
# QPushButton, QLabel, QLineEdit, etc.	Widgets específicos que puedes colocar en la ventana.
# QVBoxLayout, QHBoxLayout	Sistemas de distribución para organizar los widgets.
# QMainWindow	Ventana principal con barra de menú, barra de herramientas, etc.
# QDialog	Ventana secundaria o emergente, útil para formularios o confirmaciones.