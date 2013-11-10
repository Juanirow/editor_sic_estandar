# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 22:28:27 2013

@author: juanmanuelhernandezlinan
"""
from convert import Convert
from hexadecimal import Hexadecimal
from displacement import Displacement
class Nodob():

    def __init__(self, name="por omision", num=0):
        self.load_dir = "0H"
        self.name = name
        self.length = "0H"
        self.num = num
        self.last_cp = "000000H"
    ## regresa la direccion de carga del bloque  
    def get_load_dir(self):
        return self.load_dir
    ## modifica la direccion de carga del bloque
    # @param val nueva direccion de carga
    def set_load_dir(self,val):
        self.load_dir = val
    ## regresa el nombre del bloque
    def get_name(self):
        return self.name
    ## regresa el tamaño del bloque 
    def get_length(self):
        return self.length
    ## regresa el numero del bloque
    def get_num(self):
        return self.num
    ## regresa el ultimo valor del contador de programa  
    def get_last_cp(self):
        return self.last_cp
    ## modifica el ultimo valor del contador de programa
    def set_last_cp(self,cp):
        self.last_cp = cp
        

class Bloques():
    def __init__(self):
        self.bloques = []
        self.index_bloque = 0
        self.bloques.append(Nodob())

    ## regresa un bloque que tiene como atributo nombre igual a
    # el parametro name si no lo encuentra regresa None
    def existe_bloque(self, name):
        for x in self.bloques:
            if x.name == name:
                return x
        return None

    ## crea un nuevo bloque si la lista de bloques ya contiene uno 
    # con el nombre del bloque que se quiere crear regresa el bloque existente
    def nuevo_bloque(self, name):
        b = self.existe_bloque(name)
        if b == None:
            self.index_bloque = len(self.bloques)        
            b = Nodob(name,self.index_bloque)
            self.bloques.append(b)
        else:
            self.index_bloque = b.get_num()
    
    ## regresa el ultimo valor del contador de programa
    def get_last_cp(self):
        b = self.bloques[self.index_bloque]
        return b.get_last_cp()
    
    ## modifica el ultimo valor del contador de programa
    def set_last_cp(self,cp):
         b = self.bloques[self.index_bloque]
         b.set_last_cp(cp)
    ## regresa el index del bloque actual
    def get_index(self):
        return self.index_bloque

    ## regresa una cadena que representa la tabla de bloques que 
    # indican la dir de inicio , el nombre, el numero de bloque,
    # y el tamaño del bloque
    def get_tab_bloq(self):
        d = Displacement()
        tam = 18
        string = d.get_tex_space("DIR",tam)
        string += d.get_tex_space("NOMBRE",tam)
        string += d.get_tex_space("BLOQUE",tam)
        string += d.get_tex_space("TAMAÑO",tam)+"\n"
        for x in self.bloques:
            string += d.get_tex_space(x.get_load_dir(), tam)
            string += d.get_tex_space(x.get_name(), tam)
            string += d.get_tex_space(x.get_num(), tam)
            string += d.get_tex_space(x.get_length(), tam)+"\n"
        return string

    ## genera la tabla para calcula la direccion de inicio del bloque   
    def gen_table(self):
        h = Hexadecimal()
        dir_c = self.bloques[0].get_load_dir()
        for x in self.bloques:
            x.set_load_dir(dir_c)
            if x.name == "por omision":
                x.length = h.subs(x.last_cp,x.get_load_dir())
            else: 
                x.length = x.last_cp
            dir_c = h.plus(dir_c,x.length)
    
    ## pbtinene el tamaño del programa        
    def get_len_program(self):
        c = Convert()
        x = self.bloques[-1]
        ini = self.bloques[0]
        val = c.to_decimal(x.get_load_dir())
        val_len = c.to_decimal(x.length)
        val_ini = c.to_decimal(ini.get_load_dir())
        val = val + val_len - val_ini
        val = c.decimal_to_hexadecimal(val)
        return val
    ## modifica la direccion de carga del bloque inicial o por omision
    def set_load_dir(self,val):
        self.bloques[0].set_load_dir(val)
    ## regresa el bloque del estado acutal  
    def get_bloque_act(self):
        index = self.index_bloque
        return self.bloques[index]
    ## regresa el ultimo valor del contador de programa del bloque especificado
    # @param index numero de bloque 
    def get_last_pc_at(self,index):
        return self.bloques[index].get_last_cp()

    ## regresa el ultimo valor del inicio de  programa del bloque especificado
    # @param index numero de bloque 
    def get_load_dir_at(self,index):
        return self.bloques[index].get_load_dir()
        