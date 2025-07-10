'''Write a Python program that asks the user to enter their full name and age.
 The program should then print:
"Hello, <NAME>! You will be <AGE + 5> years old in 5 years."'''

name=input("Enter Your Full Name:")
age=int(input("Enter Your Age:"))
print("Hello, <{}>! you will be <{}> years old in 5 years.".format(name,age+5))