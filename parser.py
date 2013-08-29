#encoding: utf-8
# Archivo: parser.py
# Autor: Juan Manuel Hernandez Liñan
# Fecha: 19 de Agosto del 2013
# Descripción: Practica 1 Analizador lexico y sintactico del ensamblador SIC estandar
# Modolu donde se definen las reglas gramaticales de 
# el lenguaje sic estandar y se manejan los errores sintacticos
from scanner import tokens
from scanner import scann
import ply.yacc as yacc
import scanner

errors = []
list_line_errors = []

def get_lexic_errors():
  return scann.errors

def get_sintactic_errors():
  return errors 

#  definicion de las reglas gramaticas con operaciones de dos operandos

# regla inicial la cual empareja la instruccion de start
# y despues el conjunto de directivas o intrucciones y por ultimo
# el END
def p_inicial(p):
  '''
    INI : DS C DE
  '''
  pass 

#regla de la directiva start
#checa si la direccion es hexadecimal y es diferente de 0
def p_directiva_start(p):
  '''
    DS : ETIQUETA START HEX
  '''
  s = p[3]
  if compare_string_number(s):
    errors.append("\nEn la linea 1: \n\tLa direccion inicial debe ser mayor a cero\n")


#metodo que compara si una cadena (hexadecimal) es igual a 0
def compare_string_number(s):
  string_len=len(s[0:-1])
  compare = ""
  iterator = 0
  while iterator < string_len:
    compare+="0"
    iterator += 1
  return  compare == s[0:-1]


def p_directiva_end(p):
  '''
    DE : END ETIQUETA
    | END
  '''
  pass 

def p_codigo(p):
  '''
  C : DC C 
  | CP C
  | EPSILON
  '''
  pass 

def p_epsilon(p):
  ' EPSILON : ' 
  pass 

def p_codigo_Directivas(p):
  '''
  DC : DBYTE 
  | DIRECTIVA
  '''
  pass 

def p_directiva_byte(p):
  '''
    DBYTE : ETIQUETA BYTE BVALOR
    | BYTE BVALOR
  '''
  pass 

def p_byte_valor(p):
  '''
  BVALOR : CVALOR
  | XVALOR
  '''
  pass

def p_byte_valor_error(p):
  'BVALOR : error'
  errors.append("\nEn la linea:"+str(p.lineno(1))+"\n\t Al definir la constante en la directiva Byte")

def p_directivas(p):
  '''
  DIRECTIVA : ETIQUETA NEMDIRECTIVA
  | NEMDIRECTIVA
  '''
  pass

def p_nemonico_directivas(p):
  '''
   NEMDIRECTIVA : NEMONICO HEX
  | NEMONICO DECIMAL
  '''
  pass

def p_nemonico_directivas_error(p):
  '''NEMDIRECTIVA : NEMONICO error '''
  errors.append("\nEn la linea:"+str(p.lineno(2))+"\n\t Se esperaba un numero decimal o hexadecimal")
  pass

def p_nemonico(p):
  '''
  NEMONICO : WORD
  | RESB
  | RESW
  '''
  pass

def p_codigo_operacion(p):
  '''CP : ETIQUETA CI
  | CI'''
  pass

def p_instruccion_codigo(p):
  ''' CI : INSTRUCCION ETIQUETA
  | INSTRUCCION ETIQUETA DIR
  | RSUB
  '''
  pass

def p_instruccion(p):
  ''' INSTRUCCION : ADD
  | AND
  | COMP 
  | DIV 
  | J 
  | JEQ 
  | JGT 
  | JLT
  | JSUB 
  | LDA 
  | LDCH 
  | LDL 
  | LDX
  | MUL 
  | OR 
  | RD 
  | TIX 
  | STA
  | STCH 
  | STL 
  | STSW 
  | STX 
  | SUB
  | TD 
  | WD
  '''
  pass

def p_error(t):
  if t:
    line_error = str(t.lexer.lineno)
    if not line_error in list_line_errors:
      token = get_token(t.value)
      error ="\nEn la linea: " + line_error+" cerca de: "+token+"\n"
      errors.append(error)
      list_line_errors.append(line_error)
      yacc.errok()
  else: 
    errors.append("No se encontro contenido en el archivo")
  
  
def get_token(value):
  return value.split("\n")[0]
  
parse = yacc.yacc()

