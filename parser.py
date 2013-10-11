#encoding: utf-8
##
# @file my_file.py
# @autor Juan Manuel Hernandez LiÃ±an
# @brief Practica 2 Paso 1 del ensamblador para SIC estandar
# clase para manejar los archivos y checar las extensiones de estos 
# @date 29 de Agosto del 2013
# Modolu donde se definen las reglas gramaticales de 
# el lenguaje sic estandar y se manejan los errores sintacticos
from scanner import tokens
from scanner import scann
import ply.yacc as yacc
from convert import Convert
from displacement import Displacement
from hexadecimal import Hexadecimal
from step2 import Step2
from register import Register

hex = Hexadecimal()
conv = Convert()
disp = Displacement()
step2 = Step2()
reg = Register("R")

errors = {}
warnings = {}
dir_init = ""
pc = []
obj_code=[]
symbols = {}

extencion =""
base = 0

registers = {"A":0,"X":1,"L":2,"CP":8,"SW":9,"B":3,"S":4,"T":5,"F":6}
## regresa el codigo objeto de cada linea
# @return lista de cadenas de bytes que representan el codigo objeto de cada
#instruccion
def get_obj_code():
    return obj_code

## regresa los registros del archivo objeto
#@return lista de cadenas que representan los registros de el archivo fuente
def get_registers():
    return step2.list_registers

##inserta una etiqueta a la tabla de simbolos y si esta ya se encuentra marca un error
#@param value simbolo que se intentara insertar a la tabla
#@param lineno numero de linea donde se encontro la etiqueta
def insert_symbol(value,lineno):
    if value in symbols:
        insert_error(lineno,"etiqueta previamente definida")
    else:
        symbols[value] = pc[-1]
        
## calcula el tamaÃ±o del programa 
#@return regresa en hexadecimal el tamaÃ±o del programa
def get_len_program():
    num1 = conv.to_decimal(parse.inicial)
    num2 = conv.to_decimal(pc[-1])
    res = num2 - num1
    return conv.decimal_to_hexadecimal(res)

## obtiene el numero de errores lexicos y sintacticos obtenidos
# @return regresa la suma de los errores lexicos y sintacticos
def num_errors():
    e1 = len(scann.errors)
    e2 = len(errors)
 
    return e1+e2
    
##regresa los errores obtenidos en la parte lexica
#@return errores lexicos en un diccionario    
def get_lexic_errors():
  return scann.errors

##regresa los errores obtenidos en la parte sintactica
#@return errores sintacticos en un diccionario  
def get_sintactic_errors():
    return errors 

##regresa el siguiente token de una cadena separada por '
#@return siguiente token a analizar
def get_token(value):
  return value.split("\n")[0]

##checa si en el diccionario de errores ya se inserto un error en esa linea de codigo
#y si no es asi la inserta 
#@param line linea de codigo donde se encontro un error
#@param text cadena que se genera en el error
def insert_error(line,text):
  if not line in errors:
    errors[line]= text
    
##checa si en el diccionario de advertencias ya se inserto un error en esa linea de codigo
#y si no es asi la inserta 
#@param line linea de codigo donde se encontro un warnind
#@param text cadena que se genera en el warning
def insert_warning(line,text):
  if not line in errors:
    warnings[line]= text

##aumenta el contador de programa 
#@param increment cantidad en hexadecimal que se le agregara al CP
def increment_PC(increment):
    num1 = pc[-1]
    if not conv.is_hexadecimal(str(increment)):
        increment = conv.decimal_to_hexadecimal(increment)
    val = hex.plus(num1,increment)
    val = reg.adjust_bytes(val,6)
    pc.append(val+"H")

#==============================================================================
#                       Reglas Gramaticales
#==============================================================================

## regla inicial la cual consta de la directiva start un conjunto de instrucciones y 
# la directiva end
#@param p arreglo mapeado con los simbolos gramaticales de la regla
def p_inicial(p):
  '''
    INI : DS C DE
  '''
  pass 

