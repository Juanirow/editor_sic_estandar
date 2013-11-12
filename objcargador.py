from objform import Ui_objform
from PyQt4 import QtCore, QtGui
from listobj import Ui_DockWidget
from Cargadorx import Cargadorx
import re

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
        self.window.pushButton_2.clicked.connect(self.cargar_ligar)
        self.cargador = None

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
            self.window.listWidget.setCurrentItem(item)

    def down(self):
        item = self.window.listWidget.currentItem()
        if item:
            item_row = self.window.listWidget.currentRow()
            item2 = self.window.listWidget.takeItem(item_row)
            item2 = None
            self.window.listWidget.insertItem(item_row+1,item)
            self.window.listWidget.setCurrentItem(item)

    def delete(self):
        item = self.window.listWidget.currentItem()
        if item:
            item_row = self.window.listWidget.currentRow()
            item2 = self.window.listWidget.takeItem(item_row)
            item2 = None

    def cargar_ligar(self):
        text = str(self.window.lineEdit.text())
        if not text.strip() == "":
            regex = re.compile("[0-9A-F]+[H]?")
            res = regex.search(text)
            if res:
                res = res.group()
                if res == text:
                    list_obj = self.get_list_obj()
                    self.cargador = Cargadorx()
                    elf.cargador.show()
                    self.cargador.load_file_name(list_obj)

    def get_list_obj(self):
        count = self.window.listWidget.count()
        it = 0
        list_obj = []
        while it < count:
            item = self.window.listWidget.item(it)
            list_obj.append(str(item.text()))
            it += 1
        return list_obj