from typing import Dict, List
import json

from .transaction import Transaction
from .core.table import Table
from .core.column import Column


class Database:
    """
    Центральний клас для управління базою даних.

    Відповідає за створення таблиць, доступ до них,
    транзакції та серіалізацію.
    """

    def __init__(self, name: str) -> None:
        self.name: str = name
        self._tables: Dict[str, Table] = {}

    def create_table(self, name: str, columns: List[Column]) -> Table:
        """
        Створює нову таблицю.

        :param name: назва таблиці
        :param columns: список колонок
        :return: об'єкт Table
        """
        if name in self._tables:
            raise ValueError(f"Table '{name}' already exists.")

        table = Table(name, columns)
        self._tables[name] = table
        return table

    def get_table(self, name: str) -> Table:
        """
        Повертає таблицю за назвою.
        """
        table = self._tables.get(name)
        if not table:
            raise ValueError(f"Table '{name}' not found.")
        return table

    def transaction(self) -> Transaction:
        """
        Повертає об'єкт транзакції.
        """
        return Transaction(self)

    def save_to_json(self, filename: str) -> None:
        """
        Зберігає стан бази даних у JSON файл.
        """
        data = {}

        for table_name, table in self._tables.items():
            data[table_name] = []

            for row in table:
                data[table_name].append(row._data)

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_from_json(self, filename: str) -> None:
        """
        Завантажує стан бази даних з JSON файлу.
        """
        with open(filename, "r") as f:
            data = json.load(f)

        for table_name, rows in data.items():
            table = self.get_table(table_name)

            for row_data in rows:
                table.insert(row_data, database=self)