#Nicks Dicts
#Nicholas Norman
#March 2024

import math

#Valid Operations
operations = {
    "+": "PLUS",
    "-": "SUB",
    "*": "MULT",
    "/": "DIV",
    "^": "POW",
    "(": "RPAR",
    ")": "LPAR"
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
    "arctanh": math.atanh
}

#Valid Symbols
symbols = {
    "e": math.e,
    "pi": math.pi
}