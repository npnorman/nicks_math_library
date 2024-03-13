#Lexer
#Nicholas Norman
#March 2024

import token as token
import parse

def eqToTokens(equation):
    #convert to list of tokens

    if(equation == ""):
        return None

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
                tempToken = _convertNumberToken(tempNum)
                tempNum = ""
                tokens.append(tempToken)

            #convert current char
            tempToken = _convertNonNumberToken(char)

            #append to list
            tokens.append(tempToken)

    if(tempNum != ""):
        #pass last number made
        tempToken = _convertNumberToken(tempNum)
        tempNum = ""
        tokens.append(tempToken)


    if (_validateTokens(tokens)):
        return tokens
    else:
        return None
    

def _convertNumberToken(str):

    tempToken = None
    num = float(str)
    tempToken = token.Token(num,"NUM")

    return tempToken

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

    elif(char == "^"):
        #if character is ^, POW
        tempToken = token.Token('^', "POW")

    else:
        tempToken = None
        print("unknown symbol",char)

    return tempToken

def _validateTokens(tokens):

    #if no tokens, fail
    if (len(tokens) == 0):
        return False
    
    parStack = []

    for tok in tokens:
        if(tok == None):
            return False

    for i in range(0, len(tokens)):
        if(parse.isOperator(tokens[i])):

            #cant be first or last
            if(i == 0 or i == len(tokens) - 1):
                return False

            if(parse.isNumOrVar(tokens[i+1]) == False):
                #must have number, "(" or "VAR" to right
                if(tokens[i+1].type != "LPAR"):
                    return False
            
            if(parse.isNumOrVar(tokens[i-1]) == False):
                #must have number, "(" or "VAR" to right
                if(tokens[i-1].type != "RPAR"):
                    return False
                
        elif(tokens[i].type == "LPAR"):
            #parenthesis check
            #if LPAR, push to stack
            parStack.append("LPAR")

        elif(tokens[i].type == "RPAR"):
            #if RPAR, pop stack (if stack is empty before pop, return false)
            if (len(parStack) == 0):
                print("mismatched parenthesis")
                return False
            else:
                parStack.pop()
    
    if (len(parStack) != 0):
        #if stack is not empty, mismatched parenthesis
        print("mismatched parenthesis")
        return False
    
    return True

#testing
if __name__ == "__main__":
    lex = "5 + 3.5 * x - 4 / 76 + (0.2 + 4) + 5.8"
    lex = "5 + 3.5 * (2 - 7) + 3^4"
    #lex = "5 + (3 - 3)"

    lex = "5+(3+4)"

    print(lex)
    tokens = eqToTokens(lex)
    
    if(tokens != None):
        for tok in tokens:
            print(f"[{tok}]", end=", ")
        print("\n")
    else:
        print("ERROR")