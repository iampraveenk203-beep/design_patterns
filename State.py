"""
State Pattern: Is behavioral pattern every every state of system/machine has own class.

Ex: Vending Machine states:
    1. Idle
    2. Inserted money
    3. Out of stock
"""

from abc import ABC, abstractmethod

class VendingMachine:
    def __init__(self):
        self.snacks = 5
        self.ideal_state  = IdealState()
        self.has_money_state = HasMoneyState()
        self.out_of_stock_state = OutofStockState()
        self.state = self.ideal_state
    
    def handle (self, action):
        self.state.handle(self, action)

# State Pattern interface
class State(ABC):
    @abstractmethod
    def handle(self, action):
        pass
    
# Ideal State
class IdealState(State):
    def handle(self, machine: VendingMachine, action: str):
        if action == "insert_coin":
            machine.state = machine.has_money_state
            print(f"Coin Inserted. You can select snack")
        else:
            print("Insert coin first..!")

class HasMoneyState(State):
    def handle(self, machine: VendingMachine, action: str):
        if action == "select_snack":
            if machine.snacks > 0:
                machine.snacks -= 1
                machine.state = machine.ideal_state
                print(f"Dispensing snack, Thank You..!")
            else:
                machine.state = machine.out_of_stock_state
                print(f"Out of stock snack ! Refund Initialted.")

class OutofStockState(State):
    def handle(self, machine: VendingMachine, action: str):
        print(f"Sorry No stock left ! Refund Initialted.")


# Driver code
machine  = VendingMachine()
machine.handle("insert_coin")
machine.handle("select_snack")
machine.handle("insert_coin")
machine.handle("select_snack")
machine.handle("insert_coin")
machine.handle("select_snack")
machine.handle("insert_coin")
machine.handle("select_snack")
machine.handle("insert_coin")
machine.handle("select_snack")
machine.handle("insert_coin")
machine.handle("select_snack")
