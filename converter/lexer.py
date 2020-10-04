from sly import Lexer

class PdLexer(Lexer):
    def __init__(self):
        self.obj_counter = 0
    
    # Set of token names.   This is always required
    tokens = { CANVAS, OBJ, TEXT, CONNECT, DECLARE, FLOATATOM, MSG, FLOAT, LITERAL, END }

    # String containing ignored characters between tokens
    ignore = ' \t'
    ignore_newline = r'\s*\n\s*'
    ignore_prefix = r'#[A-Z] '

    # Regular expression rules for tokens
    
    CANVAS = r'#N canvas'
    OBJ = r'#X obj'
    TEXT = r'#X text'
    CONNECT = r'#X connect'
    DECLARE = r'#X declare'
    FLOATATOM = r'#X floatatom'
    MSG = r'#X msg'
    FLOAT = r'\d+\.*\d*'
    LITERAL = r'[ a-zA-Z_*~\(\)\.\-\+0-9\nèùàéò%\\\$=,]+'
    
    @_(r';')
    def END(self, t):
        self.lineno += len(t.value)
        return t