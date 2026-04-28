import unittest
from minidb.query.engine import Query
from minidb.core.table import Table
from minidb.core.column import Column
from minidb.core.datatypes import IntegerType


class TestQuery(unittest.TestCase):

    def setUp(self):
        self.table = Table("t", [
            Column("id", IntegerType())
        ])

        self.table.insert({"id": 1})
        self.table.insert({"id": 2})

    def test_where(self):
        result = Query(self.table).where("id", ">", 1).execute()

        self.assertEqual(len(result), 1)

    def test_limit(self):
        result = Query(self.table).limit(1).execute()

        self.assertEqual(len(result), 1)