__author__ = 'Macintosh'

import ply.lex as lex

#lexicon,
tokens = ['PROGRAM',#reserved
          'EXIT',
          'ID',
          'MAIN',
          'PRINT',
          'DO',
          'WHILE',
          'VAR',
          'INT',
          'FLOAT',
          'CHAR',
          'STRING',
          'BOOL',
          'ARR',
          'IF',
          'ELSE',
          'FUNCTION',
          'RETURN',

          'CFLOAT',# constant
          'CINT',
          'CCHAR',
          'CSTRING',

            #simple
          'EQUAL', # =
          'OPAR',# (
          'CPAR',# )
          'SEMICOL',# ;
          'OBRAK', # {
          'CBRAK',# }
          'OBRAC',# [
          'CBRAC',
          'PLUS',
          'MINUS',
          'TIMES',
          'DIVIDE',
          'EQUALTO',
          'MTHANE',
          'LTHANE',
          'NOTEQUAL',
          'MTHAN',
          'LTHAN',
          'COMA'


          #'QUOTE',# '
          #'DQUOTE', "
           ]


t_ignore = ' \t\n'

#simple
t_SEMICOL = r'\;'
t_EQUAL = r'\='
t_OBRAK = r'\{'
t_CBRAK = r'\}'
t_OBRAC = r'\['
t_CBRAC = r'\]'
t_OPAR = r'\('
t_CPAR = r'\)'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALTO = r'=='
t_MTHANE = r'>='
t_LTHANE = r'<='
t_NOTEQUAL = r'<>'
t_MTHAN = r'>'
t_LTHAN = r'<'
t_COMA = r'\,'

#t_QUOTE = r'\''
#t_DQUOTE = r'\"'



#res
t_PRINT = r'print'
t_EXIT = r'exit'
t_MAIN = r'main'
t_PROGRAM = r'program'
t_DO = r'do'
t_WHILE = r'while'
t_VAR = r'var'
t_INT = r'int'
t_FLOAT = r'float'
t_CHAR = r'char'
t_STRING = r'string'
t_BOOL = r'bool'
t_ARR = r'arr'
t_IF = r'if'
t_ELSE = r'else'
t_RETURN = r'return'
t_FUNCTION = r'function'



#complex
t_CCHAR = r'[\'][a-zA-Z][\']'
t_CSTRING = r'[\"][a-zA-Z ]*[\"]'
t_CINT = r'\d'
t_CFLOAT = r'(\d*[.])?\d+'
t_ID = r'[A-Z_][a-zA-Z0-9_]*'




def t_error (t):
    print('error en el lexico')
    quit()




#build the lexer
lex.lex()

#data = "program Thingprogram;  " \
#       "declarearr declarevar " \
#       "assarr assvar " \
#       "function " \
#       "function " \
#       "main { assvar assarr while do condition " \
#       "print ( 3 + 3 + 3 ) ;  " \
#       "do declarearr } exit"


#lex.input(data)

#while True:
#    tok = lex.token()
#    print (tok)
#    if not tok: break



