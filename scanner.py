#encoding: utf-8
##
# @file my_file.py
# @autor Juan Manuel Hernandez Liñan
# @brief Practica 2 Paso 1 del ensamblador para SIC estandar
# clase para manejar los archivos y checar las extensiones de estos 
# @date 29 de Agosto del 2013
# Modulo donde se definen los tokens y se genera la lista de tokens 
#de acuerdo a un texto de entrada


import ply.lex as lex
##declaracion de las palabras reservadas
keyword = (
	'START','END','BYTE','WORD','RESB','RESW',
	'AND','COMP','DIV','J','JEQ','JGT', 
  	'JLT','JSUB', 'LDA',  'LDCH',  'LDL',
  	'LDX', 'MUL',  'OR',  'RD',  'TIX',
  	'STA', 'STCH',  'STL',  'STSW',  'STX',
  	'SUB', 'TD',  'WD','RSUB','ADD','ADDF','ADDR',
      'CLEAR','COMPF','COMPR','DIVF','DIVR','FLOAT',
      'BASE','HIO','LDB','LDF','LPS','LDS','LDT','MULF','MULR',
      'NORM','RMO','SHIFTL','SHIFTR','SIO','SSK','STB','STF',
      'STI','STT','STS','SUBF','SUBR','SVC','TIO','TIXR','FIX','EQU','ORG')

## declaracion de los tokens
tokens = keyword + (
			'ETIQUETA','DECIMAL',
			'DIR','HEX','CVALOR','XVALOR','REGISTER','COMMA','PLUS','HASHTAG','AT',
               'MINUS','DIVI','MULTI','PARENO','PARENC','_SALTO',
		)

registers = ('A','X','L','CP','SW','B','S','T','F')


##metodo que empareja con el caracter de asignacion
# @param t instancia del token de leX
# @return instancia del token que emparejo
def t_EQUAL(t):
    r'\='
    return t
    
##metodo que empareja con el caracter de parentesis abierto
# @param t instancia del token de leX
# @return instancia del token que emparejo
def t_PARENC(t):
    r'\)'
    return t
    
    
##metodo que empareja con el caracter de parentesis abierto
# @param t instancia del token de leX
# @return instancia del token que emparejo
def t_PARENO(t):
    r'\('
    return t
    
##metodo que empareja con el caracter de multiplicacion
# @param t instancia del token de leX
# @return instancia del token que emparejo
def t_MULTI(t):
    r'\*'
    return t
    
##metodo que empareja con el caracter de divicion
# @param t instancia del token de leX
# @return instancia del token que emparejo
def t_DIVI(t):
    r'\/'
    return t
    
##metodo que empareja con el caracter de resta
# @param t instancia del token de leX
# @return instancia del token que emparejo
def t_MINUS(t):
    r'\-'
    return t
    
##metodo que empareja con el caracter de suma
# @param t instancia del token de leX
# @return instancia del token que emparejo
def t_PLUS(t):
    r'\+'
    return t
    
##metodo que empareja con el caracter de "#"
# @param t instancia del token de leX
# @return instancia del token que emparejo
def t_HASHTAG(t):
    r'\#'
    return t

##metodo que empareja con el caracter de "@"
# @param t instancia del token de leX
# @return instancia del token que emparejo
def t_AT(t):
    r'@'
    return t

## metodo que empareja las constantes para la directiva byte de tipo cadena
# que tienen la forma C'VALOR'
# @param t instancia del token de leX
# @return instancia del token que emparejo
def t_CVALOR(t):
	r'C\'[a-zA-Z][a-zA-Z_ ]*\''
	return t
## metodo que empareja las constantes para la directiva BYTE de tipo hexadecimal 
# que tienen la forma X'VALOR'
# @param t instancia del token de leX
# @return instancia del token que emparejo
def t_XVALOR(t):
	r'X\'[0-9a-fA-F]+\''
	return t
## metodo para emparejar numeros hexadecimales las cules pueden llevar letras 
# de la A-F y con una H al final 
# @param t instancia del token de leX
# @return instancia del token que emparejo
def t_HEX(t):
	r'[0-9a-fA-F]+[hH]'
	return t
##metodo que empareja el direccionamiento indexado para los codigos de operacion
# el cual tiene un formato , X
# @param t instancia del token de leX
# @return instancia del token que emparejo
def t_DIR(t):
	r'\,[\t ]*X'
	return t
##metodo que empareja con la coma
# @param t instancia del token de leX
# @return instancia del token que emparejo 
def t_COMMA(t):
    r'\,'
    return t

    
##metodo para emparejar numeros decimales 
# @param t instancia del token de leX
# @return instancia del token que emparejo
def t_DECIMAL(t):
	r'[0-9]+'
	return t

##metodo para aumentar la linea de codigo cuando se encuentra un salto de linea
# @param t instancia del token de leX
def t__SALTO(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t
    
##metodo que analiza las etiquetas y checa si no son palabras reservadas
# @param t instancia del token de leX
# @return instancia del token que emparejo o de la palabra reservada 
def t_ETIQUETA(t):
    r'[A-Z][A-Z_0-9]*'
    if t.value in keyword:
        t.type = t.value
    if t.value in registers:
        t.type = "REGISTER"
    return t
    
## caracteres de espacio y tabulador ignorados
t_ignore = ' \t'


##muestra un mensaje de error cuando un token no es valido
# y lo guarda en el diccionario de errores lexicos
# @param valor instancia del token que genero el error
# @return instancia del token que genero el error
def t_error(valor):
	line_num = str(valor.lineno)
	token_error = str(valor.value[0])
	if not line_num in scann.errors:
		def_error = "token desconocido: \" "+token_error+" \" "
		scann.errors[line_num] = def_error
	valor.lexer.skip(1)
	return valor

scann = lex.lex()
scann.errors = {}
##imprime en terminal la lista de token que produce al analizar una cadena
#@texto texto a analizar 
def entrada(texto):
	scann.input(texto)
	while 1:
	    tok = lex.token()
	    if not tok: break
	    print tok


