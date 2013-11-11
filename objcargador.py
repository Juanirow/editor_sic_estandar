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

    def abrir(self):
    	fname = QtGui.QFileDialog.getOpenFileNames(self, 'Abrir Archivo', 
                '/home/Desktop/Progra/EditorSIC/ejemplos', "Files (*.os)")
    	string = self.window.textEdit.toPlainText()
    	list_str = string.split("\n")
    	for s in fname:
    		if not s in list_str:
    			string += s + "\n"
		self.window.textEdit.setText(string)