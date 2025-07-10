class Sol:
    def __init__(self,b):
        self.__balance=b
    def setBalance(self,b):
        self.__balance=b
    def getBalance(self):
        return self.__balance
    def updateBalance(self,b):
        self.__balance+=b
        return self.__balance
obj = Sol(10)
obj.setBalance(10)
print(obj.getBalance())
print(obj.updateBalance(10))
print(obj.__balance)