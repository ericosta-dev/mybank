from datetime import datetime
from enum import Enum

from .category import Category


class TypeTransaction(Enum):
    INCOME = "INCOME"
    EXPENSE = "EXPENSE"


class Transaction:
    """
    Transaction entity
    Attributes:
        id (int): Transaction id
        category (Category): Category entity
        type (TypeTransaction): Transaction type
        value (float): Transaction value
        date (datetime): Transaction date
        note (str): Transaction note
    """

    def __init__(
        self,
        id: int,
        category: Category,
        type: TypeTransaction,
        value: float,
        date: datetime,
        note: str,
    ):
        self.id = self.validate_id(id)
        self.category = self.validate_category(category)
        self.type = self.validate_type(type)
        self.value = self.validate_value(value)
        self.date = self.validate_date(date)
        self.note = self.validate_note(note)

    def __str__(self):
        return f"Transaction {self.id}: {self.category.name} - {self.value} - {self.date}"

    @staticmethod
    def validate_id(id: int):
        if not isinstance(id, int) or id <= 0:
            raise TypeError("Transaction id must be an positive integer")
        return id

    @staticmethod
    def validate_category(category: Category):
        if not isinstance(category, Category) or category.id <= 0:
            raise TypeError("Transaction category must be a Category entity")
        return category

    @staticmethod
    def validate_type(type: TypeTransaction):
        if not isinstance(type, TypeTransaction) or type not in TypeTransaction:
            raise TypeError("Transaction type must be a TypeTransaction entity")
        return type

    @staticmethod
    def validate_value(value: float):
        if not isinstance(value, float) or value < 0:
            raise TypeError("Transaction value must be a positive float")
        return value

    @staticmethod
    def validate_date(date: datetime):
        if not isinstance(date, datetime):
            raise TypeError("Transaction date must be a datetime entity")
        return date

    @staticmethod
    def validate_note(note: str):
        if not isinstance(note, str):
            raise TypeError("Transaction note must be a string")
        return note
