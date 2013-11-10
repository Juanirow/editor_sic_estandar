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
from register import Register
from segment import Segment

seg = Segment()
hex = Hexadecimal()
conv = Convert()
disp = Displacement()
reg = Register("R")
extension =""
registers = {"A":0,"X":1,"L":2,"CP":8,"SW":9,"B":3,"S":4,"T":5,"F":6}

## carga el codigo en la lista de codigo y le elimina los 
# nodos vacios 
def load_code(code):
    parse.list_code = code
    delete_spaces(parse.list_code)


def delete_spaces(code):
    it = 0
    while it < len(code):
        item = code[it]
        if item.strip() == "":
            code.remove(item)
        else:
            it += 1
## obtiene el numero de errores lexicos y sintacticos obtenidos
# @return regresa la suma de los errores lexicos y sintacticos
def num_errors():
    return seg.get_num_errors_all()
    # print seg.get_segment().errors
    # print seg.get_segment().errors_s
    # e1 = len(seg.get_segment().errors_s)
    # e2 = len(seg.get_segment().errors)
    # return e1+e2
    
##regresa los errores obtenidos en la parte lexica
#@return errores lexicos en un diccionario    
def get_lexic_errors():
  return scann.errors

##regresa el siguiente token de una cadena separada por '
#@return siguiente token a analizar
def get_token(value):
  return value.split("\n")[0]
    
def equal_type(type1,type2,sym_type):
    if type1 == sym_type:
        if type2 == sym_type:
            return True
    return False
    
def check_error(type1,type2):
    return type1 == "error" or type2 == "error"

def get_line_at(line):
    return line - parse.last_index
    
def get_pc_at(line):
    line_n = line - parse.last_index
    pc =  seg.get_segment().pc[line_n]
    # print "parserL141",line,line_n,seg.get_segment().pc,parse.last_index,pc
    return pc

def get_bloque_at(line):
    line_n = line - parse.last_index
    # print "parserL141",line,line_n,seg.get_segment().num_bloque,parse.last_index
    return seg.get_segment().num_bloque[line_n]
    

#==============================================================================
#                       Reglas Gramaticales
#==============================================================================

## regla inicial la cual consta de la directiva start un conjunto de instrucciones y 
# la directiva end
#@param p arreglo mapeado con los simbolos gramaticales de la regla
def p_inicial(p):
  '''
    INI : DS C DE _SALTO
        | DS C DE 
  '''
  pass 

## regla de la directiva start
# checa si la direccion es hexadecimal y es diferente de 0
#@param p arreglo mapeado con los simbolos gramaticales de la regla
def p_directiva_start(p):
    '''
    DS : ETIQUETA START HEX _SALTO _D
    | ETIQUETA START DECIMAL _SALTO _D
    '''
    list_e = p[5]
    if parse.pasada == 1:
        seg.get_segment().bloques.nuevo_bloque("por omision")
        seg.get_segment().name = p[1]
        s = p[3]
        val = conv.to_decimal(s)
        if extension == "s":
            if val == 0:
                seg.insert_error(str(p.lineno(1)),"La Sic estandar no soporta direcciones relativas")
        else:
            if val > 0:
                seg.insert_error(str(p.lineno(1)),"La SIC Extendida no soporta direcciones absolutas")
        if conv.is_hexadecimal(s):
            val = p[3]
        elif s == "0":
            val = "000000H"
        else:
            val = conv.decimal_to_hexadecimal(s)
        seg.get_segment().inicial = val
        seg.get_segment().bloques.set_load_dir(val)
        seg.get_segment().pc.append(seg.get_segment().inicial)
        seg.get_segment().pc.append(seg.get_segment().inicial)
        seg.get_segment().num_bloque.append(0)
        seg.get_segment().num_bloque.append(0)
        if list_e:
            for item_l in list_e:
                seg.increment_PC(0)
                seg.get_segment().num_bloque.append(0)
                if item_l[0] == "EXTREF":
                    l_etiq = item_l[1]
                    for item_etiq in l_etiq:
                        seg.insert_symbol(item_etiq,"0H","_",0,0,True)
                    seg.get_segment().step2.make_register_r(l_etiq)
                    

    else:
        length = seg.get_len_program()
        if length == "H":
            length = "0H"
        seg.get_segment().step2.directive_start(p[1],length,p[3])
        seg.get_segment().obj_code.append("")  
        if list_e:
            it = 0
            while it < len(list_e):
                seg.get_segment().obj_code.append("")
                it += 1
            for item_l in list_e:
                if item_l[0] == "EXTDEF":
                    l_etiq = item_l[1]
                    seg.get_segment().step2.make_register_d(l_etiq,seg.get_segment().symbols)

