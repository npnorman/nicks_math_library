#Lexer
#Nicholas Norman
#March 2024

class Lexer():
    def __init__(self, equation):
        #take in string
        self._equation = equation
        self._tokens = []

    def __str__(self):
        return self._equation

    def getEquation(self):
        return self._equation
    
    def getTokens(self):
        #access to tokens
        return self._tokens
    
    def convertEqToTokens(self):
        #convert to list of tokens
        pass

    tokens = property(getTokens)
    equation = property(getEquation)

#testing
if __name__ == "__main__":
    lex = Lexer("5 + 3")
    print(lex.getEquation())
    print(lex)