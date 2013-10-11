#encoding: utf-8
##
# @file registe.py
# @autor Juan Manuel Hernandez Liñan
# @brief Practica 3 Paso 2 del ensamblador para SIC estandar
# Clase para representa un registro
# @date 2 de Septiembre del 2013

from convert import Convert
##clase que representa un registro de ensamblador
class Register:
    ##constructor de la clase registro 
    def __init__(self,type):
        self.type=type
        self.register = ""
        self.init_dir = ""
    ## obtiene el tamaño del registro
    # @return regresa el tamaño en decimal
    def get_len(self):
        return len(self.register)
        
    ## checa si el registro esta lleno dependiendo el tipo de registro 
    # @return regresa True si el registro esta lleno
    def is_full(self):
        if self.type == 'T' and self.get_len() <= 59:
            return False
        return True
     
     ##checa si una cadena de bytes cabe en el registro
     #@param string cadena de bytes que se intentara insertar al registro
     #@return regresa un True si la cadena se puede insertar
    def fits_in(self,string):
        size = len(string)
        if self.type == 'T' and self.get_len()+size <= 60:
            return True
        return False
    
    ## ajusta el numero de bytes de una cadena a un numero maximo agregando 0 
    # al inicio
    # @param string cadena de bytes que se ajustaran a un tamaño
    # @param num_max tamaño al que se ajustara la cadena de bytes 
    # @return regresa una nueva cadena de bytes de tamalo num_max
    def adjust_bytes(self,string,num_max):
        new_byte = ""
        string = self.filter_number(string)
        len_str = len(string)
        it = 0
        if not num_max == len_str:
            if num_max < len_str:
                it = len_str - num_max
                return string[it:]
            while it < num_max:
                if it < len_str:
                    new_byte += string[it]
                else:
                    new_byte = "0"+new_byte
                it += 1
            return new_byte
        return string
    
    ## checa si un numero contiene la H al final y si es asi se la quita 
    # @param value cadena que representa un numero
    # @return regresa el valor hexadecimal si la H al final
    def filter_number(self,value):
        if value[-1].upper() == "H":
            return value[0:-1]
        else:
            return value
    
    ##inserta una cadena de Bytes en el registro
    def instert_string(self,str):
        str = self.filter_number(str)
        self.register+=str
#==============================================================================
#         ============ Registro de Inicio ============
#==============================================================================
    ## genera el registro de inicio
    # @param name nombre del programa
    # @param length tamaño del programa
    # @param inicial direccion de inicio del programa
    # @return regresa el registro generado
    def make_H(self,name,length,inicial):
       length = self.filter_number(length)
       inicial = self.filter_number(inicial)
       name = self.adjust_name(name)
       inicial = self.adjust_bytes(inicial,6)
       length = self.adjust_bytes(length,6)
       self.register = "H"+name+inicial+length
       return self.register
       
    ## ajusta una cadena a un tamaño definido si la cadena es menor al tamaño 
    # se le concatenan _ 
    # @param name cadena que contiene el nombre del programa
    # @return cadena con el nombre del programa ajustado a seis caracteres
    def adjust_name(slef,name):
        new_name =""       
        len_name = len(name)
        it = 0 
        while it < 6:
            if it < len_name:
                new_name += name[it]
            else:
                new_name += " "
            it += 1
        return new_name
#==============================================================================
#       =========== Registro final ============
#==============================================================================
    ## crea el registro final del codigo objeto
    # @param direccion de la etiqueta de la primera instruccion
    # @param dir_ini direccion inicial del programa
    # @return cadena con el registro final de 7 bytes
    def make_E(self,label,dir_ini):
        if label == "":
            dir = self.adjust_bytes(dir_ini,6)
        else:
            dir = self.filter_number(label)
        return "E"+self.adjust_bytes(dir,6)
        
#==============================================================================
#         ========== Registro T ==========
#==============================================================================
    ## genera un registr T con la direccion inical el tamaño del registro 
    #  y la cadena de bytes
    # @return cadena con el registro T       
    def make_T(self):
        c = Convert()
        dir = self.filter_number(self.init_dir)
        dir = self.adjust_bytes(dir,6)
        len_register = len(self.register)/2
        len_hex = c.decimal_to_hexadecimal(len_register)
        hex = self.filter_number(len_hex)
        hex = self.adjust_bytes(hex,2)
        register = "T" + dir +hex+self.register
        return register
        
    def make_M(self,obj_code,cp_num):
        c = Convert()
        cp_num = c.to_decimal(cp_num) + 1
        cp_num = c.decimal_to_hexadecimal(cp_num)        
        dir= self.filter_number(cp_num)
        dir = self.adjust_bytes(dir,6)
        edit_bytes = obj_code[3:]
        len_bytes = len(edit_bytes)
        len_bytes = self.adjust_bytes(str(len_bytes),2)
        register = "M" + str(dir) + str(len_bytes)
        return register
        
        
        
            
    
    
         
#r = Register('T')
#r.register= "1234567890"
#r.init_dir="4242H"
#print r.make_T()
