class Account:
    def __init__(self, id: int, name: str, balance: float):
        self.id = self.validate_id(id)
        self.name = self.validate_name(name)
        self.balance = self.validate_balance(balance)

    def __str__(self):
        return f"Account {self.id}: {self.name} - {self.balance}"

    @staticmethod
    def validate_id(id: int):
        if not isinstance(id, int) or id <= 0:
            raise TypeError("Account id must be an positive integer")
        return id

    @staticmethod
    def validate_name(name: str):
        if not isinstance(name, str) or len(name) == 0:
            raise TypeError("Account name must be a non-empty string")
        return name

    @staticmethod
    def validate_balance(balance: float):
        if not isinstance(balance, float) or balance < 0:
            raise TypeError("Account balance must be a positive float")
        return balance
