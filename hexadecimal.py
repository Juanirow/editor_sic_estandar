#encoding: utf-8
##
# @file parser.py
# @autor Juan Manuel Hernandez Liñan
# @brief Practica 2 Paso 1 del ensamblador para SIC estandar
# Clase para sumar dos numeros hexadecimales 
# @date 29 de Agosto del 2013

from convert import Convert

class Hexadecimal:
    
    ## suma dos numeros hexadecimales
    # @param num1 valor numerico a sumar 
    # @param num2 valor numerico a sumar 
    # @return regresa la suma de dos numeros y si alguno de estos numeros no es 
    # correcto regresa error
    def plus(self,num1,num2):
        convert = Convert()
        num1 = self.change_hexadecimal(num1)
        num2 = self.change_hexadecimal(num2)
        num1 = convert.to_decimal(num1)
        num2 = convert.to_decimal(num2)
        if not num1 == -1 and not num2 ==-1:            
            res = num1+num2
            res = convert.decimal_to_hexadecimal(res)
            return res
        else:
            return "error"
    ## resta dos numeros hexadecimales
    # @param num1 valor numerico a restar 
    # @param num2 valor numerico a restar 
    # @return regresa la resta de dos numeros y si alguno de estos numeros no es 
    # correcto regresa error        
    def subs(self,num1,num2):
        convert = Convert()
        num1 = self.change_hexadecimal(num1)
        num2 = self.change_hexadecimal(num2)
        num1 = convert.to_decimal(num1)
        num2 = convert.to_decimal(num2)          
        res = num1-num2
        if res < 0:
            res = int(res * -1)
            res = res ^ 4095
            res += 1
        if res == 0:
            res = "0H"
        else:
            res = convert.decimal_to_hexadecimal(res)
        return res

    def suma(self,num1,num2):
        convert = Convert()
        print "antes",num1,num2       
        num1 = self.get_int_operator(num1)
        num2 = self.get_int_operator(num2)  
        res = num1+num2     
        print "despues",num1,num2,res
        if res < 0:
            res = int(res * -1)
            res = res ^ 4095
            res += 1
        if res == 0:
            res = "0H"
        else:
            res = convert.decimal_to_hexadecimal(res)
        print "resultado",res
        return res

    def get_int_operator(self,dat):
        convert = Convert()
        if dat[-1] == "H":
            dat = dat[:-1]
        if dat[0] == "F":
            string = ""
            it = 0
            while it < len(dat):
                if not dat[it] == "F":
                    string += dat[it]
                it += 1
            if len(string) == 0:
                return -1
            else:
                val = "1"+("0"*len(string))+"H"
                val = convert.to_decimal(val)
                val2 = convert.to_decimal(string+"H")
                return val2-val
        else:
            return convert.to_decimal(dat+"H")
        
    ## resta dos numeros hexadecimales
    # @param num1 valor numerico a restar 
    # @param num2 valor numerico a restar 
    # @return regresa la resta de dos numeros y si alguno de estos numeros no es 
    # correcto regresa error    
    def subs_minus(self,num1,num2):
        convert = Convert()
        num1 = self.change_hexadecimal(num1)
        num2 = self.change_hexadecimal(num2)
        num1 = convert.to_decimal(num1)
        num2 = convert.to_decimal(num2)          
        res = num1-num2
        sign = "+"
        if res < 0:
            sign = "-"
            res = int(res * -1)
            res = res ^ 4095
            res += 1
        if res == 0:
            res = "0H"
        else:
            res = convert.decimal_to_hexadecimal(res)
        return [res,sign]


    ## checa si una cadena representa un  numero  hexadecimal 
    # @param num cadena que se checa si el ultimo caracter es H 
    # @return regresa el numero con una H al final si es que no la tiene
    def change_hexadecimal(self,num):
        num = str(num)
        if num[-1].upper() == "H":
            return num
        else:
            return num+"H"

    ## compara si un numero es menor a otro
    # @param num1 valor numerico a comparar 
    # @param num2 valor numerico a comparar 
    # @return regresa un booleano
    def minus_than(self,num1,num2):
        convert = Convert()
        num1 = self.change_hexadecimal(num1)
        num2 = self.change_hexadecimal(num2)
        num1 = convert.to_decimal(num1)
        num2 = convert.to_decimal(num2)
        del convert
        return num1<num2

    ## regresa la operacion and entre 2 valores
    # @param num1 valor numerico a comparar 
    # @param num2 valor numerico a comparar 
    # @return regresa un booleano    
    def and_op(self,num1,num2):
        convert = Convert()
        num1 = self.change_hexadecimal(num1)
        num2 = self.change_hexadecimal(num2)
        num1 = convert.to_decimal(num1)
        num2 = convert.to_decimal(num2)
        res = int(num1)&int(num2)
        res = convert.decimal_to_hexadecimal(res)
        del convert
        return res
    
    ## regresa la operacion or entre 2 valores
    # @param num1 valor numerico a comparar 
    # @param num2 valor numerico a comparar 
    # @return regresa un booleano     
    def or_op(self,num1,num2):
        convert = Convert()
        num1 = self.change_hexadecimal(num1)
        num2 = self.change_hexadecimal(num2)
        num1 = convert.to_decimal(num1)
        num2 = convert.to_decimal(num2)
        res = int(num1)|int(num2)
        res = convert.decimal_to_hexadecimal(res)
        del convert
        return res
    
    ## compara dos numeros 
    # @param num1 valor numerico a comparar 
    # @param num2 valor numerico a comparar 
    # @return regresa un booleano     
    def cmp_op(self,num1,num2):
        convert = Convert()
        num1 = self.change_hexadecimal(num1)
        num2 = self.change_hexadecimal(num2)
        num1 = convert.to_decimal(num1)
        num2 = convert.to_decimal(num2)
        ret = "="
        if num1 < num2:
            ret = "<"
        elif num1 > num2:
            ret = ">"
        del convert
        return ret
    ## divide dos numeros hexadecimales
    # @param num1 valor numerico a dividir 
    # @param num2 valor numerico a dividir 
    # @return regresa la divide de dos numeros y si alguno de estos numeros no es 
    # correcto regresa error    
    def div(self,num1,num2):
        convert = Convert()
        num1 = self.change_hexadecimal(num1)
        num2 = self.change_hexadecimal(num2)
        num1 = convert.to_decimal(num1)
        num2 = convert.to_decimal(num2)
        res = int(num1)/int(num2)
        res = convert.decimal_to_hexadecimal(res)
        del convert
        return res
    ## multiplica dos numeros hexadecimales
    # @param num1 valor numerico a multiplicar 
    # @param num2 valor numerico a multiplicar 
    # @return regresa la multiplica de dos numeros y si alguno de estos numeros no es 
    # correcto regresa error   
    def mul(self,num1,num2):
        convert = Convert()
        num1 = self.change_hexadecimal(num1)
        num2 = self.change_hexadecimal(num2)
        num1 = convert.to_decimal(num1)
        num2 = convert.to_decimal(num2)
        res = int(num1)*int(num2)
        res = convert.decimal_to_hexadecimal(res)
        del convert
        return res

    
    
            
#hex = Hexadecimal()
#print hex.plus("0H","23H")