#Evaluator
#Nicholas Norman
#March 2024

#goal: evaluate this
#input << tree, some x to replace sym
#output >> number (float)

import parse as parse
import operationTree as operationTree
import nicks_dicts as nd

def evaluateOpTree(node:operationTree.Node, x:float):
    
    #store L / R numbers
    Num1 = None
    Num2 = None

    #start at root
    #figure out what kind of node this is
    
    if(node.token.type == "NUM"):
        #number
        return node.token.value
    
    elif(node.token.type == "VAR"):
        #variable (assume for now only one variable)
        return x

    elif(parse.isOperator(node.token)):
        #if operator
        #figure out which
        #use nicks handy functions
        dict = nd.operationFunctions
        
        func = dict.get(node.token.type)

        #get numbers for function
        num1 = evaluateOpTree(node.left, x)
        num2 = evaluateOpTree(node.right,x)
        
        #return Num1 func Num2
        res = func(num1, num2)
        return res
    
    elif (node.token.type == "FUNC"):
        #evaluating a function

        #we know a function only has a left
        #and it holds the function in its own token type
        func = node.token.value

        #get numbers for the function
        num3 = evaluateOpTree(node.left, x)

        #return the function
        res = func(num3)
        return res
        
    
    print("unaccounted for")
    return None

if __name__ == "__main__":
    #test
    #set up equation
    lex = "5 + 3.5 * x - 4 / 76 + (0.2 + 4) + 5.8"
    lex = "sin(pi/2) + x"

    #put into parser
    tree = parse.tokensToBinTree(lex)
    print(lex)
    #evaluate tree
    for x in range(-2, 2+1):
        print(f"Eval at {x}: {evaluateOpTree(tree.root, x)}")
    