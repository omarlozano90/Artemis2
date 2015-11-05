__author__ = 'Macintosh'

import ply.yacc as yacc
import lexicon
import sys

#lista de tokens
tokens = lexicon.tokens

def p_progmain(p):
    '''main : PROGRAM ID SEMICOL decglobal decfunc MAIN block EXIT
            | PROGRAM ID SEMICOL decfunc MAIN block EXIT
            | PROGRAM ID SEMICOL decglobal MAIN block EXIT
            | PROGRAM ID SEMICOL MAIN block EXIT'''
    print('win')

def p_decglobal(p):
        '''decglobal : decarr decglobal
                    | decvar decglobal
                    | decarr
                    | decvar'''


def p_decfunc(p):
        '''decfunc : assvar decfunc
                    | assarr decfunc
                    | function decfunc
                    | assvar
                    | assarr
                    | function'''

def p_function(p):
    '''function : FUNCTION ID type OPAR type ID CPAR block
                | FUNCTION ID type OPAR type ID COMA functionhelp'''

def p_functionhelp(p):
    '''functionhelp : type ID COMA functionhelp
                | type ID CPAR block'''

def p_return(p):
    '''return : RETURN association SEMICOL'''

def p_block(p):
        '''block : OBRAK estatuto CBRAK
                | OBRAK estatuto block
                | estatuto block
                | estatuto CBRAK'''

def p_estatuto(p):
        '''estatuto : assvar
                | assarr
                | decvar
                | decarr
                | condition
                | writing
                | cycle
                | return'''

def p_assvar(p):
    '''assvar : ID EQUAL asshelp'''



def p_assarr(p):
    '''assarr : ID OBRAC arrdim EQUAL asshelp'''


def p_asshelp(p):
    '''asshelp : association SEMICOL
                | CCHAR SEMICOL
                | CSTRING SEMICOL'''

def p_condition(p):
    '''condition : IF OPAR association CPAR block else'''

def p_else(p):
    '''else : ELSE block
            |'''

def p_decvar(p):
        '''decvar : VAR type ID SEMICOL'''



def p_type(p):
        '''type : INT
                | FLOAT
                | CHAR
                | STRING
                | BOOL'''


def p_writing(p):
        '''writing : PRINT OPAR exp CPAR SEMICOL
                | PRINT OPAR CSTRING CPAR SEMICOL
                | PRINT OPAR CCHAR CPAR SEMICOL'''

def p_cycle(p):
        '''cycle : WHILE OPAR association CPAR block
                | DO block WHILE OPAR association CPAR SEMICOL '''



#THIS IS EXP
def p_exp(p):
    '''exp : term PLUS exp
            | term MINUS exp
            | term'''

def p_term(p):
    '''term : term TIMES factor
            | factor DIVIDE factor
            | factor'''

def p_factor(p):
    '''factor : OPAR exp CPAR
            | varcte'''

def p_varcte(p):
    '''varcte : ID OBRAC arrdim
            | ID
            | CINT
            | CFLOAT'''



#for arr dimesions
def p_arrdim(p):
    '''arrdim :  exp CBRAC OBRAC arrdim
            | exp CBRAC'''


def p_decarr(p):
        '''decarr : ARR type ID OBRAC arrdim SEMICOL'''


def p_association(p):
    '''association : exp MTHAN exp
                 | exp LTHAN exp
                 | exp MTHANE exp
                 | exp LTHANE exp
                 | exp NOTEQUAL exp
                 | exp EQUALTO exp
                 | exp'''




filename = sys.argv[1]
file = open(filename)
characters = file.read()
file.close()

def p_error (t):
    print('error  Semantica')
    quit()

yacc.yacc()

t = yacc.parse(characters)

