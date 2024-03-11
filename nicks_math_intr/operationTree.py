#Binary Tree
#Nicholas Norman
#March 2024

import token

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
    
    def setLeft(self, node):
        self._left = node

    def setRight(self, node):
        self._right = node

    token = property(getToken, setToken)
    left = property(getLeft, setLeft)
    right = property(getRight, setRight)
    
class OperationTree():
    def __init__(self, node):
        self._root = node

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