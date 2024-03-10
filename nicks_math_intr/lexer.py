#Lexer
#Nicholas Norman
#March 2024

import token as token

class Lexer():
    def __init__(self):
        pass
    
    @staticmethod
    def _convertEqToTokens(self, equation):
        #convert to list of tokens

        #temp token
        tempToken = None
        tempNum = ""
        tokens = []

        #remove whitespace
        eq = equation
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
                    tokens.append(tempToken)

                #convert current char
                tempToken = self._convertNonNumberToken(char)

                #append to list
                tokens.append(tempToken)

        if(tempNum != ""):
            #pass last number made
            tempToken = self._convertNumberToken(tempNum)
            tempNum = ""
            tokens.append(tempToken)

        return tokens

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

#testing
if __name__ == "__main__":
    lex = Lexer("5 + 3.5 * x - 4 / 76 + (0.2 + 4) + 5.8")
    print(lex)
    print("converting")
    
    for tok in lex.tokens:
        print(f"[{tok}]", end=", ")
    print("\n")