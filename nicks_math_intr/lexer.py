#Lexer
#Nicholas Norman
#March 2024

class Lexer():
    def __init__(self, equation):
        #take in string
        self.equation = equation
        self.tokens = []

    def __str__(self):
        return self.equation

    def getEquation(self):
        return self.equation
    
    def getTokens(self):
        #access to tokens
        return self.tokens
    
    def convertEqToTokens(self):
        #convert to list of tokens
        pass

#testing
if __name__ == "__main__":
    lex = Lexer("5 + 3")
    print(lex.getEquation())