## regla de la directiva start
# checa si la direccion es hexadecimal y es diferente de 0
#@param p arreglo mapeado con los simbolos gramaticales de la regla
def p_directiva_start(p):
    '''
    DS : ETIQUETA START HEX
    | ETIQUETA START DECIMAL
    '''
    if parse.pasada == 1:
        s = p[3]
        if conv.is_hexadecimal(s):
            val = p[3]
        elif s == "0":
            val = "000000H"
        else:
            val = conv.decimal_to_hexadecimal(s)
        parse.inicial = val
        pc.append(parse.inicial)
        pc.append(parse.inicial)
    else:
        length = get_len_program()
        step2.directive_start(p[1],length,p[3])
        obj_code.append("")   


## metodo que compara si una cadena (hexadecimal) es igual a 0
#@param s cadena la cual es un numero diferente de 0
def compare_string_number(s):
  string_len=len(s[0:-1])
  compare = ""
  iterator = 0
  while iterator < string_len:
    compare+="0"
    iterator += 1
  return  compare == s[0:-1]

##directiva de cierre de programa la cual puede o no llevar una etiqueta al final
#@param p arreglo mapeado con los simbolos gramaticales de la regla
def p_directiva_end(p):
  '''
    DE : END ETIQUETA
    | END
  '''
  if parse.pasada == 2:
      dir = ""
      step2.complete_register()
      step2.make_register_m(obj_code,pc)
      if len(p) == 3:
          dir = p[2]
          dir = symbols[dir]
      step2.directive_end(dir,pc[0])
      obj_code.append("")
  pass 

## conjunto de instrucciones las cuales pueden ser directivas o codigos de operacion
# @brief se usa para encadenar instrucciones
#@param p arreglo mapeado con los simbolos gramaticales de la regla
def p_codigo(p):
  '''
  C : DC C 
  | CP C
  | EPSILON
  '''
  pass 

## regla de epsilon que produce a vacio
#@param p arreglo mapeado con los simbolos gramaticales de la regla
def p_epsilon(p):
  ' EPSILON : ' 
  pass 

##  regla para las directivas que se divide en dos partes la directiva 
# BYTE y el resto
#@param p arreglo mapeado con los simbolos gramaticales de la regla 
def p_codigo_Directivas(p):
  '''
  DC : DBYTE 
  | DIRECTIVA
  '''
  pass 

## directiva BYTE la cual puede tener o no una etiqueta antes de definirla y la 
# cual lleva una constante como argumento ya sea de cadena o hexadecimal
#aqui se almacena la etiqueta en la tabla de simbolos y se incrementa el PC
#@param p arreglo mapeado con los simbolos gramaticales de la regla
def p_directiva_byte(p):
  '''
    DBYTE : ETIQUETA BYTE BVALOR
    | BYTE BVALOR
  '''
  symb=""
  if p[2] == "BYTE":
      num = p[3]
      symb = p[1]
  else: 
      num = p[2]
  if parse.pasada == 1:
      if not symb == "":
          insert_symbol(p[1],p.lineno(1))
      increment_PC(num)
  else:
      str = step2.const_BYTE(num)
      step2.insert_str(str,pc[p.lineno(1)-1])
      obj_code.append(str)
  pass 

## regla de las constantes para la directiva BYTE 
# el cual calcula el desplazamiento de la constante y la devuelve por medio 
#del arreglo p 
#@param p arreglo mapeado con los simbolos gramaticales de la regla
def p_byte_valor(p):
  '''
  BVALOR : CVALOR
  | XVALOR
  '''
  if parse.pasada == 1:
      val = disp.directive_byte(p[1])
      p[0]= conv.decimal_to_hexadecimal(val)
  else:
      p[0] = p[1]
  pass

##regla que captura el error en las constantes de la directiva byte 
#@param p arreglo mapeado con los simbolos gramaticales de la regla
def p_byte_valor_error(p):
  'BVALOR : error'
  insert_error(str(p.lineno(1)),"Al definir la constante en la directiva Byte")
  p[0] ="1"

## regla para las directivas las cuales pueden llevar una etiqueta 
#aqui se almacena la etiqueta en la tabla de simbolos y se incrementa el PC
#@param p arreglo mapeado con los simbolos gramaticales de la regla
def p_directivas(p):
  '''
  DIRECTIVA : ETIQUETA NEMDIRECTIVA
  | NEMDIRECTIVA
  '''
  if parse.pasada == 1:
      if len(p) == 3:
          insert_symbol(p[1],p.lineno(1))
          inc = p[2]
      else:
          inc = p[1]
      increment_PC(inc) 
  pass

