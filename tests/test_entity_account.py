import pytest

from app.entities.account import Account


class TestAccount:
    def test_account_creation(self):
        account_obj = Account(id=1, name="Test Account", balance=100.00)

        assert account_obj.id == int(1)
        assert account_obj.name == "Test Account"
        assert account_obj.balance == float(100.00)

    def test_account_creation_with_invalid_id(self):
        with pytest.raises(TypeError) as excinfo:
            Account(id="1", name="Test Account", balance=100.00)

            assert "Account id must be an positive integer" in str(excinfo.value)

    def test_account_creation_with_invalid_name(self):
        with pytest.raises(TypeError) as excinfo:
            Account(id=1, name="", balance=100.00)

            assert "Account name must be a non-empty string" in str(excinfo.value)

    def test_account_creation_with_invalid_balance(self):
        with pytest.raises(TypeError) as excinfo:
            Account(id=1, name="Test Account", balance=-1.00)

            assert "Account balance must be a positive float" in str(excinfo.value)
