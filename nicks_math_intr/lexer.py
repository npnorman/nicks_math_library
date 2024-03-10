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
        self._convertEqToTokens()

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
        tempNum = ""

        #remove whitespace
        eq = self._equation
        eq = eq.strip()
        eq = eq.replace(' ', '')

        #go character by character
        for char in eq:

            #conversion
            if(char.isdigit() or char == "."):
                tempNum += char
            else:
                if(tempNum != ""):
                    #pass last number made
                    tempToken = self._convertNumberToken(tempNum)
                    tempNum = ""
                    self._tokens.append(tempToken)

                #convert current char
                tempToken = self._convertNonNumberToken(char)

                #append to list
                self._tokens.append(tempToken)

        if(tempNum != ""):
            #pass last number made
            tempToken = self._convertNumberToken(tempNum)
            tempNum = ""
            self._tokens.append(tempToken)

    def _convertNumberToken(self, str):

        tempToken = None
        num = float(str)
        tempToken = token.Token(num,"NUM")

        return tempToken

    def _convertNonNumberToken(self, char):
        
        tempToken = None
        
        #create a variable token and append
        if(char == 'x'):
            #if character is an x
            tempToken = token.Token('sym', "VAR")

        elif(char == "+"):
            #if character is +, plus
            tempToken = token.Token('+', "PLUS")

        elif(char == "-"):
            #if character is -, sub
            tempToken = token.Token('-', "SUB")
        
        elif(char == "*"):
            #if character is -, sub
            tempToken = token.Token('*', "MULT")
        
        elif(char == "/"):
            #if character is -, sub
            tempToken = token.Token('/', "DIV")

        elif(char == "("):
            #if character is -, sub
            tempToken = token.Token('(', "LPAR")
        
        elif(char == ")"):
            #if character is -, sub
            tempToken = token.Token(')', "RPAR")

        else:
            tempToken = None
            print("unknown symbol",char)

        return tempToken

    tokens = property(getTokens)
    equation = property(getEquation)

#testing
if __name__ == "__main__":
    lex = Lexer("5 + 3.5 * x - 4 / 76 + (0.2 + 4) + 5.8")
    print(lex)
    print("converting")
    
    for tok in lex.tokens:
        print(f"[{tok}]", end=", ")
    print("\n")