def p_directiva_base(p):
  '''
  DIRECTIVA : ETIQUETA DIR_BASE
  | DIR_BASE
  '''
  if parse.pasada == 1:
      if len(p) == 3:
          insert_symbol(p[1],p.lineno(1))
      increment_PC(0)
  pass

def p_directiva_base_valor(p):
    '''DIR_BASE : BASE ETIQUETA'''
    if parse.pasada == 2:
        label = p[2]
        if not label in symbols:
            symbols[label] = "7FFFH"
            insert_warning(str(p.lineno(2)),"No existe la etiqueta "+label)
        m = symbols[p[2]]
        obj_code.append("")
        step2.base = m
    pass

def p_directiva_base_valor_etiqueta(p):
    '''DIR_BASE : BASE HEX
                | BASE DECIMAL'''
    if parse.pasada == 2:
        obj_code.append("")
        decimal = conv.to_decimal(p[2])
        step2.base = conv.decimal_to_hexadecimal(decimal)
    pass

##  checa si las directivas para reservar memoria e incrementa el contador de 
# programa regresa el incremento o la cantidad de bytes reservados por la directivas
#@param p arreglo mapeado con los simbolos gramaticales de la regla
def p_nemonico_directivas_hex(p):
  '''
   NEMDIRECTIVA : NEMONICO HEX
  | NEMONICO DECIMAL
  '''
  val = conv.to_decimal(p[2])
  if parse.pasada == 1:
      inc = 3
      if p[1] == "RESW":
          inc = val * 3
      elif p[1] == "RESB":
          inc = val    
      p[0]=inc
  else:
      if p[1] == "WORD":
          val = step2.directive_word(str(val))
          obj_code.append(val)
          step2.insert_str(val,pc[p.lineno(2)-1])
      else:
          step2.complete_register()
          obj_code.append("")
  pass

## regresa un error si el valor para reservar esta mal declarado
#@param p arreglo mapeado con los simbolos gramaticales de la regla
def p_nemonico_directivas_error(p):
  '''NEMDIRECTIVA : NEMONICO error '''
  insert_error(str(p.lineno(2)),"Se esperaba un numero decimal o hexadecimal")
  p[0] = "error"
  pass

## tipo de directivas para reservar memoria 
#@param p arreglo mapeado con los simbolos gramaticales de la regla
def p_nemonico(p):
  '''
  NEMONICO : WORD
  | RESB
  | RESW
  '''
  p[0] = p[1]
  pass

## si el codigo de operacion lleva una etiqueta la agrega a la 
#    tabla de sinbolos e incrementa el contador de programa 
#@param p arreglo mapeado con los simbolos gramaticales de la regla
def p_codigo_operacion(p):
  '''CP : ETIQUETA CI
  | CI'''
  if parse.pasada == 1:
      if len(p)==3:
          insert_symbol(p[1],p.lineno(1))
          val = p[2]
      else:
          val = p[1]
      val = conv.to_decimal(str(val))
      increment_PC(val)
  else:
      list = p[1]
      if len(p) == 3:
          list = p[2]
      step2.insert_str(list[0],list[1])
      obj_code.append(list[0])
  pass

## conjunot de instrucciones que produce instruccones de 1 ,2 ,3 y 4 bytes 
# @param o arreglo mapeado con los simbolos gramaticales de la regla 
def p_instrucciones(p):
    '''CI : INS_1
        | INS_2
        | INS_3
        | INS_4'''
    p[0]=p[1]
    pass

## instrucciones que produce codigo de  de 1 byte 
# @param o arreglo mapeado con los simbolos gramaticales de la regla 
def p_instrucciones_1(p):
    '''INS_1 : FIX
             | FLOAT
             | HIO
             | NORM
             | SIO
             | TIO '''
    if parse.pasada == 1:
        if extencion == "s":
            insert_error(str(p.lineno(1)),"instruccion solo valida para la arquitectura XE")
        p[0]=1
    else:
        operation = p[1]
        code = step2.operations[operation]
        line = pc[p.lineno(1)-1] 
        p[0] = [code,line]
    pass

