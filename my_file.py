#encoding: utf-8
# Archivo: my_file.py
# Autor: Juan Manuel Hernandez Liñan
# Fecha: 19 de Agosto del 2013
# Descripción: Practica 1 Analizador lexico y sintactico del ensamblador SIC estandar
#clase para la manipulacion de archivos

class File:

	#Constructor de la clase donde se definen sus variables
	def __init__(self):
		self.name = ""
		self.file = None

	#metodo para abrir un archivo el cual checa si la 
	#extension es .s regresa True si el archico se pudo abrir y si 
	#es de la extencion correcta
	def open(self,file_name):
		if self.get_file_name(file_name):
			self.file = open(file_name)
			return True
		else:
			print "No se pudo abrir el archivo no es una archivo .s"
		return False

	def create_file(self,name,extension):
		self.name = name
		file_name = name+"."+extension
		self.file = open(file_name,"w")


	#regresa el contenido del archivo
	def read(self):
		return self.file.read()

	#escribe en el archivo lo que contenga la variable string
	def write(self,string):
		self.file.write(string)

	def write_list(self,list_string):
		for x in list_string:
			self.file.write(x+"\n")

	#cierra el archivo
	def close(self):
		self.file.close()

	#separa la cadena para obtener su extension y el nombre del archivo
	def get_file_name(self,string):
		list_names =  string.split('.')
		if self.is_extension_valid(string,'s'):
			self.extension = list_names[-1]
			name_part = list_names[-2]
			list_names = name_part.split('/')
			self.name = list_names[-1]
			return True
		return False

	#checa si la lista de cadenas el tiene mas de dos elementos
	#y si el ultimo elemento es de s	
	def is_extension_valid(self,name,extension):
		list_names = name.split('.') 
		ret = False
		if list_names.count >= 2:
			if list_names[-1] == extension:
				ret = True
		return ret

