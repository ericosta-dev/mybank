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
        self.id = id
        self.category = category
        self.type = type
        self.value = value
        self.date = date
        self.note = note
