from operation import average
from operation import grades
name=input("Enter student name: ")
marks=[]
print("Enter your 6 subject marks :")
i=1
while i<=6:
    mark=int(input(f"Enter {i}: "))
    if mark>=0 and mark<=100:
        marks.append(mark)
        i+=1
    else:
        print("Enter valid marks")
print(marks)
print("Average:" ,average(marks))
print("Grades:")
print(grades(marks))
print(grades(marks))


