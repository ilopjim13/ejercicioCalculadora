# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculadora.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLCDNumber, QMainWindow,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(452, 597)
        MainWindow.setStyleSheet(u"\n"
"\n"
"background-color:rgb(255, 224, 225)")
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.Botones = QWidget(MainWindow)
        self.Botones.setObjectName(u"Botones")
        self.LcdNumber = QLCDNumber(self.Botones)
        self.LcdNumber.setObjectName(u"LcdNumber")
        self.LcdNumber.setGeometry(QRect(10, 10, 341, 121))
        self.LcdNumber.setMaximumSize(QSize(341, 16777215))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        self.LcdNumber.setFont(font)
        self.Bt_borrar = QPushButton(self.Botones)
        self.Bt_borrar.setObjectName(u"Bt_borrar")
        self.Bt_borrar.setGeometry(QRect(10, 150, 71, 71))
        font1 = QFont()
        font1.setFamilies([u"Vrinda"])
        font1.setPointSize(22)
        font1.setBold(True)
        font1.setItalic(False)
        self.Bt_borrar.setFont(font1)
        self.Bt_borrar.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient(spread:pad x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 rgba(156,152,215,100), stop: 0.4 rgba(58,52,151,100), stop: 1.0 rgba(78,70,190,100));\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 35;\n"
"padding: 3px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"font:bold;\n"
"font-family:Vrinda;\n"
"}")
        self.Bt_porcentaje = QPushButton(self.Botones)
        self.Bt_porcentaje.setObjectName(u"Bt_porcentaje")
        self.Bt_porcentaje.setGeometry(QRect(100, 150, 71, 71))
        self.Bt_porcentaje.setFont(font1)
        self.Bt_porcentaje.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient(spread:pad x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 rgba(156,152,215,100), stop: 0.4 rgba(58,52,151,100), stop: 1.0 rgba(78,70,190,100));\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 35;;\n"
"padding: 3px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"font:bold;\n"
"font-family:Vrinda;\n"
"}")
        self.delete_2 = QPushButton(self.Botones)
        self.delete_2.setObjectName(u"delete_2")
        self.delete_2.setGeometry(QRect(190, 150, 71, 71))
        self.delete_2.setFont(font1)
        self.delete_2.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient(spread:pad x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 rgba(156,152,215,100), stop: 0.4 rgba(58,52,151,100), stop: 1.0 rgba(78,70,190,100));\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 35;;\n"
"padding: 3px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"font:bold;\n"
"font-family:Vrinda;\n"
"}")
        self.Bt_dividir = QPushButton(self.Botones)
        self.Bt_dividir.setObjectName(u"Bt_dividir")
        self.Bt_dividir.setGeometry(QRect(280, 150, 71, 71))
        font2 = QFont()
        font2.setFamilies([u"Vrinda"])
        font2.setPointSize(25)
        font2.setBold(True)
        font2.setItalic(False)
        self.Bt_dividir.setFont(font2)
        self.Bt_dividir.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient(spread:pad x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 rgba(156,152,215,100), stop: 0.4 rgba(58,52,151,100), stop: 1.0 rgba(78,70,190,100));\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 35;;\n"
"padding: 3px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"font:bold;\n"
"font-family:Vrinda;\n"
"}")
        self.Bu7 = QPushButton(self.Botones)
        self.Bu7.setObjectName(u"Bu7")
        self.Bu7.setGeometry(QRect(10, 240, 71, 71))
        self.Bu7.setFont(font1)
        self.Bu7.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient(spread:pad x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 rgba(156,152,215,100), stop: 0.4 rgba(58,52,151,100), stop: 1.0 rgba(78,70,190,100));\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 12;\n"
"padding: 3px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"font:bold;\n"
"font-family:Vrinda;\n"
"}")
        self.Bt_multi = QPushButton(self.Botones)
        self.Bt_multi.setObjectName(u"Bt_multi")
        self.Bt_multi.setGeometry(QRect(280, 240, 71, 71))
        self.Bt_multi.setFont(font1)
        self.Bt_multi.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient(spread:pad x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 rgba(156,152,215,100), stop: 0.4 rgba(58,52,151,100), stop: 1.0 rgba(78,70,190,100));\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 35;\n"
