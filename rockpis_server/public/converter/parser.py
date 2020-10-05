import lexer
from sly import Parser

class PdParser(Parser):
    # Get the token list from the lexer (required)
    tokens = lexer.PdLexer.tokens

    # Grammar rules and actions
    @_('CPREFIX CANVAS FLOAT FLOAT FLOAT FLOAT FLOAT END')
    def expr(self, p):
        return {"type": p[1], "x": int(p[4]), "y": int(p[5])}
    
    @_('PREFIX corpus END')
    def expr(self, p):
        return p.corpus 

    @_('OBJ FLOAT FLOAT object_data')
    def corpus(self, p):
        return { "type": p[0], "x": int(p[1]), "y": int(p[2]), "data": p[3].replace('\\','') }   

    @_('LITERAL')
    def object_data(self, p):
        return p.LITERAL 

    """@_('TEXT LITERAL')
    def object_data(self, p):
        return " ".join([p.TEXT, p.LITERAL]).replace('\\','') """

    @_('CONNECT FLOAT FLOAT FLOAT FLOAT')
    def corpus(self, p):
        return {"type": p[0], "_from": int(p[1]), "outlet": int(p[2]), "_to": int(p[3]), "inlet": int(p[4]) }

    @_('MSG FLOAT FLOAT LITERAL')
    def corpus(self, p):
        return {"type": p[0], "x": int(p[1]), "y": int(p[2]), "message": p[3].replace('\n',' ').replace('\\','')}

    """@_('TEXT FLOAT FLOAT LITERAL')
    def corpus(self, p):
        return {"type": p[0], "x": int(p[1]), "y": int(p[2]), "message": p[3].replace('\n',' ')}"""