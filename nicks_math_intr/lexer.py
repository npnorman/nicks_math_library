#Lexer
#Nicholas Norman
#March 2024

import token as token

class Lexer():
    def __init__(self, equation):
        #take in string
        self._equation = equation
        self._tokens = []

        #convert when initialized
        self.convertEqToTokens()

    def __str__(self):
        return self._equation

    def getEquation(self):
        return self._equation
    
    def getTokens(self):
        #access to tokens
        return self._tokens
    
    def _convertEqToTokens(self):
        #convert to list of tokens

        #temp token
        tempToken = None

        #remove whitespace
        eq = self._equation
        eq = eq.strip()
        eq = eq.replace(' ', '')

        #go character by character
        for char in eq:
            if(char == 'x'):
            #if character is an x
                #create a variable token and append
                tempToken = token.Token(None, "VAR")
            else:
                tempToken = None

            self._tokens.append(tempToken)

        return self._tokens

    tokens = property(getTokens)
    equation = property(getEquation)

#testing
if __name__ == "__main__":
    lex = Lexer("5 + 3 * x - 4 / 3 + (5 + 4 )")
    print(lex)
    print("converting")
    print(lex.tokens)