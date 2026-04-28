from typing import List, Any, Optional
from .conditions import Condition
from ..core.table import Table

class Query:
    """
    Клас для побудови та виконання запитів до таблиці.
    """
    def __init__(self, table: Table) -> None:
        self.table: Table = table
        
        self._columns: Optional[List[Any]] = None
        self._condition: Optional[Any] = None
        self._order: Optional[tuple[str, bool]] = None
        self._limit: Optional[int] = None
        self._offset: int = 0
        self._group_by: Optional[str] = None


    def select(self, columns: List[Any]) -> 'Query':
        self._columns = columns
        return self


    def where(self, column: str, operator: str, value: Any) -> 'Query':
        self._condition = Condition(column, operator, value)
        return self

    def order_by(self, column: str, ascending: bool = True) -> 'Query':
        self._order = (column, ascending)
        return self   

    def limit(self, count: int) -> 'Query':
        self._limit = count
        return self   

    def offset(self, count: int) -> 'Query':
        self._offset = count
        return self

    def group_by(self, column: str) -> 'Query':
        self._group_by = column
        return self

    def execute(self) -> List[Any]:
        """
        Виконує запит і повертає результат.
        """
        result = list(self.table)

        # WHERE
        if self._condition:
            result = [row for row in result if self._condition.evaluate(row)]

        # ORDER
        if self._order:
            col, asc = self._order
            result.sort(key=lambda r: r[col], reverse=not asc)

        # OFFSET
        if self._offset:
            result = result[self._offset:]

        # LIMIT
        if self._limit is not None:
            result = result[:self._limit]

        if self._group_by:
            grouped = {}

            for row in result: #проходимо по всіх рядках після WHERE / LIMIT
                key = row[self._group_by] #отримуємо значення колонки для групування
                grouped.setdefault(key, []).append(row) # якщо ключа немає - створюємо новий список, якщо є - додаємо ряд до існуючого списку

            final_result = []

            for key, rows in grouped.items():
                result_row = {self._group_by: key}

                for col in self._columns or []: # проходимо по тому, що передали в select (може бути None)
                    if isinstance(col, Count):
                        result_row["count"] = len(rows)

                    elif isinstance(col, Sum):
                        result_row["sum"] = sum(r[col.column] for r in rows)

                    elif isinstance(col, Avg):
                        values = [r[col.column] for r in rows]
                        result_row["avg"] = sum(values) / len(values) if values else 0

                    elif isinstance(col, Max):
                        result_row["max"] = max(r[col.column] for r in rows)

                    elif isinstance(col, Min):
                        result_row["min"] = min(r[col.column] for r in rows)

                final_result.append(result_row)

            return final_result


            
        # SELECT
        if self._columns:
            result = [
                {col: row[col] for col in self._columns if isinstance(col, str)}
                for row in result
            ]

        # якщо є агрегації
        if self._columns:
            # перевіряємо чи є хоч одна агрегація
            has_agg = any(isinstance(col, (Count, Sum, Avg, Max, Min)) for col in self._columns)

            if has_agg:
                result_row = {}

                for col in self._columns:
                    if isinstance(col, Count):
                        result_row["count"] = len(result)

                    elif isinstance(col, Sum):
                        result_row["sum"] = sum(row[col.column] for row in result)

                    elif isinstance(col, Avg):
                        values = [row[col.column] for row in result]
                        result_row["avg"] = sum(values) / len(values) if values else 0

                    elif isinstance(col, Max):
                        result_row["max"] = max(row[col.column] for row in result)

                    elif isinstance(col, Min):
                        result_row["min"] = min(row[col.column] for row in result)


                return [result_row]
        return result


class Count:
    def __init__(self, column):
        self.column = column


class Sum:
    def __init__(self, column):
        self.column = column


class Avg:
    def __init__(self, column):
        self.column = column


class Max:
    def __init__(self, column):
        self.column = column


class Min:
    def __init__(self, column):
        self.column = column