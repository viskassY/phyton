import unittest
from minidb.query.joined_table import JoinedTable
from minidb.core.table import Table
from minidb.core.column import Column
from minidb.core.datatypes import IntegerType


class TestJoin(unittest.TestCase):

    def setUp(self):
        self.t1 = Table("t1", [Column("id", IntegerType())])
        self.t2 = Table("t2", [Column("id", IntegerType())])

        self.t1.insert({"id": 1})
        self.t2.insert({"id": 1})

    def test_join(self):
        join = JoinedTable(self.t1, self.t2, "id", "id")
        result = join.execute()

        self.assertEqual(len(result), 1)