'''Write a Python program to take 5 numbers as input from the user,
store them in a list, and then:Print the list in reverse order.
Print the sum and average of the numbers.'''
l=[]
for i in range(5):
    l.append(int(input("Enter no{}:".format(i+1))))
print(l[::-1])
s=sum(l)
print(s)
print(s/5)
print("The sum")