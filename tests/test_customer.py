from bank_account.customer import Customer

def test_customer():
    assert Customer(1,'Alice').name=='Alice'
