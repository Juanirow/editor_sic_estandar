#encoding: utf-8
##
# @file my_file.py
# @autor Juan Manuel Hernandez Liñan
# @brief Practica 2 Paso 1 del ensamblador para SIC estandar
# clase para manejar los archivos y checar las extensiones de estos 
# @date 29 de Agosto del 2013

class File:

    ## Constructor de la clase donde se definen sus variables 
    # la variable que almacenara el nombre y la otra el archivo en si 
    def __init__(self):
        self.name = ""
        self.file = ""

    ## metodo para abrir un archivo el cual checa si la 
    #extension es .s 
    # @param file_name nombre del archivo a abrir
    # @return regresa True si el archivo se pudo abrir 
    def open(self,file_name):
        if self.get_file_name(file_name):
            self.file = open(file_name)
            return True
        else:
            print "No se pudo abrir el archivo no es una archivo .s"
        return False

    ## crea un archivo de escritura 
    # @param name nombre del archivo de salida
    # @param extension extension de salida del archivo
    def create_file(self,name,extension):
        self.name = name
        file_name = name+"."+extension
        print "Creando archivo "+file_name+"..."
        self.file = open(file_name,"w")


    
    ## regresa el contenido completo del archivo
    # @return regresa el contenido de el archivo
    def read(self):
        return self.file.read()

    ## escribe en el archivo lo que contenga la variable string
    # @param string cadena la cual se escribira en el archivo 
    def write(self,string):
        self.file.write(string)
      
    ## escribe el contenido de una lista de strings en un archivo 
    # @param list_string lista de cadenas 
    def write_list(self,list_string):
        for x in list_string:
            self.file.write(x+"\n")

    ## cierra el archivo
    def close(self):
        self.file.close()

    ## separa la cadena para obtener su extension y el nombre del archivo
    # regresa un True si la extension es s para la SIC 
    # @param string nombre del archivo con ruta 
    # @return True si el archivo es de extension correcta 
    def get_file_name(self,string):
        list_names =  string.split('.')
        if self.is_extension_valid(list_names,'s'):
            self.extension = list_names[-1]
            name_part = list_names[-2]
            list_names = name_part.split('/')
            self.name = list_names[-1]
            return True
        return False

    ##checa si la lista de cadenas el tiene mas de dos elementos
    #y si el ultimo elemento es de s
    # @param list lista de las cadenas que conforma el nombre del archivo
    # @return True si la extension es valida    
    def is_extension_valid(self,list,extension):
        ret = False
        if list.count >= 2:
            if list[-1] == extension:
                ret = True
        return ret
    
    ## regresa el contenido del archivo por lineas en una lista 
    # @return lista de cadenas que contiene el archivo 
    def get_lines(self):
        list_lines = []       
        for line in self.file:
            list_lines.append(line)
        return list_lines
