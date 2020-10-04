import lexer
from sly import Parser

class PdParser(Parser):
    # Get the token list from the lexer (required)
    tokens = lexer.PdLexer.tokens

    # Grammar rules and actions
    @_('CANVAS FLOAT FLOAT FLOAT FLOAT FLOAT END')
    def expr(self, p):
        return {"type": p[0], "x": int(p[1]), "y": int(p[2])}
    
    @_('OBJ FLOAT FLOAT LITERAL END')
    def expr(self, p):
        return {"type": p[0], "x": int(p[1]), "y": int(p[2]), "data": p[3].replace('\\$','$')} 
    
    @_('CONNECT FLOAT FLOAT FLOAT FLOAT END')
    def expr(self, p):
        return {"type": p[0], "_from": int(p[1]), "outlet": int(p[2]), "_to": int(p[3]), "inlet": int(p[4])}
    
    @_('MSG FLOAT FLOAT LITERAL END')
    def expr(self, p):
        return {"type": p[0], "x": int(p[1]), "y": int(p[2]), "message": p[3].replace('\n',' ')}
    
    
    @_('TEXT FLOAT FLOAT LITERAL END')
    def expr(self, p):
        return {"type": p[0], "x": int(p[1]), "y": int(p[2]), "message": p[3].replace('\n',' ')}