"padding: 3px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"font:bold;\n"
"font-family:Vrinda;\n"
"}")
        self.Bu9 = QPushButton(self.Botones)
        self.Bu9.setObjectName(u"Bu9")
        self.Bu9.setGeometry(QRect(190, 240, 71, 71))
        self.Bu9.setFont(font1)
        self.Bu9.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient(spread:pad x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 rgba(156,152,215,100), stop: 0.4 rgba(58,52,151,100), stop: 1.0 rgba(78,70,190,100));\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 12;\n"
"padding: 3px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"font:bold;\n"
"font-family:Vrinda;\n"
"}")
        self.Bu8 = QPushButton(self.Botones)
        self.Bu8.setObjectName(u"Bu8")
        self.Bu8.setGeometry(QRect(100, 240, 71, 71))
        self.Bu8.setFont(font1)
        self.Bu8.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient(spread:pad x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 rgba(156,152,215,100), stop: 0.4 rgba(58,52,151,100), stop: 1.0 rgba(78,70,190,100));\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 12;\n"
"padding: 3px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"font:bold;\n"
"font-family:Vrinda;\n"
"}")
        self.Bu5 = QPushButton(self.Botones)
        self.Bu5.setObjectName(u"Bu5")
        self.Bu5.setGeometry(QRect(100, 330, 71, 71))
        self.Bu5.setFont(font1)
        self.Bu5.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient(spread:pad x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 rgba(156,152,215,100), stop: 0.4 rgba(58,52,151,100), stop: 1.0 rgba(78,70,190,100));\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 12;\n"
"padding: 3px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"font:bold;\n"
"font-family:Vrinda;\n"
"}")
        self.Bu6 = QPushButton(self.Botones)
        self.Bu6.setObjectName(u"Bu6")
        self.Bu6.setGeometry(QRect(190, 330, 71, 71))
        self.Bu6.setFont(font1)
        self.Bu6.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient(spread:pad x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 rgba(156,152,215,100), stop: 0.4 rgba(58,52,151,100), stop: 1.0 rgba(78,70,190,100));\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 12;\n"
"padding: 3px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"font:bold;\n"
"font-family:Vrinda;\n"
"}")
        self.Bt_restar = QPushButton(self.Botones)
        self.Bt_restar.setObjectName(u"Bt_restar")
        self.Bt_restar.setGeometry(QRect(280, 330, 71, 71))
        font3 = QFont()
        font3.setFamilies([u"Vrinda"])
        font3.setPointSize(30)
        font3.setBold(True)
        font3.setItalic(False)
        self.Bt_restar.setFont(font3)
        self.Bt_restar.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient(spread:pad x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 rgba(156,152,215,100), stop: 0.4 rgba(58,52,151,100), stop: 1.0 rgba(78,70,190,100));\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius:35;\n"
"padding: 3px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"font:bold;\n"
"font-family:Vrinda;\n"
"}")
        self.Bu4 = QPushButton(self.Botones)
        self.Bu4.setObjectName(u"Bu4")
        self.Bu4.setGeometry(QRect(10, 330, 71, 71))
        self.Bu4.setFont(font1)
        self.Bu4.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient(spread:pad x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 rgba(156,152,215,100), stop: 0.4 rgba(58,52,151,100), stop: 1.0 rgba(78,70,190,100));\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 12;\n"
"padding: 3px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"font:bold;\n"
"font-family:Vrinda;\n"
"}")
        self.Bt_sumar = QPushButton(self.Botones)
        self.Bt_sumar.setObjectName(u"Bt_sumar")
        self.Bt_sumar.setGeometry(QRect(280, 420, 71, 71))
        self.Bt_sumar.setFont(font1)
        self.Bt_sumar.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient(spread:pad x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 rgba(156,152,215,100), stop: 0.4 rgba(58,52,151,100), stop: 1.0 rgba(78,70,190,100));\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 35;\n"
