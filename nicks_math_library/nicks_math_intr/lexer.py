#Lexer
#Nicholas Norman
#March 2024

import token as token

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


    #convert to postfix
    return tokens

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
    tokens = eqToTokens(lex)
    for tok in tokens:
        print(f"[{tok}]", end=", ")
    print("\n")