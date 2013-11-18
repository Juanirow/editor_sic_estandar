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
		self.end_program = "0H"
		self.window.btnSimular.clicked.connect(self.simular)
		self.operations_3 = {"18":"ADD","00":"LDA","40":"AND","28":"COMP","24":"DIV","3C":"J","30":"JEQ","34":"JGT","38":"JLT",
                           "48":"JSUB","50":"LDCH","08":"LDL","04":"LDX","20":"MUL","4C":"RSUB","0C":"STA","54":"STCH","14":"STL",
                           "E8":"STSW","10":"STX","1C":"SUB","2C":"TIX","58":"ADDF","88":"COMPF","64":"DIVF","68":"LDB","70":"LDF",
                           "6C":"LDS","74":"LDT","D0":"LPS","60":"MULF","EC":"SSK","78":"STB","80":"STF","D4":"STI","7C":"STC","E8":"STSW",
                           "84":"STT","5C":"SUBF","E0":"TD","DC":"WD"}
		self.operations_1 = {"C4":"FIX","C0":"FLOAT","F4":"HIO","C8":"NORM","F0":"SIO","F8":"TIO"}
		self.operations_2 = {"90":"ADDR","B4":"CLEAR","A0":"COMPR","9C":"DIVR","98":"MULR","AC":"RMO","A4":"SHIFTL","A8":"SHIFTR",
							"94":"SUBR","B0":"SVC","B8":"TIXR"}
		self.operations = {"18":self.add,"00":"LDA","40":"AND","28":"COMP","24":"DIV","3C":"J","30":"JEQ","34":"JGT","38":"JLT",
                           "48":"JSUB","50":"LDCH","08":"LDL","04":"LDX","20":"MUL","4C":"RSUB","0C":"STA","54":"STCH","14":"STL",
                           "E8":"STSW","10":"STX","1C":"SUB","2C":"TIX","58":self.float_operations,"88":self.float_operations,
                           "64":self.float_operations,"68":"LDB","70":self.float_operations,"6C":"LDS","74":"LDT",
                           "D0":self.system_operations,"60":self.float_operations,"EC":self.system_operations,"78":"STB",
                           "80":self.float_operations,"D4":self.system_operations,"7C":"STC","E8":self.system_operations,
                           "84":"STT","5C":"SUBF","E0":self.system_operations,"DC":self.system_operations,"C4":self.float_operations,
                           "C0":self.float_operations,"F4":self.system_operations,"C8":self.float_operations,"F0":self.system_operations,
                           "F8":self.system_operations,"90":self.addr,"B4":"CLEAR","A0":"COMPR","9C":"DIVR","98":"MULR","AC":"RMO","A4":"SHIFTL",
                           "A8":"SHIFTR","94":"SUBR","B0":"SVC","B8":"TIXR"}
		self.registers = {"0":[self.REG_A,"A"],"1":[self.REG_X,"X"],"2":[self.REG_L,"L"],"8":[self.REG_CP,"CP"],"9":[self.REG_SW,"SW"],"3":[self.REG_B,"B"],
       "4":[self.REG_S,"S"],"5":[self.REG_T,"T"],"6":[self.REG_F,"F"]}

	def simular(self):
		num_actions = self.get_count_next_actions()
		if num_actions == -1:
			self.window.textEdit_Actions.setText("Numero de simulaciones no Validas")
		else:
			self.make_n_simulations(num_actions)

	def make_n_simulations(self,number):
		it = 0
		while it < number:
			cp = self.get_register(self.REG_CP)
			if self.hexa.minus_than(cp,self.end_program):
				op = self.get_operation()
				type_op = op[2]
				m = self.get_m(type_op,cp)
				if m == "Error":
					self.window.textEdit_Actions.setText("El programa se termino debido a un error de operacion")
				else:
					fun = self.operations[op[0]]
					fun(m)
					self.show_next_instr()
			else:
				self.window.textEdit_Actions.setText("El programa se termino")
			it += 1

	def get_m(self,type_op,cp):
		if type_op == "Error":
			return type_op
		if type_op == "1":
			return "0"
			self.increment_cp(1)
		if type_op == "2":
			cp_n = self.hexa.plus(cp,"1H")
			self.increment_cp(2)
			return self.get_data_form_mem(cp_n,1)
		return self.get_m_type3()

	def get_count_next_actions(self):
		count_actions = str(self.window.textEdit_Num.toPlainText())
		if count_actions == "":
			count_actions = 1
		elif not count_actions.isdigit():
			return -1
		return int(count_actions)

 	def system_operations(self,val):
 		self.window.textEdit_Actions.setText("No tiene los permisos \n para ejecutar esta instruccion")

	def float_operations(self,val):
 		self.window.textEdit_Actions.setText("Las instrucciones flotantes \n no se pueden ejecutar")

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
		self.show_next_instr()
		self.end_program = self.cargador.dirsc

	def increment_cp(self,num):
		num_hexa = self.convert.decimal_to_hexadecimal(num)
		cp = self.get_register(self.REG_CP)
		res = self.hexa.plus(num_hexa,cp)
		self.set_register(self.REG_CP,res)

	def show_next_instr(self):
		op = self.get_operation()
		self.window.label_sig.setText(op[1])
	
	def get_operation(self):
		cp = self.get_register(self.REG_CP)
		value = self.get_data_form_mem(cp,1)
		val = value[0]
		val2 = value[1]
		val_d = int(self.convert.to_decimal(val2+"H"))
		val_d = val_d & 12
		value = val + self.convert.decimal_to_hexadecimal(str(val_d))[:-1]
		tip = "Error"
		op = self.operations_1.get(value,"Error")
		if not op == "Error":
			tip = "1"
		else:
			op = self.operations_2.get(value,"Error")
			if not op == "Error":
				tip = "2"
			else:
				op = self.operations_3.get(value,"Error")
				if not op == "Error":
					tip = "3"
		return [value,op,tip]
		
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

	def get_m_type3(self):
		cp = self.get_register(self.REG_CP)
		data1 = self.get_data_form_mem(cp,1)
		type_d = self.get_operation_type(data1)
		next_loc = self.hexa.plus(cp,"1H")
		data = self.get_data_form_mem(next_loc,1)
		print data1,type_d,next_loc,data
		msb = data[0]
		msb_d = int(self.convert.to_decimal(msb+"H"))
		tam = 3
		if (msb_d & 1) == 1:
			tam = 4
		next_loc = self.hexa.plus(next_loc,"1H")
		m = data[1] + self.get_data_form_mem(next_loc,tam-2)
		print m,tam,next_loc
		cp = self.get_register(self.REG_CP)
		cp = self.hexa.plus(cp,str(tam))
		self.set_register(self.REG_CP,cp)
		if type_d == "simple_s":
			m = str(msb_d & 7) + m
			type_d = "simple"
		elif (msb_d & 6) == 0:
			m = m
		else:
			if (msb_d & 4) == 4:
				b = self.get_register(REG_B)
				m = self.hexa.suma(m+"H",b)
			if (msb_d & 2) == 2:
				cp = self.get_register(self.REG_CP)
				m = self.hexa.suma(m+"H",cp)
		if (msb_d & 8) == 8:
			x = self.get_register(REG_X)
			m = self.hexa.suma(m+"H",x)
		print "mem",m
		if not type_d == "inmediato":
			m = self.get_data_form_mem(m,3)
			if not type_d == "simple":
				m = self.get_data_form_mem(m,3)
		return m
		
	def get_operation_type(self,data):
		d = data[1]
		d_d = int(self.convert.to_decimal(d+"H"))
		val = d_d & 3
		if val == 3:
			return "simple"
		elif val == 2:
			return "indirecto"
		elif val == 1:
			return "inmediato"
		return "simple_s"


	def add(self,m):
		string = "(A) <- (m..m+2)"+"\n" + "(A) <-  "+ m
		self.set_register(self.REG_A,m)
		self.window.textEdit_Actions.setText(string)

	def addr(self,m):
		string ="r2 <- (r1) + (r2)"+"\n"
		r1 = self.registers[m[0]]
		r2 = self.registers[m[1]]
		string += "(r1) = "+r1[1]+"\n (r2) = "+r2[1]+"\n"
		dat1 = self.get_register(r1[0])
		dat2 = self.get_register(r2[0])
		res = self.hexa.plus(dat1,dat2)
		string += "("+r2[1]+")<-"+res
		self.set_register(r2[0],res)
		self.window.textEdit_Actions.setText(string)
