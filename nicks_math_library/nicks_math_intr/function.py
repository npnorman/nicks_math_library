#function
#Nicholas Norman
#March 2024

#goal is to wrap everything together and create a custom function
#input: function as a string
#output: a function that you acn evaluate

import parse
from operationTree import OperationTree
import evaluate

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
    

    #get input of equation
    print("Welcome to Nick's Math Library")
    print("Current Operators accepted are [+, -, *, /]")
    print("To use a variable, please type 'x'")
    print("f(x) = ", end="")

    equation = input()
    f = N_function(equation)

    keepGoing = True
    while(keepGoing):
        #ask for x
        print("x = ", end="")
        x = input()
        
        try:
            x = float(x)
        except:
            print("x not valid, defaulting to 1")
            x = 1


        #print equation and x
        print(f.equation)
        print(f"f({x}) = {f(x)}")

        #ask to exit
        exitCheck = input("to exit enter exit()\n")
        if (exitCheck == "exit()"):
            keepGoing = False