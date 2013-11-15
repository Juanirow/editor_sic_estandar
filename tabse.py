from tabse_form import Ui_DockWidget
from PyQt4 import QtCore, QtGui

class Nodot():
	## Constructor de la clase nodoT que representa un registro en 
	# la tabla de TABSE
	# @param name nombre de la variable o seccion de control (string) 
	# @param dirc direccion de la variable o seccion de control (hexadecimal-string)
	# @param sc campo booleano que indica si es o no seccion de control
	# @param leng longitud de la seccion de control (hexadecimal-string)
	def __init__(self,name,dirc,sc=False,leng="0H"):
		self.name = name
		self.dir = dirc
		self.sc = sc
		self.len = leng

	# regresa el nombre de la variable o seccione de control
	def get_name(self):
		return self.name

	#regresa la direccion de la variable o seccion de control
	def get_dir(self):
		return self.dir

	#regresa true si el registro es una seccion de control
	def get_sc(self):
		return self.sc

	#regresa la longitud de la seccion
	def get_len(self):
		return self.len

	# modifica el nombre de la variable o seccione de control
	def set_name(self,val):
		self.name = val

	#modifica la direccion de la variable o seccion de control
	def set_dir(self,val):
		self.dir = val

	#modifica true si el registro es una seccion de control
	def set_sc(self,val):
		self.sc = val

	#modifica la longitud de la seccion
	def set_len(self,val):
		self.len = val

class Tabse():
	## constructor de la clase tabse que representa la tabla 
	# de secciones 
	def __init__(self):
		self.list_n = []
		self.table = None

	## metodo que regresa si una variable fue previamente definida
	def exist_node(self,val):
		for n in self.list_n:
			if n.get_name() == val:
				return True
		return False

	## regresa el registro de la tabse el cual coiside el nombre
	def get_register(self,name):
		val = name.strip()
		for n in self.list_n:
			if n.get_name() == val:
				return n
		return None

	## inserta una variable a la tabla si esque esta no esta definida
	# regresa True si la pudo insertar 
	def insert_variable(self,name,dirc):
		if not self.exist_node(name):
			self.list_n.append(Nodot(name,dirc))
			return True
		return False

	## inserta una seccion a la tabla si esque esta no esta definida
	# regresa True si la pudo insertar 
	def insert_section(self,name,dirc,leng):
		if not self.exist_node(name):
			self.list_n.append(Nodot(name,dirc,True,leng))
			return True
		return False

	def print_tabse(self):
		self.table = Table_tabse()
		self.table.show()
		self.table.load_tabse(self.list_n)
		for n in self.list_n:
			print n.get_name(),n.get_dir()


class Table_tabse(QtGui.QDockWidget):

    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self)
        self.window = Ui_DockWidget()
        self.window.setupUi(self)

    def load_tabse(self,list_n):
    	it = 0
    	self.window.tableWidget.setRowCount(len(list_n))
    	for n in list_n:
    		item_text = QtGui.QTableWidgetItem(n.get_name())
        	self.window.tableWidget.setItem(it,0,item_text)
        	item_text = QtGui.QTableWidgetItem(n.get_dir())
        	self.window.tableWidget.setItem(it,1,item_text)
        	item_text = QtGui.QTableWidgetItem(str(n.get_sc()))
        	self.window.tableWidget.setItem(it,2,item_text)
        	item_text = QtGui.QTableWidgetItem(n.get_len())
        	self.window.tableWidget.setItem(it,3,item_text)
        	it += 1








