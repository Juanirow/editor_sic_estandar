# -*- coding: utf-8 -*-
class Symbol:
    def __init__(self,name,dir_val,sym_type):
        self.name = name
        self.dir_val = dir_val
        self.sym_type=sym_type
    
    def get_name(self):
        return self.name
    
    def set_name(self,name):
        self.name = name
        
    def get_dir_val(self):
        return self.dir_val
    
    def set_dir_val(self,dir_val):
        self.dir_val = dir_val
        
    def get_sym_type(self):
        return self.sym_type
    
    def set_sym_type(self,sym_type):
        self.sym_type = sym_type

                
        
