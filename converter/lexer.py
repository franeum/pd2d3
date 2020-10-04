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
    
    CANVAS = r'canvas'
    OBJ = r'obj'
    TEXT = r'text'
    CONNECT = r'connect'
    DECLARE = r'declare'
    FLOATATOM = r'floatatom'
    MSG = r'msg'
    FLOAT = r'\d+\.*\d*'
    LITERAL = r'[ a-zA-Z_*~\(\)\.\-\+0-9\nèùàéò%\\\$=,]+'
    
    @_(r';')
    def END(self, t):
        self.lineno += len(t.value)
        return t