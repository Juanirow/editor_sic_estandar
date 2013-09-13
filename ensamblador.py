#encoding: utf-8

## Clase que ensambla archivos .s
# @file convert.py
# @autor Juan Manuel Hernandez Liñan
# @brief Practica 2 Paso 1 del ensamblador para SIC estandar
# clase para ensamblar archivos .s
# @date 06 de Septiembre del 2013

from my_file import File
from parser import parse
from step2 import Step2
import parser

class Ensamblador:
    
    
    ## metodo donse se aplica el paso 1 y paso 2 
    # a un archivo fuente .s 
    # @param file nombre del archivo a abrir
    def ensambla(self,file):
        self.init()
        file_name = file
        fi = File()
        if fi.open(file_name):
            text = fi.read()
            text_file=self.new_line_filter(text)
            list_text = text_file.split("\n")
            parse.parse(text_file)
            file_name = fi.name
            fo = File()
            fo.create_file(file_name,"t")
            if not parser.num_errors() == 0:            
                self.print_error_step1(fo,list_text)
            else:
                parse.pasada=2
                parser.scann.lineno = 1
                parse.parse(text_file)
                len_p = parser.get_len_program()
                fi.close()
                print "============"
                print "Del archivo "+fo.name
                print "Errores: "+str(parser.num_errors())
                print "Warnings: " +str(len(parser.warnings))
                fo.write("Tamaño del Programa:" + str(len_p)+"\n\n")
                self.print_program(fo,list_text)
                fo.write("\n\n")
                self.print_symbols(fo)
                if parser.num_errors()==0:
                    fo_obj = File()
                    fo_obj.create_file(file_name,"os")
                    self.print_obj_file(fo_obj)
            fo.close()
            
    ##inicializa los valores usados en analisis lexico y sintactico
    def init(self):
        parser.step2 = Step2()
        parser.scann.lineno = 1        
        parser.errors = {}
        parser.dir_init = ""
        parser.pc = []
        parser.obj_code=[]
        parser.symbols = {}
        parse.pasada=1
        parse.inicial = "0H"
        parser.warnings = {}
            
    ## concatena una lista de strings para formar un unico texto
    #@param list: lista de cadenas que se concatenara
    #@return regresa un string        
    def list_to_string(self,list):
        text = ""
        for line in list:
            text += line
        return text
    
    
    
    ## regresa los errores de una linea de codigo
    # @param line linea de codigo la cual se busca si tubo un error
    # @return errores lexicos y sintacticos de la linea de codigo
    def get_line_error(self,line):
        error_s = parser.scann.errors.get(str(line),"")
        error_p = parser.errors.get(str(line),"")
        warning = parser.warnings.get(str(line),"")
        if error_s == "":
            error = error_p
        else:
            error = error_s + "\t" + error_p
        return error + "\t"+ warning
        
    ## genera una cadena de espacios (caracter) con una longitud calculada
    #por un numero dado menos el tamaño de una cadena
    # @param string cadena la cual se le restara al numero maximo de espacios 
    # @num numero maximo de espacios que se quiere
    #@return cadena con espacios en blanco calculados
    def str_space(self,string,num):
        val = len(string)
        cad = " "
        while val < num:
            cad += " "
            val += 1
        return cad
        
    ##imprime en un archivo el codigo de entrada pero con contador de programa y errores 
    #@param file archivo de salida
    #@param lista de cadenas que forman el archivo
    def print_program(self,file,list):
        file.write("Archivo intermedio\n")
        ite = 0
        while ite < len(list):
            error = self.get_line_error(ite+1)
            code = list[ite]
            if not code == "":
                string = list[ite]
                string = parser.pc[ite] + "\t" + string+ self.str_space(string,30)
                if ite < len(parser.obj_code):
                    string += parser.obj_code[ite] + "\t" 
                string += error +"\n"
                file.write(string)
            ite += 1
    
    ## imprime la tabla de simbolos
    # @param fo archivo donde se imprimiran los simbolos      
    def print_symbols(self,fo):
        fo.write("Tabla de Simbolos \n\n")
        for s in parser.symbols:
            str = s + self.str_space(s,10) + parser.symbols[s]+"\n"
            fo.write(str)
    
    ## elimina los saltos de linea consecutivos 
    # @param str cadena a la que se le eliminaran los saltos de linea          
    def new_line_filter(self,str):
        list_str = str.split('\n')
        cad =""
        for str in list_str:
            if not str == "": 
                cad += str+"\n"
        return cad
    
    ## imprime los registros que forman el archivo objeto
    # @param fo archivo donde se imprimiran los registros
    def print_obj_file(self,fo):
        for s in parser.step2.list_registers:
            fo.write(s+"\n")     
    
    def print_error_step1(self,fo,list):
        it = 0
        len_p = len(list)
        while it < len_p:
            error = self.get_line_error(it)
            fo.write(error+"\n")
            it += 1 
            