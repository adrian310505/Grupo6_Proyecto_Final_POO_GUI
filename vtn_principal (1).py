# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtn_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_ServicioHotel(object):
    def setupUi(self, ServicioHotel):
        if not ServicioHotel.objectName():
            ServicioHotel.setObjectName(u"ServicioHotel")
        ServicioHotel.resize(900, 700)
        self.centralwidget = QWidget(ServicioHotel)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_titulo = QLabel(self.centralwidget)
        self.lbl_titulo.setObjectName(u"lbl_titulo")
        self.lbl_titulo.setGeometry(QRect(100, 15, 700, 45))
        font = QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.lbl_titulo.setFont(font)
        self.lbl_titulo.setStyleSheet(u"color: #1a5276;")
        self.lbl_titulo.setAlignment(Qt.AlignCenter)
        self.lbl_codigo = QLabel(self.centralwidget)
        self.lbl_codigo.setObjectName(u"lbl_codigo")
        self.lbl_codigo.setGeometry(QRect(60, 80, 140, 36))
        font1 = QFont()
        font1.setPointSize(12)
        self.lbl_codigo.setFont(font1)
        self.txt_Codigo = QLineEdit(self.centralwidget)
        self.txt_Codigo.setObjectName(u"txt_Codigo")
        self.txt_Codigo.setGeometry(QRect(220, 80, 180, 36))
        self.txt_Codigo.setStyleSheet(u"background-color: rgb(255,255,180);")
        self.txt_Codigo.setMaxLength(5)
        self.lbl_descripcion = QLabel(self.centralwidget)
        self.lbl_descripcion.setObjectName(u"lbl_descripcion")
        self.lbl_descripcion.setGeometry(QRect(60, 140, 140, 36))
        self.lbl_descripcion.setFont(font1)
        self.txt_descripcion = QLineEdit(self.centralwidget)
        self.txt_descripcion.setObjectName(u"txt_descripcion")
        self.txt_descripcion.setGeometry(QRect(220, 140, 400, 36))
        self.txt_descripcion.setStyleSheet(u"background-color: rgb(255,255,180);")
        self.lbl_precio = QLabel(self.centralwidget)
        self.lbl_precio.setObjectName(u"lbl_precio")
        self.lbl_precio.setGeometry(QRect(60, 200, 140, 36))
        self.lbl_precio.setFont(font1)
        self.txt_precio_base = QLineEdit(self.centralwidget)
        self.txt_precio_base.setObjectName(u"txt_precio_base")
        self.txt_precio_base.setGeometry(QRect(220, 200, 180, 36))
        self.txt_precio_base.setStyleSheet(u"background-color: rgb(255,255,180);")
        self.lbl_correo = QLabel(self.centralwidget)
        self.lbl_correo.setObjectName(u"lbl_correo")
        self.lbl_correo.setGeometry(QRect(60, 260, 140, 36))
        self.lbl_correo.setFont(font1)
        self.txt_correo = QLineEdit(self.centralwidget)
        self.txt_correo.setObjectName(u"txt_correo")
        self.txt_correo.setGeometry(QRect(220, 260, 300, 36))
        self.txt_correo.setStyleSheet(u"background-color: rgb(255,255,180);")
        self.btn_guardar = QPushButton(self.centralwidget)
        self.btn_guardar.setObjectName(u"btn_guardar")
        self.btn_guardar.setGeometry(QRect(60, 330, 130, 42))
        self.btn_guardar.setStyleSheet(u"background-color:#27ae60;color:white;font-size:13px;font-weight:bold;border-radius:6px;")
        self.btn_actualizar = QPushButton(self.centralwidget)
        self.btn_actualizar.setObjectName(u"btn_actualizar")
        self.btn_actualizar.setGeometry(QRect(210, 330, 130, 42))
        self.btn_actualizar.setStyleSheet(u"background-color:#e67e22;color:white;font-size:13px;font-weight:bold;border-radius:6px;")
        self.btn_eliminar = QPushButton(self.centralwidget)
        self.btn_eliminar.setObjectName(u"btn_eliminar")
        self.btn_eliminar.setGeometry(QRect(360, 330, 130, 42))
        self.btn_eliminar.setStyleSheet(u"background-color:#c0392b;color:white;font-size:13px;font-weight:bold;border-radius:6px;")
        self.btn_mostrar = QPushButton(self.centralwidget)
        self.btn_mostrar.setObjectName(u"btn_mostrar")
        self.btn_mostrar.setGeometry(QRect(510, 330, 130, 42))
        self.btn_mostrar.setStyleSheet(u"background-color:#2980b9;color:white;font-size:13px;font-weight:bold;border-radius:6px;")
        self.btn_limpiar = QPushButton(self.centralwidget)
        self.btn_limpiar.setObjectName(u"btn_limpiar")
        self.btn_limpiar.setGeometry(QRect(660, 330, 130, 42))
        self.btn_limpiar.setStyleSheet(u"background-color:#7f8c8d;color:white;font-size:13px;font-weight:bold;border-radius:6px;")
        self.lbl_tabla = QLabel(self.centralwidget)
        self.lbl_tabla.setObjectName(u"lbl_tabla")
        self.lbl_tabla.setGeometry(QRect(60, 390, 300, 28))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.lbl_tabla.setFont(font2)
        self.tbl_servicios = QTableWidget(self.centralwidget)
        self.tbl_servicios.setObjectName(u"tbl_servicios")
        self.tbl_servicios.setGeometry(QRect(60, 425, 780, 230))
        self.tbl_servicios.setColumnCount(4)
        self.tbl_servicios.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tbl_servicios.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_servicios.setAlternatingRowColors(True)
        ServicioHotel.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ServicioHotel)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 26))
        ServicioHotel.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ServicioHotel)
        self.statusbar.setObjectName(u"statusbar")
        ServicioHotel.setStatusBar(self.statusbar)

        self.retranslateUi(ServicioHotel)

        QMetaObject.connectSlotsByName(ServicioHotel)
    # setupUi

    def retranslateUi(self, ServicioHotel):
        ServicioHotel.setWindowTitle(QCoreApplication.translate("ServicioHotel", u"Sistema de Gesti\u00f3n de Servicios de Hotel", None))
        self.lbl_titulo.setText(QCoreApplication.translate("ServicioHotel", u"Sistema de Gesti\u00f3n de Servicios de Hotel", None))
        self.lbl_codigo.setText(QCoreApplication.translate("ServicioHotel", u"C\u00f3digo:", None))
        self.lbl_descripcion.setText(QCoreApplication.translate("ServicioHotel", u"Descripci\u00f3n:", None))
        self.lbl_precio.setText(QCoreApplication.translate("ServicioHotel", u"Precio base:", None))
        self.lbl_correo.setText(QCoreApplication.translate("ServicioHotel", u"Correo:", None))
        self.btn_guardar.setText(QCoreApplication.translate("ServicioHotel", u"Guardar", None))
        self.btn_actualizar.setText(QCoreApplication.translate("ServicioHotel", u"Actualizar", None))
        self.btn_eliminar.setText(QCoreApplication.translate("ServicioHotel", u"Eliminar", None))
        self.btn_mostrar.setText(QCoreApplication.translate("ServicioHotel", u"Mostrar", None))
        self.btn_limpiar.setText(QCoreApplication.translate("ServicioHotel", u"Limpiar", None))
        self.lbl_tabla.setText(QCoreApplication.translate("ServicioHotel", u"Registros en base de datos:", None))
    # retranslateUi

