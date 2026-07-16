from .validators import positive
from .exceptions import InsufficientFundsError
class BankAccount:
    def __init__(self, number:str,balance:float=0):
        self.number=number
        self.balance=balance
    def deposit(self,amount:float):
        positive(amount); self.balance+=amount
    def withdraw(self,amount:float):
        positive(amount)
        if amount>self.balance: raise InsufficientFundsError()
        self.balance-=amount
