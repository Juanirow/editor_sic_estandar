from objform import Ui_objform
from PyQt4 import QtCore, QtGui
from listobj import Ui_DockWidget
from Cargadorx import Cargadorx
from simuladorx import Simuladorx
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
        self.simulador = None

    def show_error(self,msg):
        QtGui.QMessageBox.about(self,"Error",msg)

    def abrir(self):
    	fname = QtGui.QFileDialog.getOpenFileNames(self, 'Abrir Archivo', 
                '/home/juan/Escritorio/ejemplos', "Files (*.ox)")
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
            regex = re.compile("[0-9A-F]+H")
            res = regex.search(text)
            if res:
                res = res.group()
                if res == text:
                    list_obj = self.get_list_obj()
                    if len(list_obj) > 0:
                        self.simulador = Simuladorx()
                        self.simulador.show()
                        list_obj = self.get_list_of_list(list_obj)
                        self.simulador.carga(list_obj,text)
                    else:
                        self.show_error("No hay archivos para cargar")
                else:
                    self.show_error("La direccion no es correcta")
            else:
                self.show_error("La direccion de carga no es correcta")
        else:
            self.show_error("Falta la direccion de carga")

    ## rergesa una lista que contiene una lista de registros
    # que contiene cada archivo en la lista de parametro 
    def get_list_of_list(self,list_obj):
        list_ret = []
        for s in list_obj:
            f = open(s)
            obj = f.read()
            list_ret.append(obj.split("\n")[:-1])
        return list_ret

    def get_list_obj(self):
        count = self.window.listWidget.count()
        it = 0
        list_obj = []
        while it < count:
            item = self.window.listWidget.item(it)
            list_obj.append(str(item.text()))
            it += 1
        return list_obj