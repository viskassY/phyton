import unittest
from minidb.database import Database
from minidb.core.column import Column
from minidb.core.datatypes import IntegerType


class TestTransaction(unittest.TestCase):

    def test_rollback(self):
        db = Database("test")

        table = db.create_table("users", [
            Column("id", IntegerType())
        ])

        try:
            with db.transaction():
                table.insert({"id": 1}, database=db)
                raise Exception("fail")
        except:
            pass

        self.assertEqual(len(table), 0)