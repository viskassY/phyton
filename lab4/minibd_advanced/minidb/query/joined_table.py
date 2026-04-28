from typing import List, Dict, Any
from ..core.table import Table


class JoinedTable:
    """
    Клас для виконання INNER JOIN між двома таблицями.

    Повертає список об'єднаних рядків у вигляді словників.
    Імена колонок мають префікси (table.column) для уникнення конфліктів.
    """

    def __init__(self, table1: Table, table2: Table, key1: str, key2: str) -> None:
        """
        Ініціалізація JOIN.

        :param table1: перша таблиця
        :param table2: друга таблиця
        :param key1: колонка з першої таблиці
        :param key2: колонка з другої таблиці
        """
        self.table1: Table = table1
        self.table2: Table = table2
        self.key1: str = key1
        self.key2: str = key2

    def execute(self) -> List[Dict[str, Any]]:
        """
        Виконує INNER JOIN між таблицями.

        :return: список об'єднаних рядків
        """
        result: List[Dict[str, Any]] = []

        for row1 in self.table1:
            for row2 in self.table2:
                if row1[self.key1] == row2[self.key2]:
                    merged: Dict[str, Any] = {}

                    # поля з першої таблиці
                    for key in row1:
                        merged[f"{self.table1.name}.{key}"] = row1[key]

                    # поля з другої таблиці
                    for key in row2:
                        merged[f"{self.table2.name}.{key}"] = row2[key]

                    result.append(merged)

        return result