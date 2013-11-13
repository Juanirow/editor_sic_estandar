CP        BLOQUE    CODIGO                                       C. Objeto 
1000h     0         COPY	START	1000h                                       	         
1000h     0         FIRST	STL	RETADR                             141033    	         
001003H   0         CLOOP	JSUB	RDREC                             482039    	         
001006H   0         	LDA	LENGTH                                  001036    	         
001009H   0         	COMP	ZERO                                   281030    	         
00100CH   0         	JEQ	ENDFIL                                  301015    	         
00100FH   0         	JSUB	WRREC                                  482061    	         
001012H   0         	J	CLOOP                                     3C1003    	         
001015H   0         ENDFIL	LDA	EOF                               00102A    	         
001018H   0         	STA	BUFFER                                  0C1039    	         
00101BH   0         	LDA	THREE                                   00102D    	         
00101EH   0         	STA	LENGTH                                  0C1036    	         
001021H   0         	JSUB	WRREC                                  482061    	         
001024H   0         	LDL	RETADR                                  081033    	         
001027H   0         	RSUB                                        4C0000    	         
00102AH   0         EOF	BYTE	C'EOF'                              454F46    	         
00102DH   0         THREE	WORD	3                                 000003    	         
001030H   0         ZERO	WORD	0                                  000000    	         
001033H   0         RETADR	RESW	1                                          	         
001036H   0         LENGTH	RESW	1                                          	         
001039H   0         BUFFER	RESB	4096                                       	         
002039H   0         RDREC	LDX	ZERO                               041030    	         
00203CH   0         	LDA	ZERO                                    001030    	         
00203FH   0         RLOOP	TD	INPUT                               E0205D    	         
002042H   0         	JEQ	RLOOP                                   30203F    	         
002045H   0         	RD	INPUT                                    D8205D    	         
002048H   0         	COMP	ZERO                                   281030    	         
00204BH   0         	JEQ	EXIT                                    302057    	         
00204EH   0         	STCH	BUFFER,X                               549039    	         
002051H   0         	TIX	MAXLEN                                  2C205E    	         
002054H   0         	JLT	RLOOP                                   38203F    	         
002057H   0         EXIT	STX	LENGTH                              101036    	         
00205AH   0         	RSUB                                        4C0000    	         
00205DH   0         INPUT	BYTE	X'F1'                             F1        	         
00205EH   0         MAXLEN	WORD	4096                             001000    	         
002061H   0         WRREC	LDX	ZERO                               041030    	         
002064H   0         WLOOP	TD	OUTPUT                              E02079    	         
002067H   0         	JEQ	WLOOP                                   302064    	         
00206AH   0         	LDCH	BUFFER, X                              509039    	         
00206DH   0         	WD	OUTPUT                                   DC2079    	         
002070H   0         	TIX	LENGTH                                  2C1036    	         
002073H   0         	JLT	WLOOP                                   382064    	         
002076H   0         	RSUB                                        4C0000    	         
002079H   0         OUTPUT	BYTE	X'05'                            05        	         
00207AH   0         	END	FIRST                                             	         
Tabla de Simbolos 

NOMBRE      DIR/VAL     TIPO        BLOQUE      EXTERNO     
FIRST       1000h       relativo    0           False       
CLOOP       001003H     relativo    0           False       
ENDFIL      001015H     relativo    0           False       
EOF         00102AH     relativo    0           False       
THREE       00102DH     relativo    0           False       
ZERO        001030H     relativo    0           False       
RETADR      001033H     relativo    0           False       
LENGTH      001036H     relativo    0           False       
BUFFER      001039H     relativo    0           False       
RDREC       002039H     relativo    0           False       
RLOOP       00203FH     relativo    0           False       
EXIT        002057H     relativo    0           False       
INPUT       00205DH     relativo    0           False       
MAXLEN      00205EH     relativo    0           False       
WRREC       002061H     relativo    0           False       
WLOOP       002064H     relativo    0           False       
OUTPUT      002079H     relativo    0           False       


Tabla de Bloques 

DIR_CARGA         NOMBRE            NUM_BLOQUE        TAMAÑO           
1000h             por omision       0                 107AH             


