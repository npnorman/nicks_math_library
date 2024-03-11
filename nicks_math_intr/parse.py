#Parser
#Nicholas Norman
#March 2024

import token
import lexer

class Parser():
    def __init__(self):
        pass

    @staticmethod
    def _postfixToPrefix(tokes):
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
                while (Parser()._operatorCheck(operatorStack, tok) == True):
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
    def tokensToBinTree(tokens):

        #binTree to store everything

        return "tree"

if __name__ == "__main__":

    #set up equation
    lex = "3 + 5.7"
    tokens = lexer.Lexer().eqToTokens(lex)
    print(lex)
    for tok in tokens:
        print(f"[{tok}]", end=", ")
    print("\n")
    tokens2 = Parser()._infixToPostfix(tokens)
    for tok in tokens2:
        print(f"[{tok}]", end=", ")
    print("\n")

    #put into parser
    tree = Parser().tokensToBinTree(tokens)
    #print tree
    print(tree)