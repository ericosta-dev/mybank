from datetime import datetime

import pytest

from app.entities.category import Category
from app.entities.transaction import Transaction, TypeTransaction


def test_transaction_creation():
    obj_category = Category(1, "Test", 100.0)
    obj_transaction = Transaction(
        1, obj_category, TypeTransaction.INCOME, 100.0, datetime.now(), "note"
    )
    assert obj_transaction.id == 1
    assert obj_transaction.category == obj_category
    assert obj_transaction.type == TypeTransaction.INCOME
    assert obj_transaction.value == 100.0
    assert isinstance(obj_transaction.date, datetime)
    assert obj_transaction.note == "note"


def test_invalid_id():
    obj_category = Category(2, "Test", 100.0)
    with pytest.raises(TypeError) as excinfo:
        Transaction(
            "1", obj_category, TypeTransaction.INCOME, 100.0, datetime.now(), "note"
        )

        assert "Transaction id must be an positive integer" in str(excinfo.value)


def test_invalid_category():
    with pytest.raises(TypeError) as excinfo:
        Transaction(
            1, "obj_category", TypeTransaction.INCOME, 100.0, datetime.now(), "note"
        )

        assert "Transaction category must be a Category entity" in str(excinfo.value)


def test_invalid_type():
    obj_category = Category(1, "Test", 100.0)
    with pytest.raises(TypeError) as excinfo:
        Transaction(
            1, obj_category, "TypeTransaction.INCOME", 100.0, datetime.now(), "note"
        )

        assert "Transaction type must be a TypeTransaction entity" in str(excinfo.value)


def test_invalid_value():
    obj_category = Category(1, "Test", 100.0)
    with pytest.raises(TypeError) as excinfo:
        Transaction(
            1, obj_category, TypeTransaction.INCOME, -100.0, datetime.now(), "note"
        )

        assert "Transaction value must be a positive float" in str(excinfo.value)


def test_invalid_date():
    obj_category = Category(1, "Test", 100.0)
    with pytest.raises(TypeError) as excinfo:
        Transaction(
            1, obj_category, TypeTransaction.INCOME, 100.0, "datetime.now()", "note"
        )

        assert "Transaction date must be a datetime" in str(excinfo.value)


def test_invalid_note():
    obj_category = Category(1, "Test", 100.0)
    with pytest.raises(TypeError) as excinfo:
        Transaction(1, obj_category, TypeTransaction.INCOME, 100.0, datetime.now(), 1)

        assert "Transaction note must be a string" in str(excinfo.value)
