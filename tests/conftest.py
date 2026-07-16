from bank_account.account import BankAccount
import pytest
@pytest.fixture
def account(): return BankAccount('1001',100)
