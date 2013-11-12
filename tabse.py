
class nodot():
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
		self.len = lengs

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
	def get_len(self,val):
		self.len = val

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

class tabse():
	## constructor de la clase tabse que representa la tabla 
	# de secciones 
	def __init__(self):
		self.list_n = []

	## metodo que regresa si una variable fue previamente definida
	def exist_node(self,val):
		for n in self.list_n:
			if n.get_name() == val:
				return True
		return False

	## inserta una variable a la tabla si esque esta no esta definida
	# regresa True si la pudo insertar 
	def insert_variable(self,name,dirc):
		if not self.exist_node(name):
			self.list_n.appen(nodot(name,dirc))
			return True
		return False

	## inserta una seccion a la tabla si esque esta no esta definida
	# regresa True si la pudo insertar 
	def insert_secction(self,name,dirc,leng):
		if not self.exist_node(name):
			self.list_n.append(nodot(name,dirc,True,leng))
			return True
		return False







