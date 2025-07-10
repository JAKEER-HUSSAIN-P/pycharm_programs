class Calculator:
    # gives the addition of two numbers
    def Addition(self,a,b):
        return a+b

    # gives the substraction of two numbers
    def Subtraction(self,a,b):
        return a-b

    # gives the Multiplication of two numbers
    def Multiplication(self,a,b):
        return a*b
    # returns the divion of two number
    def Division(self,a,b):
        try:
            ans=a/b
            return ans
        except ZeroDivisionError:
            return ("Error: 'Division by zero is not allowed'")
obj=Calculator()
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("Addition({}+{}):".format(a,b),obj.Addition(a,b))
print("substraction({}-{}):".format(a,b),obj.Subtraction(a,b))
print("Multiplication({}*{}):".format(a,b),obj.Multiplication(a,b))
print("Division({}/{}):".format(a,b),obj.Division(a,b))

