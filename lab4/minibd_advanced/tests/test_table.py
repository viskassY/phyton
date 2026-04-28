import unittest
from minidb.core.table import Table
from minidb.core.column import Column
from minidb.core.datatypes import IntegerType


class TestTable(unittest.TestCase):

    def setUp(self):
        self.table = Table("test", [
            Column("id", IntegerType(), unique=True)
        ])

    def test_insert(self):
        row = self.table.insert({"id": 1})
        self.assertEqual(row["id"], 1)

    def test_get_by_id(self):
        row = self.table.insert({"id": 1})
        found = self.table.get_by_id(row.id)

        self.assertEqual(found, row)

    def test_delete(self):
        row = self.table.insert({"id": 1})
        self.table.delete(row.id)

        self.assertIsNone(self.table.get_by_id(row.id))