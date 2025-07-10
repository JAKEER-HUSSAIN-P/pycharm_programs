'''Write a Python program to implement a class Student that has the following
 functionalities:Private Attributes:name (a string representing the student's name)
 marks (an integer representing the student's marks, ranging from 0 to 100)
 Methods:A setter method set_name(name) that sets the student's name.A getter method get_name()
  that returns the student's name.A setter method set_marks(marks) that sets the student's marks
   (ensuring marks are between 0 and 100).A getter method get_marks() that returns the student's
    marks.Constraints:Marks should be between 0 and 100 (both inclusive).If invalid marks are entered
    (like negative values or values above 100), print an error message.

Output:
Student Name: Alice
Student Marks: 85
Error: Marks should be between 0 and 100.
Student Marks (after invalid input): 85'''
class Student:
    #A Method to intialze the student name and marks
    def set_name(self,name):
        self.__name = name
    def set_marks(self,marks):
        if marks<0 or marks>100:
            print("Error: Marks Should be between 0 and 100.")
        else:
            self.marks = marks
    def get_name(self):
        print("Student Name:",self.__name)
    def get_marks(self):
        print("Student Marks:",self.marks)
    #A method to retrive marks
obj=Student()
obj.set_name("Alice")
obj.set_marks(85)
obj.get_name()
obj.get_marks()
obj.set_marks(102)
obj.get_marks()