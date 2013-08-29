#encoding: utf-8
# Archivo: principal.py
# Autor: Juan Manuel Hernandez Liñan
# Fecha: 22 de Agosto del 2013
# Descripción: Practica 1 Analizador lexico y sintactico del ensamblador Sic estandar. 
#         En este modulo se checara la extencion del archivo de entrada y se creara el archivo 
# de salida que contendra los errores sintacticos y lexicos 
from parser import parse
import parser

class Ensamblador:

	def get_scanner_errors(self):
		errors = parser.get_lexic_errors()
		return errors
		
	def get_parser_errors(self):
		errors = parser.get_sintactic_errors()
		return errors

	def analiza(self,text):
		parser.errors = []
		parser.list_line_errors = []
		parser.scann.errors = []
		parser.scann.list_error_line = []
		parse.parse(text)

	def get_all_errors(self):
		return self.get_scanner_errors() + self.get_parser_errors()

	def num_errors(self):
		return len(self.get_all_errors())

	def get_errors_string(self):
		errors = self.get_all_errors()
		text = ""
		for n in errors:
			text += n
		return text