#Parser
#Nicholas Norman
#March 2024

import token as token
import lexer as lexer
import operationTree as operationTree
import nicks_dicts as nicks_dicts

def _postfixToPrefix(tokens):
    #from geeks4geeks

    if(tokens == None):
        return None

    stack = []

    #for all tokens in tokens
    for tok in tokens:
        #if token is operand put on stack
        if(tok.type == "NUM" or tok.type == "VAR"):
            stack.append([tok])
        elif(tok.type == "FUNC"):
            #type is function
            op1 = stack.pop()
            #pop 1 operator and combine
            tempExpr = [tok] + op1
            stack.append(tempExpr)
        else:
            #if symbol is operator, pop two operands from stack
            op1 = stack.pop()
            op2 = stack.pop()

            #combine two lists
            tempExpr = [tok] + op2 + op1
            
            #should look like this: operator, operand2, operand1
            #push these to stack
            stack.append(tempExpr)
    
    return stack[0]

def _infixToPostfix(tokens):
    #use shunting yard algorithm  **p.s. thanks edwin
    #pulled from wikipedia
    #tokens are of type Token()

    if(tokens == None):
        return None
    
    #output & stack
    output = []
    operatorStack = []

    #while there are tokens to be read:
    for tok in tokens:
        if (tok.type == "NUM" or tok.type == "VAR"):
            #if a number, put in output queue
            output.append(tok)

        elif(tok.type == "FUNC"):
            #if it is a function
            #push to operator stack
            operatorStack.append(tok)

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
            while (_operatorCheck(operatorStack, tok) == True):
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

def _operatorCheck(operatorStack, tok):
    #check for operator in while loop

    #precedence
    precedence = {"PLUS": 2, "SUB": 2, "MULT": 3, "DIV": 3, "POW": 4, "FUNC": 5}
    
    output = False
    #if operator stack is not empty
    if (len(operatorStack) != 0):
        #if not a left parenthesis
        if (operatorStack[-1].type != "LPAR"):
            #if operator on stack has greater or equal precedence
            if(precedence[operatorStack[-1].type] >= precedence[tok.type]):
                output = True
    
    return output

def tokensToBinTree(eqn):

    #binTree to store everything
    
    #convert tokens to prefix to make it easier
    tokens = lexer.eqToTokens(eqn)

    #if return None
    if(tokens == None):
        #not a correct list, print error and try again
        print(f"UNKNOWN TOKEN ERROR: Lexer could not tokenize {eqn}")
        return None

    postTokens = _infixToPostfix(tokens)
    preTokens = _postfixToPrefix(postTokens)
    #create the tree
    tr = operationTree.OperationTree()
    tr.buildTreeFromPrefix(preTokens)

    #implement eqn store in tree

    return tr

def isNumOrVar(token):
    if(token.type == "NUM"):
        return True
    elif(token.type == "VAR"):
        return True
    else:
        #not a number or var
        return False

def isOperator(token):
    res = False
    operators = nicks_dicts.operations
    
    if(operators.get(token.value) == None):
        #not an operator
        res = False
    else:
        #is an operator
        res = True

    return res


if __name__ == "__main__":

    #set up equation
    lex = "5 + 3.5 * x - 4 / 76 + (0.2 + 4) + 5.8"
    lex = "5+(sin(x))^2"

    tokens = lexer.eqToTokens(lex)
    for t in tokens:
        print(f"infix: {t}")
    postTokens = _infixToPostfix(tokens)
    print("")
    for t in postTokens:
        print(f"postfix: {t}")
    preTokens = _postfixToPrefix(postTokens)
    print("")
    for t in preTokens:
        print(f"prefix: {t}")

    print("")

    tree = tokensToBinTree(lex)
    tree.printTree(tree.root)