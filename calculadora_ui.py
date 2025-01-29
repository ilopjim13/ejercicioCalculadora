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
        self.Bu7 = QPushButton(self.centralwidget)
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
        self.Bu9 = QPushButton(self.centralwidget)
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
        self.Bu8 = QPushButton(self.centralwidget)
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
        self.Bu5 = QPushButton(self.centralwidget)
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
        self.Bu6 = QPushButton(self.centralwidget)
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
        self.Bu4 = QPushButton(self.centralwidget)
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
        self.Bu3 = QPushButton(self.centralwidget)
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
        self.Bu2 = QPushButton(self.centralwidget)
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
        self.raiz = QPushButton(self.centralwidget)
        self.raiz.setObjectName(u"raiz")
        self.raiz.setGeometry(QRect(10, 510, 71, 71))
        self.raiz.setFont(font1)
        self.raiz.setStyleSheet(u"QPushButton {\n"
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
        self.Bu7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.multi.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.Bu9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.Bu8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.Bu5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.Bu6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.restar.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.Bu4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.sumar.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.Bu1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.Bu3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.Bu2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.igual.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.cero.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.coma.setText(QCoreApplication.translate("MainWindow", u",", None))
        self.raiz.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
    # retranslateUi