"padding: 3px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"font:bold;\n"
"font-family:Vrinda;\n"
"}")
        self.Bu1 = QPushButton(self.Botones)
        self.Bu1.setObjectName(u"Bu1")
        self.Bu1.setGeometry(QRect(10, 420, 71, 71))
        self.Bu1.setFont(font1)
        self.Bu1.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient(spread:pad x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 rgba(156,152,215,100), stop: 0.4 rgba(58,52,151,100), stop: 1.0 rgba(78,70,190,100));\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 12;\n"
"padding: 3px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"font:bold;\n"
"font-family:Vrinda;\n"
"}")
        self.Bu3 = QPushButton(self.Botones)
        self.Bu3.setObjectName(u"Bu3")
        self.Bu3.setGeometry(QRect(190, 420, 71, 71))
        self.Bu3.setFont(font1)
        self.Bu3.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient(spread:pad x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 rgba(156,152,215,100), stop: 0.4 rgba(58,52,151,100), stop: 1.0 rgba(78,70,190,100));\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 12;\n"
"padding: 3px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"font:bold;\n"
"font-family:Vrinda;\n"
"}")
        self.Bu2 = QPushButton(self.Botones)
        self.Bu2.setObjectName(u"Bu2")
        self.Bu2.setGeometry(QRect(100, 420, 71, 71))
        self.Bu2.setFont(font1)
        self.Bu2.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient(spread:pad x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 rgba(156,152,215,100), stop: 0.4 rgba(58,52,151,100), stop: 1.0 rgba(78,70,190,100));\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 12;\n"
"padding: 3px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"font:bold;\n"
"font-family:Vrinda;\n"
"}")
        self.Bt_igual = QPushButton(self.Botones)
        self.Bt_igual.setObjectName(u"Bt_igual")
        self.Bt_igual.setGeometry(QRect(280, 510, 71, 71))
        self.Bt_igual.setFont(font1)
        self.Bt_igual.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient(spread:pad x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 rgba(156,152,215,100), stop: 0.4 rgba(58,52,151,100), stop: 1.0 rgba(78,70,190,100));\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 35;\n"
"padding: 3px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"font:bold;\n"
"font-family:Vrinda;\n"
"}")
        self.Bu0 = QPushButton(self.Botones)
        self.Bu0.setObjectName(u"Bu0")
        self.Bu0.setGeometry(QRect(100, 510, 71, 71))
        self.Bu0.setFont(font1)
        self.Bu0.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient(spread:pad x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 rgba(156,152,215,100), stop: 0.4 rgba(58,52,151,100), stop: 1.0 rgba(78,70,190,100));\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 12;\n"
"padding: 3px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"font:bold;\n"
"font-family:Vrinda;\n"
"}")
        self.Bt_coma = QPushButton(self.Botones)
        self.Bt_coma.setObjectName(u"Bt_coma")
        self.Bt_coma.setGeometry(QRect(190, 510, 71, 71))
        self.Bt_coma.setFont(font1)
        self.Bt_coma.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient(spread:pad x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 rgba(156,152,215,100), stop: 0.4 rgba(58,52,151,100), stop: 1.0 rgba(78,70,190,100));\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 12;\n"
"padding: 3px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"font:bold;\n"
"font-family:Vrinda;\n"
"}")
        self.Bt_raiz = QPushButton(self.Botones)
        self.Bt_raiz.setObjectName(u"Bt_raiz")
        self.Bt_raiz.setGeometry(QRect(10, 510, 71, 71))
        self.Bt_raiz.setFont(font1)
        self.Bt_raiz.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient(spread:pad x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 rgba(156,152,215,100), stop: 0.4 rgba(58,52,151,100), stop: 1.0 rgba(78,70,190,100));\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 12;\n"
