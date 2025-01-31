
import os
import sys
from PyQt6.QtWidgets import * # Librerías de los componentes
from PyQt6 import uic  # Librería para trabajar con el archivo de la interfaz

 
class pantalla(QMainWindow): # Se crea una clase por ventana
    def __init__(self): 
        super(pantalla, self).__init__() # Reservamos un espacio en memoria para la clase
        file_name = 'calculadora.ui'
        uic.loadUi(os.path.abspath(file_name), self)  # Cargamos la interfaz de Designer
        
       

        # Cargamos la interfaz de Designer
        self.setWindowTitle("Calculadora") # Nombre de la Ventana al abrir la aplicación
        self.Bt_igual.clicked.connect(self.sumar) # nombre del componente.evento(clicked).connect(self.<funcion>)

# A partir de aquí se escribe la lógica los componentes de la interfaz
    def sumar(self):
        try:
            print("hola")  
        except:
            QMessageBox.critical(self,'Error', 'Verifique los datos de entrada')

    def restar(self):
        try:
            print("adios")
        except:
            QMessageBox.critical(self,'Error', 'Verifique los datos de entrada')
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = pantalla()
    window.show()
    app.exec() 