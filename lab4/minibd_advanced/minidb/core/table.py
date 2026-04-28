from typing import Any, List, Dict, Optional
from .row import Row
from .column import Column

class Table:
    """
    Клас, що представляє таблицю в базі даних.
    Зберігає рядки та виконує CRUD-операції.
    """
    def __init__(self, name: str, columns: List[Column]) -> None:
        self.name: str = name
        self.columns: List[Column] = columns

        self._rows: List[Row] = []
        self._next_id: int = 1
        self._unique_indexes: Dict[str, Dict[Any, Row]] = {}


    def insert(self, data: Dict[str, Any], database=None) -> Row:
        """
    Додає новий рядок у таблицю.

    :param data: словник значень
    :param database: об'єкт Database для перевірки FK
    :return: створений рядок
    """
        # перевірка всіх колонок
        for column in self.columns:
            value = data.get(column.name)

            column.validate(value)
            column.check_unique(value, self._rows)

            if database:
                column.check_foreign_key(value, database)

        #створення row
        row = Row(data, self._next_id) 
        self._rows.append(row)

        # оновлення унікальних індексів
        for column in self.columns:
            if column.unique:
                self._unique_indexes .setdefault(column.name, {})
                self._unique_indexes[column.name][data.get(column.name)] = row

        self._next_id += 1
        return row
    
    def get_row(self, index: int) -> Row:
       return self._rows[index]
    
    def get_by_id(self, row_id: int) -> Optional[Row]:
        """
        Повертає рядок за ID.
        """
        for row in self._rows:
            if row.id == row_id:
                return row
        return None
    
    
    def update(self, row_id: int, new_data: Dict[str, Any], database=None) -> Row:
        """
        Оновлює дані рядка.

        :param row_id: ідентифікатор
        :param new_data: нові значення
        :param database: для перевірки FK
        :return: оновлений рядок
        """
        
        row = self.get_by_id(row_id)
        if not row:
            raise ValueError("Row not found")

        for column in self.columns:
            if column.name in new_data:
                value = new_data[column.name]

                column.validate(value)
                column.check_unique(value, self._rows)

                if database:
                    column.check_foreign_key(value, database)

                row[column.name] = value

        return row
    

    def delete(self, row_id: int) -> None:
        row = self.get_by_id(row_id)
        if not row:
            raise ValueError("Row not found")

        self._rows.remove(row)

    def __iter__(self):
        return iter(self._rows)
    
    def __len__(self) -> int:
        return len(self._rows)
    
    