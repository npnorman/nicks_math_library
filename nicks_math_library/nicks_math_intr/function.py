#function
#Nicholas Norman
#March 2024

#goal is to wrap everything together and create a custom function
#input: function as a string
#output: a function that you acn evaluate

import parse as parse
from operationTree import OperationTree
import evaluate as evaluate
import nicks_dicts as nd

#function object
class N_function():
    def __init__(self, equation=None):
        self.operationTree:OperationTree = None
        self._equation = ""

        #if equation is not None, then make a tree
        if(equation != None):
            self._equation = equation
            self._buildTree()

    def __str__(self):
        return self._getEqn()
    
    def __call__(self, x):
        #evaluate tree
        return self.evaluate(x)

    def _getEqn(self):
        return f"f(x) = {self._equation}"
    
    def _setEqn(self, eqn:str):
        #delete old tree get new one
        self._equation = eqn
        self._buildTree()

    def evaluate(self, x:float):
        #evaluates function
        if(self.operationTree != None):
            return evaluate.evaluateOpTree(self.operationTree.root, x)
        else:
            print("ERROR: Cannot find tree")
            return None


    def _buildTree(self):
        self.operationTree = parse.tokensToBinTree(self._equation)

    equation = property(_getEqn, _setEqn)

if __name__ == "__main__":
    
    #function
    newFunc = None

    #get input of equation
    print("Welcome to Nick's Math Library")

    keepGoing = True
    while(keepGoing):
        #main loop
        cli = input("N_M_L > ")

        if (cli == "e()"):
            #exit
            keepGoing = False
        elif(cli == "new func"):
            
            eqn = input("f(x) = ")

            try:
                newFunc = N_function(eqn)
            except:
                print("invalid function")
        elif(cli == "eval"):
            
            #evaluate at x
            try:
                xCLI = input("x = ")
                x = eval(xCLI)
                print(f"{newFunc.equation}")
                print(f"f({x}) = {newFunc.evaluate(x)}")
            except Exception as error:
                print("Error:", error)
        elif(cli == "help"):
            #help command
            #print how to use
            print("To create a function type 'new func'")
            print("To evaluate a function type 'eval'")
            print("to view known operations type 'help -o'")
            print("to view known functions type 'help -f'")
            print("to view known symbols type 'help -s'")
            pass
        elif(cli == "help -o"):
            #print known operations
            print("Valid Operations")
            for key in nd.operations:
                print(f"{key}", end=" ")
            print("")
        elif(cli == "help -s"):
            #print known symbols
            print("Valid Symbols")
            for key in nd.symbols:
                print(f"{key}", end=" ")
            print("")
            pass
        elif(cli == "help -f"):
            #print known functions
            print("Valid functions")
            for key in nd.functions:
                print(f"{key}", end=" ")
            print("")
            pass
        else:
            print("unknown command")
            print("for help type 'help'")
            print("to exit type 'e()'")
