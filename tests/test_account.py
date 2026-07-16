from bank_account.exceptions import InsufficientFundsError
import pytest

def test_deposit(account):
    account.deposit(50); assert account.balance==150

def test_withdraw(account):
    account.withdraw(50); assert account.balance==50

def test_overdraw(account):
    with pytest.raises(InsufficientFundsError): account.withdraw(1000)
