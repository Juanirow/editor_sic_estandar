# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 22:16:19 2013

@author: juanmanuelhernandezlinan
"""

from bloque import Bloques
from symbol import Symbol
from convert import Convert
from register import Register
from hexadecimal import Hexadecimal
from step2 import Step2
from displacement import Displacement
from my_file import File
class NodoS:
    
    def __init__(self,name,index=0):
        self.bloques = Bloques()
        self.errors_s = {}
        self.errors = {}
        self.warnings = {}
        self.dir_init = ""
        self.pc = []
        self.obj_code=[]
        self.symbols = []
        self.num_bloque =[]
        self.name = name
        self.step2 = Step2()
        self.inicial = "0H"
        self.code = []
        self.index= index
        self.file_name = name

    ## imprime la tabla de simbolos en un archivo 
    # @param fo archivo donde se agregara la tabla de simbolos
    def print_symbols(self,fo):
        fo.write("Tabla de Simbolos \n\n")
        d = Displacement()
        tam = 12
        string = d.get_tex_space("NOMBRE",tam)
        string += d.get_tex_space("DIR/VAL",tam)
        string += d.get_tex_space("TIPO",tam)
        string += d.get_tex_space("BLOQUE",tam)
        string += d.get_tex_space("EXTERNO",tam)+"\n"
        for s in self.symbols:
            string += d.get_tex_space(s.get_name(),tam)
            string += d.get_tex_space(str(s.get_dir_val()),tam)
            string += d.get_tex_space(s.get_sym_type(),tam)
            string += d.get_tex_space(s.num_bloque,tam)
            string += d.get_tex_space(str(s.is_externo()),tam)+"\n"
        fo.write(string+"\n\n")
    

    ## imprime la tabla de bloques en un archivo 
    # @param fo archivo donde se agregara la tabla de bloques  
    def print_bloques(self,fo):
        fo.write("Tabla de Bloques \n\n")
        d = Displacement()
        tam = 18
        string = d.get_tex_space("DIR_CARGA",tam)
        string += d.get_tex_space("NOMBRE",tam)
        string += d.get_tex_space("NUM_BLOQUE",tam)
        string += d.get_tex_space("TAMAÑO",tam)+"\n"
        for b in self.bloques.bloques:
            string += d.get_tex_space(b.load_dir,tam)
            string += d.get_tex_space(b.name,tam)
            string += d.get_tex_space(b.num,tam)
            string += d.get_tex_space(b.length,tam)+"\n"            
        fo.write(string+"\n\n")
    
    ## crea el archivo intermedio de este segmento 
    # @param extension extension del archivo intermedio que se generara 
    def archivo_intermedio(self,extension):
        fo = File()
        name_file = "./salidas/"+self.file_name+".t"+extension
        print name_file
        fo1 = open(name_file,"w")
        fo.create_file(self.file_name,"t"+extension)
        self.delete_spaces()
        self.print_intr_code(fo)
        self.print_intr_code(fo1)
        self.print_symbols(fo)
        self.print_symbols(fo1)
        self.print_bloques(fo)
        self.print_bloques(fo1)
        fo.close()
        fo1.close()
    
    ## crea el archivo objeto de este segmento 
    # @param extension extension del archivo objeto que se generara 
    def archivo_objeto(self,extension):
        fo = File()
        fo.create_file(self.file_name,"o"+extension)
        name_file = "./salidas/"+self.file_name+".o"+extension 
        fo1 = open(name_file,"w")
        self.bloques.gen_table()
        len_program = self.bloques.get_len_program()
        self.step2.directive_start(self.name,len_program,self.pc[0])               
        self.step2.complete_register()
        self.step2.make_register_m(self.obj_code,self.pc,self.num_bloque,self.bloques)
        if not self.index == 0:        
            self.step2.directive_end_segment()
        list_r = self.step2.all_registers()
        for s in list_r:
           fo.write(s+"\n")
           fo1.write(s+"\n")
        fo1.close()
        fo.close()
    
    ## crea la tabla del codigo con los campos de contador de programa
    # de numero de bloque y el codigo objeto
    # @param fo archivo donde se agregara la tabla de codigo
    def print_intr_code(self,fo):
        d = Displacement()
        tam = 18
        string = d.get_tex_space("CP",10)
        string += d.get_tex_space("BLOQUE",10)
        string += d.get_tex_space("CODIGO",45)
        string += d.get_tex_space("C. Objeto",10)+"\n"
        tam = len(self.code)
        it = 0
        while it < tam:
            string += d.get_tex_space(self.pc[it],10)
            string += d.get_tex_space(self.num_bloque[it],10)
            string += d.get_tex_space(self.code[it],45)
            if len(self.obj_code) > it:
                string += d.get_tex_space(self.obj_code[it],10)
            error = self.get_line_error(it)
            string += d.get_tex_space(error,10)+"\n"
            it += 1
        fo.write(string)

    ## elimina los espacion es una lista de codigo   
    def delete_spaces(self):
        it = 0
        while it < len(self.code):
            item = self.code[it]
            if item.strip() == "":
                self.code.remove(item)
            else:
                it += 1
    ## regresa los errores de una linea de codigo
    # @param line linea de codigo la cual se busca si tubo un error
    # @return errores lexicos y sintacticos de la linea de codigo
    def get_line_error(self,line):
        error_s = self.errors_s.get(str(line),"")
        error_p = self.errors.get(str(line),"")
        warning = self.warnings.get(str(line),"")
        if error_s == "":
            error = error_p
        else:
            error = error_s + "\t" + error_p
        return error + "\t"+ warning

        
#==============================================================================
#       Clase de segmentos  
#==============================================================================
## clase que controla los segmentos de un programa         
class Segment:
    def __init__(self):
        self.index = 0
        self.list_n = []
        self.conv = Convert()
        self.reg = Register("X")
        self.hexa = Hexadecimal()
        self.last_code = 0

    ## regresa el segmento actual
    def get_segment(self):
        return self.list_n[self.index]
    
    ##crea un segmento con el nombre especificado
    # @param name nombre del segmento que se creara 
    def new_segment(self,name):
        self.index = len(self.list_n)
        self.list_n.append(NodoS(name,self.index))


    ##inserta una etiqueta a la tabla de simbolos y si esta ya se encuentra marca un error
    #@param name simbolo que se intentara insertar a la tabla
    #@param dir_val direccion o valor del simbolo
    #@param sym_type tipo del simbolo el cual puede ser relativo o absoluto
    #@param lineno numero de linea donde se encontro la etiqueta
    def insert_symbol(self,name,dir_val,sym_type,lineno,bloque_index,externo = False):
        if self.exist_symbol(name):
            self.insert_error(str(lineno),"etiqueta previamente definida")
        else:
            sym = Symbol(name,dir_val,sym_type,bloque_index,externo)
            self.get_segment().symbols.append(sym)
            
    def exist_symbol(self ,name):
        for it in self.get_segment().symbols:
            if it.get_name() == name:
                return it
        return None
        
    ##checa si en el diccionario de errores ya se inserto un error en esa linea de codigo
    #y si no es asi la inserta 
    #@param line linea de codigo donde se encontro un error
    #@param text cadena que se genera en el error
    def insert_error(self,line,text):
        l = int(line) - self.last_code -1
        if not str(l) in self.get_segment().errors and l >= 0:
            self.get_segment().errors[str(l)]= text
    
    ##checa si en el diccionario de advertencias ya se inserto un error en esa linea de codigo
    #y si no es asi la inserta 
    #@param line linea de codigo donde se encontro un warnind
    #@param text cadena que se genera en el warning
    def insert_warning(self,line,text):
        l = int(line) - self.last_code
        if not str(l) in self.get_segment().warnings:
            self.get_segment().warnings[str(line)] = text
            
    ##aumenta el contador de programa 
    #@param increment cantidad en hexadecimal que se le agregara al CP
    def increment_PC(self,increment):
        num1 = self.get_segment().pc[-1]
        if not self.conv.is_hexadecimal(str(increment)):
            increment = self.conv.decimal_to_hexadecimal(increment)
        val = self.hexa.plus(num1,increment)
        if val == "H":
            val = "0H"
        val = self.reg.adjust_bytes(val,6,False)+"H"
        self.get_segment().bloques.set_last_cp(val)
        self.get_segment().pc.append(val)
        self.get_segment().num_bloque.append(self.get_segment().bloques.get_index())
        
    ## calcula el tamaño del programa 
    #@return regresa en hexadecimal el tamaÃ±o del programa
    def get_len_program(self):
        return  self.get_segment().bloques.get_len_program()

    ## genera y completa la tabla de bloques de todos los segmentos 
    def genera_tabla_bloques(self):
        for it in self.list_n:
            it.bloques.gen_table()
    ## regresa un segmento en un index especificado   
    # @param index posicion del segmento que se quiere
    def get_segment_at(self,index):
        return self.list_n[index] 
    
    ## imprime los resultados de un segmento 
    # @param extension es la extencion que tendran los archivos de salida de los segmentos       
    def print_results(self,extension):
        for it in self.list_n:
            # print it.errors,it.errors_s
            it.archivo_intermedio(extension)
            if len(it.errors) == 0 and len(it.errors_s) == 0:
                it.archivo_objeto(extension)
            print "Errors", len(it.errors)+len(it.errors_s)

    def get_num_errors_all(self):
        cant = 0
        for it in self.list_n:
            cant += len(it.errors_s)
            cant += len(it.errors)
        return cant 

    
