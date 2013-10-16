EJERCICIO START 0
FIRST	EQU	1
SECOND	EQU	FIRST+1
THIRD	EQU	SECOND+1
SIMBOLO   RESW  1                
NUMERO    WORD  FIRST+(SECOND+THIRD)*THIRD
DECIMAL   RESB  5                
INICIO   +RD    #SIMBOLO        
          MUL   NUMERO        
          FLOAT                     
          MULF  DECIMAL        
          CLEAR X                
CICLO    +JSUB  @RAIZ        
          LDA   ARREGLO, X
          TIX   #1                
          COMP  #0                
         +JGT  2000H, X        
ARREGLO   RESW  800H                
RAIZ      CLEAR B                
          STA   TEMP                
          WD    @100H        
         +LPS   #2000H        
          J     400H, X        
TEMP      RESW  1                
FIN       SIO                               
          LDX   @AUX        
          SUBR  A, X                
AUX       RESB  250H                
MAIN      BASE  INICIO        
          JSUB  INICIO        
          JSUB  FIN                
          END   MAIN

