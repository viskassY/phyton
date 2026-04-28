import unittest
from minidb.database import Database
from minidb.core.column import Column
from minidb.core.datatypes import IntegerType


class TestDatabase(unittest.TestCase):

    def test_create_table(self):
        db = Database("test")

        table = db.create_table("users", [
            Column("id", IntegerType())
        ])

        self.assertIsNotNone(table)