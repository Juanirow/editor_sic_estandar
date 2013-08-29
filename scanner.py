#encoding: utf-8
# Archivo: scanner.py
# Autor: Juan Manuel Hernandez Liñan
# Fecha: 20 de Agosto del 2013
# Descripción: Practica 1  Analizador lexico y sintactico del ensamblador SIC estandar
# 				En este modulo se encuentra el analizador lexico y la definicion de los tokens


import ply.lex as lex
#declaracion de los tokens
keyword = (
	'START','END','BYTE','WORD','RESB','RESW',
	'AND','COMP','DIV','J','JEQ','JGT', 
  	'JLT','JSUB', 'LDA',  'LDCH',  'LDL',
  	'LDX', 'MUL',  'OR',  'RD',  'TIX',
  	'STA', 'STCH',  'STL',  'STSW',  'STX',
  	'SUB', 'TD',  'WD','RSUB','ADD'
)

tokens = keyword + (
			'ETIQUETA','DECIMAL',
			'DIR','HEX','CVALOR','XVALOR'
		)



def t_CVALOR(t):
	r'C\'[a-zA-Z][a-zA-Z_]*\''
	return t

def t_XVALOR(t):
	r'X\'[0-9a-fA-F]+\''
	return t

def t_HEX(t):
	r'[0-9a-fA-F]+[hH]'
	return t

def t_DIR(t):
	r'\,[\t ]*X'
	return t

def t_DECIMAL(t):
	r'[0-9]+'
	return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_ETIQUETA(t):
	r'[A-Z][A-Z_0-9]*'
	if t.value in keyword:
		t.type = t.value
	return t

t_ignore = ' \t'


#muestra un mensaje de error cuando un token no es valido
def t_error(valor):
	line_num = str(valor.lineno)
	token_error = str(valor.value[0])
	if not line_num in scann.list_error_line:
		def_error = "En la linea:"+line_num+" \n\ttoken desconocido: \" "+token_error+" \" "
		scann.errors.append(def_error)
		scann.list_error_line.append(line_num)
	valor.lexer.skip(1)
	return valor

scann = lex.lex()
scann.errors = []
scann.list_error_line = []


def entrada(texto):
	scann = lex.lex()
	scann.input(texto)
	tok = lex.token()
	print str(tok)
	while 1:
	    tok = lex.token()
	    if not tok: break
	    print tok





