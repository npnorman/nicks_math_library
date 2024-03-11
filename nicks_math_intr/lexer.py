#Lexer
#Nicholas Norman
#March 2024

import token as token

class Lexer():
    def __init__(self):
        pass
    
    @staticmethod
    def _infixToPostfix(tokens):
        #use shunting yard algorithm  **p.s. thanks edwin
        #pulled from wikipedia
        #tokens are of type Token()

        print("changing order")
        #output & stack
        output = []
        operatorStack = []

        #while there are tokens to be read:
        for tok in tokens:
            if (tok.type == "NUM" or tok.type == "VAR"):
                #if a number, put in output queue
                output.append(tok)

            elif(tok.type == "FUNC"):
                #if it is a function (NOT IMPLEMENTED)
                #push to operator stack
                pass

            elif (tok.type == "LPAR"):
                #left parenthesis
                #push it to operator stack
                operatorStack.append(tok)

            elif (tok.type == "RPAR"):
                #right parenthesis
                #while operator at top of stack is NOT a left parentheses
                while (operatorStack[-1].type != "LPAR"):
                    #make sure stack isnt empty
                    if (len(operatorStack) == 0):
                        print("Mismatched ( or )")
                    else:
                        #pop the operator from stack into output queue
                        output.append(operatorStack.pop())
                
                #make sure there is left parenthesis at top
                if (operatorStack[-1].type == "LPAR"):
                    operatorStack.pop()
                
                #if there is a function operator at the top
                if (len(operatorStack) != 0):
                    if (operatorStack[-1].type == "FUNC"):
                        #pop it and put to output queue
                        output.append(operatorStack.pop())
            
            else:
                #operator
                while (Lexer()._operatorCheck(operatorStack, tok) == True):
                    #pop stack operator to output
                    output.append(operatorStack.pop())
                operatorStack.append(tok)
        
        #after loop
        while (len(operatorStack) != 0):
            #if operator is ( or ), mismatched
            if (operatorStack[-1] == "(" or operatorStack[-1] == "-1"):
                print("mismatched ( or )")
            else:
                output.append(operatorStack.pop())

        return output

    @staticmethod
    def _operatorCheck(operatorStack, tok):
        #check for operator in while loop

        #precedence
        precedence = {"PLUS": 2, "SUB": 2, "MULT": 3, "DIV": 3, "EXP": 4}
        
        output = False
        #if operator stack is not empty
        if (len(operatorStack) != 0):
            #if not a left parenthesis
            if (operatorStack[-1].type != "LPAR"):
                #if operator on stack has greater or equal precedence
                if(precedence[operatorStack[-1].type] >= precedence[tok.type]):
                    output = True
        
        return output

    @staticmethod
    def eqToTokens(equation):
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
                    tempToken = Lexer()._convertNumberToken(tempNum)
                    tempNum = ""
                    tokens.append(tempToken)

                #convert current char
                tempToken = Lexer()._convertNonNumberToken(char)

                #append to list
                tokens.append(tempToken)

        if(tempNum != ""):
            #pass last number made
            tempToken = Lexer()._convertNumberToken(tempNum)
            tempNum = ""
            tokens.append(tempToken)


        #convert to postfix
        return Lexer()._infixToPostfix(tokens)

    @staticmethod
    def _convertNumberToken(str):

        tempToken = None
        num = float(str)
        tempToken = token.Token(num,"NUM")

        return tempToken

    @staticmethod
    def _convertNonNumberToken(char):
        
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
    lex = "5 + 3.5 * x - 4 / 76 + (0.2 + 4) + 5.8"
    lex = "5 + 3.5 * (2 - 7)"
    #lex = "5 + (3 - 3)"
    print(lex)
    print("converting")
    tokens = Lexer.eqToTokens(lex)
    for tok in tokens:
        print(f"[{tok}]", end=", ")
    print("\n")