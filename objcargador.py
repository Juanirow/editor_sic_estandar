from objform import Ui_objform
from PyQt4 import QtCore, QtGui
from listobj import Ui_DockWidget

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
    
class Objcargador(QtGui.QDockWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self)
        self.window = Ui_DockWidget()
        self.window.setupUi(self)
        self.window.pushButton.clicked.connect(self.abrir)
        self.window.btn_subir.clicked.connect(self.up)
        self.window.btn_abajo.clicked.connect(self.down)
        self.window.btn_eliminar.clicked.connect(self.delete)

    def abrir(self):
    	fname = QtGui.QFileDialog.getOpenFileNames(self, 'Abrir Archivo', 
                '/home/Desktop/Progra/EditorSIC/ejemplos', "Files (*.os)")
    	for s in fname:
    		self.window.listWidget.addItem(s)

    def up(self):
        item = self.window.listWidget.currentItem()
        if item:
            item_row = self.window.listWidget.currentRow()
            item2 = self.window.listWidget.takeItem(item_row)
            item2 = None
            self.window.listWidget.insertItem(item_row-1,item)

    def down(self):
        item = self.window.listWidget.currentItem()
        if item:
            item_row = self.window.listWidget.currentRow()
            item2 = self.window.listWidget.takeItem(item_row)
            item2 = None
            self.window.listWidget.insertItem(item_row+1,item)

    def delete(self):
        item = self.window.listWidget.currentItem()
        if item:
            item_row = self.window.listWidget.currentRow()
            item2 = self.window.listWidget.takeItem(item_row)
            item2 = None