def p_extref(p):
    '_D : EXTREF VAR _SALTO _D'
    if parse.pasada == 1:
        if extension == "s":
            seg.insert_error(str(p.lineno(1)),"Directiva no valida para la sic estandar")
    d_ant = p[4]    
    p[0] = [["EXTREF",p[2]]]
    if d_ant:
        p[0]+=d_ant
    pass

def p_extdef(p):
    '_D : EXTDEF VAR _SALTO _D'
    if parse.pasada == 1:
        if extension == "s":
            seg.insert_error(str(p.lineno(1)),"Directiva no valida para la sic estandar")
    d_ant = p[4]
    p[0]= [["EXTDEF",p[2]]]
    if d_ant:
        p[0]+=d_ant 
    pass

def p_def_epsilon(p):
    '_D : EPSILON'
    p[0] = None
    pass
    
def p_var(p):
    'VAR : ETIQUETA VARP'
    ret_list = [p[1]]
    if type(p[2]) is list:
        ret_list+=p[2]
    p[0] = ret_list

def p_var_p(p):
    'VARP : COMMA ETIQUETA VARP'
    ret_list = [p[2]]
    if type(p[3]) is list:
        ret_list+=p[3]
    p[0] = ret_list
    
def p_var_p_eps(p):
    'VARP : EPSILON'
    p[0] = p[1]
    
def p_csect(p):
    'CS : ETIQUETA CSECT _SALTO _D '
    list_e = p[4]
    line = p.lineno(1)-1

    if parse.pasada == 1:
        errors = errors_offset(scann.errors,line)
        seg.get_segment().errors_s = errors
        code =  parse.list_code[seg.last_code:line]
        seg.get_segment().code = code
        seg.last_code = line
        parse.last_index = line
        name = p[1].strip().lower()
        seg.new_segment(name)
        seg.get_segment().pc.append("00H")
        seg.increment_PC(0)
        seg.get_segment().num_bloque.append(0)
        if list_e:
            for item_l in list_e:
                seg.increment_PC(0)
                seg.get_segment().num_bloque.append(0)
                if item_l[0] == "EXTREF":
                    l_etiq = item_l[1]
                    for item_etiq in l_etiq:
                        seg.insert_symbol(item_etiq,"0H","_",0,0,True)
                    seg.get_segment().step2.make_register_r(l_etiq)
    else:
        seg.last_code = line
        parse.last_index = line
        seg.index += 1
        len_program = seg.get_segment().bloques.get_len_program()
        seg.get_segment().step2.directive_start(seg.get_segment().name,len_program,seg.get_segment().pc[0])
        seg.get_segment().obj_code.append("")
        if list_e:
            it = 0
            while it < len(list_e):
                seg.get_segment().obj_code.append("")
                it += 1
            for item_l in list_e:
                if item_l[0] == "EXTDEF":
                    l_etiq = item_l[1]
                    seg.get_segment().step2.make_register_d(l_etiq,seg.get_segment().symbols)
    pass


def errors_offset(errors,line):
    ret = {}
    for e in errors:
        # print errors[e]
        val = int(e)-parse.last_index
        if val > 0 and val < line:
            ret[e] = errors[e]
    return ret
            
        

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
      seg.index = 0
      if len(p) == 3:
          dir = p[2]
          sym = seg.exist_symbol(dir)
          if sym:
              dir = sym.get_dir_val()
          else:
              seg.insert_error(str(p.lineno(1)),"No se reconoce la etiqueta "+dir)
              dir = "000000H"
      seg.get_segment().step2.directive_end(dir,seg.get_segment().pc[0])
      seg.get_segment().obj_code.append("")
  else:
      seg.get_segment().code = parse.list_code[seg.last_code:-1]
      seg.get_segment_at(0).code.append(parse.list_code[-1])
  pass 
 
## conjunto de instrucciones las cuales pueden ser directivas o codigos de operacion
# @brief se usa para encadenar instrucciones
#@param p arreglo mapeado con los simbolos gramaticales de la regla
def p_codigo(p):
  '''
  C : DC _SALTO C 
  | CP _SALTO C
  | CS C
  | EPSILON
  '''
  pass 


def p_org(p):
    'DC : ORG CONSTANT'
    if parse.pasada == 2:
        seg.get_segment().step2.complete_register()
        seg.get_segment().obj_code.append("")
    else:
        seg.increment_PC(0)
        seg.get_segment().pc[-1] = p[2]
    pass

