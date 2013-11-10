# -*- coding: utf-8 -*-
class Symbol:
    def __init__(self,name,dir_val,sym_type,num_bloque=0,externo=False):
        self.name = name
        self.dir_val = dir_val
        self.sym_type=sym_type
        self.num_bloque = num_bloque
        self.externo = externo
    
    ##regresa si el simbolo es externo
    def is_externo(self):
        return self.externo
    ## modifica el atributo que indica si el simbolo es externo
    def set_externo(self,ext):
        self.externo = ext
    ##obtiene el nombre del simbolo
    def get_name(self):
        return self.name
    ## modifica el nombre del simbolo
    # @param name nombre nuevo del simbolo
    def set_name(self,name):
        self.name = name
    ## regresa la direccion o el valor del simbolo   
    def get_dir_val(self):
        return self.dir_val
    ## modifica la direccion o el valor del simbolo
    # @param dir_val nuevo valor de direccion del simbolo
    def set_dir_val(self,dir_val):
        self.dir_val = dir_val
    # regresa el tipo de simbolo (relativo, absoluto,_ == externo )
    def get_sym_type(self):
        return self.sym_type
    ## modifica el tipo de simbolo
    # @param sym_type nuevo tipo que se le asignara al tipo 
    def set_sym_type(self,sym_type):
        self.sym_type = sym_type
    ## regresa el numero de bloque al que pertenece el simbolo
    def get_num_bloque(self):
        return self.num_bloque

