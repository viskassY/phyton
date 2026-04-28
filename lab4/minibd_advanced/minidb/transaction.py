import copy
from typing import Optional, Type
from unicodedata import name


class TransactionError(Exception):
    """Помилка транзакції."""
    pass


class Transaction:
    """
    Контекстний менеджер для транзакцій.

    Забезпечує атомарність:
    - commit при успіху
    - rollback при помилці
    """

    def __init__(self, database) -> None:
        self.database = database
        self._backup = None

    def __enter__(self) -> "Transaction":
        self._backup = copy.deepcopy(self.database._tables)
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback,
    ) -> bool:
        if exc_type:
            # rollback
            for name in self.database._tables:
                self.database._tables[name]._rows = self._backup[name]._rows
                self.database._tables[name]._next_id = self._backup[name]._next_id
            raise TransactionError("Transaction rolled back")

        
        return True