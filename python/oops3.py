class User:
    def login(self):
        print("Login Successful")
class Business(User):
    def hello(self):
        print("Hello")
obj=Business()
obj2=User()
obj.login()
obj.hello()