from windowapp import Ui_windowApp
import sys
from PyQt4 import QtCore, QtGui
from my_file import File 
from Cargador import Cargador
from Cargadorx import Cargadorx
from objcargador import Objcargador
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
        self.fc = None
        self.tab_t = None
        self.tab_o = None
        self.cargadorx = None 
        # self.create_tabs()
        QtCore.QObject.connect(self.window.actionAbrir, QtCore.SIGNAL("triggered()"), self.open_file)
        QtCore.QObject.connect(self.window.actionNuevo, QtCore.SIGNAL("triggered()"), self.create_file)
        QtCore.QObject.connect(self.window.actionGuardar, QtCore.SIGNAL("triggered()"), self.save_file)
        QtCore.QObject.connect(self.window.actionSalir, QtCore.SIGNAL("triggered()"), self.close)
        QtCore.QObject.connect(self.window.actionCerrar, QtCore.SIGNAL("triggered()"), self.close_file)
        QtCore.QObject.connect(self.window.actionEnsamblar, QtCore.SIGNAL("triggered()"), self.compile)
        QtCore.QObject.connect(self.window.actionCargar, QtCore.SIGNAL("triggered()"), self.cargar)
        QtCore.QObject.connect(self.window.actionLigar, QtCore.SIGNAL("triggered()"), self.ligar)

    def ligar(self):
        self.cargadorx = Objcargador()
        self.cargadorx.show()

    def cargar(self):
        if self.is_file_open():
            if self.fc.extension == 's':
                self.cargador = Cargador()
                self.cargador.show()
                self.cargador.load_file_name(self.file_name)
            else:
                self.set_statusBar_Text("El archivo no es uno de la version estandar")

    def close_file(self):
        if self.textbox:
            self.textbox.close()
            self.set_statusBar_Text("Cerrando archivo")
        self.close_text_errors()
        self.close_textBox_obj()
        self.file = None

    def close_textBox_obj(self):
        if self.textbox_obj:
            self.textbox_obj.close()
            
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
        self.textbox.setGeometry(0,65,600,600)
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
        self.delete_salidas_file()
        if self.is_file_open():
            self.fc = File()
            if self.fc.is_extension_valid(self.file,'s') or self.fc.is_extension_valid(self.file,'x') :
                self.file_name = self.fc.get_file_name(self.file)
                self.file_name = self.fc.name
                self.set_statusBar_Text("Compilando") 
                os.system("python principal.py "+str(self.file))
                self.set_statusBar_Text("Cargando archivo intermedio "+self.file_name)
                self.load_output_files()
                self.set_statusBar_Text("Se termino el ensablado de "+self.file_name)
            else:
                self.set_statusBar_Text("No se puede compilar el archivo no es un .s o .x")
        else: 
            self.set_statusBar_Text("No hay un archivo por compilar")

    def show_textBox_errors(self,errors):
        if self.textbox_errors:
            self.textbox_errors.close()
        self.textbox_errors = QtGui.QTextEdit(self)
        self.textbox_errors.setGeometry(400,35,800,350)
        self.textbox_errors.setText(errors)
        self.textbox_errors.show()

    def create_tabs(self):
        if self.tab_t:
            self.tab_t.close()
        self.tab_t = QtGui.QTabWidget(self)
        self.tab_t.setGeometry(610,65,680,320)
        if self.tab_o:
            self.tab_o.close()
        self.tab_o = QtGui.QTabWidget(self)
        self.tab_o.setGeometry(610,390,680,320)
        self.tab_o.show()
        self.tab_t.show()

    def load_output_files(self):
        self.create_tabs()
        ficheros = os.listdir("./salidas")
        for s in ficheros:
            info = self.get_file_info(s)
            tab = QtGui.QWidget()
            text_e = QtGui.QTextEdit(tab)
            text_e.setText(info[2])
            text_e.setGeometry(10,10,650,310)
            extension = info[1]
            print extension
            if extension[0] == "t":
                self.tab_t.addTab(tab,info[0])
            else:
                self.tab_o.addTab(tab,info[0]) 

    def get_file_info(self,fichero):
        list_name = fichero.split(".")
        extension = list_name[-1]
        name = list_name[0]
        f = open(fichero)
        text = f.read()
        return [name,extension,text]

    def delete_salidas_file(self):
        ficheros = os.listdir("./salidas")
        for s in ficheros:
             os.remove("./salidas/"+s)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = Window_Form()
    myapp.show()
    sys.exit(app.exec_())