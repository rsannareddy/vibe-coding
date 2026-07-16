from bank_account.transaction import Transaction

def test_tx():
    assert Transaction('deposit',10).amount==10
