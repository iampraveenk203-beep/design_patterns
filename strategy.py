"""
Strategy Pattern: It is behavioral design pattern that lets you define a family of algorithms, encapsulate each one, and make them interchangeable.
"""
from abc import ABC, abstractmethod

# Step 1: Create interface for PaymentStrategy
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Step 2: Implement pay method in subclass
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing payment of {amount} using Credit Card.")

# Step 3: Implement pay method in Paypal class
class PaypalPayment(PaymentStrategy):
    def pay(slef, amount):
        print(f"Processing payment of {amount} using PayPal.")

# Step 4: Implement pay method in crypto class
class CryptoPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing payment of {amount} using Crypto.")

# Step 5: Context class to use strategies
class PaymentProcessor:
    def __init__(self, Strategy):
        self.Strategy = Strategy
    
    def set_strategy(self, Strategy: PaymentStrategy):
        self.Strategy = Strategy
    
    def process_payemnt(self, amount):
        self.Strategy.pay(amount)

# Driver code
cardpayment = CreditCardPayment()
paypal = PaypalPayment()
crypto = CryptoPayment()

payment = PaymentProcessor(cardpayment)
payment.process_payemnt(100)

payment.set_strategy(paypal)
payment.process_payemnt(200)

payment.set_strategy(crypto)
payment.process_payemnt(300)



