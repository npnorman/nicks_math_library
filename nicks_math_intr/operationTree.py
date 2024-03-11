#Binary Tree
#Nicholas Norman
#March 2024

import token
import parse

class Node():
    def __init__(self, token):
        self._token = token #class token
        self._left = None
        self._right = None
    
    def __str__(self):
        return (self.token.__str__())
    
    def getToken(self):
        return self._token
    
    def setToken(self, token):
        self._token = token

    def getLeft(self):
        return self._left
    
    def getRight(self):
        return self._right
    
    def setLeft(self, token):
        self._left = Node(token)

    def setRight(self, token):
        self._right = Node(token)

    token = property(getToken, setToken)
    left = property(getLeft, setLeft)
    right = property(getRight, setRight)
    
class OperationTree():
    def __init__(self):
        self._root = None

    def buildTreeFromPrefix(tokens):
        pass

    def lowestOperatorOpen(self, node):
        print(f"entered with node: [{node}]")

        if(node == None):
            return [False, None]
            #no node exists
        elif(node.left == None):
            #base case
            return [True, node]
        elif(node.right == None):
            #base case
            return [True, node]
        elif(parse.Parser().isNumOrVar(node.left.token) and parse.Parser().isNumOrVar(node.right.token)):
            #if both equal nums, dead end
            return [False, None]
        else:
            #right or left is an operator
            lCheck = [False, None]
            rCheck = [False, None]
            #check which
            if(node.left.token.type != "NUM" and node.left.token.type != "VAR"):
                #fo sho an operator
                lCheck = self.lowestOperatorOpen(node.left)
            #note: parallel ifs
            if(node.right.token.type != "NUM" and node.right.token.type != "VAR"):
                #fo sho an operator
                rCheck = self.lowestOperatorOpen(node.right)

            if(lCheck[0] == False and rCheck[0] == False):
                print("this wasnt supposed to happen")
                return [False, None]
            elif(lCheck[0] == True):
                #moving node from lCheck up
                return [True, lCheck[1]]
            elif(rCheck[0] == True):
                #moving node from rCheck up
                return [True, rCheck[1]]
        
    def getRoot(self):
        return self._root
    
    def setRoot(self, token):
        if(self._root == None):
            self._root = Node(token)

    root = property(getRoot, setRoot)


    #insert new stuff

if __name__ == "__main__":
    print("testing")
    node = Node(token.Token('+', "PLUS"))
    tk1 = token.Token(5.0, "NUM")
    tk2 = token.Token(3.0, "NUM")
    node.right = Node(tk1)
    node.left = Node(tk2)

    # 5 + 3
    print(node)
    print(node.right)
    print(node.left)

    # (5 + 3) * 2
    tk3 = token.Token('*', "MULT")
    tk4 = token.Token(2.0, "NUM")
    n1 = Node(tk3)
    n1.right = Node(tk4)
    print(" ")
    print(n1)
    print(n1.right)
    n1.left = node
    print(n1.left)
    print(n1.left.left)
    print(n1.left.right)

    print("\nTREE TESTING")
    tk = [token.Token('+', "PLUS"), token.Token("-", "SUB"),token.Token(7, "NUM")]
    opTr = OperationTree()
    opTr.root = tk[0]
    opTr.root.left = tk[1]
    opTr.root.right = tk[2]

    print(f"Root: {opTr.root}\n")
    result = opTr.lowestOperatorOpen(opTr.root)
    print("LowOpenOper:",result[0],":", result[1])
    