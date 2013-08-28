# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowapp.ui'
#
# Created: Tue Aug 27 08:49:55 2013
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
        windowApp.resize(800, 600)
        self.centralWidget = QtGui.QWidget(windowApp)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        windowApp.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(windowApp)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuArchivo = QtGui.QMenu(self.menuBar)
        self.menuArchivo.setObjectName(_fromUtf8("menuArchivo"))
        windowApp.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(windowApp)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        windowApp.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(windowApp)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        windowApp.setStatusBar(self.statusBar)
        self.actionNuevo = QtGui.QAction(windowApp)
        self.actionNuevo.setObjectName(_fromUtf8("actionNuevo"))
        self.actionAbrir = QtGui.QAction(windowApp)
        self.actionAbrir.setObjectName(_fromUtf8("actionAbrir"))
        self.actionGuardar = QtGui.QAction(windowApp)
        self.actionGuardar.setObjectName(_fromUtf8("actionGuardar"))
        self.actionCerrar = QtGui.QAction(windowApp)
        self.actionCerrar.setObjectName(_fromUtf8("actionCerrar"))
        self.actionSalir = QtGui.QAction(windowApp)
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionNuevo)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addAction(self.actionCerrar)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menuBar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(windowApp)
        QtCore.QMetaObject.connectSlotsByName(windowApp)

    def retranslateUi(self, windowApp):
        windowApp.setWindowTitle(QtGui.QApplication.translate("windowApp", "windowApp", None, QtGui.QApplication.UnicodeUTF8))
        self.menuArchivo.setTitle(QtGui.QApplication.translate("windowApp", "Archivo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNuevo.setText(QtGui.QApplication.translate("windowApp", "Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbrir.setText(QtGui.QApplication.translate("windowApp", "Abrir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGuardar.setText(QtGui.QApplication.translate("windowApp", "Guardar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCerrar.setText(QtGui.QApplication.translate("windowApp", "Cerrar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir.setText(QtGui.QApplication.translate("windowApp", "Salir", None, QtGui.QApplication.UnicodeUTF8))