## instrucciones que produce codigo de 2 bytes 
# @param o arreglo mapeado con los simbolos gramaticales de la regla 
def p_intrucciones_2(p):
    '''INS_2 : INS_2_R
             | INS_2_N
             | INS_2_RR
             | INS_2_RN'''
    p[0]=2
    if parse.pasada == 2:
        p[0]=p[1]
    pass


## instrucciones de tipo 2 que tienen como parametro un registro  
# @param o arreglo mapeado con los simbolos gramaticales de la regla  
def p_inst_r(p):
    '''INS_2_R : TIXR REGISTER
               | CLEAR REGISTER'''
    if parse.pasada == 1:
        if extencion == "s":
            insert_error(str(p.lineno(1)),"instruccion solo valida para la arquitectura XE")
    else:
        p[0] = [step2.operations_type_2(p[1],p[2],""),pc[p.lineno(1)-1]]
    pass

## instrucciones de tipo 2 que tienen como parametro un numero entre 1 y 16
# @param o arreglo mapeado con los simbolos gramaticales de la regla  
def p_inst_n(p):
    ''' INS_2_N : SVC NUMBER'''
    if parse.pasada == 1:
        if extencion == "s":
            insert_error(str(p.lineno(1)),"instruccion solo valida para la arquitectura XE")
    else:
        p[0] = [step2.operations_type2_n(p[1],p[2]),pc[p.lineno(1)-1]]
    pass

## numero que se encuentra entre el 1 y 16
# @param o arreglo mapeado con los simbolos gramaticales de la regla  
def p_number(p):
    '''NUMBER : DECIMAL'''
    if parse.pasada == 1:    
        val = int(p[1])
        if not (val < 17 and val > 0):
            insert_error(str(p.lineno(1)),"El numero debe ser ente 1 y 16")
    else:
        p[0] = p[1]
    pass

## regla que empareja las instrucciones de tipo 2 
#que tiene como argumentos dos registros 
# @param o arreglo mapeado con los simbolos gramaticales de la regla 
def p_inst_2_reg_reg(p):
    '''INS_2_RR : ARG_RR REGISTER COMMA REGISTER
    | ARG_RR REGISTER DIR'''
    if parse.pasada == 2:
        if len(p)== 5:    
            p[0] = [step2.operations_type_2(p[1],p[2],p[4]),pc[p.lineno(2)-1]]
        else:
            p[0] = [step2.operations_type_2(p[1],p[2],"X"),pc[p.lineno(2)-1]]
    pass

## instrucciones de tipo 2 que tiene como argumentos dos registros 
# @param o arreglo mapeado con los simbolos gramaticales de la regla 
def p_op_arg_rr(p):
    ''' ARG_RR : SUBR
               | RMO
               | MULR
               | DIVR
               | COMPR
               | ADDR'''
    if parse.pasada == 1:
        if extencion == "s":
            insert_error(str(p.lineno(1)),"instruccion solo valida para la arquitectura XE")
    else:
        p[0] = p[1]
    pass

## regla que empareja las instrucciones de tipo 2 
#que tiene como argumentos un registro y un numero  
# @param o arreglo mapeado con los simbolos gramaticales de la regla 
def p_inst_2_reg_num(p):
    ''' INS_2_RN : ARG_R_N REGISTER COMMA NUMBER'''
    if parse.pasada == 2:
        p[0] = [step2.operations_type_2_rn(p[1],p[2],p[4]),pc[p.lineno(2)-1]]
    pass

## instrucciones de tipo 2 que tiene como argumentos un registro y un numero 
# @param o arreglo mapeado con los simbolos gramaticales de la regla
def p_op_arg_rn(p):
    '''ARG_R_N : SHIFTL
                | SHIFTR'''
    if parse.pasada == 1:
        if extencion == "s":
            insert_error(str(p.lineno(1)),"instruccion solo valida para la arquitectura XE")
    else:
        p[0]=p[1]
    pass

