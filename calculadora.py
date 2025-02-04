
import os
import math
import re
import sys
from PyQt6.QtWidgets import * 
from PyQt6 import uic  

class pantalla(QMainWindow): # Se crea una clase por ventana
    def __init__(self): 
        super(pantalla, self).__init__() 
        file_name = 'calculadora.ui'
        uic.loadUi(os.path.abspath(file_name), self)  # Cargamos la interfaz de Designer
        self.setWindowTitle("Calculadora") # Nombre de la Ventana al abrir la aplicación
        self.expresion = "" 

        for i in range(10):
            getattr(self, f'Bu{i}').clicked.connect(lambda _, num=i: self.pulsar_numero(num))

        self.Bt_coma.clicked.connect(lambda: self.pulsar_operador("."))
        self.Bt_raiz.clicked.connect(lambda: self.pulsar_operador("√"))
        self.Bt_multi.clicked.connect(lambda: self.pulsar_operador("*"))
        self.Bt_sumar.clicked.connect(lambda: self.pulsar_operador("+"))
        self.Bt_restar.clicked.connect(lambda: self.pulsar_operador("-"))
        self.Bt_paren1.clicked.connect(lambda: self.pulsar_operador("("))
        self.Bt_paren2.clicked.connect(lambda: self.pulsar_operador(")"))
        self.Bt_dividir.clicked.connect(lambda: self.pulsar_operador("/"))
        self.Bt_elevar.clicked.connect(lambda: self.pulsar_operador("**"))
        self.Bt_porcentaje.clicked.connect(lambda: self.pulsar_operador("%"))

        self.Bt_borrar.clicked.connect(self.borrar_todo)
        self.Bt_delete.clicked.connect(self.borrar_ultimo)
        self.Bt_igual.clicked.connect(self.calcular_resultado)


    def pulsar_numero(self, num):
        self.expresion += str(num)
        self.actualizar_pantalla()


    def pulsar_operador(self, operador):
        if self.expresion and self.expresion[-1] not in "+-*/" or operador in ["(", ")", "√"]:
            self.expresion += operador
            self.actualizar_pantalla()


    def calcular_resultado(self):
        try:
            expresion = self.expresion
            expresion = self.expresion.replace("%", "/100")
            expresion = re.sub(r'√(\d+)', r'math.sqrt(\1)', self.expresion)
            if (len(self.expresion) > 1):
                resultado = eval(expresion, {"math": math})
                self.Le_pantalla.setText(str(resultado))
                self.agregar_historial(self.expresion, str(resultado))
                self.expresion = str(resultado)
        except:
            self.Le_pantalla.setText("Err")
            self.expresion = ""


    def borrar_todo(self):
        self.expresion = ""
        self.actualizar_pantalla()


    def borrar_ultimo(self):
        self.expresion = self.expresion[:-1]
        self.actualizar_pantalla()


    def actualizar_pantalla(self):
        self.Le_pantalla.setText(self.expresion if self.expresion else "0")


    def agregar_historial(self, expresion, resultado):
        self.Ta_Historial.setColumnCount(2)
        row_count = self.Ta_Historial.rowCount()
        self.Ta_Historial.insertRow(row_count)
        self.Ta_Historial.setItem(row_count, 0, QTableWidgetItem(expresion))
        self.Ta_Historial.setItem(row_count, 1, QTableWidgetItem(str(resultado)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = pantalla()
    window.show()
    app.exec() 