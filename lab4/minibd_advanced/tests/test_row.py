import unittest
from minidb.core.row import Row

class TestRow(unittest.TestCase):
    
    def test_row_set(self):
        row = Row({"name": "Alice"}, 1)

        self.assertEqual(row["name"], "Alice")
        row["name"] = "Bob"
        self.assertEqual(row["name"], "Bob")

    def test_equality(self):
        r1 = Row({"a": 1}, 1)
        r2 = Row({"a": 1}, 1)

        self.assertEqual(r1, r2)
        
    def test_iteration(self):
        row = Row({"a": 1, "b": 2}, 1)
        keys = list(row)

        self.assertIn("a", keys)
        self.assertIn("b", keys)