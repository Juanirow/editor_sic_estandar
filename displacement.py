# -*- coding: utf-8 -*-
##
# @file displacement.py
# @autor Juan Manuel Hernandez Liñan
# @brief Practica 2 Paso 1 del ensamblador para SIC estandar
# Calcula los desplazamientos de la directiva BYTE 
# @date 29 de Agosto del 2013

from convert import Convert

## clase para calcular los desplazamientos de la directiva BYTE
class Displacement: 
    
    ## Calcula el desplazamiento dependiendo si el argumento es una constante o hexadecimal 
    # @param value valor del argumento de la directiva BYTE 
    # @return el valor en decimal del desplazamiento 
    def directive_byte(self,value):
        data = self.filter_byte(value)
        if self.is_constant_hexadecimal(value):
            val =  self.displacement_constant_hexadecimal(data)
            return val/2
        else:
            return len(data)
        
        

    ## regresa el contenido de la constante ya sea hexadecimal o cadena
    # @param value argumento en formato X'VALOR' o C'VALOR'
    # @return regresa el contenido VALOR de una constante de 
    def filter_byte(self,value):
        return value.split("'")[1]
        
    ## checa si la constante o argumento es hexadecimal 
    # @param argumento de la directiva BYTE 
    # @return regresa True si la contante a definir es de tipo hexadecimal
    def is_constant_hexadecimal(self,value):
        if value[0] is "X":
            return True
        return False


    ## si la constante es una cadena se calcula el desplazamiento contando el 
    # numero de caracteres de la cadena y si es impar se le suma uno 
    # @param value la cadena constante 
    # @return regresa el tamaño dela cadena y si es impar se le suma uno         
    def displacement_constant_hexadecimal(self,value):
        cant = len(value)
        if cant % 2 == 0:
            return cant
        return cant+1
    
    ## regresa una cadena que representa un texto mas una serie de espacios
    # la cual es del tamaño del parametro tam menos la longitud de la cadena    
    def get_tex_space(self,texto,tam):
        texto = str(texto)
        tam_real = tam - len(texto)
        string = " "
        string = string*tam_real
        string = texto+string
        return string
