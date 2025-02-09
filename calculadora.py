
import os
import math
import re
import sys
from PyQt6.QtWidgets import * 
from PyQt6 import uic  
from PyQt6.QtGui import QIcon

class pantalla(QMainWindow): # Se crea una clase por ventana
    def __init__(self): 
        super(pantalla, self).__init__() 
        file_name = '_internal/calculadora.ui'
        uic.loadUi(os.path.abspath(file_name), self)  # Cargamos la interfaz de Designer
        self.setWindowTitle("Calculadora") # Nombre de la Ventana al abrir la aplicación
        self.setWindowIcon(QIcon("_internal/calculadora_icon.ico"))
        self.operacion = "" 

        # Se conectan los botones de los numeros del 0 al 9
        for i in range(10):
            getattr(self, f'Bu{i}').clicked.connect(lambda _, num=i: self.pulsar_numero(num))

        # Se conenctan los operadores
        self.Bt_coma.clicked.connect(lambda: self.pulsar_operador("."))
        self.Bt_raiz.clicked.connect(lambda: self.pulsar_operador("√"))
        self.Bt_cos.clicked.connect(lambda: self.pulsar_operador("cos"))
        self.Bt_sen.clicked.connect(lambda: self.pulsar_operador("sen"))
        self.Bt_multi.clicked.connect(lambda: self.pulsar_operador("*"))
        self.Bt_sumar.clicked.connect(lambda: self.pulsar_operador("+"))
        self.Bt_restar.clicked.connect(lambda: self.pulsar_operador("-"))
        self.Bt_paren1.clicked.connect(lambda: self.pulsar_operador("("))
        self.Bt_paren2.clicked.connect(lambda: self.pulsar_operador(")"))
        self.Bt_dividir.clicked.connect(lambda: self.pulsar_operador("/"))
        self.Bt_elevar.clicked.connect(lambda: self.pulsar_operador("**"))
        self.Bt_porcentaje.clicked.connect(lambda: self.pulsar_operador("%"))

        # Se conectan los botones de funcionabilidad
        self.Bt_borrar.clicked.connect(self.borrar_todo)
        self.Bt_delete.clicked.connect(self.borrar_ultimo)
        self.Bt_igual.clicked.connect(self.calcular_resultado)
        self.Bt_papelera.clicked.connect(self.borrar_historial)


    def pulsar_numero(self, num):
        self.operacion += str(num) # Introduce un número a la operación
        self.actualizar_pantalla() # Actualiza la pantalla con ese número


    def pulsar_operador(self, operador):
        if self.operacion and self.operacion[-1] not in "+-*/" or operador in ["(", ")", "√", "sen", "cos"]:
            self.operacion += operador # Introduce un operardor a la operación
            self.actualizar_pantalla() # Actualiza la pantalla con ese operador


    def calcular_resultado(self):
        try:
            # Remplaza los signos con calculos matemáticos de la libreria math para que funcione eval()
            operacion = self.operacion
            operacion = operacion.replace("%", "/100")
            operacion = re.sub(r'√(\d+)', r'math.sqrt(\1)', operacion)
            operacion = re.sub(r'sen(\d+)', r'math.sin(\1)', operacion)
            operacion = re.sub(r'cos(\d+)', r'math.cos(\1)', operacion)

            if (self.contiene_signos()): # Si la expresión contiene signos se ejecutará, si no no hará el igual
                resultado = eval(operacion, {"math": math}) # Ejecuta la función eval con funcionabilidad de la librería math

                if self.notacion_cientifica(resultado=resultado): # si el resultado tiene más de 4 decimales se pondrá en notación científica
                    resultado_cientifico = "{:.4e}".format(resultado)
                    self.Le_pantalla.setText(str(resultado_cientifico))
                    self.agregar_historial(self.operacion, str(resultado_cientifico))
                    self.operacion = str(resultado_cientifico)
                else:
                    self.Le_pantalla.setText(str(resultado))
                    self.agregar_historial(self.operacion, str(resultado))
                    self.operacion = str(resultado)
        except:
            self.Le_pantalla.setText("SyntaxError") # Si eval no se ha podido ejecutar saltará la execepción y aparecerá SyntaxError
            self.operacion = ""


    def notacion_cientifica(self, resultado):
        if "." in str(resultado):
            if (len(str(resultado).split('.')[1]) > 4):
                return True
        return False


    def contiene_signos(self):
        signos = [".", "√", "cos", "sen", "*", "+", "-", "(", ")", "/", "**", "%"]
        for signo in signos:
            if signo in self.operacion:
                return True
        return False
    


    def borrar_todo(self):
        self.operacion = ""
        self.actualizar_pantalla()


    def borrar_ultimo(self):
        self.operacion = self.operacion[:-1]
        self.actualizar_pantalla()


    def actualizar_pantalla(self):
        self.Le_pantalla.setText(self.operacion if self.operacion else "0")


    def agregar_historial(self, operacion, resultado):
        self.Ta_Historial.setColumnCount(2) #Pone las columnas a 2
        self.Ta_Historial.setHorizontalHeaderLabels(["Operación", "Resultado"]) # Le da nombre a esas dos columnas
        row_count = self.Ta_Historial.rowCount() # Cuenta las filas
        self.Ta_Historial.insertRow(row_count) # Inserta una fila
        self.Ta_Historial.setItem(row_count, 0, QTableWidgetItem(operacion)) # Inserta la operación en la columna 1
        self.Ta_Historial.setItem(row_count, 1, QTableWidgetItem(str(resultado))) # Inserta el resultado en la columna 2


    def borrar_historial(self):
        while self.Ta_Historial.rowCount() > 0:
            self.Ta_Historial.removeRow(0)
            self.Ta_Historial.setColumnCount(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = pantalla()
    window.show()
    app.exec() 