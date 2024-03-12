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
        return evaluate.evaluateOpTree(self.operationTree.root, x)


    def _buildTree(self):
        self.operationTree = parse.tokensToBinTree(self._equation)

    equation = property(_getEqn, _setEqn)

if __name__ == "__main__":
    
    #get input of equation
    pass