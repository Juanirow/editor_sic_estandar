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
from hexadecimal import Hexadecimal
## clase para generar el los bytes para los registros del codigo objeto
class Step2:
    ##constructor de la clase se inicializan los codigos de operacion
    def __init__(self):
        self.operations = {
            'ADD':'18','ADDF':'58','ADDR':'90','AND':'40','CLEAR':'B4','COMP':'28',
            'COMPF':'88','DIV':'24','COMPR':'A0','DIVF':'64','DIVR':'9C','FIX':'C4',
            'FLOAT':'C0','HIO':'F4','J':'3C','JEQ':'30','JGT':'34','JLT':'38',
            'JSUB':'48','LDA':'00','LDB':'68','LDCH':'50','LDF':'70','LDL':'08','LDS':'6C',
            'LDT':'74','LDX':'04','LPS':'D0','MUL':'20','MULF':'60','MULR':'98','NORM':'C8',
            'OR':'44','RD':'D8','RMO':'AC','RSUB':'4C','SHIFTL':'A4','SHIFTR':'A8','SIO':'F0',
            'SSK':'EC','STA':'0C','STB':'78','STCH':'54','STF':'80','STI':'D4',
            'STL':'14','STS':'7C','STSW':'E8','STT':'84','STX':'10',
            'SUB':'1C','SUBF':'5C','SUBR':'94','SVC':'B0','TD':'E0','TIO':'F8','TIX':'2C',
            'TIXR':'B8','WD':'DC'            
        }
        self.d = Displacement()
        self.list_registers = []
        self.current_register = Register("T")
        self.registers = {"A":"0","X":"1","L":"2","CP":"8","SW":"9","B":"3","S":"4","T":"5","F":"6"}
        self.base = "1038H"
        self.m_register = []
    
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
    
    def make_register_m(self,obj_list,cp_list):
        r = Register("M")
        it = 0 
        while it < len(self.m_register):
            index = self.m_register[it]
            register = r.make_M(obj_list[index-1],cp_list[index-1])
            self.list_registers.append(register)
            it += 1
    
    
    def directive_word(self,value):
        c = Convert()
        if not c.is_hexadecimal(value):
            value = int(float(value))
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
        
    ## regresa una cadena de bytes que genera una operacion de tipo 2 
    # con 2 parametros que son registros 
    # @param operator instruccion la cual se generara la cadena de bytes
    # @param r1 primer registro del parametro
    # @param r2 segundo registro del parametro
    # @return cadena de bytes que representa el codigo objeto de la operacion
    def operations_type_2(self,operator,r1,r2):
        operation_code = self.operations[operator]
        r1 = self.registers.get(r1,"")
        r2 = self.registers.get(r2,"0")
        obj_code = operation_code + r1 + r2
        return obj_code
        
    ## regresa una cadena de bytes que genera una operacion de tipo 2 
    # con un numero del 1 - 16 como parametro
    # @param operator instruccion la cual se generara la cadena de bytes
    # @param r1 primer registro del parametro en formato de caracter 
    # @param r2 segundo registro del parametro en formato de caracter
    # @return cadena de bytes que representa el codigo objeto de la operacion
    def operations_type2_n(self,operator,n1):
        operation_code = self.operations[operator]
        c = Convert()
        n1 = c.decimal_to_hexadecimal(n1)
        n1 = n1[:-1]
        del c
        return operation_code + str(n1) + "0"
        
    ## regresa una cadena de bytes que genera una operacion de tipo 2 
    # con 2 parametros que son un registro y un numero 
    # @param operator instruccion la cual se generara la cadena de bytes
    # @param r el reistro al que se le aplicara la operacion
    # @param n segundo numero entre 1 y 16
    # @return cadena de bytes que representa el codigo objeto de la operacion
    def operations_type_2_rn(self,operator,r,n):
        operation_code = self.operations[operator]
        r = self.registers.get(r,"")
        c = Convert()
        n = c.decimal_to_hexadecimal(n)
        n = n[:-1]
        del c
        obj_code = operation_code + r + str(n)
        return obj_code
        
#==============================================================================
#               TYPE 3 & 4
#==============================================================================
    ## Regresa los 6 bits mas significativos de un numero 
    # metodo usado para recuperar el valor del codigo de operacion
    # @param operator instruccion de tipo cadena la cual sera convertida a binario
    # @return cadena de bits que representan el codigo de operacion
    def get_binary_code(self,operator):
        code = self.operations[operator]
        c = Convert()
        dec_code = c.to_decimal(code+"H")
        binary = c.decimal_to_binary(int(dec_code),8)
        binary = binary[0:-2]
        del c
        return binary
        
    ##checa si es una numero menor a 4096 
    #@param desp constante numerica en formato hexadecimal
    #@return regresa True si la constante es menor a (4096)dec
    def is_type_c(self,desp):
        c = Convert()
        desp = c.to_decimal(desp)
        del c
        if desp < 4096:
            return True
        return False
    
    def get_flags(self,type):
        flags = {'n':0,'i':0,'x':0,'b':0,'p':0,'e':0}
        n = 1
        i = 1
        if type == "Indirecto":
            n=1
            i=0
        elif type == "Inmediato":
            n = 0
            i = 1
        flags['n'] = n
        flags['i'] = i 
        return flags
    
    
    def is_relative_cp(self,cp,arg):
        hex = Hexadecimal()
        c = Convert()        
        res = hex.subs(arg,cp)
        res = c.to_decimal(res)
        if res <= 2047 and res >= -2048:
            return c.decimal_to_hexadecimal(res)
        else: 
            return None
        
    def relative_base(self,arg):
        hex = Hexadecimal()
        c = Convert()        
        res = hex.subs(arg,self.base)
        res_dec = c.to_decimal(res)
        if res_dec >= 0 and res_dec <= 4095:
            return res
        del c
        del hex
        return None
    
    def operation_type_3_4(self,cp,operator,arg,format_type,num_line,dir_type,type_c,is_index,valid_label):
        c = Convert()
        operator = self.get_binary_code(operator)
        flags = self.get_flags(dir_type)
        num_max = 3
        res = arg
        entra = True
        if format_type == 4:
            flags['e']=1
            num_max=5
            if not type_c:
                self.m_register.append(num_line)
            res = self.current_register.adjust_bytes(arg,num_max)
        else:
            if type_c:
                if not self.is_type_c(arg):
                    entra = True
                else:
                    entra = False
                    if not c.is_hexadecimal(arg):
                        arg = c.decimal_to_hexadecimal(arg)
                    res = self.current_register.adjust_bytes(arg,3)
            if entra:
                res = self.is_relative_cp(cp,arg)
                if not res:
                    res = self.relative_base(arg)
                    if res:
                        flags['b'] = 1
                    else:
                        res = arg
                        valid_label = False
                else:
                    flags['p'] = 1
                res = self.current_register.adjust_bytes(res,num_max)
        if is_index:
            flags['x'] = 1
        if not valid_label:
            flags['b'] = 1
            flags['p'] = 1
        flags = self.flags_string(flags)
        val = operator + flags
        val = str(int(val,2))
        val = c.decimal_to_hexadecimal(val)
        val = self.current_register.adjust_bytes(val,3)
        val += str(res)
        del c
        return val
        
    def flags_string(self,dicc):
        string = ""
        string += str(dicc['n'])+str(dicc['i'])
        string += str(dicc['x'])+str(dicc['b'])
        string += str(dicc['p'])+str(dicc['e'])
        return string

        
#st = Step2()
#st.operation_type_indirecto("0004H","LDT","103BH",3,2)
#print st.m_register

                
            
        
        
