# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal.ui'
#
# Created: Sun Nov 10 18:31:08 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_objform(object):
    def setupUi(self, principal):
        principal.setObjectName(_fromUtf8("principal"))
        principal.resize(400, 300)
        self.centralWidget = QtGui.QWidget(principal)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.textEdit = QtGui.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 50, 341, 181))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 141, 16))
        self.label.setObjectName(_fromUtf8("label"))
        principal.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(principal)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuArchivo = QtGui.QMenu(self.menuBar)
        self.menuArchivo.setObjectName(_fromUtf8("menuArchivo"))
        self.menuCompilador = QtGui.QMenu(self.menuBar)
        self.menuCompilador.setObjectName(_fromUtf8("menuCompilador"))
        principal.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(principal)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        principal.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(principal)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        principal.setStatusBar(self.statusBar)
        self.actionAbrir = QtGui.QAction(principal)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../editor_sic_estandar/images/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbrir.setIcon(icon)
        self.actionAbrir.setObjectName(_fromUtf8("actionAbrir"))
        self.actionSalir = QtGui.QAction(principal)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../editor_sic_estandar/images/cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSalir.setIcon(icon1)
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))
        self.actionCargar = QtGui.QAction(principal)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../editor_sic_estandar/images/run.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCargar.setIcon(icon2)
        self.actionCargar.setObjectName(_fromUtf8("actionCargar"))
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionSalir)
        self.menuCompilador.addAction(self.actionCargar)
        self.menuBar.addAction(self.menuArchivo.menuAction())
        self.menuBar.addAction(self.menuCompilador.menuAction())
        self.mainToolBar.addAction(self.actionAbrir)
        self.mainToolBar.addAction(self.actionSalir)
        self.mainToolBar.addAction(self.actionCargar)

        self.retranslateUi(principal)
        QtCore.QMetaObject.connectSlotsByName(principal)

    def retranslateUi(self, principal):
        principal.setWindowTitle(_translate("principal", "principal", None))
        self.label.setText(_translate("principal", "Archivos a Cargar", None))
        self.menuArchivo.setTitle(_translate("principal", "Archivo", None))
        self.menuCompilador.setTitle(_translate("principal", "Compilador", None))
        self.actionAbrir.setText(_translate("principal", "Abrir", None))
        self.actionSalir.setText(_translate("principal", "Salir", None))
        self.actionCargar.setText(_translate("principal", "Cargar", None))


# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     principal = QtGui.QMainWindow()
#     ui = Ui_objform()
#     ui.setupUi(principal)
#     principal.show()
#     sys.exit(app.exec_())

