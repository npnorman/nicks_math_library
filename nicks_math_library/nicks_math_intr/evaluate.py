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

#get nicks handy functions
p_d = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(p_d)

import nicks_handy_funcs as nhf

def evaluateOpTree(node:operationTree.Node):
    
    #start at root
    #figure out what kind of node this is
    #if operator
    if(parse.Parser().isOperator(node.token)):
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
    
    return 0