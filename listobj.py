# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listobj.ui'
#
# Created: Sun Nov 10 20:10:06 2013
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

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName(_fromUtf8("DockWidget"))
        DockWidget.resize(427, 300)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.pushButton = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 71, 27))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../editor_sic_estandar/images/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 10, 87, 27))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../editor_sic_estandar/images/cargar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setGeometry(QtCore.QRect(20, 50, 121, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.dockWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(200, 40, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(self.dockWidgetContents)
        self.lineEdit.setGeometry(QtCore.QRect(260, 40, 113, 25))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.listWidget = QtGui.QListWidget(self.dockWidgetContents)
        self.listWidget.setGeometry(QtCore.QRect(10, 70, 311, 192))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.btn_subir = QtGui.QPushButton(self.dockWidgetContents)
        self.btn_subir.setGeometry(QtCore.QRect(330, 110, 87, 27))
        self.btn_subir.setObjectName(_fromUtf8("btn_subir"))
        self.btn_eliminar = QtGui.QPushButton(self.dockWidgetContents)
        self.btn_eliminar.setGeometry(QtCore.QRect(330, 150, 87, 27))
        self.btn_eliminar.setObjectName(_fromUtf8("btn_eliminar"))
        self.btn_abajo = QtGui.QPushButton(self.dockWidgetContents)
        self.btn_abajo.setGeometry(QtCore.QRect(330, 190, 87, 27))
        self.btn_abajo.setObjectName(_fromUtf8("btn_abajo"))
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(_translate("DockWidget", "Cargador de OX", None))
        self.pushButton.setText(_translate("DockWidget", "Abrir", None))
        self.pushButton_2.setText(_translate("DockWidget", "Cargar", None))
        self.label.setText(_translate("DockWidget", "Archivo a Cargar", None))
        self.label_2.setText(_translate("DockWidget", "<html><head/><body><p>Dir Carga</p></body></html>", None))
        self.btn_subir.setText(_translate("DockWidget", "Subir", None))
        self.btn_eliminar.setText(_translate("DockWidget", "Eliminar", None))
        self.btn_abajo.setText(_translate("DockWidget", "Bajar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DockWidget = QtGui.QDockWidget()
    ui = Ui_DockWidget()
    ui.setupUi(DockWidget)
    DockWidget.show()
    sys.exit(app.exec_())