"padding: 3px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"font:bold;\n"
"font-family:Vrinda;\n"
"}")
        self.Ta_Historial = QTableWidget(self.Botones)
        self.Ta_Historial.setObjectName(u"Ta_Historial")
        self.Ta_Historial.setGeometry(QRect(470, 10, 256, 561))
        self.igual_2 = QPushButton(self.Botones)
        self.igual_2.setObjectName(u"igual_2")
        self.igual_2.setGeometry(QRect(370, 510, 71, 71))
        self.igual_2.setFont(font1)
        self.igual_2.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient(spread:pad x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 rgba(156,152,215,100), stop: 0.4 rgba(58,52,151,100), stop: 1.0 rgba(78,70,190,100));\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 35;\n"
"padding: 3px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"font:bold;\n"
"font-family:Vrinda;\n"
"}")
        self.igual_3 = QPushButton(self.Botones)
        self.igual_3.setObjectName(u"igual_3")
        self.igual_3.setGeometry(QRect(370, 420, 71, 71))
        self.igual_3.setFont(font1)
        self.igual_3.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient(spread:pad x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 rgba(156,152,215,100), stop: 0.4 rgba(58,52,151,100), stop: 1.0 rgba(78,70,190,100));\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 35;\n"
"padding: 3px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"font:bold;\n"
"font-family:Vrinda;\n"
"}")
        self.restar_2 = QPushButton(self.Botones)
        self.restar_2.setObjectName(u"restar_2")
        self.restar_2.setGeometry(QRect(370, 330, 71, 71))
        self.restar_2.setFont(font3)
        self.restar_2.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient(spread:pad x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 rgba(156,152,215,100), stop: 0.4 rgba(58,52,151,100), stop: 1.0 rgba(78,70,190,100));\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius:35;\n"
"padding: 3px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"font:bold;\n"
"font-family:Vrinda;\n"
"}")
        self.dividir_2 = QPushButton(self.Botones)
        self.dividir_2.setObjectName(u"dividir_2")
        self.dividir_2.setGeometry(QRect(370, 150, 71, 71))
        self.dividir_2.setFont(font2)
        self.dividir_2.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient(spread:pad x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 rgba(156,152,215,100), stop: 0.4 rgba(58,52,151,100), stop: 1.0 rgba(78,70,190,100));\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 35;;\n"
"padding: 3px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"font:bold;\n"
"font-family:Vrinda;\n"
"}")
        self.multi_2 = QPushButton(self.Botones)
        self.multi_2.setObjectName(u"multi_2")
        self.multi_2.setGeometry(QRect(370, 240, 71, 71))
        self.multi_2.setFont(font1)
        self.multi_2.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient(spread:pad x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 rgba(156,152,215,100), stop: 0.4 rgba(58,52,151,100), stop: 1.0 rgba(78,70,190,100));\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 35;\n"
"padding: 3px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"font:bold;\n"
"font-family:Vrinda;\n"
"}")
        self.dividir_3 = QPushButton(self.Botones)
        self.dividir_3.setObjectName(u"dividir_3")
        self.dividir_3.setGeometry(QRect(370, 40, 71, 71))
        self.dividir_3.setFont(font2)
        self.dividir_3.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient(spread:pad x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 rgba(156,152,215,100), stop: 0.4 rgba(58,52,151,100), stop: 1.0 rgba(78,70,190,100));\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 35;;\n"
"padding: 3px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"font:bold;\n"
"font-family:Vrinda;\n"
"}")
        MainWindow.setCentralWidget(self.Botones)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Bt_borrar.setText(QCoreApplication.translate("MainWindow", u"AC", None))
        self.Bt_porcentaje.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.delete_2.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.Bt_dividir.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.Bu7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.Bt_multi.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.Bu9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.Bu8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.Bu5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.Bu6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.Bt_restar.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.Bu4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.Bt_sumar.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.Bu1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.Bu3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.Bu2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.Bt_igual.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.Bu0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Bt_coma.setText(QCoreApplication.translate("MainWindow", u",", None))
        self.Bt_raiz.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
        self.igual_2.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.igual_3.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.restar_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.dividir_2.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.multi_2.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.dividir_3.setText(QCoreApplication.translate("MainWindow", u"H", None))
    # retranslateUi

