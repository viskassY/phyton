from typing import Dict, Any, Iterator


class Row:
    """
    Клас, що представляє один рядок таблиці.

    Дані зберігаються у вигляді словника.
    Забезпечує зручний доступ через [] та ітерацію.
    """

    def __init__(self, data: Dict[str, Any], row_id: int) -> None:
        """
        Ініціалізація рядка.

        :param data: словник значень
        :param row_id: унікальний ідентифікатор
        """
        self._data: Dict[str, Any] = data
        self.id: int = row_id


    def __getitem__(self, key: str) -> Any:
        return self._data.get(key)

    def __setitem__(self, key: str, value: Any) -> None:
        self._data[key] = value

    def __eq__(self, other: object) -> bool:  #порівняння рядків
        if not isinstance(other, Row):
            return False
        return self.id == other.id and self._data == other._data

    def __iter__(self) -> Iterator[str]: # щоб об'єкт класу Row тепер можна було використовувати в циклі for
        return iter(self._data)