def p_directiva_equ_multi(p):
    '''DC : ETIQUETA EQU MULTI'''
    if parse.pasada == 1:
        if extension == "s":
            seg.insert_error(str(p.lineno(1)),"Directiva no soportada por la sic estandar")
        seg.insert_symbol(p[1],seg.get_segment().pc[-1],
                        "relativo",p.lineno(1),seg.get_segment().bloques.get_index())
        seg.increment_PC(0)
    else:
        seg.get_segment().obj_code.append("")
    pass

def p_directiva_use(p):
    '''DC : USE ETIQUETA 
    | USE '''
    if parse.pasada == 1:
        if extension == "s":
            seg.insert_error(str(p.lineno(1)),"Directiva no soportada por la sic estandar")
        if len(p) == 2:
            seg.get_segment().bloques.nuevo_bloque("por omision")
        else:
            seg.get_segment().bloques.nuevo_bloque(p[2])
        cp = seg.get_segment().bloques.get_last_cp()
        seg.get_segment().pc[-1] = cp
        seg.get_segment().num_bloque[-1] = seg.get_segment().bloques.get_index()
        seg.increment_PC(0)
    else:
        seg.get_segment().step2.complete_register()
        seg.get_segment().obj_code.append("")

def p_directiva_equ_exp(p):
    'DC : ETIQUETA EQU _EXP'
    if parse.pasada == 1:
        if extension == "s":
            seg.insert_error(str(p.lineno(1)),"Directiva no soportada por la sic estandar")
        exp = p[3]
        type_exp = check_is_valid_exp(p.lineno(1),exp[1])
        val = conv.exp_to_hexadecimal(exp[0])
        seg.insert_symbol(p[1],val,type_exp,p.lineno(1),seg.get_segment().bloques.get_index())
        seg.increment_PC(0)
    else:
        seg.get_segment().obj_code.append("")
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
          pc_val = get_pc_at(p.lineno(1)-1)
          seg.insert_symbol(p[1],pc_val,"relativo",p.lineno(1),seg.get_segment().bloques.get_index())
      seg.increment_PC(num)
  else:
      str = seg.get_segment().step2.const_BYTE(num)
      if extension == "x":
          load_dir = seg.get_segment().bloques.get_load_dir_at(get_bloque_at(p.lineno(1)-1))
          pc_val = get_pc_at(p.lineno(1)-1)
          val = hex.plus(load_dir,pc_val)
          if val == "H":
              val = "0H"
          val =  reg.adjust_bytes(val,6,False)   
      else:
          val = get_pc_at(p.lineno(1)-1)
      seg.get_segment().step2.insert_str(str,val)
      seg.get_segment().obj_code.append(str)
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
  seg.insert_error(str(p.lineno(1)),"Al definir la constante en la directiva Byte")
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
          pc_val = get_pc_at(p.lineno(1)-1)
          seg.insert_symbol(p[1],pc_val,"relativo",p.lineno(1),seg.get_segment().bloques.get_index())
          inc = p[2]
      else:
          inc = p[1]
      seg.increment_PC(inc) 
  pass

def p_directiva_base(p):
  '''
  DIRECTIVA : ETIQUETA DIR_BASE
  | DIR_BASE
  '''
  if parse.pasada == 1:
      
      if len(p) == 3:
          pc_val = get_pc_at(p.lineno(1)-1)
          seg.insert_symbol(p[1],pc_val,"relativo",p.lineno(1),seg.get_segment().bloques.get_index())
      seg.increment_PC(0)
  pass

def p_directiva_base_valor(p):
    '''DIR_BASE : BASE ETIQUETA'''
    if parse.pasada == 2:
        label = p[2]
        sym = seg.exist_symbol(label)
        if sym:
            dir = sym.get_dir_val()
        else:
          seg.insert_error(str(p.lineno(1)),"No se reconoce la etiqueta "+label)
          dir = "0FFFFFH"
        seg.get_segment().obj_code.append("")
        seg.get_segment().step2.base = dir
    elif extension == "s":
          seg.insert_error(str(p.lineno(1)),"Directiva no soportada por la sic estandar")
    pass

