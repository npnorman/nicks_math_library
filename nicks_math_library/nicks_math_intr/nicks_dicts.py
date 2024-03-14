#Nicks Dicts
#Nicholas Norman
#March 2024

import os
import sys
import math

#get nicks handy functions
p_d = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(p_d)

import nicks_handy_funcs as nhf

#Valid Operations
operations = {
    '+': "PLUS",
    '-': "SUB",
    '*': "MULT",
    '/': "DIV",
    '^': "POW"
}

#operators linked to functions
operationFunctions = {
    "PLUS": nhf.plus,
    "SUB": nhf.minus,
    "MULT": nhf.mult,
    "DIV": nhf.div,
    "POW": nhf.pow,
}

#Valid Functions
functions = {
    "abs": abs,
    "factorial": math.factorial,
    "sqrt": math.sqrt,
    "log10": math.log10,
    "ln": math.log,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "arcsin": math.asin,
    "arccos": math.acos,
    "arctan": math.atan,
    "sinh": math.sinh,
    "cosh": math.cosh,
    "tanh": math.tanh,
    "arcsinh": math.asinh,
    "arccosh": math.acosh,
    "arctanh": math.atanh,
}

#Valid Symbols
symbols = {
    "e": math.e,
    "pi": math.pi
}