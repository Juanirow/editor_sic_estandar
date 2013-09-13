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
            
    def subs(self,num1,num2):
        convert = Convert()
        num1 = self.change_hexadecimal(num1)
        num2 = self.change_hexadecimal(num2)
        num1 = convert.to_decimal(num1)
        num2 = convert.to_decimal(num2)
        if not num1 == -1 and not num2 ==-1:            
            res = num1-num2
            if res == 0:
                res = "0H"
            else:
                res = convert.decimal_to_hexadecimal(res)
            return res
        else:
            return "error"

    ## checa si una cadena representa un  numero  hexadecimal 
    # @param num cadena que se checa si el ultimo caracter es H 
    # @return regresa el numero con una H al final si es que no la tiene
    def change_hexadecimal(self,num):
        num = str(num)
        if num[-1].upper() == "H":
            return num
        else:
            return num+"H"
            
#hex = Hexadecimal()
#print hex.plus("0H","23H")