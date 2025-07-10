class Car:

    def __init__ (self):
        self.color = "Black"
        print(self.color)
    def getcolor(self):
        return self.color
    def setcolor(self,c):
        self.color=c
obj=Car()
print(obj.getcolor())
print(obj.setcolor("Green"))
print(obj.getcolor())

#OverLoading
class operations:
    def add(self,n1,n2):
        return n1+n2
    def add(self,n1,n2,n3):
        return n1+n2+n3
ob=operations()
print(ob.add(10,11))
print(ob.add(10,11,12))
