from abc import ABC, abstractmethod
from typing import Any

from polars import datetime


class DataType(ABC):
    """
    Абстрактний базовий клас для всіх типів даних у базі.
    """
    @abstractmethod
    def validate(self, value: Any) -> bool:
        """Перевіряє, чи відповідає значення даному типу.
        """
        pass
    
    @abstractmethod
    def __str__(self) -> str:
        """Повертає рядкове представлення типу даних"""
        pass
    
   

class IntegerType(DataType):
    def validate(self, value: Any) -> bool:
        return isinstance(value, int)
    
    def __str__(self) -> str:
        return "INTEGER"

class StringType(DataType):
    def validate(self, value: Any) -> bool:
        return isinstance(value, str)
    
    def __str__(self) -> str:
        return "STRING"

class BooleanType(DataType):
    def validate(self, value: Any) -> bool:
        return isinstance(value, bool)
    
    def __str__(self) -> str:
        return "BOOLEAN"

class FloatType(DataType):
    def validate(self, value: Any) -> bool:
        return isinstance(value, (float, int))
    
    def __str__(self) -> str:
        return "FLOAT"

class DateType(DataType):
    def validate(self, value: Any) -> bool:
        # Примітивна перевірка на об'єкт дати або рядок формату YYYY-MM-DD
        return isinstance(value, datetime)
    
    def __str__(self) -> str:
        return "DATE"
    

    @classmethod
    def from_string(cls, type_name: str) -> 'DataType':
        """Створює екземпляр типу даних з рядкового представлення
        :param type_name: назва типу (наприклад, "INTEGER")
        :return: екземпляр відповідного типу.
        """
        type_name = type_name.upper()
        
        if type_name == 'INTEGER':
            return IntegerType()
        elif type_name == 'STRING':
            return StringType()
        elif type_name == 'BOOLEAN':
            return BooleanType()
        elif type_name == 'FLOAT':
            return FloatType()
        elif type_name == 'DATE':
            return DateType()
        else:
            raise ValueError(f"Невідомий тип даних: {type_name}")
        

        #метод, що належить класу, а не об'єкту. Використовується, щоб працювати з даними всього класу або створювати нові об'єкти