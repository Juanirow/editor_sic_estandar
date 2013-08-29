from windowapp import Ui_windowApp
import sys
from PyQt4 import QtCore, QtGui
from my_file import File 
from ensamblador import Ensamblador
import scanner
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Window_Form(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self)
        self.window = Ui_windowApp()
        self.window.setupUi(self)
        self.file = None
        self.textbox = None
        self.textbox_errors = None
        QtCore.QObject.connect(self.window.actionAbrir, QtCore.SIGNAL("triggered()"), self.open_file)
        QtCore.QObject.connect(self.window.actionNuevo, QtCore.SIGNAL("triggered()"), self.create_file)
        QtCore.QObject.connect(self.window.actionGuardar, QtCore.SIGNAL("triggered()"), self.save_file)
        QtCore.QObject.connect(self.window.actionSalir, QtCore.SIGNAL("triggered()"), self.close)
        QtCore.QObject.connect(self.window.actionCerrar, QtCore.SIGNAL("triggered()"), self.close_file)
        QtCore.QObject.connect(self.window.actionCompilar, QtCore.SIGNAL("triggered()"), self.compile)


    def close_file(self):
        if self.textbox:
            self.textbox.close()
            self.set_statusBar_Text("Cerrando archivo")
        self.close_text_errors()

    def close_text_errors(self):
        if self.textbox_errors:
            self.textbox_errors.close()

    def set_statusBar_Text(self,mensaje): 
        sb = QtGui.QStatusBar(self)
        sb.setFixedHeight(18)
        self.setStatusBar(sb)
        self.statusBar().showMessage(self.tr(mensaje))

    def create_text_edit(self,text):
        if self.textbox:
            self.textbox.close()
        self.textbox = QtGui.QTextEdit(self)
        self.textbox.setGeometry(0,35,395,545)
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

    def compile(self):
        self.save_file()
        self.set_statusBar_Text("Compilando")
        if self.is_file_open():
            fc = File()
            if fc.is_extension_valid(self.file,'s'):
                e = Ensamblador()
                self.close_text_errors()
                text = self.textbox.toPlainText()
                text = str(text)
                e.analiza(text)
                text = self.show_textBox_errors(e)
                fo = File()
                fc.open(self.file)
                fc.close()
                fo.create_file(fc.name,'t')
                fo.write(text)
                fo.close()
                del e
            else:
                self.set_statusBar_Text("No se puede compilar el archivo no es un .s")


    def show_textBox_errors(self,e):
        text = "No se detecto ningun error"
        if e.num_errors() > 0:
            if self.textbox_errors:
                self.textbox_errors.close()
            text = e.get_errors_string()
            self.textbox_errors = QtGui.QTextEdit(self)
            self.textbox_errors.setGeometry(400,35,800,545)
            self.textbox_errors.setText(text)
            self.textbox_errors.show()
        else:
            self.set_statusBar_Text(text)
        return text 

    

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = Window_Form()
    myapp.show()
    sys.exit(app.exec_())