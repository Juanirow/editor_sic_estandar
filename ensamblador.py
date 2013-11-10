#encoding: utf-8

## Clase que ensambla archivos .s
# @file convert.py
# @autor Juan Manuel Hernandez Liñan
# @brief Practica 2 Paso 1 del ensamblador para SIC estandar
# clase para ensamblar archivos .s
# @date 06 de Septiembre del 2013

from my_file import File
from parser import parse
from displacement import Displacement
import parser
from segment import Segment
import scanner

class Ensamblador:
    
    
    ## metodo donse se aplica el paso 1 y paso 2 
    # a un archivo fuente .s 
    # @param file nombre del archivo a abrir
    def ensambla(self,file):
        self.init()
        file_name = file
        fi = File()
        print "==============="
        if fi.open(file_name):
            text = fi.read()
            parser.seg.new_segment(fi.name)
            parser.extension = fi.extension
            text_file=self.new_line_filter(text)
            list_text = text_file.split("\n")
            parser.load_code(list_text)
            # scanner.entrada(text_file)
            # parser.scann.lineno = 1
            parse.parse(text_file)
            if parser.num_errors() == 0:
                parse.pasada = 2
                parser.seg.genera_tabla_bloques()
                parser.scann.lineno = 1
                parser.scann.linea = 1
                parse.last_index = 0
                parser.seg.index = 0
                parse.parse(text_file)
            parser.seg.print_results(fi.extension)
                
    ##inicializa los valores usados en analisis lexico y sintactico
    def init(self):
        parser.scann.lineno = 1
        parser.scann.linea = 1
        parse.pasada=1
        parse.inicial = "0H"
        parse.list_code = []
        parser.seg = Segment()
        parse.last_index = 0
    
    ## elimina los saltos de linea consecutivos 
    # @param str cadena a la que se le eliminaran los saltos de linea          
    def new_line_filter(self,str):
        list_str = str.split('\n')
        cad =""
        for str in list_str:
            if not str == "" and not str == "\t": 
                cad += str+"\n"
        return cad    

            