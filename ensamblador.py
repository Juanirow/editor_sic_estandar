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
		parser.ini_sintactic_errors()
		parser.ini_lexic_errors()
		print str(self.num_errors())
		parse.parse(text)
		print str(self.num_errors())

	def get_all_errors(self):
		print self.get_scanner_errors()
		print self.get_parser_errors()
		return self.get_scanner_errors() + self.get_parser_errors()

	def num_errors(self):
		print "num_errors"
		return len(self.get_all_errors())

	def get_errors_string(self):
		print "errors_string"
		errors = self.get_all_errors()
		text = ""
		for n in errors:
			text += n
		return text