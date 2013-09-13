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
  	'SUB', 'TD',  'WD','RSUB','ADD'
)

## declaracion de los tokens
tokens = keyword + (
			'ETIQUETA','DECIMAL',
			'DIR','HEX','CVALOR','XVALOR'
		)


## metodo que empareja las constantes para la directiva byte de tipo cadena
# que tienen la forma C'VALOR'
# @param t instancia del token de leX
# @return instancia del token que emparejo
def t_CVALOR(t):
	r'C\'[a-zA-Z][a-zA-Z_]*\''
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
##metodo para emparejar numeros decimales 
# @param t instancia del token de leX
# @return instancia del token que emparejo
def t_DECIMAL(t):
	r'[0-9]+'
	return t

##metodo para aumentar la linea de codigo cuando se encuentra un salto de linea
# @param t instancia del token de leX
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
##metodo que analiza las etiquetas y checa si no son palabras reservadas
# @param t instancia del token de leX
# @return instancia del token que emparejo o de la palabra reservada 
def t_ETIQUETA(t):
	r'[A-Z][A-Z_0-9]*'
	if t.value in keyword:
		t.type = t.value
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