##regla que empareja las instrucciones de formato simple del tipo 3
#@param p arreglo mapeado con los simbolos gramaticales de la regla 
def p_instruction_3_simple(p):
    '''INS_3 : SIMPLE'''
    if parse.pasada == 1:
        p[0]=3
    else:
        if extencion == "s":
            p[0] = p[1]
        else:
            l = p[1]
            code = step2.operation_type_3_4(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[9])
            p[0]=[code,l[8]]
    pass

## regla que empareja las instrucciones de tipo 3   
# @param o arreglo mapeado con los simbolos gramaticales de la regla 
def p_instruction_3(p):
    '''INS_3  : INDIRECTO
              | INMEDIATO'''
    p[0] = 3
    if parse.pasada == 1:
        if extencion == "s":
            insert_error(str(p.lineno(1)),"instruccion solo valida para la arquitectura XE")
    else:
        l = p[1]
        code = step2.operation_type_3_4(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[9])
        p[0]=[code,l[8]]
    pass

## regla que empareja las instrucciones de tipo 4 
# @param o arreglo mapeado con los simbolos gramaticales de la regla 
def p_instruccion_4(p):
    ''' INS_4 : PLUS SIMPLE
            | PLUS INDIRECTO
            | PLUS INMEDIATO'''
    if parse.pasada == 1:
        if extencion == "s":
            insert_error(str(p.lineno(1)),"formato valido solo  para la arquitectura XE")
        p[0]=4
    else:
        l = p[2]
        code = step2.operation_type_3_4(l[0],l[1],l[2],4,l[4],l[5],l[6],l[7],l[9])
        p[0]=[code,l[8]]
    pass

## operacion RSUB la cual es la unica sin registro m
# @param o arreglo mapeado con los simbolos gramaticales de la regla 
def p_instruccion_codigo_RSUB(p):
    ''' CI : RSUB'''
    if parse.pasada==2:
        if extencion =="s":
            p[0]=["4C0000",pc[p.lineno(1)-1]]
        else:
            p[0]=["4F0000",pc[p.lineno(1)-1]]
    else:    
        p[0]=3
    pass

## instrucciones que generan 3 p 4 bytes 
# empareja las de direccionamiento simple
# @param o arreglo mapeado con los simbolos gramaticales de la regla  
def p_simple(p):
    '''SIMPLE : SIMPLEC
              | SIMPLEM'''
    p[0] = p[1]
    pass

## una constante que su valor entero debe de ser estre 1 y 4095
# @param p arreglo mapeado con los simbolos gramaticales de la regla 
def p_constante(p):
    '''CONSTANT : DECIMAL
                | HEX'''
    p[1]=conv.to_decimal(p[1])
    p[1]= conv.decimal_to_hexadecimal(p[1])
    p[0]=p[1]
    pass

## instrucciones de operaciones con direccionamiento  simple y con un argumento 
# de tipo m 
# @param p arreglo mapeado con los simbolos gramaticales de la regla 
def p_simple_m_etiqueta(p):
    ''' SIMPLEM : OP_3_4 ETIQUETA
                | OP_3_4 ETIQUETA DIR'''
    if parse.pasada == 2:
      label = p[2]
      valid_label = True
      if not label in symbols:
          symbols[label] = "7FFFH"
          insert_warning(str(p.lineno(2)),"No existe la etiqueta "+label)
          valid_label = False
      m = symbols[p[2]]
      index = len(p) == 4
      op = p[1]
      if extencion == "s": 
          string = step2.operations_code(op,m,index)
          p[0]=string
          p[0]=[string,pc[p.lineno(2)-1]]
      else:
          is_index = len(p) == 4
          cp = pc[p.lineno(2)]
          format_type = 3
          num_line = p.lineno(2)
          dir_type ="Simple"
          p[0] = [cp,op,m,format_type,num_line,dir_type,False,is_index,pc[p.lineno(2)-1],valid_label]
    pass


