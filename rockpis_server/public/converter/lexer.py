from sly import Lexer

class PdLexer(Lexer):
    def __init__(self):
        self.obj_counter = 0
    
    # Set of token names.   This is always required
    tokens = { CPREFIX, PREFIX, CANVAS, LITERAL, OBJ, CONNECT, DECLARE, FLOATATOM, MSG, FLOAT, END }

    # String containing ignored characters between tokens
    ignore = ' \t'
    ignore_newline = r'\s*\n\s*'
    ignore_prefix = r'#A.+'
    ignore_text = r'#X text.+'
    #ignore_semi = r';'

    # Regular expression rules for tokens
    
    CPREFIX = r'#N'
    PREFIX = r'#X'
    CANVAS = r'canvas'
    OBJ = r'obj'
    #TEXT = r'text'
    CONNECT = r'connect'
    DECLARE = r'declare'
    FLOATATOM = r'floatatom'
    MSG = r'msg'
    FLOAT = r'\d+\.*\d*'
    LITERAL = r'[ a-zA-Z_*~\(\)\.\-\+0-9\nèùàéò%\\\$=,/\':#\\]+'

    @_(r';')
    def END(self, t):
        self.lineno += len(t.value)
        return t

    #LITERAL = r'[ ;a-zA-Z_*~\(\)\.\-\+0-9\nèùàéò%\\\$=,/\':#\\]+'

    # Error handling rule
    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1