def p_directiva_base_valor_etiqueta(p):
    '''DIR_BASE : BASE HEX
                | BASE DECIMAL'''
    if parse.pasada == 2:
        seg.get_segment().obj_code.append("")
        decimal = conv.to_decimal(p[2])
        seg.get_segment().step2.base = conv.decimal_to_hexadecimal(decimal)
    elif extension == "s":
          seg.insert_error(str(p.lineno(1)),"Directiva no soportada por la sic estandar")
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
      if p[1] == "RESW":
          inc = val * 3
      elif p[1] == "RESB":
          inc = val    
      p[0]=inc
  else:
      if p[1] == "WORD":
          val = seg.get_segment().step2.directive_word(str(val))
          seg.get_segment().obj_code.append(val)
          if extension == "x":
              blq_val = get_bloque_at(p.lineno(2)-1)
              load_dir = seg.get_segment().bloques.get_load_dir_at(blq_val)
              pc_val = get_pc_at(p.lineno(2)-1)              
              val2 = hex.plus(load_dir,pc_val)
              if val2 == "H":
                  val2 = "0H"
              val2 =  reg.adjust_bytes(val2,6,False)
          else:
             val2 = get_pc_at(p.lineno(2)-1) 
          seg.get_segment().step2.insert_str(val,val2)
      else:
          seg.get_segment().step2.complete_register()
          seg.get_segment().obj_code.append("")
  pass

def p_directiva_word(p):
    'NEMDIRECTIVA : WORD _EXP'
    if parse.pasada == 2:
        exp = p[2]
        if not exp[1] == "_":
            res = check_is_valid_exp(p.lineno(1),exp[1])
            if res == "relativo":
                seg.get_segment().step2.m_modif_register.append(p.lineno(1)-parse.last_index)
        else:
            for it in exp[2]:
                seg.get_segment().step2.list_word_m.append(it)
        val = int(p[2][0])
        val = conv.exp_to_hexadecimal(val)
        val = seg.get_segment().step2.directive_word(str(val))
        seg.get_segment().obj_code.append(val)
        if extension == "x":
            blq_val = get_bloque_at(p.lineno(1)-1)
            load_dir = seg.get_segment().bloques.get_load_dir_at(blq_val)
            pc_val = get_pc_at(p.lineno(1)-1)
            val2 = hex.plus(load_dir,pc_val)
            if val2 == "H":
              val2 = "0H"
            val2 =  reg.adjust_bytes(val2,6,False)
        else:
            val2 = get_pc_at(p.lineno(1)-1)
        seg.get_segment().step2.insert_str(val,val2)
    p[0] = 3

## regresa un error si el valor para reservar esta mal declarado
#@param p arreglo mapeado con los simbolos gramaticales de la regla
def p_nemonico_directivas_error(p):
  '''NEMDIRECTIVA : NEMONICO error '''
  seg.insert_error(str(p.lineno(2)),"Se esperaba un numero decimal o hexadecimal")
  p[0] = "error"
  pass

