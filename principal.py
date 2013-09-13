#encoding: utf-8
##
# @file principal.py
# @autor Juan Manuel Hernandez Liñan
# @brief Practica 2 Paso 1 del ensamblador para SIC estandar
# modulo principal el cual se ejecuta para analizar un codigo de la SIC estandar 
# @date 29 de Agosto del 2013


import sys
from ensamblador import Ensamblador


def main(): 
    num = len(sys.argv)
    e = Ensamblador()
    if(num > 1):
        num_file = 1
        while num_file < num:
            file_name = sys.argv[num_file]
            e.ensambla(file_name)
            num_file += 1
    else:
        print "Debes indicar el nombre del archivo"

if __name__ == "__main__":
    main()