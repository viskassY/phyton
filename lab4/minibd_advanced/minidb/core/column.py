from typing import Any, Optional, Tuple, List

from .datatypes import DataType
from .row import Row


class Column:
    """
    Клас, що представляє колонку таблиці.

    Містить інформацію про назву, тип даних та обмеження
    (nullable, unique, foreign key).
    """

    def __init__ (self, name:str ,data_type: DataType, nullable: bool = True, unique: bool = False, references: Optional[Tuple[str, str]] = None) -> None:
        self.name = name
        self.data_type = data_type
        self.nullable = nullable
        self.unique = unique
        self.references = references  

    def __repr__(self) -> str:
        """Повертає форматоване рядкове представлення об'єкта Column."""
        return (
            f"Column(name={self.name}, type={self.data_type}, "
            f"nullable={self.nullable}, unique={self.unique})"
        )
    
    def validate(self, value: Any) -> bool:
        """
    Перевіряє значення на відповідність типу та nullable.

    :param value: значення
    :return: True, якщо валідне
    :raises ValueError: якщо значення некоректне
    """
        if value is None:
            if not self.nullable:
                raise ValueError(f"Значення для стовпця '{self.name}' не може бути NULL")
            return True
        
        if not self.data_type.validate(value):
            raise ValueError(f"Значення '{value}' не відповідає типу даних '{self.data_type}' для стовпця '{self.name}'")
        
        return True
    

    def check_unique(self, value: Any, table_rows: List[Row]) -> bool:
        """
        Перевіряє, чи значення є унікальним у таблиці.

        :param value: значення
        :param table_rows: список рядків таблиці
        :return: True, якщо унікальне
        :raises ValueError: якщо знайдено дублікат
        """
        if not self.unique:
            return True

        for row in table_rows:
            if row[self.name] == value:
                raise ValueError(f"Значення '{value}' для стовпця '{self.name}' повинно бути унікальним")
        
        return True
    

    def check_foreign_key(self, value: Any, database) -> bool:
        """
        Перевіряє зовнішній ключ.

        :param value: значення
        :param database: об'єкт Database
        :return: True, якщо значення існує у пов'язаній таблиці
        :raises ValueError: якщо значення не знайдено
        """
        if self.references is None:
            return True
        
        table_name, column_name = self.references
        table = database.get_table(table_name)
        
        for row in table:
            if row[column_name] == value:
                return True
        
        raise ValueError(f"Значення '{value}' не знайдено в '{table_name}.{column_name}'")
    

    