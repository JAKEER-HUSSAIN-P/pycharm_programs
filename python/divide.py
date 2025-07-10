def divide(a,b):
    try:
        return a//b
    except ZeroDivisionError:
        return "Zero Division Error"
a=int(input("Enter a:"))
b=int(input("Enter b:"))
print(divide(a,b))