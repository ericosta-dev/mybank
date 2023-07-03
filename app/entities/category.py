class Category:
    def __init__(self, id: int, name: str, goal: float):
        self.id = self.validate_id(id)
        self.name = self.validate_name(name)
        self.goal = self.validate_goal(goal)

    def __str__(self):
        return f"Category {self.id}: {self.name}"

    @staticmethod
    def validate_id(id: int):
        if not isinstance(id, int) or id <= 0:
            raise TypeError("Category id must be an positive integer")
        return id

    @staticmethod
    def validate_name(name: str):
        if not isinstance(name, str) or len(name) == 0:
            raise TypeError("Category name must be a non-empty string")
        return name

    @staticmethod
    def validate_goal(goal: float):
        if not isinstance(goal, float) or goal < 0:
            raise TypeError("Category goal must be a positive float")
        return goal
