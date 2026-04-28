import unittest
from minidb.core.column import Column
from minidb.core.datatypes import IntegerType

class TestColumn(unittest.TestCase):

    def test_validate(self):
        col = Column("age", IntegerType(), nullable=False)

        self.assertTrue(col.validate(25))

        with self.assertRaises(ValueError):
            col.validate(None)

    def test_unique(self):
        col = Column("id", IntegerType(), unique=True)

        class FakeRow:
            def __getitem__(self, key):
                return 1
            
        rows = [FakeRow()]

        with self.assertRaises(ValueError):
            col.check_unique(1, rows)