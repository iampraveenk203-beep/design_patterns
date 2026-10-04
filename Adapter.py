"""
Adapter Pattern: This is structural pattern that acts as a bridge between two incompatible interfaces.
Client calling not supported method ----> Write Adapter ---> BankService method.
"""
from abc import ABC, abstractmethod

class PaymentService(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class BankServiceAdapter(PaymentService):
    def __init__(self, bank_service):
        self.bank_service = bank_service
    
    def pay(self, amount):
        self.bank_service.make_payment(amount)

class BankService:
    def __init__(self):
        pass
    
    def make_payment(self, amount):
        print(f"Payment completed for {amount}.")

# Client Code
def process_payemnt(payment_service, amount):
    payment_service.pay(amount)

bankAdapter = BankServiceAdapter(BankService())
process_payemnt(bankAdapter,100)
