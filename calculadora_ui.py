# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculadora.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(678, 597)
        font = QFont()
        font.setFamilies([u"Verdana"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"\n"
"\n"
"background-color:rgb(0, 0, 0)")
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.Botones = QWidget(MainWindow)
        self.Botones.setObjectName(u"Botones")
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
"color: black;\n"
"background-color: rgb(197, 255, 253);\n"
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
        self.Bt_porcentaje.setGeometry(QRect(190, 150, 71, 71))
        self.Bt_porcentaje.setFont(font1)
        self.Bt_porcentaje.setStyleSheet(u"QPushButton {\n"
"color: black;\n"
"background-color: rgb(85, 85, 255);\n"
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
        self.Bt_delete = QPushButton(self.Botones)
        self.Bt_delete.setObjectName(u"Bt_delete")
        self.Bt_delete.setGeometry(QRect(280, 150, 71, 71))
        self.Bt_delete.setFont(font1)
        self.Bt_delete.setStyleSheet(u"QPushButton {\n"
"color: black;\n"
"background-color: rgb(85, 85, 255);\n"
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
        self.Bt_dividir = QPushButton(self.Botones)
        self.Bt_dividir.setObjectName(u"Bt_dividir")
        self.Bt_dividir.setGeometry(QRect(370, 150, 71, 71))
        font2 = QFont()
        font2.setFamilies([u"Vrinda"])
        font2.setPointSize(25)
        font2.setBold(True)
        font2.setItalic(False)
        self.Bt_dividir.setFont(font2)
        self.Bt_dividir.setStyleSheet(u"QPushButton {\n"
"color: black;\n"
"background-color: rgb(85, 85, 255);\n"
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
        self.Bu7 = QPushButton(self.Botones)
        self.Bu7.setObjectName(u"Bu7")
        self.Bu7.setGeometry(QRect(100, 240, 71, 71))
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
        self.Bt_multi.setGeometry(QRect(370, 240, 71, 71))
        self.Bt_multi.setFont(font1)
        self.Bt_multi.setStyleSheet(u"QPushButton {\n"
"color: black;\n"
"background-color: rgb(85, 85, 255);\n"
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
        self.Bu9.setGeometry(QRect(280, 240, 71, 71))
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
        self.Bu8.setGeometry(QRect(190, 240, 71, 71))
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
        self.Bu5.setGeometry(QRect(190, 330, 71, 71))
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
        self.Bu6.setGeometry(QRect(280, 330, 71, 71))
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
        self.Bt_restar.setGeometry(QRect(370, 330, 71, 71))
        font3 = QFont()
        font3.setFamilies([u"Vrinda"])
        font3.setPointSize(30)
        font3.setBold(True)
        font3.setItalic(False)
        self.Bt_restar.setFont(font3)
        self.Bt_restar.setStyleSheet(u"QPushButton {\n"
"color: black;\n"
"background-color: rgb(85, 85, 255);\n"
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
        self.Bu4 = QPushButton(self.Botones)
        self.Bu4.setObjectName(u"Bu4")
        self.Bu4.setGeometry(QRect(100, 330, 71, 71))
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
        self.Bt_sumar.setGeometry(QRect(370, 420, 71, 71))
        self.Bt_sumar.setFont(font1)
        self.Bt_sumar.setStyleSheet(u"QPushButton {\n"
"color: black;\n"
"background-color: rgb(85, 85, 255);\n"
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
        self.Bu1.setGeometry(QRect(100, 420, 71, 71))
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
        self.Bu3.setGeometry(QRect(280, 420, 71, 71))
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
        self.Bu2.setGeometry(QRect(190, 420, 71, 71))
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
        self.Bt_igual.setGeometry(QRect(370, 510, 71, 71))
        self.Bt_igual.setFont(font1)
        self.Bt_igual.setStyleSheet(u"QPushButton {\n"
"color: black;\n"
"background-color: rgb(85, 170, 255);\n"
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
        self.Bu0.setGeometry(QRect(190, 510, 71, 71))
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
        self.Bt_coma.setGeometry(QRect(280, 510, 71, 71))
        self.Bt_coma.setFont(font1)
        self.Bt_coma.setStyleSheet(u"QPushButton {\n"
"color: black;\n"
"background-color: rgb(85, 85, 255);\n"
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
        self.Ta_Historial.setGeometry(QRect(460, 10, 201, 571))
        font4 = QFont()
        font4.setBold(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.Ta_Historial.setFont(font4)
        self.Ta_Historial.setStyleSheet(u"QTableView {\n"
"    gridline-color: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: white;\n"
"    color: black;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    color: white; \n"
"	text-align: center;\n"
"}\n"
"\n"
"QTableView::item[id=\"your-id-here\"] {\n"
"    color: white;\n"
"	text-align: center;\n"
"}\n"
"")
        self.Ta_Historial.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.Ta_Historial.setRowCount(0)
        self.Ta_Historial.setColumnCount(0)
        self.Ta_Historial.horizontalHeader().setStretchLastSection(False)
        self.Ta_Historial.verticalHeader().setStretchLastSection(False)
        self.Bt_paren1 = QPushButton(self.Botones)
        self.Bt_paren1.setObjectName(u"Bt_paren1")
        self.Bt_paren1.setGeometry(QRect(10, 510, 71, 71))
        self.Bt_paren1.setFont(font1)
        self.Bt_paren1.setStyleSheet(u"QPushButton {\n"
"color: black;\n"
"background-color: rgb(85, 85, 255);\n"
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
        self.Bt_paren2 = QPushButton(self.Botones)
        self.Bt_paren2.setObjectName(u"Bt_paren2")
        self.Bt_paren2.setGeometry(QRect(10, 420, 71, 71))
        self.Bt_paren2.setFont(font1)
        self.Bt_paren2.setStyleSheet(u"QPushButton {\n"
"color: black;\n"
"background-color: rgb(85, 85, 255);\n"
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
        self.Bt_elevar = QPushButton(self.Botones)
        self.Bt_elevar.setObjectName(u"Bt_elevar")
        self.Bt_elevar.setGeometry(QRect(100, 150, 71, 71))
        self.Bt_elevar.setFont(font3)
        self.Bt_elevar.setStyleSheet(u"QPushButton {\n"
"color: black;\n"
"background-color: rgb(85, 85, 255);\n"
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
        self.Le_pantalla = QLineEdit(self.Botones)
        self.Le_pantalla.setObjectName(u"Le_pantalla")
        self.Le_pantalla.setGeometry(QRect(10, 10, 431, 111))
        font5 = QFont()
        font5.setPointSize(60)
        self.Le_pantalla.setFont(font5)
        self.Le_pantalla.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.Bt_raiz = QPushButton(self.Botones)
        self.Bt_raiz.setObjectName(u"Bt_raiz")
        self.Bt_raiz.setGeometry(QRect(100, 510, 71, 71))
        self.Bt_raiz.setFont(font1)
        self.Bt_raiz.setStyleSheet(u"QPushButton {\n"
"color: black;\n"
"background-color: rgb(85, 85, 255);\n"
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
        self.Bt_papelera = QPushButton(self.Botones)
        self.Bt_papelera.setObjectName(u"Bt_papelera")
        self.Bt_papelera.setGeometry(QRect(580, 500, 71, 71))
        self.Bt_papelera.setFont(font1)
        self.Bt_papelera.setStyleSheet(u"QPushButton {\n"
"color: black;\n"
"background-color: rgb(85, 85, 255);\n"
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
        self.Bt_sen = QPushButton(self.Botones)
        self.Bt_sen.setObjectName(u"Bt_sen")
        self.Bt_sen.setGeometry(QRect(10, 330, 71, 71))
        self.Bt_sen.setFont(font1)
        self.Bt_sen.setStyleSheet(u"QPushButton {\n"
"color: black;\n"
"background-color: rgb(85, 85, 255);\n"
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
        self.Bt_cos = QPushButton(self.Botones)
        self.Bt_cos.setObjectName(u"Bt_cos")
        self.Bt_cos.setGeometry(QRect(10, 240, 71, 71))
        self.Bt_cos.setFont(font1)
        self.Bt_cos.setStyleSheet(u"QPushButton {\n"
"color: black;\n"
"background-color: rgb(85, 85, 255);\n"
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
        MainWindow.setCentralWidget(self.Botones)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Bt_borrar.setText(QCoreApplication.translate("MainWindow", u"AC", None))
        self.Bt_porcentaje.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.Bt_delete.setText(QCoreApplication.translate("MainWindow", u"\u232b", None))
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
        self.Bt_paren1.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.Bt_paren2.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.Bt_elevar.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.Le_pantalla.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Le_pantalla.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Bt_raiz.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
        self.Bt_papelera.setText(QCoreApplication.translate("MainWindow", u"\ud83d\uddd1", None))
        self.Bt_sen.setText(QCoreApplication.translate("MainWindow", u"sen", None))
        self.Bt_cos.setText(QCoreApplication.translate("MainWindow", u"cos", None))
    # retranslateUi