## instrucciones de operaciones con direccionamiento  simple y con un argumento 
# de tipo c (constante)
# @param p arreglo mapeado con los simbolos gramaticales de la regla 
def p_simple_c(p):
    ''' SIMPLEC : OP_3_4 CONSTANT
                | OP_3_4 CONSTANT DIR'''
    if parse.pasada == 2:
        m = p[2]
        op = p[1]
        is_index = len(p) == 4
        cp = pc[p.lineno(2)]
        format_type = 3
        num_line = p.lineno(2)
        dir_type ="Simple"
        p[0] = [cp,op,m,format_type,num_line,dir_type,True,is_index,pc[p.lineno(2)-1],True]
    pass


def p_indirecto_constante(p):
   '''INDIRECTO : OP_3_4 AT CONSTANT '''
   if parse.pasada == 2:
        m = p[3]
        op = p[1]
        cp = pc[p.lineno(2)]
        format_type = 3
        num_line = p.lineno(2)
        dir_type ="Indirecto"
        p[0] = [cp,op,m,format_type,num_line,dir_type,True,False,pc[p.lineno(2)-1],True]
   pass

def p_indirecto_etiqueta(p):
    '''INDIRECTO : OP_3_4 AT ETIQUETA'''
    if parse.pasada == 2:
      label = p[3]
      valid_label = True
      if not label in symbols:
          symbols[label] = "7FFFH"
          insert_warning(str(p.lineno(2)),"No existe la etiqueta "+label)
          valid_label = False
      m = symbols[p[3]]
      op = p[1]
      cp = pc[p.lineno(2)]
      format_type = 3
      num_line = p.lineno(2)
      dir_type ="Indirecto"
      p[0] = [cp,op,m,format_type,num_line,dir_type,False,False,pc[p.lineno(2)-1],valid_label]
    pass
    
def p_inmediato_constante(p):
    '''INMEDIATO : OP_3_4 HASHTAG CONSTANT'''
    if parse.pasada == 2:
        m = p[3]
        op = p[1]
        cp = pc[p.lineno(2)]
        format_type = 3
        num_line = p.lineno(2)
        dir_type ="Inmediato"
        p[0] = [cp,op,m,format_type,num_line,dir_type,True,False,pc[p.lineno(2)-1],True]
    pass 

def p_inmediato_etiqueta(p):
    '''INMEDIATO : OP_3_4 HASHTAG ETIQUETA'''
    if parse.pasada == 2:
      label = p[3]
      valid_label = True
      if not label in symbols:
          symbols[label] = "7FFFH"
          insert_warning(str(p.lineno(2)),"No existe la etiqueta "+label)
          valid_label = False
      m = symbols[p[3]]
      op = p[1]
      cp = pc[p.lineno(2)]
      format_type = 3
      num_line = p.lineno(2)
      dir_type ="Inmediato"
      p[0] = [cp,op,m,format_type,num_line,dir_type,False,False,pc[p.lineno(2)-1],valid_label]
    pass

def p_operation_3_4(p):
    ''' OP_3_4 : OP_S
                | OP_XE'''
    p[0]=p[1]
    pass

        

def p_operation_S(p):
    ''' OP_S : ADD
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
              | WD'''
    p[0]=p[1]

def p_operation_XE(p):
    ''' OP_XE : ADDF
              | COMPF
              | DIVF
              | LDB
              | LDF
              | LPS
              | LDS
              | LDT
              | MULF
              | STB
              | STF
              | STI
              | STS 
              | STT
              | SUBF
              | SSK'''
    if parse.pasada == 1:
        if extencion == "s":
            insert_error(str(p.lineno(1)),"instruccion solo valida para la arquitectura XE")
    p[0]=p[1]

## cuando el analizador detecta un error o una regla no empareja 
#se llama este metodo el cual inserta el error en el diccionario de errores sintacticos
#@param t donde viene el token que produjo el error
def p_error(t):
  if t:
      line_error = str(t.lexer.lineno)
      if t.type == "error":
          token = t.value[0]
      else:
          token = get_token(t.value)
      insert_error(line_error,"No se reconoce el token "+ token)
      yacc.errok()
      if len(pc)==0:
          pc.append("0000H")
      else:
          increment_PC(3)
      tok = yacc.token()
      return tok
  else:
      print "NONE"

  
parse = yacc.yacc()
parse.inicial = "0H"
parse.pasada = 1