#Evaluator
#Nicholas Norman
#March 2024

#goal: evaluate this
#input << tree, some x to replace sym
#output >> number (float)

import os
import sys
import parse
import operationTree
import math

#get nicks handy functions
p_d = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(p_d)

import nicks_handy_funcs as nhf

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
        dict = {
            "PLUS": nhf.plus,
            "SUB": nhf.minus,
            "MULT": nhf.mult,
            "DIV": nhf.div,
            "POW": nhf.pow
            }
        
        func = dict.get(node.token.type)

        #get numbers for function
        Num1 = evaluateOpTree(node.left, x)
        Num2 = evaluateOpTree(node.right,x)
        
        #return Num1 func Num2
        res = func(Num1, Num2)
        return res
    
    print("unaccounted for")
    return None

if __name__ == "__main__":
    #test
    #set up equation
    lex = "5 + 3.5 * x - 4 / 76 + (0.2 + 4) + 5.8"
    lex = "2^x"

    #put into parser
    tree = parse.tokensToBinTree(lex)
    print(lex)
    #evaluate tree
    for x in range(-2, 2+1):
        print(f"Eval at {x}: {evaluateOpTree(tree.root, x)}")
    