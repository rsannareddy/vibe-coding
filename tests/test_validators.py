import pytest
from bank_account.validators import positive

def test_positive():
    with pytest.raises(ValueError): positive(0)
