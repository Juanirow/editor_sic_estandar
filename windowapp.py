# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowapp.ui'
#
# Created: Wed Sep 11 09:04:49 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_windowApp(object):
    def setupUi(self, windowApp):
        windowApp.setObjectName(_fromUtf8("windowApp"))
        windowApp.resize(1300, 700)
        self.centralWidget = QtGui.QWidget(windowApp)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        windowApp.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(windowApp)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuArchivo = QtGui.QMenu(self.menuBar)
        self.menuArchivo.setObjectName(_fromUtf8("menuArchivo"))
        self.menuCompilador = QtGui.QMenu(self.menuBar)
        self.menuCompilador.setObjectName(_fromUtf8("menuCompilador"))
        windowApp.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(windowApp)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        windowApp.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(windowApp)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        windowApp.setStatusBar(self.statusBar)
        self.actionNuevo = QtGui.QAction(windowApp)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./images/new.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNuevo.setIcon(icon)
        self.actionNuevo.setObjectName(_fromUtf8("actionNuevo"))
        self.actionAbrir = QtGui.QAction(windowApp)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("./images/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbrir.setIcon(icon1)
        self.actionAbrir.setObjectName(_fromUtf8("actionAbrir"))
        self.actionGuardar = QtGui.QAction(windowApp)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("./images/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGuardar.setIcon(icon2)
        self.actionGuardar.setObjectName(_fromUtf8("actionGuardar"))
        self.actionCerrar = QtGui.QAction(windowApp)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("./images/cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCerrar.setIcon(icon3)
        self.actionCerrar.setObjectName(_fromUtf8("actionCerrar"))
        self.actionSalir = QtGui.QAction(windowApp)
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))
        self.actionEnsamblar = QtGui.QAction(windowApp)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("./images/build.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEnsamblar.setIcon(icon4)
        self.actionEnsamblar.setObjectName(_fromUtf8("actionEnsamblar"))
        self.actionCargar = QtGui.QAction(windowApp)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("./images/cargar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCargar.setIcon(icon5)
        self.actionCargar.setObjectName(_fromUtf8("actionCargar"))
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionNuevo)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addAction(self.actionCerrar)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menuCompilador.addAction(self.actionEnsamblar)
        self.menuCompilador.addAction(self.actionCargar)
        self.menuBar.addAction(self.menuArchivo.menuAction())
        self.menuBar.addAction(self.menuCompilador.menuAction())
        self.mainToolBar.addAction(self.actionNuevo)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionAbrir)
        self.mainToolBar.addAction(self.actionGuardar)
        self.mainToolBar.addAction(self.actionCerrar)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionEnsamblar)
        self.mainToolBar.addAction(self.actionCargar)

        self.retranslateUi(windowApp)
        QtCore.QMetaObject.connectSlotsByName(windowApp)

    def retranslateUi(self, windowApp):
        windowApp.setWindowTitle(QtGui.QApplication.translate("windowApp", "windowApp", None, QtGui.QApplication.UnicodeUTF8))
        self.menuArchivo.setTitle(QtGui.QApplication.translate("windowApp", "Archivo", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCompilador.setTitle(QtGui.QApplication.translate("windowApp", "Compilador", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNuevo.setText(QtGui.QApplication.translate("windowApp", "Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbrir.setText(QtGui.QApplication.translate("windowApp", "Abrir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGuardar.setText(QtGui.QApplication.translate("windowApp", "Guardar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCerrar.setText(QtGui.QApplication.translate("windowApp", "Cerrar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir.setText(QtGui.QApplication.translate("windowApp", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnsamblar.setText(QtGui.QApplication.translate("windowApp", "Ensamblar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnsamblar.setToolTip(QtGui.QApplication.translate("windowApp", "Ensamblar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCargar.setText(QtGui.QApplication.translate("windowApp", "Cargar", None, QtGui.QApplication.UnicodeUTF8))

