#Binary Tree
#Nicholas Norman
#March 2024

import token
import lexer
import parse

class Node():
    def __init__(self, token):
        self._token = token #class token
        self._left = None
        self._right = None
    
    def __str__(self):
        return f"[{self.token.__str__()}]: NODE"
    
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

    def lowestOperatorOpen(self, node):

        if(node == None):
            return [False, None]
            #no node exists
        
        if(node.left == None):
            #base case
            return [True, node]
        elif(parse.isOperator(node.left.token)):
            #go deeper
            res = None
            res = self.lowestOperatorOpen(node.left)
            if (res[0] == True):
                return res
            #else check right subtree

        if(node.right == None):
            #base case
            return [True, node]
        elif(parse.isOperator(node.right.token)):
            #go deeper
            res = None
            res = self.lowestOperatorOpen(node.right)

            if (res[0] == True):
                return res
            #else check dead end

        if(parse.isNumOrVar(node.left.token) and parse.isNumOrVar(node.right.token)):
            #dead end
            return [False, None]
        
        #did not find an open operator // dead subtree
        return [False, None]
        
    def getRoot(self):
        return self._root
    
    def setRoot(self, token):
        if(self._root == None):
            self._root = Node(token)

    def setNodeBranch(self, ln, tok):
        if (ln.left == None):
            #if open set left
            ln.left = tok
        elif (ln.right == None):
            #if open set right
            ln.right = tok
        else:
            #filled up/dead end
            print(f"dead end with : {tok}")
            #self.setNodeBranch(ln, tok)

    def buildTreeFromPrefix(self, tokens):
        
        ln = None
        
        #for every token
        for tok in tokens:
            if (self._root == None):
                #no nodes yet
                self.root = tok
                lowestNode = self.lowestOperatorOpen(self.root)
                ln = lowestNode[1]
            else:
                #find node to set
                lowestNode = self.lowestOperatorOpen(self.root)
                ln = lowestNode[1]
                self.setNodeBranch(ln, tok)

    def printTree(self, node, level=0, prefix='Root: '):
        #prints tree
        if node is not None:
            print(' ' * (level * 4) + prefix + str(node.token.value))
            if node.left is not None or node.right is not None:
                self.printTree(node.left, level + 1, 'L-- ')
                self.printTree(node.right, level + 1, 'R-- ')


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
    tk = [token.Token('+', "PLUS"), token.Token("-", "SUB"),token.Token(7, "NUM"), token.Token('/', "DIV"), token.Token('*2', "MULT"), token.Token(5.0, "NUM"), token.Token(3.0, "NUM")]
    opTr = OperationTree()
    opTr.root = tk[0]
    opTr.root.left = tk[1]
    opTr.root.right = tk[2]
    opTr.root.left.left = tk[3]
    opTr.root.left.right = tk[4]
    opTr.root.left.left.left = tk[5]
    opTr.root.left.left.right = tk[6]

    print(f"Root: {opTr.root}\n")
    result = opTr.lowestOperatorOpen(opTr.root)
    print(f"LowOpenOper: {result[0]} : [{result[1]}]")

    print("\n\n")
    eqn = "5 + 3.5 * x - 4 / 76 + (0.2 + 4) + 5.8"
    tokens = lexer.eqToTokens(eqn)
    postTokens = parse._infixToPostfix(tokens)
    preTokens = parse._postfixToPrefix(postTokens)
    tr = OperationTree()
    tr.buildTreeFromPrefix(preTokens)

    print(f"input equation: {eqn}")
    tr.printTree(tr.root)