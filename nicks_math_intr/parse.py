#Parser
#Nicholas Norman
#March 2024

import token
import lexer

class Parser():
    def __init__(self, tokens):
        #list of tokens
        self._tokens = tokens

        #binary tree setup
        self._binTree = None

if __name__ == "__main__":

    #set up equation
    lex = lexer.Lexer("3 + 5.7")
    print(lex.equation)
    for tok in lex.tokens:
        print(f"[{tok}]", end=", ")
    print("\n")

    #put into parser
    #print tree