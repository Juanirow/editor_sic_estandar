# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowcargador.ui'
#
# Created: Fri Sep 20 00:09:00 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName(_fromUtf8("DockWidget"))
        DockWidget.resize(950, 700)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.tableWidget = QtGui.QTableWidget(self.dockWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(0, 10, 901, 331))
        self.tableWidget.setMinimumSize(QtCore.QSize(801, 0))
        self.tableWidget.setColumnCount(17)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)
        self.tableWidget_2 = QtGui.QTableWidget(self.dockWidgetContents)
        self.tableWidget_2.setGeometry(QtCore.QRect(40, 390, 171, 181))
        self.tableWidget_2.setRowCount(5)
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(60)
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setGeometry(QtCore.QRect(40, 350, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit_Num = QtGui.QTextEdit(self.dockWidgetContents)
        self.textEdit_Num.setGeometry(QtCore.QRect(240, 350, 41, 41))
        self.textEdit_Num.setObjectName(_fromUtf8("textEdit_Num"))
        self.btnSimular = QtGui.QPushButton(self.dockWidgetContents)
        self.btnSimular.setGeometry(QtCore.QRect(290, 360, 98, 27))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../EditorSIC/images/run.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSimular.setIcon(icon)
        self.btnSimular.setObjectName(_fromUtf8("btnSimular"))
        self.textEdit_Actions = QtGui.QTextEdit(self.dockWidgetContents)
        self.textEdit_Actions.setGeometry(QtCore.QRect(240, 410, 421, 251))
        self.textEdit_Actions.setObjectName(_fromUtf8("textEdit_Actions"))
        self.label_2 = QtGui.QLabel(self.dockWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(720, 380, 191, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_sig = QtGui.QLabel(self.dockWidgetContents)
        self.label_sig.setGeometry(QtCore.QRect(750, 410, 660, 17))
        self.label_sig.setObjectName(_fromUtf8("label_sig"))
        DockWidget.setWidget(self.dockWidgetContents)
        self.actionSimular = QtGui.QAction(DockWidget)
        self.actionSimular.setObjectName(_fromUtf8("actionSimular"))

        self.retranslateUi(DockWidget)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QtGui.QApplication.translate("DockWidget", "Mapa de Memoria", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("DockWidget", "DIR", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("DockWidget", "0", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("DockWidget", "1", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(QtGui.QApplication.translate("DockWidget", "2", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(QtGui.QApplication.translate("DockWidget", "3", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(QtGui.QApplication.translate("DockWidget", "4", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(QtGui.QApplication.translate("DockWidget", "5", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(QtGui.QApplication.translate("DockWidget", "6", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(QtGui.QApplication.translate("DockWidget", "7", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(QtGui.QApplication.translate("DockWidget", "8", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(QtGui.QApplication.translate("DockWidget", "9", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(QtGui.QApplication.translate("DockWidget", "A", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(QtGui.QApplication.translate("DockWidget", "B", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(QtGui.QApplication.translate("DockWidget", "C", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(QtGui.QApplication.translate("DockWidget", "D", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(QtGui.QApplication.translate("DockWidget", "E", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(QtGui.QApplication.translate("DockWidget", "F", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("DockWidget", "CP", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("DockWidget", "A", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("DockWidget", "X", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(QtGui.QApplication.translate("DockWidget", "L", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(QtGui.QApplication.translate("DockWidget", "SW", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("DockWidget", "VALOR", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DockWidget", "Registros", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSimular.setText(QtGui.QApplication.translate("DockWidget", "Simular", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DockWidget", "Siguiente Instruccion", None, QtGui.QApplication.UnicodeUTF8))
        self.label_sig.setText(QtGui.QApplication.translate("DockWidget", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSimular.setText(QtGui.QApplication.translate("DockWidget", "Simular", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSimular.setToolTip(QtGui.QApplication.translate("DockWidget", "<html><head/><body><p>Simular</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

