#encoding: utf-8
##
# @file pass2.py
# @autor Juan Manuel Hernandez Liñan
# @brief Practica 3 Paso 2 del ensamblador para SIC estandar
# clase que regresa los valores para la parte 2 del ensamblador
# @date 2 de Septiembre del 2013

from displacement import Displacement
from register import Register
from convert import Convert
## clase para generar el los bytes para los registros del codigo objeto
class Step2:
    ##constructor de la clase se inicializan los codigos de operacion
    def __init__(self):
        self.operations = {
            'ADD':'18','AND':'40','COMP':'28','DIV':'24',
            'J':'3C','JEQ':'30','JGT':'34','JLT':'38',
            'JSUB':'48','LDA':'00','LDCH':'50','LDL':'08',
            'LDX':'04','MUL':'20','OR':'44','RD':'D8','RSUB':'4C',
            'STA':'0C','STCH':'54','STL':'14','STSW':'E8','STX':'10',
            'SUB':'1C','TD':'E0','TIX':'2C','WD':'DC'            
        }
        self.d = Displacement()
        self.list_registers = []
        self.current_register = Register("T")
    
    ## inserta una cadena de bytes en el registro T actual si no cabe genera 
    #otro registro nuevo para almacenar los datos
    # @param str cadena que contiene la serie de bytes
    # @param dir direccion donde se encontro la instruccion
    def insert_str(self,str,dir):
        if self.current_register.get_len() == 0:
            self.current_register.init_dir = dir
            self.current_register.instert_string(str)
        else:
            if self.current_register.fits_in(str):
                self.current_register.instert_string(str)
            else:
                self.complete_register()
                self.insert_str(str,dir)
                
    ## termina el registro actual T y genera uno nuevo 
    def complete_register(self):
        if not self.current_register.get_len()==0:
            register_t = self.current_register.make_T()
            self.list_registers.append(register_t)
            self.current_register = Register("T")
#==============================================================================
#               Directiva START 
#==============================================================================
    ## Crea el registro de inicio y lo inserta  en la lista de registros
    # @param name nombre del programa
    # @param length tamaño del programa
    # @param inicial direccion de inicio del programa
    def directive_start(self,name,length,inicial):
        r = Register("H")
        register_h = r.make_H(name,length,inicial)
        self.list_registers.append(register_h)
        del r
        
#==============================================================================
#           Directiva END
#==============================================================================
    ## Crea el registro de final y lo inserta  en la lista de registros
    # @param direccion de la etiqueta de la primera instruccion a ejecutar o vacio
    def directive_end(self,label,dir_init):
        r = Register("E")
        register_e = r.make_E(label,dir_init)
        self.list_registers.append(register_e)
        del r
    
    def directive_word(self,value):
        c = Convert()
        if not c.is_hexadecimal(value):
            value = c.decimal_to_hexadecimal(value)
        r = Register("T")
        value = r.adjust_bytes(value,6)
        value = r.filter_number(value)
        del r
        return value
        
#==============================================================================
#       Directiva BYTE
#==============================================================================
    ## regresa los bytes que genera las constantes de BYTE
    # @param value argumento de la directiva BYTE
    # @return secuenca de bytes que genero la constante
    def const_BYTE(self,value):
        data = self.d.filter_byte(value)        
        if self.d.is_constant_hexadecimal(value):
            return self.get_value_hex_BYTE(data)
        else:
            return self.get_value_cad_BYTE(data)
            
    ## genera la secuencia de bytes para constantes hexadecimales 
    # valor de la constante a calcular su secuencia de bytes
    # @param data valor de la constante hexadecimal
    # @return regresa un numero par de bytes que representan el numero hexadecimal
    def get_value_hex_BYTE(self,data):
        if len(data) % 2 == 0:
            return data
        else: 
            return "0"+data
    ## genera la secuancia de bytes para las constantes de cadena de BYTE
    # convirtiendo cada caracter en su codigo ascii
    #@param data valor de la constante de cadena
    # @return secuencia de codigos ascii que representan la cadena
    def get_value_cad_BYTE(self,data):
        string_out =""
        c = Convert()
        r = Register("T")        
        for caracter in data:
            car = str(ord(caracter))
            car = c.decimal_to_hexadecimal(car)
            car = r.filter_number(car)
            string_out+=car
        del c
        return string_out
        
#==============================================================================
#         =======  Conjunt de Instrucciones =====
#==============================================================================
    ## regresa la cadena de bytes que representa la operacion RSUB
    def operation_RSUB(self):
        val = self.operations['RSUB']
        val +="H"
        c = Convert()
        val = c.to_decimal(val)
        val = int(val)
        binary = c.decimal_to_binary(val,24)
        binary = c.shift_binary_left(binary,16)
        val = c.decimal_to_hexadecimal(int(binary,2))
        r = Register("T")
        val = r.filter_number(val)
        del r
        del c
        return val
        
        
#        return self.operations['RSUB']+"0000"
     
    ## regresa una cadena de bytes que genera una operacion del conjunto de 
     #instrucciones
     #@param operator instruccion la cual se generara la cadena de Bytes
     #@param m argumento de la instruccion
     #@param is_index el modo de direccionamiento True es indexado
     #@return regresa la cadena de bytes
    def operations_code(self,operator,m,is_index):
        r = Register("T")
        c = Convert()        
        op = self.operations[operator]
        op = op+"H"
        op = c.to_decimal(op)
        op = int(op)
        binary = c.decimal_to_binary(op,24)
        binary = c.shift_binary_left(binary,16)
        if is_index:
            binary = c.mask_or(binary,"000000001000000000000000")
        m = c.to_decimal(m)
        m = int(m)
        m = c.decimal_to_binary(m,24)
        binary = c.mask_or(binary,m)
        val = int(binary,2)
        val = c.decimal_to_hexadecimal(val)
        val = r.filter_number(val)  
        val = r.adjust_bytes(val,6)
        del r
        del c
        return val
        
