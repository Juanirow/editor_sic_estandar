from windowapp import Ui_windowApp
import sys
from PyQt4 import QtCore, QtGui
from my_file import File 
from Cargador import Cargador
import os


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
        self.file_name = None
        self.textbox = None
        self.textbox_errors = None
        self.textbox_obj = None
        self.cargador = None
        QtCore.QObject.connect(self.window.actionAbrir, QtCore.SIGNAL("triggered()"), self.open_file)
        QtCore.QObject.connect(self.window.actionNuevo, QtCore.SIGNAL("triggered()"), self.create_file)
        QtCore.QObject.connect(self.window.actionGuardar, QtCore.SIGNAL("triggered()"), self.save_file)
        QtCore.QObject.connect(self.window.actionSalir, QtCore.SIGNAL("triggered()"), self.close)
        QtCore.QObject.connect(self.window.actionCerrar, QtCore.SIGNAL("triggered()"), self.close_file)
        QtCore.QObject.connect(self.window.actionEnsamblar, QtCore.SIGNAL("triggered()"), self.compile)
        QtCore.QObject.connect(self.window.actionCargar, QtCore.SIGNAL("triggered()"), self.cargar)

    def cargar(self):
        if self.is_file_open():
            self.cargador = Cargador()
            self.cargador.show()
            self.cargador.load_file_name(self.file_name)

    def close_file(self):
        if self.textbox:
            self.textbox.close()
            self.set_statusBar_Text("Cerrando archivo")
        self.close_text_errors()
        self.file = None

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
        self.textbox.setGeometry(0,35,395,630)
        self.textbox.setText(text)
        self.textbox.setFont(QtGui.QFont ("Courier", 9))
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
                '/home/Desktop/Progra/EditorSIC/ejemplos')
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
        if self.file:
            return True
        return False

    def compile(self):
        self.save_file()
        self.set_statusBar_Text("Compilando")
        if self.is_file_open():
            fc = File()
            if fc.is_extension_valid(self.file,'s'):
                self.file_name = fc.get_file_name(self.file)
                self.file_name = fc.name
                self.set_statusBar_Text("Compilando") 
                os.system("python principal.py "+str(self.file))
                self.set_statusBar_Text("Cargando archivo intermedio "+self.file_name)              
                file_error = open(self.file_name+".t")
                text_errors = file_error.read()
                self.show_textBox_errors(text_errors)
                self.set_statusBar_Text("Cargando archivo objeto "+self.file_name+".os")
                if os.path.isfile(self.file_name+".os"):
                    file_obj = open(self.file_name+".os")
                    obj_text = file_obj.read()
                    self.show_textBox_obj(obj_text)
                self.set_statusBar_Text("Se termino el ensablado de "+self.file_name+".s")
            else:
                self.set_statusBar_Text("No se puede compilar el archivo no es un .s")
        else: 
            self.set_statusBar_Text("No hay un archivo por compilar")


    def show_textBox_errors(self,errors):
        if self.textbox_errors:
            self.textbox_errors.close()
        self.textbox_errors = QtGui.QTextEdit(self)
        self.textbox_errors.setGeometry(400,35,800,350)
        self.textbox_errors.setText(errors)
        self.textbox_errors.setFont(QtGui.QFont ("Courier", 9))
        self.textbox_errors.show()

    def show_textBox_obj(self,text):
        if self.textbox_obj:
            self.textbox_obj.close()
        self.textbox_obj = QtGui.QTextEdit(self)
        self.textbox_obj.setGeometry(400,480,800,510)
        self.textbox_obj.setText(text)
        self.textbox_obj.setFont(QtGui.QFont ("Courier", 14))
        self.textbox_obj.show()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = Window_Form()
    myapp.show()
    sys.exit(app.exec_())