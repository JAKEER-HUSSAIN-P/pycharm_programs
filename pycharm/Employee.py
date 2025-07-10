class Employee:
    def __init__(self):
        self.__name = ""
        self.__salary = 0.0
        self.__age = 0

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for salary with validation
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Error: Salary must be greater than 0.")

    # Getter for salary
    def get_salary(self):
        return self.__salary

    # Setter for age with validation
    def set_age(self, age):
        if 18 <= age <= 100:
            self.__age = age
        else:
            print("Error: Age must be between 18 and 100.")

    # Getter for age
    def get_age(self):
        return self.__age


# Example usage
emp = Employee()
emp.set_name("John Doe")
emp.set_salary(50000.0)
emp.set_age(30)

print("Employee Name:", emp.get_name())
print("Employee Salary:", emp.get_salary())
print("Employee Age:", emp.get_age())
emp.set_salary(-1000)