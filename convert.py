#encoding: utf-8

##
# @file convert.py
# @autor Juan Manuel Hernandez Liñan
# @brief Practica 2 Paso 1 del ensamblador para SIC estandar
# clase para convertir cadenas en numeros o numeros de diferente base 
#a otra especifica 
# @date 29 de Agosto del 2013


import math
class Convert:
    
    ## Constructor de la clase 
    # Aqui se inicializan los diccionarios de las literales hexadecimales 
    # para facilitar su conversion     
    # @param self: apuntador del objeto
    def __init__(self):
        self.hex_caracters = {
            'A' : 10,
            'B' : 11,
            'C' : 12,
            'D' : 13,
            'E' : 14,
            'F' : 15
        }
        self.dec_caracters = {
            10 : 'A',
            11 : 'B',
            12 : 'C',
            13 : 'D',
            14 : 'E',
            15 : 'F'
        }


    ##  Metodo para obtener el valor semantico de un caracter
    # @param self: apuntador del objeto
    # @param value: caracter a checar su valor semantico
    # @param is_hex: bandera que indica si el caracter corresponde a un numero hexadecimal
    # @return valor semantico del caracter o NONE si el caracter no es numerico
    def get_semantic_value_caracter(self,value,is_hex):
        ret = None
        if is_hex:
            ret = self.semantic_value_dec(value)
        else:
            if not value.isdigit():
                ret = None
            else:
                ret = int(value)
        return ret

    ## Convierte una literal de un numero hexadecimal en su valor decimal 
    # @param value: caracter a convertir 
    # @return regresa el valor decimal del caracter y si el caracter no es entre A-F regresa None
    def semantic_value_dec(self,value):
        ret = None
        if not value.isdigit():
            val = self.hex_caracters.get(value.upper(),'none')
            if val == 'none':
                ret = None
            else:
                ret = val
        else:
            ret = int(value)
        return ret
    ## Convierte una cadena str a decimal
    # @param value: cadena a convertir a decimal puede ser en formato hexadecimal
    # @return regresa el valor decimal de la cadena 
    def to_decimal(self,value):
        value_pow = 0
        if value == "error":
            return 0
        if self.is_hexadecimal(value):
            value = value[0:-1]
            value_pow = 16
            return self.string_decimal(value,value_pow)
        else:
            return int(value)
        


    ## Checa si una cadena representa un numero hexadecimal 
    # @param value: cadena a checar
    # @return regresa true si la cadena representa a un hexadecimal 
    def is_hexadecimal(self,value):
        literal = value[-1]
        return literal.upper() == "H"
     
    ## convierte una cadena de diferente base a decimal
    # @param value: numero a convertir
    # @param base: base en la que se encuentra el numero     
    # @return  regresa el valor en decimal 
    def string_decimal(self,value,base):
        is_hex=False
        if base == 16:
            is_hex = True
        len_value = len(value)
        count = 0
        decimal = 0
        while count < len_value:
            pos = len_value - (count + 1)
            real_value = self.get_semantic_value_caracter(value[pos],is_hex)          
            if not real_value == None:
                decimal += (real_value * math.pow(base,count))
                count += 1
            else:
                return -1
        return decimal
    
    ## convierte un numero decimal en binario
    # @param value valor decimal a convertir
    # @param max_num numero de bits en la que se representara el numero
    # @return cadena de 1 y 0 que representa el valor de tamaño max_num    
    def decimal_to_binary(self,value,max_num):
        string = '#0'+str(max_num+2)+'b'
        value = format(value,string)[2:]
        return value
    
    ## desplazamineto a la izquierda en n bits
    # @param numero binareo a desplazar 
    # @param num numero de bits que se desplazara a la izquierda
    # @return regresa el resultado del desplazamiento
    def shift_binary_left(self,binary,num):
        num_max = len(binary)
        val = int(binary,2)
        val = val << num
        val = self.decimal_to_binary(val,num_max)
        return val

    ## desplazamineto a la derecha en n bits
    # @param numero binareo a desplazar 
    # @param num numero de bits que se desplazara a la derecha
    # @return regresa el resultado del desplazamiento        
    def shift_binary_right(self,binary,num):
        num_max = len(binary)
        val = int(binary,2)
        val = val >> num
        val = self.decimal_to_binary(val,num_max)
        return val
    
    ## hace un enmascaramiento con el operador OR 
    # @param binary numero que se le hara la mascara 
    # @param mask mascara que se aplicara
    # @return resultado de la mascara
    def mask_or(self,binary,mask):
        num_max = len(binary)
        val1 = int(binary,2)
        val2 = int(mask,2)
        val = val1 | val2
        return self.decimal_to_binary(val,num_max)

    ## hace un enmascaramiento con el operador OR 
    # @param binary numero que se le hara la mascara 
    # @param mask mascara que se aplicara
    # @return resultado de la mascara        
    def mask_and(self,binary,mask):
        num_max = len(binary)
        val1 = int(binary,2)
        val2 = int(mask,2)
        val = val1 & val2
        return self.decimal_to_binary(val,num_max)
    
    ## convierte un numero decimal a hexadecimal 
    # @param value valor decimal que se convertira
    # @return valor hexadecimal 
    def decimal_to_hexadecimal(self, value):
      if not str(value).replace(".","",1).isdigit():
          vi = 0
          s="0"
      else:
          vi = int(value)
          s = ""
      while vi > 0:
          vf = float(vi)
          vi = vi / 16
          res = str(vf / 16.0).split('.')[1]
          vf = float("."+res)
          ns = str(int(vf*16))
          ns = self.dec_caracters.get(int(ns),ns)
          s = ns + s
      return s+"H"
  
    def list_to_string(self,dicc):
          string = ""
          for l in dicc:
              string += str(dicc[l])
          return string
          
#dic = {'n':1,'i':2}
#print c.list_to_string(dic)

#print c.decimal_to_hexadecimal("0")
#print c.shift_binary_left("000000110011",2)
#print c.shift_binary_right("000000110011",2)
#print c.mask_and("0000000000","0000011111")
#val = c.decimal_to_binary(14,24)
#print val
#val = int(val,2)
#
#val = val << 16
#print val
#val = c.decimal_to_binary(val,24)
#val = int(val,2)
#print val


#val = bin(12)
#print val
#val << 1
#print val