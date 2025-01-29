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
from PySide6.QtWidgets import (QApplication, QLCDNumber, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(361, 601)
        MainWindow.setStyleSheet(u"\n"
"\n"
"background-color:rgb(255, 224, 225)")
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.LcdNumber = QLCDNumber(self.centralwidget)
        self.LcdNumber.setObjectName(u"LcdNumber")
        self.LcdNumber.setGeometry(QRect(10, 10, 341, 121))
        self.LcdNumber.setMaximumSize(QSize(341, 16777215))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        self.LcdNumber.setFont(font)
        self.borrar = QPushButton(self.centralwidget)
        self.borrar.setObjectName(u"borrar")
        self.borrar.setGeometry(QRect(10, 150, 71, 71))
        font1 = QFont()
        font1.setFamilies([u"Vrinda"])
        font1.setPointSize(22)
        font1.setBold(True)
        font1.setItalic(False)
        self.borrar.setFont(font1)
        self.borrar.setStyleSheet(u"QPushButton {\n"
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
        self.porcentaje = QPushButton(self.centralwidget)
        self.porcentaje.setObjectName(u"porcentaje")
        self.porcentaje.setGeometry(QRect(100, 150, 71, 71))
        self.porcentaje.setFont(font1)
        self.porcentaje.setStyleSheet(u"QPushButton {\n"
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
        self.delete_2 = QPushButton(self.centralwidget)
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
        self.dividir = QPushButton(self.centralwidget)
        self.dividir.setObjectName(u"dividir")
        self.dividir.setGeometry(QRect(280, 150, 71, 71))
        font2 = QFont()
        font2.setFamilies([u"Vrinda"])
        font2.setPointSize(25)
        font2.setBold(True)
        font2.setItalic(False)
        self.dividir.setFont(font2)
        self.dividir.setStyleSheet(u"QPushButton {\n"
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
        self.siete = QPushButton(self.centralwidget)
        self.siete.setObjectName(u"siete")
        self.siete.setGeometry(QRect(10, 240, 71, 71))
        self.siete.setFont(font1)
        self.siete.setStyleSheet(u"QPushButton {\n"
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
        self.multi = QPushButton(self.centralwidget)
        self.multi.setObjectName(u"multi")
        self.multi.setGeometry(QRect(280, 240, 71, 71))
        self.multi.setFont(font1)
        self.multi.setStyleSheet(u"QPushButton {\n"
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
        self.nueve = QPushButton(self.centralwidget)
        self.nueve.setObjectName(u"nueve")
        self.nueve.setGeometry(QRect(190, 240, 71, 71))
        self.nueve.setFont(font1)
        self.nueve.setStyleSheet(u"QPushButton {\n"
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
        self.ocho = QPushButton(self.centralwidget)
        self.ocho.setObjectName(u"ocho")
        self.ocho.setGeometry(QRect(100, 240, 71, 71))
        self.ocho.setFont(font1)
        self.ocho.setStyleSheet(u"QPushButton {\n"
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
        self.cinco = QPushButton(self.centralwidget)
        self.cinco.setObjectName(u"cinco")
        self.cinco.setGeometry(QRect(100, 330, 71, 71))
        self.cinco.setFont(font1)
        self.cinco.setStyleSheet(u"QPushButton {\n"
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
        self.seis = QPushButton(self.centralwidget)
        self.seis.setObjectName(u"seis")
        self.seis.setGeometry(QRect(190, 330, 71, 71))
        self.seis.setFont(font1)
        self.seis.setStyleSheet(u"QPushButton {\n"
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
        self.restar = QPushButton(self.centralwidget)
        self.restar.setObjectName(u"restar")
        self.restar.setGeometry(QRect(280, 330, 71, 71))
        font3 = QFont()
        font3.setFamilies([u"Vrinda"])
        font3.setPointSize(30)
        font3.setBold(True)
        font3.setItalic(False)
        self.restar.setFont(font3)
        self.restar.setStyleSheet(u"QPushButton {\n"
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
        self.cuatro = QPushButton(self.centralwidget)
        self.cuatro.setObjectName(u"cuatro")
        self.cuatro.setGeometry(QRect(10, 330, 71, 71))
        self.cuatro.setFont(font1)
        self.cuatro.setStyleSheet(u"QPushButton {\n"
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
        self.sumar = QPushButton(self.centralwidget)
        self.sumar.setObjectName(u"sumar")
        self.sumar.setGeometry(QRect(280, 420, 71, 71))
        self.sumar.setFont(font1)
        self.sumar.setStyleSheet(u"QPushButton {\n"
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
        self.Bu1 = QPushButton(self.centralwidget)
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
        self.tres = QPushButton(self.centralwidget)
        self.tres.setObjectName(u"tres")
        self.tres.setGeometry(QRect(190, 420, 71, 71))
        self.tres.setFont(font1)
        self.tres.setStyleSheet(u"QPushButton {\n"
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
        self.dos = QPushButton(self.centralwidget)
        self.dos.setObjectName(u"dos")
        self.dos.setGeometry(QRect(100, 420, 71, 71))
        self.dos.setFont(font1)
        self.dos.setStyleSheet(u"QPushButton {\n"
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
        self.igual = QPushButton(self.centralwidget)
        self.igual.setObjectName(u"igual")
        self.igual.setGeometry(QRect(280, 510, 71, 71))
        self.igual.setFont(font1)
        self.igual.setStyleSheet(u"QPushButton {\n"
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
        self.cero = QPushButton(self.centralwidget)
        self.cero.setObjectName(u"cero")
        self.cero.setGeometry(QRect(100, 510, 71, 71))
        self.cero.setFont(font1)
        self.cero.setStyleSheet(u"QPushButton {\n"
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
        self.coma = QPushButton(self.centralwidget)
        self.coma.setObjectName(u"coma")
        self.coma.setGeometry(QRect(190, 510, 71, 71))
        self.coma.setFont(font1)
        self.coma.setStyleSheet(u"QPushButton {\n"
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
        self.dobleCero = QPushButton(self.centralwidget)
        self.dobleCero.setObjectName(u"dobleCero")
        self.dobleCero.setGeometry(QRect(10, 510, 71, 71))
        self.dobleCero.setFont(font1)
        self.dobleCero.setStyleSheet(u"QPushButton {\n"
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.borrar.setText(QCoreApplication.translate("MainWindow", u"AC", None))
        self.porcentaje.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.delete_2.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.dividir.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.siete.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.multi.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.nueve.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.ocho.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.cinco.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.seis.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.restar.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.cuatro.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.sumar.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.Bu1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.tres.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.dos.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.igual.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.cero.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.coma.setText(QCoreApplication.translate("MainWindow", u",", None))
        self.dobleCero.setText(QCoreApplication.translate("MainWindow", u"00", None))
    # retranslateUi