## tipo de directivas para reservar memoria 
#@param p arreglo mapeado con los simbolos gramaticales de la regla
def p_nemonico(p):
  '''
  NEMONICO : RESB
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
          pc_val = get_pc_at(p.lineno(1)-1)
          seg.insert_symbol(p[1],pc_val,"relativo",p.lineno(1),seg.get_segment().bloques.get_index())
          val = p[2]
      else:
          val = p[1]
      val = conv.to_decimal(str(val))
      seg.increment_PC(val)
  else:
      list = p[1]
      if len(p) == 3:
          list = p[2]
      if extension == "s":
          val = get_pc_at(list[1])
      else:
#          print "g48",seg.get_segment().num_bloque,list[1]
          blq_val = get_bloque_at(list[1])
          load_dir = seg.get_segment().bloques.get_load_dir_at(blq_val)
          pc_val = get_pc_at(list[1])
          val = hex.plus(load_dir,pc_val)
          if val == "H":
              val = "0H"
          val =  reg.adjust_bytes(val,6,False)
      seg.get_segment().step2.insert_str(list[0],val)
      seg.get_segment().obj_code.append(list[0])
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
        if extension == "s":
            seg.insert_error(str(p.lineno(1)),"instruccion solo valida para la arquitectura XE")
        p[0]=1
    else:
        operation = p[1]
        code = seg.get_segment().step2.operations[operation]
        line = p.lineno(1)-1
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
        if extension == "s":
            seg.insert_error(str(p.lineno(1)),"instruccion solo valida para la arquitectura XE")
    else:
        p[0] = [seg.get_segment().step2.operations_type_2(p[1],p[2],""),p.lineno(1)-1]
    pass

## instrucciones de tipo 2 que tienen como parametro un numero entre 1 y 16
# @param o arreglo mapeado con los simbolos gramaticales de la regla  
def p_inst_n(p):
    ''' INS_2_N : SVC NUMBER'''
    if parse.pasada == 1:
        if extension == "s":
            seg.insert_error(str(p.lineno(1)),"instruccion solo valida para la arquitectura XE")
    else:
        p[0] = [seg.get_segment().step2.operations_type2_n(p[1],p[2]),p.lineno(1)-1]
    pass

## numero que se encuentra entre el 1 y 16
# @param o arreglo mapeado con los simbolos gramaticales de la regla  
def p_number(p):
    '''NUMBER : DECIMAL'''
    if parse.pasada == 1:    
        val = int(p[1])
        if not (val < 17 and val > 0):
            seg.insert_error(str(p.lineno(1)),"El numero debe ser ente 1 y 16")
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
            p[0] = [seg.get_segment().step2.operations_type_2(p[1],p[2],p[4]),p.lineno(2)-1]
        else:
            p[0] = [seg.get_segment().step2.operations_type_2(p[1],p[2],"X"),p.lineno(2)-1]
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
        if extension == "s":
            seg.insert_error(str(p.lineno(1)),"instruccion solo valida para la arquitectura XE")
    else:
        p[0] = p[1]
    pass

## regla que empareja las instrucciones de tipo 2 
#que tiene como argumentos un registro y un numero  
# @param o arreglo mapeado con los simbolos gramaticales de la regla 
def p_inst_2_reg_num(p):
    ''' INS_2_RN : ARG_R_N REGISTER COMMA NUMBER'''
    if parse.pasada == 2:
        p[0] = [seg.get_segment().step2.operations_type_2_rn(p[1],p[2],p[4]),p.lineno(2)-1]
    pass

## instrucciones de tipo 2 que tiene como argumentos un registro y un numero 
# @param o arreglo mapeado con los simbolos gramaticales de la regla
def p_op_arg_rn(p):
    '''ARG_R_N : SHIFTL
                | SHIFTR'''
    if parse.pasada == 1:
        if extension == "s":
            seg.insert_error(str(p.lineno(1)),"instruccion solo valida para la arquitectura XE")
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
        if extension == "s":
            p[0] = p[1]
        else:
            l = p[1]
            if l[9] == "_":
                seg.insert_error(str(p.lineno(1)),"las expreciones con valores externos no son validos en formato 3")
                l[2] = "FFFFH"
            code = seg.get_segment().step2.operation_type_3_4(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[9])
            p[0]=[code,l[8]]
    pass

## regla que empareja las instrucciones de tipo 3   
# @param o arreglo mapeado con los simbolos gramaticales de la regla 
def p_instruction_3(p):
    '''INS_3  : INDIRECTO
              | INMEDIATO'''
    p[0] = 3
    if parse.pasada == 1:
        if extension == "s":
            seg.insert_error(str(p.lineno(1)),"instruccion solo valida para la arquitectura XE")
    else:
        l = p[1]
        if l[9] == "_":
            seg.insert_error(str(p.lineno(1)),"las expreciones con valores externos no son validos en formato 3")
            l[2] = "FFFFH"
        code = seg.get_segment().step2.operation_type_3_4(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[9])
        p[0]=[code,l[8]]
    pass

## regla que empareja las instrucciones de tipo 4 
# @param o arreglo mapeado con los simbolos gramaticales de la regla 
def p_instruccion_4(p):
    ''' INS_4 : PLUS SIMPLE
            | PLUS INDIRECTO
            | PLUS INMEDIATO'''
    if parse.pasada == 1:
        if extension == "s":
            seg.insert_error(str(p.lineno(1)),"formato valido solo  para la arquitectura XE")
        p[0]=4
    else:
        l = p[2]
        val = conv.to_decimal(l[2])
        b1 = parse.first_type == "CONSTANT" and len(parse.list_exp) == 1 and val<4095
        b2 = l[9] == "absoluto" and val<4095
        if b1 or b2:
            seg.insert_error(str(p.lineno(1)),"Formato 4 no valido")
        code = seg.get_segment().step2.operation_type_3_4(l[0],l[1],l[2],4,l[4],l[5],l[6],l[7],l[9])
        if not l[9] == "relativo":
            for it in l[10]:
                seg.get_segment().step2.list_op_m.append(it)
        p[0]=[code,l[8]]
    pass

## operacion RSUB la cual es la unica sin registro m
# @param o arreglo mapeado con los simbolos gramaticales de la regla 
def p_instruccion_codigo_RSUB(p):
    ''' CI : RSUB'''
    if parse.pasada==2:
        if extension =="s":
            p[0]=["4C0000",p.lineno(1)-1]
        else:
            p[0]=["4F0000",p.lineno(1)-1]
    else:    
        p[0]=3
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
    ''' SIMPLE : OP_3_4 _EXP
                | OP_3_4 _EXP DIR'''
    if parse.pasada == 2:
      exp = p[2]
      if p[2][1] == "_":
           type_exp = "_"
           is_c = False
      else:
          type_exp = check_is_valid_exp(parse.lineno,exp[1])
#      c = (parse.first_type == "ETIQUETA" and len(parse.list_exp) == 1) and type_exp == "absoluto"
      if type_exp == "relativo":
          is_c = False
      else:
          is_c = True
      index = len(p) == 4
      op = p[1]
      m = conv.exp_to_hexadecimal(exp[0])
      if extension == "s": 
          string = seg.get_segment().step2.operations_code(op,m,index)
          p[0]=string
          p[0]=[string,parse.lineno-1]
      else:
          is_index = len(p) == 4
          line = parse.lineno - 1
          blq_val = get_bloque_at(line)
          cp = next_cp_bloque(line,blq_val)
          #print cp,blq_val,line,op,parse.last_index,seg.index#,seg.get_segment().pc
          cp = conv.to_decimal(cp)
          cant_bloq =  seg.get_segment().bloques.get_load_dir_at(blq_val)
          cp += conv.to_decimal(cant_bloq)
          # print "caldosio",cant_bloq
          cp = conv.decimal_to_hexadecimal(cp)
          format_type = 3
          num_line = parse.lineno
          dir_type ="Simple"
          p[0] = [cp,op,m,format_type,num_line-parse.last_index,dir_type,is_c,is_index,parse.lineno-1,type_exp,p[2][2]]
    pass

def p_indirecto_constante(p):
   '''INDIRECTO : OP_3_4 AT _EXP '''
   if parse.pasada == 2:
       exp = p[3]
       if p[3][1] == "_":
           type_exp = "_"
           is_c = False
       else:
           type_exp = check_is_valid_exp(p.lineno(2),exp[1])
           if (parse.first_type == "ETIQUETA" and len(parse.list_exp) == 1) and type_exp == "relativo":
               is_c = False
           else:
               is_c = True
       m = conv.exp_to_hexadecimal(exp[0])
       op = p[1]
       line = p.lineno(2) - 1
       blq_val = get_bloque_at(p.lineno(2)-1)
       cp = next_cp_bloque(line,blq_val)
       cp = conv.to_decimal(cp) 
       cp += conv.to_decimal(seg.get_segment().bloques.get_load_dir_at(blq_val))
       cp = conv.decimal_to_hexadecimal(cp)
       format_type = 3
       num_line = p.lineno(2)
       dir_type ="Indirecto"
       p[0] = [cp,op,m,format_type,num_line-parse.last_index,dir_type,is_c,False,p.lineno(2)-1,type_exp,p[3][2]]
   pass
    
def p_inmediato_constante(p):
    '''INMEDIATO : OP_3_4 HASHTAG _EXP'''
    if parse.pasada == 2:
       exp = p[3]
       if p[3][1] == "_":
           type_exp = "_"
           is_c = True
       else:
           type_exp = check_is_valid_exp(p.lineno(2),exp[1])
           if (parse.first_type == "ETIQUETA" and len(parse.list_exp) == 1) and type_exp == "relativo":
               is_c = False
           else:
               is_c = True
       m = conv.exp_to_hexadecimal(exp[0])
#       print m,is_c,type_exp,parse.list_exp
       op = p[1]
       line = p.lineno(2) - 1
       blq_val = get_bloque_at(p.lineno(2)-1)
       cp = next_cp_bloque(line,blq_val)
       cp = conv.to_decimal(cp) 
       cp += conv.to_decimal(seg.get_segment().bloques.get_load_dir_at(blq_val))
       cp = conv.decimal_to_hexadecimal(cp)
       format_type = 3
       num_line = p.lineno(2)
       dir_type ="Inmediato"
       p[0] = [cp,op,m,format_type,num_line-parse.last_index,dir_type,is_c,False,p.lineno(2)-1,type_exp,p[3][2]]
    pass

def next_cp_bloque(line,numb):
    it = line + 1
    #print it, len(seg.get_segment().num_bloque)
    while it - parse.last_index < len(seg.get_segment().num_bloque):
        blq_val = get_bloque_at(it)
       # print numb,blq_val
        if numb == blq_val:
            return get_pc_at(it)
        it += 1
    return seg.get_segment().bloques.get_last_pc_at(numb)
    

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
        if extension == "s":
            seg.insert_error(str(p.lineno(1)),"instruccion solo valida para la arquitectura XE")
    p[0]=p[1]
#==============================================================================
#     Expresiones
#==============================================================================
def p_exp(p):
    '_EXP : _M  _E _FIN'
    p[0] = p[2]
    
    pass

def p_final_marcador(p):
    '_FIN :'
    parse.evalua = False
    pass

def p_marcador(p):
    '_M : '
    if p[-1]== "EQU":
        parse.evalua = True
    else:
        parse.evalua = False
    parse.list_exp =[]
    parse.lista_symb=["+"]
    parse.first_type = ""
    parse.lineno = 0
    pass

##regla gramatica para la suma de dos expresiones
#@param p arreglo mapeado con los simbolos gramaticales de la regla 
def p_expresion_plus(p):
    '_E : _E PLUS _T '
    if parse.pasada == 2 or parse.evalua:
        type1 = p[1][1]
        type2 = p[3][1]
        list_r = p[1][2] + p[3][2]
        res = p[1][0] + p[3][0]
        if type1 == "_" or type2 == "_":
            p[0] = [int(res),"_",list_r]
        else:
            error = check_error(type1,type2)
            if not error:
                if type2 == type1:
                    type0 = "absoluto"
                else:
                    type0 = "relativo"
                p[0] = [res,type0,list_r]
            else:
                p[0]=[-1,"error",list_r]
    pass


##regla gramatica para la resta de dos expresiones
#@param p arreglo mapeado con los simbolos gramaticales de la regla 
def p_expresion_minus(p):
    '_E : _E  MINUS _T '
    if parse.pasada == 2 or parse.evalua:
        type1 = p[1][1]
        type2 = p[3][1]
        list_r = p[1][2] + p[3][2]
        res = p[1][0] - p[3][0]
        if type1 == "_" or type2 == "_":
            p[0] = [int(res),"_",list_r]
        else:
            error = check_error(type1,type2)
            if not error:
                if type2 == type1:
                    type0 = "absoluto"
                elif type1 == "relativo":
                    type0 = "relativo"
                else:
                    error = True
                if not error:
                    res = p[1][0] - p[3][0]
                    p[0] = [res,type0,list_r]                
                else:
                    error = True
            if error:
                p[0] = [-1,"error",list_r]
    pass

##regla gramatica para la multiplicacion de dos expresiones
#@param p arreglo mapeado con los simbolos gramaticales de la regla 
def p_expresion_multi(p):
    '_T : _T MULTI _F '
    if parse.pasada == 2 or parse.evalua:
        type1 = p[1][1]
        type2 = p[3][1]
        list_r = p[1][2] + p[3][2]
        res = p[1][0] * p[3][0]
        if type1 == "_" or type2 == "_":
            p[0] = [int(res),"_",list_r]
        else:
            error = check_error(type1,type2)
            if not error:
                if equal_type(type1,type2,"absoluto"):
                    p[0] = [int(res),"absoluto",list_r]
                else:
                    error = True
            if error:
                p[0] = [-1,"error",list_r]
        
    pass
##regla gramatica para la divicion de dos expresiones
#@param p arreglo mapeado con los simbolos gramaticales de la regla 
def p_expresion_div(p):
    '_T : _T DIVI _F '
    if parse.pasada == 2 or parse.evalua:
        error = False
        list_r = p[1][2] + p[3][2]
        if p[3][0] == 0:
            seg.insert_error(p.lineno(2),"No se puede dividir un numero entre cero")
            error = True
        else:
            type1 = p[1][1]
            type2 = p[3][1]
            res = p[1][0] / p[3][0]
            if type1 == "_" or type2 == "_":
                p[0] = [int(res),"_",list_r]
            else:
                if not check_error(type1,type2):
                    if equal_type(type1,type2,"absoluto"):
                        p[0] = [int(res),"absoluto",list_r]
                    else:
                        error = True
                else:
                    error = True
        if error:
            p[0] = [-1,"error",list_r]
    pass

def p_expresion_single(p):
    ''' _E : _T
        _T : _F
    '''
    if parse.pasada == 2 or parse.evalua:    
        p[0] = p[1]

def p_f_constant(p):
    '_F : CONSTANT'
    if parse.pasada == 2 or parse.evalua:
        if parse.first_type == "":
            parse.first_type = "CONSTANT"
            parse.lineno = p.lineno(1)
        numeric_val = conv.to_decimal(p[1])
        p[0] = [numeric_val,"absoluto",[]]
        check_sign(p,"absoluto")
    pass

def p_f_etiqueta(p):
    '_F : ETIQUETA '
    if parse.pasada == 2 or parse.evalua:
        if parse.first_type == "":
            parse.first_type = "ETIQUETA"
            parse.lineno = p.lineno(1)
        symb = seg.exist_symbol(p[1]) 
        if not symb:
            if parse.pasada == 2:
                seg.insert_warning(str(p.lineno(1)),"El simbolo no existe") 
            else:
                seg.insert_error(str(p.lineno(1)),"El simbolo no existe")
            val = conv.to_decimal("7FFFH")
            p[0] = [val,"error",[]]
            parse.lista_symb.append("error")
        else:
            er = False
            if parse.evalua:
                blq_val = get_bloque_at(p.lineno(1)-1)
                if not symb.num_bloque == blq_val:
                    seg.insert_error(str(p.lineno(1)),"El simbolo no existe en el bloque actual")
                    val = conv.to_decimal("7FFFH")
                    p[0] = [val,"error",[]]
                    er = True
            if not er:
                b = seg.get_segment().bloques.bloques[symb.num_bloque]
                numeric_val = conv.to_decimal(symb.get_dir_val())
                if symb.sym_type == "relativo" and extension == "x":
                    numeric_val += conv.to_decimal(b.load_dir)
                if symb.externo or symb.sym_type == "relativo":
                    sign = ret_sign(p)
                    p[0] = [numeric_val,symb.sym_type,[[symb.name,symb.sym_type,sign,get_pc_at(p.lineno(1)-1)]]]
                else:
                    p[0] = [numeric_val,symb.get_sym_type(),[]]
                check_sign(p,symb.get_sym_type())                  
    pass

def ret_sign(p):
    sign = p[-1]    
    if  not(sign == "-" or sign == "+"):
        sign = "+"
    sign = check_result_sign(sign)
    return sign 
    
def check_sign(p,symb_type):
    sign = p[-1]            
    if  not(sign == "-" or sign == "+"):
        sign = "+"
    sign = check_result_sign(sign)
    parse.list_exp.append(sign+symb_type)
    
def p_f_expresion(p):
    ' _F : _MARC1 _E _MARC2'
    if parse.pasada == 2 or parse.evalua:
        p[0] = p[2]    
    pass


def p_mar1(p):
    '_MARC1 : PARENO'
    if p[-1] == "-" or p[-1] == "+":
        sign = check_result_sign(p[-1])
        parse.lista_symb.append(sign)
    else:
        parse.lista_symb.append(parse.lista_symb[-1])
    pass

def p_marcador2(p):
    '_MARC2 : PARENC'
    parse.lista_symb.pop(-1)      
    pass
    
def check_result_sign(sig):
    if sig == parse.lista_symb[-1]:
        return "+"
    else:
        return "-"
    
def check_is_valid_exp(lineno,type_result):
    if not type_result == "error":
        l = reduce_expretion()
        if list_all_absolute(l):
            return "absoluto"
        else:
            dicc = num_relative(l)
            if dicc['+'] == 1:
                return "relativo"
    if not str(lineno) in seg.get_segment().warnings:
        seg.insert_error(str(lineno),"Expresion no valida")
    return "error"
    
def list_all_absolute(l):
    for index in l:
        if index[1:] == "relativo":
            return False
        return True

def num_relative(l):
    count_p = 0
    count_n = 0    
    for index in l:
        sign = index[0]
        str_index = index[1:]
        if str_index == "relativo":
            if sign == "+":
                count_p += 1
            else:
                count_n += 1
    return {'+':count_p,'-':count_n}
        
def reduce_expretion():
    
    l = parse.list_exp
    it = 0
    while it < len(l):
        inc = True
        index = l[it]
        sign = index[0]
        str_index = index[1:]
        if str_index == "relativo":
            n_sign = "+"
            if sign == "+":
                n_sign = "-"
            new_index = n_sign + str_index
            if new_index in l:
                l.remove(new_index)
                l.remove(index)
                l.append("+absoluto")
                inc = False
                it = 0
        if inc:
            it += 1
    return l
            
        
        
    
#==============================================================================
#       Errores 
#==============================================================================
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
      if not token == "\n":
          seg.insert_error(line_error,"P:No se reconoce el token "+ token+str(t))
      yacc.errok()
      if len(seg.get_segment().pc)==0:
          seg.get_segment().pc.append("0000H")
      else:
          seg.increment_PC(3)
      tok = yacc.token()
      return tok
  else:
      print "NONE"

parse = yacc.yacc()
parse.inicial = "0H"
parse.pasada = 1
parse.evalua = False
parse.lista_symb=["+"]
parse.list_exp =[]
parse.first_type = ""
parse.lineno = -1
parse.last_index = 0
parse.list_code = []