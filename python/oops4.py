from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
    @abstractmethod
    def assign(self):
        pass
    def passe(self):
        print("Pass")
class implement(PaymentMethod):
    def pay(self,amount):
        print("Payment Successful",amount)
    def assign(self):
        print("Implemented abstract class")
obj=implement()
obj.pay(10)
obj.assign()
obj.passe()


