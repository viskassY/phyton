from typing import Any
from ..core.row import Row


class Condition:
    """
    Клас для представлення умови фільтрації (WHERE).
    """

    def __init__(self, column: str, operator: str, value: Any) -> None:
        self.column = column
        self.operator = operator
        self.value = value

    def evaluate(self, row: Row) -> bool:
        val = row[self.column]

        if self.operator == "=":
            return val == self.value
        elif self.operator == "!=":
            return val != self.value
        elif self.operator == "<":
            return val < self.value
        elif self.operator == ">":
            return val > self.value
        elif self.operator == "<=":
            return val <= self.value
        elif self.operator == ">=":
            return val >= self.value
        elif self.operator == "LIKE":
            return self.value in val
        else:
            raise ValueError(f"Unsupported operator: {self.operator}")


class ConditionGroup:
    """
    Клас для комбінування умов (AND / OR).
    """

    def __init__(self, left: Condition, operator: str, right: Condition) -> None:
        self.left = left
        self.operator = operator
        self.right = right

    def evaluate(self, row: Row) -> bool:
        if self.operator == "AND":
            return self.left.evaluate(row) and self.right.evaluate(row)
        elif self.operator == "OR":
            return self.left.evaluate(row) or self.right.evaluate(row)
        else:
            raise ValueError(f"Unsupported logical operator: {self.operator}")

        