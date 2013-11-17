from PyQt4 import QtCore, QtGui
from hexadecimal import Hexadecimal
from convert import Convert
from register import Register
from windowcargador import Ui_DockWidget
from Cargadorx import Cargadorx

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Simuladorx(QtGui.QDockWidget):
	REG_CP = 0
	REG_A = 1
	REG_X = 2
	REG_L = 3
	REG_SW = 4
	REG_B = 5
	REG_S = 6
	REG_T = 7
	REG_F = 8

	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self)
		self.window = Ui_DockWidget()
		self.window.setupUi(self)
		self.add_registers()
		self.cargador = None
		self.hexa = Hexadecimal()
		self.convert = Convert()
		self.register = Register("A")
		self.init_registers()
		self.operations_text = {"18":"ADD","00":"LDA","40":"AND",
                           "28":"COMP","24":"DIV","3C":"J",
                           "30":"JEQ","34":"JGT","38":"JLT",
                           "48":"JSUB","50":"LDCH","08":"LDL",
                           "04":"LDX","20":"MUL","4C":"RSUB",
                           "0C":"STA","54":"STCH","14":"STL",
                           "E8":"STSW","10":"STX","1C":"SUB","2C":"TIX"}

	def add_registers(self):
		self.window.tableWidget_2.setRowCount(9)
		item = QtGui.QTableWidgetItem()
		item.setText("B")
		self.window.tableWidget_2.setVerticalHeaderItem(5, item)
		item = QtGui.QTableWidgetItem()
		item.setText("S")
		self.window.tableWidget_2.setVerticalHeaderItem(6, item)
		item = QtGui.QTableWidgetItem()
		item.setText("T")
		self.window.tableWidget_2.setVerticalHeaderItem(7, item)
		item = QtGui.QTableWidgetItem()
		item.setText("F")
		self.window.tableWidget_2.setVerticalHeaderItem(8, item)

	def init_registers(self):
		it = 0
		while it < 9:
			item_text = QtGui.QTableWidgetItem("FFFFFFFH")
			self.window.tableWidget_2.setItem(it,0,item_text)
			it += 1


	def set_register(self,reg_num,val):
		val_hex = self.register.adjust_bytes(val,6,False)
		val_hex = self.hexa.change_hexadecimal(val_hex)
		item_text = QtGui.QTableWidgetItem(val_hex)
		self.window.tableWidget_2.setItem(reg_num,0,item_text)

	def get_register(self,reg_num):
		item = self.window.tableWidget_2.item(reg_num,0)
		return str(item.text())

	def carga(self,list_obj,dirprog):
		self.cargador = Cargadorx(self.window)
		self.cargador.load_file_name(list_obj,dirprog)
		cp = self.cargador.direj
		self.set_register(self.REG_CP,cp)
		self.get_next_instr()

	def increment_cp(self,num):
		num_hexa = self.convert.decimal_to_hexadecimal(num)
		cp = self.get_register(self.REG_CP)
		res = self.hexa.plus(num_hexa,cp)
		self.set_register(self.REG_CP,res)

	def get_next_instr(self):
		cp = self.get_register(self.REG_CP)
		data = self.get_data_form_mem(cp,1)

		self.window.textEdit_Actions.setText(data)

	##regresa los datos de una localidad y las licalidades 
	#siguientes 
	# @param localidad  donde se obtendra el dato
	# @param num_loc cuantas localidades siguientes accedera 
	def get_data_form_mem(self,location,num_loc):
		loc = self.register.filter_number(location)
		row = self.get_row_index(loc)
		col = self.get_column_index(loc)
		data = ""
		it = col
		count = 0
		while count < num_loc:
			item = self.window.tableWidget.item(row,it)
			data += str(item.text())
			it = (it+1)%17
			if it == 0:
				it = 1
				row+=1
			count += 1
		return data

		

	def get_row_index(self,value):
		index = str(value[0:-1])+"0"
		it = 0
		index = self.register.adjust_bytes(index,6,False)
		num_rows = self.window.tableWidget.rowCount()
		while it < num_rows:
			val = self.window.tableWidget.item(it,0)
			if str(val.text()) == index:
				return it
			it += 1
		return 0
        
	def get_column_index(self,value):        
		index = str(value[-1])+"H"
		index = self.convert.to_decimal(index)
		return index+1



