#Lexer
#Nicholas Norman
#March 2024

import token as token
import parse as parse
import math
import nicks_dicts as nd

def eqToTokens(equation):
    #convert to list of tokens

    if(equation == ""):
        return None

    #temp token
    tempToken = None
    tempNum = ""
    tempStr = ""
    tokens = []

    #store lecation of char
    charIndex = 0

    #remove whitespace
    eq = equation
    eq = eq.strip()
    eq = eq.replace(' ', '')

    #go character by character
    for char in eq:

        #conversion
        if(_isNumber(char) or _isNegative(char, eq, charIndex)): #remove isNegative and replace with negativeCheck
            tempNum += char
        
        elif(char.isalpha()):
        #if is text (x, e, pi, functionName)
            if(char == "x"):
                tokens.append(token.Token('sym', "VAR"))
            else:
                #not a variable
                #do tempString
                tempStr += char

        else:
            if(tempNum != ""):
                #if tempNum is made of numbers
                #pass last number made
                tempToken = _convertNumberToken(tempNum)
                tempNum = ""
                tokens.append(tempToken)
            #else if tempStr in not empty
            elif(tempStr != ""):
                #convert to math symbol or function
                tempToken = _convertSymbolToken(tempStr)
                tempStr = ""
                tokens.append(tempToken)

            #convert current char
            tempToken = _convertOperatorToken(char)

            #append to list
            tokens.append(tempToken)

        charIndex += 1

    if(tempNum != ""):
        #pass last number made
        tempToken = _convertNumberToken(tempNum)
        tempNum = ""
        tokens.append(tempToken)
    elif(tempStr != ""):
        #pass last math symbol or function
        tempToken = _convertSymbolToken(tempStr)
        tempStr = ""
        tokens.append(tempToken)


    if (_validateTokens(tokens)):
        return tokens
    else:
        return None
    

def _isNumber(char):
    if(char.isdigit() or char == "."):
        return True

def _isNegative(char, eqn, i):
    #three cases
    if (char == "-"):
        if(i != len(eqn)):
            #not last one

            if(_isNumber(eqn[i+1])):
                #right of negative is number
                # -
                if (i == 0):
                    #first sign
                    return True
                #+-
                elif (_isOperator(eqn[i-1])):
                    return True
                #(-
                elif (eqn[i-1] == "("):
                    return True
            elif(eqn[i+1] == "x"):
                print("found x")

    return False

def _convertNumberToken(str):

    tempToken = None
    num = float(str)
    tempToken = token.Token(num,"NUM")

    return tempToken

def _convertSymbolToken(str):
    
    #match to dictionary
    knownSymbols = nd.symbols

    knownFuncs = nd.functions

    if(knownSymbols.get(str) != None):
        #symbol exists in the dictionary
        return token.Token(knownSymbols.get(str), "NUM")
    elif(knownFuncs.get(str) != None):
        #if exists in the dictionary return the token
        return token.Token(knownFuncs.get(str), "FUNC")

    print(f"unknown symbol {str}")
    return None

def _convertOperatorToken(char):
    
    tempToken = None

    if(nd.operations.get(char) != None):
        tempToken = token.Token(char, nd.operations.get(char))

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

def _validateTokens(tokens):

    #if no tokens, fail
    if (len(tokens) == 0):
        print(-3)
        return False
    
    parStack = []

    for tok in tokens:
        if(tok == None):
            print(-2)
            return False

    for i in range(0, len(tokens)):
        if(parse.isOperator(tokens[i])):

            #cant be first or last
            if(i == 0 or i == len(tokens) - 1):
                print(-1)
                return False

            if(parse.isNumOrVar(tokens[i+1]) == False):
                #if not a function as well
                #must have number, "(" or "VAR" to right
                if(tokens[i+1].type != "LPAR" and tokens[i+1].type != "FUNC"):
                    print(0)
                    return False
            
            if(parse.isNumOrVar(tokens[i-1]) == False):
                #must have number, ")" or "VAR" to left
                if(tokens[i-1].type != "RPAR"):
                    print(1)
                    return False
                
        elif(tokens[i].type == "LPAR"):
            #parenthesis check
            #if LPAR, push to stack
            parStack.append("LPAR")

            if(i != 0):
                if (parse.isOperator(tokens[i-1]) == False and tokens[i-1].type != "FUNC" and tokens[i-1].type != "LPAR"):
                    print(2)
                    #must be operator or function to left of LPAR ( or other parenthesis
                    return False
                    
                if (parse.isNumOrVar(tokens[i+1]) == False and tokens[i+1].type != "FUNC" and tokens[i+1].type != "LPAR"):
                    #right of LPAR (_ must me number, function, or left parenthesis
                    print(3)
                    return False

        elif(tokens[i].type == "RPAR"):
            #if RPAR, pop stack (if stack is empty before pop, return false)
            if (len(parStack) == 0):
                print("mismatched parenthesis")
                return False
            else:
                parStack.pop()

            if(i != len(tokens)-1):
                if (parse.isOperator(tokens[i+1]) == False and tokens[i+1].type != "RPAR"):
                    #must be operator to right of )
                    print(4)
                    return False
                if (parse.isNumOrVar(tokens[i-1]) == False and tokens[i-1].type != "RPAR"):
                    #must be number or ) to left of )
                    print(5)
                    return False
    
    if (len(parStack) != 0):
        #if stack is not empty, mismatched parenthesis
        print("mismatched parenthesis")
        return False
    
    return True

def _isOperator(char):
    operators = ['+','-','*','/','^']
    if (char in operators):
        return True
    
    return False

#testing
if __name__ == "__main__":
    lex = "5 + 3.5 * x - 4 / 76 + (0.2 + 4) + 5.8"
    lex = "5 + 3.5 * (2 - 7) + 3^4"
    #lex = "5 + (3 - 3)"

    lex = "7*3+4*x+(ln(x)+6)"

    print(lex)
    tokens = eqToTokens(lex)
    
    if(tokens != None):
        for tok in tokens:
            print(f"[{tok}]", end=", ")
        print("\n")
    else:
        print("ERROR")