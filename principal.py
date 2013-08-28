from windowapp import Ui_windowApp
import sys
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Window_Form(QtGui.QMainWindow):
    def __init__(self,parent=None):
        # QtGui.QMainWindow.__init__(self)
        QtGui.QMainWindow.__init__(self)
        self.window = Ui_windowApp()
        self.window.setupUi(self)
        self.file = ""
        self.textbox = None
        QtCore.QObject.connect(self.window.actionAbrir, QtCore.SIGNAL("triggered()"), self.open_file)
        QtCore.QObject.connect(self.window.actionNuevo, QtCore.SIGNAL("triggered()"), self.create_file)
        QtCore.QObject.connect(self.window.actionGuardar, QtCore.SIGNAL("triggered()"), self.save_file)
        QtCore.QObject.connect(self.window.actionSalir, QtCore.SIGNAL("triggered()"), self.close)
        QtCore.QObject.connect(self.window.actionCerrar, QtCore.SIGNAL("triggered()"), self.close_file)

    def close_file(self):
        if self.textbox:
            self.textbox.close()
            self.set_statusBar_Text("Cerrando archivo")

    def set_statusBar_Text(self,mensaje): 
        sb = QtGui.QStatusBar(self)
        sb.setFixedHeight(18)
        self.setStatusBar(sb)
        self.statusBar().showMessage(self.tr(mensaje))

    def create_text_edit(self,text):
        if self.textbox:
            self.textbox.close()
        self.textbox = QtGui.QTextEdit(self)
        self.textbox.setMinimumSize(800,500)
        self.textbox.setText(text)
        self.textbox.show()
    
    def create_file(self):
        fname = QtGui.QFileDialog.getSaveFileName(self,'Nuevo Archivo','/home')
        if fname:
            f = open(fname,"w")
            f.close()
            self.set_statusBar_Text("Archivo "+fname+" creado")
            self.create_text_edit("")
            self.file = fname

    def open_file(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Abrir Archivo', 
                '/home')
        if fname:
            f = open(fname,"r")
            text = f.read()
            f.close()
            self.create_text_edit(text)
            self.set_statusBar_Text("Abriendo Archivo "+fname)
            self.file = fname

    def save_file(self):
        if self.is_file_open():
            f = open(self.file,"w")
            text = self.textbox.toPlainText()
            f.write(text)
            f.close()
            self.set_statusBar_Text("archivo guardado")

    def is_file_open(self):
        if self.textbox:
            return True
        return False

    

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = Window_Form()
    myapp.show()
    sys.exit(app.exec_())