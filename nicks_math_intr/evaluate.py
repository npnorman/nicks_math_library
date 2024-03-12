#Evaluator
#Nicholas Norman
#March 2024

#goal: evaluate this
#input << tree, some x to replace sym
#output >> number (float)

import token
import lexer
import parse
import operationTree

def evaluateOpTree(node:operationTree.node):
    
    #start at root
    #figure out what kind of node this is
    #if operator
    if(parse.Parser().isOperator(node.token)):
        #figure out which
        #use nicks handy functions
        dict = {}
    
    return 0