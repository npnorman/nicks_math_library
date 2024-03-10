#Parser
#Nicholas Norman
#March 2024

import token
import lexer

class Parser():
    def __init__(self):
        pass

    @staticmethod
    def tokensToBinTree(tokens):
        return "tree"

if __name__ == "__main__":

    #set up equation
    lex = "3 + 5.7"
    tokens = lexer.Lexer().eqToTokens(lex)
    print(lex)
    for tok in tokens:
        print(f"[{tok}]", end=", ")
    print("\n")

    #put into parser
    tree = Parser().tokensToBinTree(tokens)
    #print tree
    print(tree)