#Token
#Nicholas Norman
#March 2024

class Token():
    def __init__(self, value, type):
        self._value = value

        #determine type based off of value
        self._type = type

    def __str__(self):
        return f"{self._value}, {self._type}"
    
    def getValue(self):
        return self._value
    
    def setValue(self, value):
        self._value = value

    def getType(self):
        return self._type
    
    def setType(self, type):
        self._type = type

    value = property(getValue, setValue)
    type = property(getType, setType)

if __name__ == "__main__":
    #test
    tok = Token(7.0, "NUM")
    print(tok)
    print(tok.value, tok.type)
    tok.value = 1.0
    print(tok)